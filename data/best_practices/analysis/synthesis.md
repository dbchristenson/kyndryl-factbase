# Synthesis — OEM LCA/PCF Methodology Comparison

This document synthesizes findings from seven per-OEM extractions against Kyndryl's draft goal & scope statement, organized around the dimensions defined in `comparison_dimensions.md`. For each dimension it answers three questions:

1. **What's the consensus across OEMs?**
2. **Does Kyndryl's draft already match it?**
3. **Add / Modify / Keep / Drop recommendation**, with the OEM evidence behind it.

## Sources

| Tag | OEM / Doc | Source type | Length | Per-OEM file |
|---|---|---|---|---|
| DELL | Dell PCF FAQs | Methodology doc | 6 pp | `summaries/dell.md` |
| HPE | HPE PCF Methodology | Methodology doc | 12 pp | `summaries/hpe.md` |
| NV | NVIDIA HGX B200 PCF | PCF (no standalone methodology found) | 4 pp | `summaries/nvidia.md` |
| SMSL | Samsung Galaxy Chromebook 3 LCA | LCA (pp 1–2 only — declarations repeat across SKUs) | 2 pp | `summaries/samsung-laptop.md` |
| SMSC | Samsung DS-PCF DNV Validation | 3rd-party verification certificate | 1 pp | `summaries/samsung-certificate.md` |
| SEA | Seagate Embodied Carbon white paper | Methodology doc | 1 pp | `summaries/seagate.md` |
| WD | Western Digital Ultrastar HC555 PCF | PCF (no standalone methodology found) | 1 pp | `summaries/western-digital.md` |

Two of the seven sources (NVIDIA, WD) are PCF reports rather than methodology docs because no standalone methodology document could be located for those OEMs. That fact is itself a finding about disclosure depth and is preserved in the per-OEM files.

The Samsung pair (SMSL methodology declarations + SMSC verification certificate) are treated as two independent sources rather than a single Samsung column, since they cover different products (laptop vs semiconductor wafer/die) and serve different purposes. SMSC is the verifier's statement about a separate Samsung Semiconductor methodology.

---

## Synthesis matrix

Cell tags are intentionally short. Read the per-OEM `summaries/*.md` files for the underlying evidence and page citations. `—` means the dimension is not stated in the source. `n/a` means the dimension is structurally inapplicable to the source's chosen scope (e.g., use phase for a cradle-to-gate study).

