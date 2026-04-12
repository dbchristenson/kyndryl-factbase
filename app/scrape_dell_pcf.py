"""Automate Dell PCF requests for every Enterprise Product.

Setup:
    uv add playwright
    uv run playwright install chromium

Run:
    uv run python app/scrape_dell_pcf.py
    uv run python app/scrape_dell_pcf.py --headed     # watch it
    uv run python app/scrape_dell_pcf.py --dry-run    # list products, no submit
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import random
from dataclasses import dataclass

from playwright.async_api import Locator, Page, async_playwright

URL = "https://www.dell.com/en-us/dt/forms/csb/product-carbon-footprint.htm"

FIRST_NAME = "David"
LAST_NAME = "Christenson"
EMAIL = "db.christenson@northwestern.edu"
ORGANIZATION = "Northwestern University"
SALESPERSON = "Jordan Mitchell"

CATEGORIES = ["STORAGE", "SERVER"]

DELAY_BETWEEN_SUBMITS = (3.0, 6.0)

log = logging.getLogger("dell_pcf")


@dataclass
class SubmitResult:
    category: str
    product: str
    ok: bool
    note: str = ""


async def fill_personal_info(page: Page) -> None:
    """Fill the static identity fields. Safe to call once per page load."""
    await page.get_by_label("First Name", exact=False).fill(FIRST_NAME)
    await page.get_by_label("Last Name", exact=False).fill(LAST_NAME)
    await page.get_by_label("Email", exact=False).fill(EMAIL)
    await page.get_by_label("Organization", exact=False).fill(ORGANIZATION)
    await page.get_by_label("Salesperson", exact=False).fill(SALESPERSON)


ENTERPRISE_HEADER = "#Enterprise_Product"
OPEN_OPTIONS = 'ul.dt-c-form__dropdown-list[role="listbox"] li.dt-c-form__dropdown-option'


async def _open_dropdown(header: Locator) -> None:
    await header.scroll_into_view_if_needed()
    await header.click()
    # Wait until the sibling list is rendered.
    await header.locator("xpath=following-sibling::ul[contains(@class,'dt-c-form__dropdown-list')]").first.wait_for(
        state="visible", timeout=10_000
    )


async def _pick_option(header: Locator, label: str) -> None:
    """Click an option within the listbox that belongs to this dropdown header."""
    option = header.locator(
        "xpath=following-sibling::ul[contains(@class,'dt-c-form__dropdown-list')]"
        f"/li[normalize-space(.)={_xpath_literal(label)}]"
    )
    await option.first.click()


def _xpath_literal(s: str) -> str:
    if "'" not in s:
        return f"'{s}'"
    if '"' not in s:
        return f'"{s}"'
    parts = s.split("'")
    return "concat(" + ", \"'\", ".join(f"'{p}'" for p in parts) + ")"


async def _read_options(header: Locator) -> list[str]:
    items = header.locator(
        "xpath=following-sibling::ul[contains(@class,'dt-c-form__dropdown-list')]/li"
    )
    texts = await items.all_text_contents()
    return [t.strip() for t in texts if t.strip()]


async def _product_header(page: Page) -> Locator:
    """After a category is picked, a second dropdown header appears. Find it."""
    loc = page.locator(
        f".dt-c-form__dropdown-header:not({ENTERPRISE_HEADER})"
    )
    await loc.first.wait_for(state="visible", timeout=10_000)
    return loc.first


async def select_category(page: Page, category: str) -> Locator:
    """Pick STORAGE or SERVER and return the product dropdown header that appears."""
    cat = page.locator(ENTERPRISE_HEADER)
    await _open_dropdown(cat)
    await _pick_option(cat, category)
    return await _product_header(page)


async def list_products(page: Page, category: str) -> list[str]:
    header = await select_category(page, category)
    await _open_dropdown(header)
    values = await _read_options(header)
    await page.keyboard.press("Escape")
    return values


CONSENT_INPUT = "input.pmc_ncm_checkbox_input"
CONSENT_LABEL = "label.pmc_ncm_checkbox_label"
CONSENT_ERROR = "p.dt-s-error__message"


async def _check_consent(page: Page) -> None:
    label = page.locator(CONSENT_LABEL).first
    await label.scroll_into_view_if_needed()
    await label.click()
    # Verify the underlying input is actually checked. If not, fall back to
    # clicking the input itself with force=True.
    input_loc = page.locator(CONSENT_INPUT).first
    for _ in range(3):
        if await input_loc.is_checked():
            return
        await label.click()
        await page.wait_for_timeout(200)
    if not await input_loc.is_checked():
        await input_loc.check(force=True)
    if not await input_loc.is_checked():
        raise RuntimeError("Consent checkbox refused to toggle")


async def submit_one(page: Page, category: str, product_label: str) -> SubmitResult:
    await page.goto(URL, wait_until="domcontentloaded")
    await page.wait_for_timeout(1500)
    await fill_personal_info(page)
    product_header = await select_category(page, category)
    await _open_dropdown(product_header)
    await _pick_option(product_header, product_label)

    await _check_consent(page)

    submit = page.get_by_role("button", name="Submit", exact=False).last
    await submit.scroll_into_view_if_needed()
    await submit.click()

    # Wait for either the consent-error message, a generic error, or a
    # success signal (the form disappearing or a thank-you banner).
    try:
        await page.wait_for_function(
            """() => {
                const err = document.querySelector('p.dt-s-error__message');
                const errVisible = err && err.offsetParent !== null;
                const stillHasEnterpriseField = document.querySelector('#Enterprise_Product');
                const thankYou = document.body.innerText.toLowerCase();
                const success = thankYou.includes('thank you') || thankYou.includes('submitted') || thankYou.includes('received your');
                return errVisible || success || !stillHasEnterpriseField;
            }""",
            timeout=15_000,
        )
    except Exception as e:
        return SubmitResult(category, product_label, False, f"no resolution: {e}")

    err_visible = await page.locator(CONSENT_ERROR).first.is_visible()
    if err_visible:
        err_text = (await page.locator(CONSENT_ERROR).first.text_content() or "").strip()
        return SubmitResult(category, product_label, False, f"form error: {err_text}")

    return SubmitResult(category, product_label, True)


async def inspect(page: Page) -> None:
    """Dump the DOM around the terms checkbox and submit button."""
    await page.goto(URL, wait_until="domcontentloaded")
    await page.wait_for_timeout(2500)
    print("=== iframe list ===")
    frames = page.frames
    for f in frames:
        print(f"frame url={f.url}")
    print("=== form container (parent of Enterprise_Product, walked up 4 levels) ===")
    container_html = await page.evaluate(
        """() => {
            const el = document.querySelector('#Enterprise_Product');
            if (!el) return '(Enterprise_Product not found)';
            let node = el;
            for (let i = 0; i < 5; i++) if (node.parentElement) node = node.parentElement;
            // Strip the big dropdown <li>s to keep output readable
            const clone = node.cloneNode(true);
            clone.querySelectorAll('ul.dt-c-form__dropdown-list').forEach(u => u.innerHTML = '(dropdown options omitted)');
            return clone.outerHTML.slice(0, 15000);
        }"""
    )
    print(container_html)
    print("=== all checkboxes (input type=checkbox) ===")
    html = await page.evaluate(
        """() => {
            const hits = document.querySelectorAll("input[type='checkbox']");
            return Array.from(hits).map(e => {
                const label = e.closest('label') || document.querySelector(`label[for='${e.id}']`);
                return (label ? label.outerHTML : '(no label)') + '\\n>> ' + e.outerHTML;
            }).join('\\n---\\n');
        }"""
    )
    print(html)
    print("=== elements with 'agree'/'terms'/'consent' text ===")
    terms_html = await page.evaluate(
        """() => {
            const all = document.querySelectorAll('label, span, div, p');
            const matches = [];
            for (const el of all) {
                const t = (el.textContent || '').toLowerCase();
                if (t.length > 400) continue;
                if (t.includes('agree') || t.includes('terms') || t.includes('consent') || t.includes('privacy')) {
                    matches.push(el.outerHTML.slice(0, 600));
                    if (matches.length >= 10) break;
                }
            }
            return matches.join('\\n---\\n');
        }"""
    )
    print(terms_html)
    print("=== submit button ===")
    btn = await page.evaluate(
        """() => {
            const hits = document.querySelectorAll("button, input[type='submit']");
            return Array.from(hits).map(e => e.outerHTML).slice(0, 10).join('\\n---\\n');
        }"""
    )
    print(btn)


async def run(headed: bool, dry_run: bool, inspect_mode: bool = False) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not headed)
        context = await browser.new_context()
        page = await context.new_page()

        if inspect_mode:
            await inspect(page)
            await browser.close()
            return

        await page.goto(URL, wait_until="domcontentloaded")
        await fill_personal_info(page)

        catalog: dict[str, list[str]] = {}
        for category in CATEGORIES:
            catalog[category] = await list_products(page, category)
            log.info("%s: %d products", category, len(catalog[category]))
            for name in catalog[category]:
                log.info("  - %s", name)

        if dry_run:
            await browser.close()
            return

        results: list[SubmitResult] = []
        for category, products in catalog.items():
            for name in products:
                try:
                    res = await submit_one(page, category, name)
                except Exception as e:
                    res = SubmitResult(category, name, False, repr(e))
                results.append(res)
                status = "OK" if res.ok else "FAIL"
                log.info("[%s] %s / %s %s", status, category, name, res.note)
                await asyncio.sleep(random.uniform(*DELAY_BETWEEN_SUBMITS))

        await browser.close()

        failures = [r for r in results if not r.ok]
        log.info("Done. %d submitted, %d failed.", len(results) - len(failures), len(failures))
        for r in failures:
            log.info("FAILED: %s / %s -- %s", r.category, r.product, r.note)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--inspect", action="store_true", help="Dump dropdown DOM for debugging")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    asyncio.run(run(headed=args.headed, dry_run=args.dry_run, inspect_mode=args.inspect))


if __name__ == "__main__":
    main()