| Dim | Kyndryl draft | DELL | HPE | NV | SMSL | SMSC | SEA | WD |
|---|---|---|---|---|---|---|---|---|
| **A1 Goal** | Internal LCA baseline + sourcing | Customer disclosure + EPEAT | Customer disclosure + regulatory | Sustainability reporting | Product design + intl. standards | Verifier opinion | Customer purchasing decisions | Regulatory + sustainability |
| **A2 Audience** | Internal (Kyndryl) | Public + customers | Public + LCA practitioners | Public stakeholders | — | Public (verification) | Public | Public + regulators |
| **A3 Scope** | GPU, server, HDD, SSD | Notebooks → servers (incl. R750) | Servers, storage, networking | One GPU baseboard (HGX B200) | One Chromebook | Semiconductor wafer/die | HDD, SSD, tape | One HDD (Ultrastar HC555) |
| **A4 Functional unit** | 1 component × 5 yr | Per product, no FU | Per piece, no fixed lifetime | Per baseboard (no time) | Per device, 4 yr | Per wafer / per die | 5 yr referenced; per device, per TB, per TB-yr | 1 unit, 18 TB, 5 yr; per TB-yr offered |
| **A5 System boundary** | Cradle-to-grave; **transport excluded** | Cradle-to-grave incl. transport | Cradle-to-grave incl. transport; service/repair excluded | **Cradle-to-gate** (use + EoL excluded) | Cradle-to-grave incl. distribution | **Cradle-to-gate** | Cradle-to-grave | Cradle-to-grave incl. upstream transport |
| **A6 Geography** | Site-specific (Canada, Project North Star) | Country-specific use phase; mfg global | Global; country-year grid for use | — | Vietnam→Korea | — | — | — |
| **A7 Allocation** | Economic | — | Production-volume / mass at assembly | — | — | — | — | — |
| **A8 Impact categories** | Climate + water + energy (3) | Climate only (plans expansion) | Climate only | Climate only | **11 categories** (CML v4.8) | Climate only (GWP100) | 4 reported / 18 calculated (climate, human tox, water, mineral resources) | Climate (others "in full report") |
| **B1 Data sources** | Secondary OEM PCFs | PCF Calc (ISO 14040) + PAIA (IEC TR 62921); supplier BoM | IEA, ecoinvent v3.10, Ember, EPA + supplier PCFs via PACT | **90% primary by mass** + ecoinvent 3.10 + Sphera 2024 + imec net.zero | ecoinvent 3.10 (no year) | — | — | Primary from WD via Sluicebox tool |
| **B2 Use phase** | 5 yr lifetime; site grid implied | Country grid; config-dependent | Power measured; lifetime variable; **PUE multiplier**; country-year grid (Ember) | n/a (excluded) | 4 yr; no params | n/a | 5 yr; W and W/TB given; no grid | 5 yr; "conventional usage"; REC/CFE caveat |
| **B3 EoL approach** | In scope, approach unspecified | In scope, approach unspecified | **Cut-off; 80% recycled / 20% landfill by mass; 1000 km truck** | Excluded | In scope, approach unspecified | n/a | Mentions Circularity program; approach unspecified | In scope, approach unspecified |
| **C1 Standards** | — | ISO 14040; IEC TR 62921 (PAIA); ISO 14044 planned | **GHG Protocol Product, ISO 14067, ISO 14040, ISO 14044, IEC 62921, IEC 62725** | ISO 14067, 14040, 14044 | ISO 14040, 14044 | ISO 14040, 14067 (2018+2020), 14064-3, IPCC AR6 | ISO 14040, 14044 | ISO 14040, 14044 |
| **C2 LCIA method** | — | — | IPCC AR5 + AR6 GWP100 | Implicit GWP, unnamed | CML v4.8 + IPCC | IPCC 2021 AR6 | ReCiPe (GW only) + GHG Protocol | — |
| **C3 Cut-off rule** | — | — (implied via "hotspot" focus) | **5%** (excludes service/repair) | Implicit ~10% by mass | — | — | — | — |
| **C4 Temporal / vintage** | — | March 2024 doc; rolling updates | FY 2020 baseline; IEA 2023 ed.; ecoinvent v3.10 | 2024 background DBs | ecoinvent 3.10 (no year) | 2024 foreground; verified 28 Aug 2025 | 2025 doc; no data year | — |
| **C5 Data quality** | — | Std deviation for PAIA only | Multi-stage qualitative checks (manual + ML) | — | — | — | — | — |
| **C6 Uncertainty** | — | PAIA 5th/95th percentile | **First-order error propagation (Gaussian) per process** | — | Acknowledged, not quantified | — | — | — |
| **C7 3rd-party review** | — | Planned, not implemented | **DEKRA limited assurance** | **WSP critical review** | — (but see SMSC) | **DNV** (this IS the verification doc) | Auditor mentioned, unnamed | **TUV** (via Sluicebox tool) |
| **C8 Reporting transparency** | — | Medium; tools proprietary | Medium-high; methodology fully documented | Medium-high for a PCF; BoM + stage breakdown | Medium; results + categories shown | Low (1-page opinion) | Low-med; framework + worked example | Low-med; numerical stage breakdown |
| **C9 Circularity metrics** | — (handled by parallel workstream) | — | 80% recycled mass assumption (use in EoL model) | — | — | — | Circularity program named, no metrics | — |

---

## Findings by dimension group

### Group A — dimensions Kyndryl already addresses

**A1 Goal — divergent across OEMs.** No two OEMs share an identical goal statement. Kyndryl's goal (internal sourcing + circularity baseline) is distinctive: every OEM in the sample is producing disclosures *for* downstream customers, while Kyndryl is the downstream customer producing disclosures for itself. **No change needed**, but the synthesis should note that Kyndryl's role-reversal is unusual and should be stated explicitly in the goal so readers understand the methodology priorities differ from a vendor's PCF.

**A2 Audience — Kyndryl is the only "internal-only" study.** Six of seven OEM sources target external audiences (customers, regulators, EPEAT, certifiers). This is consistent with their commercial purpose. **No change needed.** Kyndryl's internal-only audience is appropriate to its goal but should be stated explicitly.

**A3 Product system — Kyndryl's scope is narrower and more specific.** Kyndryl names four component classes (GPU, rack server, HDD, SSD). Most OEMs cover their own product line; only HPE has a comparable component-class breadth. **No change needed.**

**A4 Functional unit — split between time-bounded and per-piece definitions.**
- **Includes a lifetime in the FU:** Kyndryl (5 yr), WD (5 yr, 18 TB), SMSL (4 yr), SEA (5 yr referenced). 4/8.
- **Per-piece, no lifetime:** HPE, DELL, NV, SMSC. 4/8.
- **Adds a service-based normalization (per-TB-year):** WD, SEA. 2/8.

Kyndryl's "1 component × 5 years" formulation is in the time-bounded camp and aligns directly with WD and SEA. The 5-year choice has direct precedent. **Recommendation: keep, but consider also offering a per-service-unit normalization (per TB-year for storage; per FLOPS-year for GPUs) as a secondary reporting unit.** WD and SEA both do this for storage, and for GPUs it would let Kyndryl compare hardware generations on a workload-normalized basis rather than per-box.

**A5 System boundary — Kyndryl's transportation exclusion is the strongest divergence from OEM practice.**
- **Cradle-to-grave including transport:** DELL, HPE, SMSL, SEA, WD. 5/7.
- **Cradle-to-gate (no use, no EoL):** NV, SMSC. 2/7.
- **Cradle-to-grave excluding transport:** Kyndryl alone.

Five of seven OEMs include transport. NVIDIA, despite being cradle-to-gate, includes inbound transport and reports it as 0.3% of total — empirical evidence that transport is small but non-zero and tractable to model. **Recommendation: revisit the transportation exclusion.** The original justification ("complexities in data collection") may be overstated given that OEMs routinely model inbound transport with simple distance × mode assumptions (HPE uses a default 1000 km × truck for EoL transport, p. 8). At minimum, document the materiality threshold: if transport is reliably <1% of total impact across the OEM PCFs Kyndryl will be reusing, the exclusion is defensible; otherwise it should be added back.

Worth flagging: NVIDIA explicitly excludes use phase and EoL "due to the variability in those emissions based on customer usage." This is the inverse of Kyndryl's choice. Since Kyndryl has site-specific use-phase data (Project North Star), it sidesteps NVIDIA's variability problem and can extend NVIDIA cradle-to-gate values into a full cradle-to-grave assessment by adding Kyndryl-specific use + EoL on top.

**A6 Geographic boundary — Kyndryl is the most granular in the sample.** No OEM uses site-specific data; the most granular is HPE's "country-year" grid mix from Ember Climate. Kyndryl's Project North Star site data is more precise than any OEM source. **No change needed.** This is a methodological strength worth highlighting in deliverables.

**A7 Allocation — Kyndryl is alone in stating an allocation rule.** Only HPE explicitly describes any allocation procedure (production-volume / mass at the assembly stage); everyone else is silent. Kyndryl's stated economic allocation has no direct OEM precedent in this sample. **Recommendation: revisit this choice.** Economic allocation is the lowest tier in the ISO 14044 hierarchy (avoid → physical → other). HPE's mass/production-volume approach is higher in the hierarchy and is the only OEM example available. Either (a) justify why economic is preferred for Kyndryl's specific use case, or (b) align with HPE's mass-based approach for ISO conformance.

**A8 Impact categories — Kyndryl sits between climate-only and full-LCA OEMs.**
- **Climate only:** DELL, HPE, NV, SMSC, WD. 5/7.
- **3 categories (Kyndryl):** climate, water, energy. Closest match: SEA reports 4 (climate, human toxicity, water, mineral resources), Kyndryl 3 (climate, water, energy/MJ).
- **Many categories:** SMSL reports 11 (CML v4.8); SEA calculates 18 internally.

Kyndryl's three-category set is broader than the climate-only majority but still narrower than what OEMs publishing full LCAs (SMSL, SEA) cover. **No change needed for current scope.** If Kyndryl later wants to support broader impact reporting, the SMSL 11-category set is a ready precedent and ecoinvent 3.10 provides the inventory data to compute it. Note: Kyndryl's "resource/energy use (MJ)" is not a standard impact category — it's an inventory metric, not characterized output. Worth clarifying whether Kyndryl wants Cumulative Energy Demand (CED) or a resource-depletion category like Mineral Resource Scarcity (which SEA reports).

### Group B — dimensions Kyndryl partially addresses

**B1 Data sources — Kyndryl will be a downstream secondary user; this is unusual but defensible.** Most OEMs in the sample combine primary supplier data with secondary background databases. NVIDIA goes furthest, with primary data covering 90% of product mass. Kyndryl's plan to consume OEM PCFs as inputs is reasonable given the lack of supplier relationships, but it inherits all the gaps the OEMs leave (no allocation disclosure, no LCIA method named, no uncertainty bounds — see C2/C6). **Recommendation: state Kyndryl's data strategy explicitly in the methodology, including which OEM PCFs will be accepted, what minimum disclosure standard is required (e.g., ISO 14067 conformance), and what to do when an OEM PCF is missing.** HPE's three-tier fallback (primary supplier PCF → custom attribute model → category-average) is a useful template.

Background databases that recur across OEMs: **ecoinvent v3.10** (HPE, NVIDIA, SMSL — 3/7), **Sphera Pro 2024 + Electronics Extension XI** (NVIDIA — 1/7), **IEA / Ember Climate** for grid mix (HPE — 1/7), **imec net.zero** for fab-related emissions (NVIDIA — 1/7). **Recommendation: name ecoinvent v3.10 as the default background database** and Ember Climate (by country and year) for grid mix. Both have clear precedent and Ember's data are free.

**B2 Use phase — Kyndryl has the right anchor (5 yr + Canadian site) but no parameters yet.** The most detailed use-phase model in the sample is HPE's: power measured per product, country-year grid mix from Ember, **Power Usage Effectiveness (PUE) multiplier applied** (p. 8). No other OEM in the sample mentions PUE. Since Kyndryl is modeling data center hardware in Kyndryl-owned data centers, **PUE is essential and currently missing from the draft.** **Recommendation: add PUE multiplier to the use-phase model.** The Project North Star data should provide site-specific PUE; if not, an industry default (~1.4–1.5 for modern data centers) is defensible.

Kyndryl also needs to specify TDP, average utilization, and duty cycle — none of which are in any OEM source except HPE. These are Kyndryl-internal decisions that should be documented in the methodology.

**B3 EoL — only HPE has an explicit modeling approach.** The five OEMs covering EoL all "include" it but don't say how. HPE alone gives a complete recipe: **cut-off method, 80% recycled / 20% landfill by mass, 1000 km truck transport** (p. 8). No avoided-burden or recycled-content credits. **Recommendation: adopt HPE's cut-off + 80/20 mass split as the Kyndryl default**, since (a) it's the only documented approach in the sample, (b) cut-off is the simplest to implement and least prone to double-counting, and (c) Kyndryl's parallel circularity workstream will handle any avoided-burden or refurbishment credits separately. If Kyndryl-Canada-specific recycling rates are available from Project North Star or local infrastructure, use those instead of 80/20.

### Group C — dimensions absent from Kyndryl draft

**C1 Standards conformance — strongest consensus in the sample.** **6 of 7 OEM sources cite ISO 14040 + 14044 explicitly** (Dell cites only 14040; Dell plans to add 14044). Three of seven also cite ISO 14067 (the carbon footprint of products standard). HPE alone cites GHG Protocol Product Standard, IEC 62921 (streamlined CFP for ICT), and IEC 62725. **Recommendation: add explicit ISO 14040 + ISO 14044 conformance to Kyndryl's methodology.** This is the single highest-leverage addition: it costs nothing, signals rigor, and is the universal currency of LCA disclosure. ISO 14067 is also worth adding given that 3 OEMs cite it and it's specifically the PCF standard.

**C2 LCIA method — partial consensus on IPCC for climate, no consensus elsewhere.**
- **IPCC GWP100 (AR5 or AR6):** HPE, SMSC, SMSL (via CML+IPCC), NV (implicit). 4/7.
- **CML v4.8:** SMSL alone uses for non-climate categories.
- **ReCiPe:** SEA uses for climate ("213 elementary flows ReCiPe characterizes as GHGs").

**Recommendation: name IPCC AR6 GWP100 as the climate characterization method.** This is the most current and is what the most rigorous OEM source (SMSC, DNV-verified) uses. For water and energy, Kyndryl needs to pick a method — ReCiPe 2016 (SEA's choice) covers all of Kyndryl's three categories and is the most common LCIA method in current LCA practice. **Add: "LCIA method: IPCC AR6 GWP100 for climate; ReCiPe 2016 (H/A) for all other categories."**

**C3 Cut-off rule — only HPE explicit.** HPE uses a 5% threshold and excludes service/repair below it. NVIDIA implies ~10% by mass via its "primary data covers 90%" statement. **Recommendation: adopt a 5% cumulative cut-off rule** matching HPE. This is also consistent with PEF guidance and ISO 14044's expectation that any cut-off be stated explicitly.

**C4 Temporal boundary / data vintage — fragmented but several OEMs name a year.** HPE: FY2020 baseline + IEA 2023 + ecoinvent v3.10. NV/SMSC: 2024 background. **Recommendation: state the reference year for foreground data and pin background database versions** (e.g., "Foreground data: 2025. Background: ecoinvent v3.10, Ember Climate 2024 grid mix"). Without this, results aren't reproducible.

**C5 Data quality assessment — only HPE.** HPE describes multi-stage qualitative checks. No pedigree matrix appears in any source. **Per the prune-if-empty rule this is borderline,** but since HPE's example exists and ISO 14044 requires data quality discussion, **keep as a dimension and recommend Kyndryl describe its quality checks qualitatively** (e.g., "OEM PCFs accepted only if ISO 14067 conformant; spot-checked for consistency with public ranges; flagged for follow-up if outliers"). A formal pedigree matrix is overkill for a secondary-data study.

**C6 Uncertainty & sensitivity — HPE has the only quantitative method.** HPE: first-order error propagation, percent uncertainty per unit process, summed in quadrature. Dell: PAIA 5th/95th percentile. **Recommendation: at minimum, do sensitivity analysis on the parameters Kyndryl controls** (5-year lifetime, PUE, grid mix, allocation choice). Full uncertainty propagation requires per-input variance data that secondary OEM PCFs typically don't disclose, so this may be impractical. State the limitation.

**C7 Critical review / third-party verification — strong OEM consensus.** **5 of 7 sources have explicit third-party verification** (HPE-DEKRA, NV-WSP, SMSC-DNV, SEA-unnamed auditor, WD-TUV via Sluicebox). Dell has it planned but not implemented. **Recommendation: decide whether Kyndryl wants third-party review of its methodology.** Given Kyndryl's audience is internal, full ISO 14044 critical review may not be required. However, even an internal peer review or academic review (Northwestern is involved) would close this gap and is cheap insurance against methodology errors. **Add a "review status" line to the methodology** stating what review has been conducted and by whom.

**C8 Reporting transparency — high variance.** HPE and NV are the most transparent in the sample; SMSC (a 1-page opinion) is the least. Not actionable as a Kyndryl methodology decision; this is an OEM-selection criterion (Kyndryl should prefer to consume PCFs from OEMs with high reporting transparency).

**C9 Circularity-specific metrics — silent across the sample, as expected.** Only HPE has a recycling rate (80%, used in EoL modeling, not as a standalone metric). SEA mentions a Circularity program but quantifies nothing. **Per scope decision, this dimension is intentionally not addressed in PCFs/LCAs and is being handled by Kyndryl's parallel qualitative workstream on take-back programs and sustainability reports. Drop from this matrix in the deliverable version**, but retain in the working dimension list as a reminder to cross-check the parallel workstream.

---

## Recommendations summary

### Add to Kyndryl draft

| # | Addition | Evidence | Priority |
|---|---|---|---|
| 1 | **ISO 14040 + 14044 conformance statement.** Add ISO 14067 if PCF-style outputs are intended. | 6/7 OEMs cite 14040+14044; 3/7 cite 14067. Universal LCA practice. | **High** |
| 2 | **LCIA method: IPCC AR6 GWP100 for climate; ReCiPe 2016 (H/A) for water + energy.** | HPE, SMSC use IPCC AR5/AR6; SEA uses ReCiPe; SMSL uses CML+IPCC. | **High** |
| 3 | **PUE multiplier in use-phase model.** | HPE alone uses it (p. 8); essential for any data-center-resident hardware. | **High** |
| 4 | **EoL modeling recipe: cut-off, 80% recycled / 20% landfill by mass.** Override with Project North Star site data if available. | Only HPE has an explicit recipe; cut-off is simplest and double-count-safe. | **High** |
| 5 | **Cut-off rule: 5% cumulative.** | HPE explicit (p. 5); ISO 14044 requires cut-off to be stated. | Medium |
| 6 | **Reference year for foreground data + pinned background database versions.** Recommend ecoinvent v3.10 + Ember Climate by country-year. | HPE, NV, SMSC, SMSL all cite specific DB versions. | Medium |
| 7 | **TDP, utilization rate, duty cycle assumptions** for each component class. | None of the OEMs document these beyond HPE; Kyndryl must define them itself. | Medium |
| 8 | **Per-service-unit reporting** (per TB-year for storage; consider per-FLOPS-year for GPUs) as a secondary normalization alongside per-component. | WD and SEA both report per TB-year; enables workload-normalized comparisons. | Medium |
| 9 | **Review status statement** — even an internal/academic review at Northwestern, documented in the methodology. | 5/7 OEMs have explicit third-party review. | Medium |
| 10 | **Sensitivity analysis on Kyndryl-controlled parameters** (5-year lifetime, PUE, grid mix, allocation choice). | HPE Gaussian propagation; Dell PAIA percentiles. Full uncertainty propagation impractical with secondary data. | Low |
| 11 | **Data acceptance criteria for OEM PCFs** (which standards must they conform to, what to do when missing, fallback hierarchy). | HPE's three-tier fallback (primary → attribute model → category average) is the template. | Low |

### Modify in Kyndryl draft

| # | Current draft | Recommended modification | Evidence |
|---|---|---|---|
| 12 | Transportation explicitly excluded "due to data collection complexity." | **Re-evaluate.** Either include transport with default assumptions (HPE uses 1000 km × truck for EoL; NVIDIA reports inbound transport at 0.3%), or document the materiality test that justified the exclusion. | 5/7 OEMs include transport. |
| 13 | Allocation: economic, based on market price. | **Justify or switch.** Economic is the lowest tier in the ISO 14044 hierarchy. The only OEM with explicit allocation (HPE) uses production-volume / mass. Either explain why economic suits Kyndryl's case or align with HPE. | HPE p. 5; ISO 14044 §4.3.4.2. |
| 14 | Impact categories include "resource or energy use (MJ)." | **Clarify what this is.** MJ is an inventory metric, not a characterized impact category. Likely intended as Cumulative Energy Demand (CED). State explicitly. | Standard LCA terminology. |

### Keep as-is (deliberate divergence from OEM norm)

| # | Kyndryl choice | Why keep | Note |
|---|---|---|---|
| 15 | Internal-only audience, university-initiated | Matches Kyndryl's role as downstream operator, not vendor | State explicitly so readers know to expect operator-side priorities |
| 16 | Site-specific (Canada / Project North Star) geography | More granular than any OEM source; methodological strength | Highlight in deliverables |
| 17 | 5-year functional unit lifetime | Direct precedent in WD and SEA | — |
| 18 | Goal includes circularity (handled by parallel workstream) | Right separation of concerns: PCFs/LCAs don't carry circularity metrics | Cross-check parallel workstream covers this |

### Drop from comparison template

| # | Dimension | Reason |
|---|---|---|
| 19 | C9 Circularity metrics — drop from final deliverable matrix | Per scope decision, handled by parallel qualitative workstream. Keep in working notes only. |

C5 (Data Quality) and C8 (Reporting Transparency) are borderline per the prune-if-empty rule (1/7 and variable respectively) but are kept because both feed actionable Kyndryl decisions: C5 informs the data acceptance criteria recommendation (#11), and C8 informs OEM selection criteria for the deliverables.

---

## Cross-cutting findings

1. **HPE is the gold standard in this sample.** It is the only OEM document that addresses every dimension in the template, and it should be the primary reference when Kyndryl drafts its own methodology updates. Half of the high-priority recommendations above derive from HPE alone (ISO conformance, IPCC characterization, PUE, EoL recipe, cut-off rule, uncertainty quantification).

2. **PCF reports are systematically thinner than methodology docs**, as expected. NVIDIA and WD (PCF sources) leave more dimensions silent than the methodology docs from HPE, Dell, Seagate. The thinness is itself a finding about disclosure depth — both NVIDIA and WD were included specifically because no standalone methodology doc could be found for them. This is a real signal: when Kyndryl evaluates OEMs, "publishes a public methodology document" is itself a quality criterion separate from PCF availability.

3. **Third-party verification is the clearest "table stakes" practice in the OEM sample.** Five of seven sources (HPE, NV, SMSC, SEA, WD) explicitly disclose third-party review; Dell has it planned. Kyndryl is the only entity in the sample with no review mechanism stated. Even a lightweight internal/academic review would close this gap and align with industry norm at very low cost.

4. **Use-phase modeling is the area with the largest gap between what OEMs disclose and what Kyndryl needs.** No OEM gives Kyndryl off-the-shelf use-phase parameters for data center operation. HPE comes closest by including PUE and country-year grid mix, but TDP, utilization, and duty cycle are Kyndryl's own homework regardless of OEM disclosure quality. This is the work Kyndryl will most need Project North Star for.

5. **The transportation exclusion in the Kyndryl draft is the only major scope choice that diverges from majority OEM practice.** Worth reopening — see recommendation #12.

6. **Kyndryl's economic allocation choice is unsupported by direct OEM precedent in this sample.** Worth reopening — see recommendation #13.

7. **A note on the Samsung pair:** SMSL (laptop LCA) and SMSC (DS-PCF verification) cover unrelated Samsung products and weren't designed to be read together. The SMSC document is the most rigorously verified source in the sample (DNV, ISO 14040+14067+14064-3, IPCC AR6) and proves Samsung Semiconductor takes LCA methodology seriously, but it tells you almost nothing about *what* the methodology is. This is a structural feature of verification certificates and is reflected in C8 (Reporting Transparency = Low).

---

## What this synthesis does not cover

- **Numerical PCF values for specific products.** A few sources (NVIDIA's 2,274 kg CO₂e for HGX B200; WD's 178.8 kg CO₂e for HC555 HDD) include results, but the synthesis is about methodology, not benchmarks. If Kyndryl wants a benchmark library, it would be a separate workstream and would require many more product-specific PCFs.
- **Vendor circularity programs** (take-back, refurbishment, resale rates). Per scope decision, these are in the parallel qualitative workstream.
- **Cost / economic analysis of LCA methodology choices.** The brief is environmental methodology, not cost-of-implementation.
- **Sensitivity of results to Kyndryl's specific parameter choices.** That's a downstream analysis once the methodology is fixed.
