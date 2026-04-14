# Mapping OEM Methodology Research to Deliverables 2–5

This document maps the findings from the per-OEM extractions (`summaries/*.md`) and the synthesis (`analysis/synthesis.md`) onto Kyndryl deliverables 2–5 from `data/deliverables.md`. The goal is to identify exactly which pieces of the OEM benchmarking research feed which deliverable, so the fact base can be reused without duplicating work.

Deliverables 1, 6, 7 are intentionally out of scope:
- **#1** (Current-State Circularity Assessment) is due 2026-03-09 and focuses on Kyndryl's own asset lifecycles, not OEM methodology.
- **#6** (Final Executive Presentation) is a repackaging layer, not a research input.
- **#7** (Research Repository) is the container this research already lives in.

Each deliverable section below answers four questions:
1. **What the deliverable is** (one sentence).
2. **What this research gives it** (specific findings that belong in the deliverable).
3. **Concrete content suggestions** (slides, table columns, KPI candidates).
4. **What is still missing** (what the OEM research *does not* cover, flagged so it can be scoped into another workstream).

---

## Deliverable #2 — Benchmarking & Policy Landscape Analysis

**Format:** PowerPoint. **Due:** Final presentation, May 29 – June 4, 2026 (TBD).

**What it is:** Identify best practices amongst hyperscalers, OEMs, and recyclers, and assess applicable standards/policies.

### What this research gives it

This is the deliverable the OEM research feeds most directly. The synthesis has already done the benchmark-assembly work for the "OEMs" portion of #2 — the seven per-OEM files plus the synthesis matrix are effectively the OEM benchmark. The remaining research effort for #2 is the hyperscaler and recycler tracks, plus the policy/standards track.

Specifically, this research provides:

- **A ready-made 19-dimension benchmark matrix** across 7 OEMs (`synthesis.md` § Synthesis matrix). Drop-in slide content.
- **Consensus tallies per dimension** (e.g., "6/7 OEMs cite ISO 14040+14044"; "5/7 have third-party verification"; "only HPE specifies PUE"). These are the quantitative hooks a benchmarking slide deck needs.
- **Per-OEM evidence files** (`summaries/*.md`) with page-cited direct quotes for citations.
- **Source-type findings** — NVIDIA and WD have no standalone methodology docs, only PCFs. That's itself a benchmarking finding about disclosure depth.
- **A policy/standards map** covering ISO 14040, 14044, 14067, 14025, 14064-3; GHG Protocol Product Standard; IEC 62921, IEC 62725; CML, ReCiPe, IPCC AR5/AR6 characterization models. Each is grounded to at least one OEM source.

### Concrete content suggestions

**Slide candidates for the OEM benchmarking section:**

1. **"How we built the benchmark"** — methodology transparency. 7 OEMs, 19 dimensions, source types (methodology docs vs PCFs), links to the per-OEM evidence files.
2. **"Heat map of OEM methodology disclosure"** — 19×7 grid, color-coded by "explicit / implicit / not stated." The synthesis matrix already provides this content; it just needs a visual rendering.
3. **"Where OEMs converge"** — the high-consensus dimensions:
   - ISO 14040+14044 (6/7)
   - Third-party verification (5/7)
   - Inclusion of transport (5/7)
   - Climate as the primary impact category (7/7)
4. **"Where OEMs diverge"** — the low-consensus dimensions:
   - Allocation procedure (only HPE explicit)
   - Cut-off rules (only HPE explicit)
   - Uncertainty quantification (only HPE explicit)
   - LCIA method naming (4/7 name it; IPCC and CML and ReCiPe all represented)
5. **"The HPE outlier"** — one slide framing HPE as the only OEM that addresses every dimension in the template. Use this to set the "what a fully-documented OEM methodology looks like" standard.
6. **"Industry standards landscape"** — a taxonomy slide: ISO 14040/14044 (LCA framework), ISO 14067 (product carbon footprint), ISO 14064-3 (GHG validation), IEC 62921 (streamlined CFP for ICT), IEC 62725 (ICT environmental information), GHG Protocol Product Standard, PEF, PAS 2050. Each with one-line definition and which of the 7 OEMs cites it.
7. **"OEM disclosure depth: methodology docs vs PCF-only"** — 5 OEMs publish standalone methodology docs; 2 (NVIDIA, WD) do not. Frame as a procurement-signal finding.
8. **"Kyndryl draft positioning"** — where Kyndryl's current draft sits on each high-consensus dimension (aligned / partially aligned / silent / divergent). The synthesis's Recommendations tables (`synthesis.md` §Recommendations summary) provide the underlying content.

**For the standards/policy section of #2:** The ISO and IEC standards cited across the OEM sample form a minimum viable policy landscape map. This research does NOT cover:
- Regulatory drivers (EU CSRD, EU Taxonomy, SEC climate disclosure, California SB-253/SB-261, EU Battery Regulation EoL requirements)
- Industry frameworks beyond what OEMs cite (SBTi, CDP, GRI, TCFD)
- Sector-specific guidance (ITU-T L.1410, L.1420; Climate Savers Computing)

Flag these as needing a separate policy-landscape pass before #2 is complete.

### What is still missing

- **Hyperscaler benchmarks** (AWS, Azure, Google, Meta). Their methodology disclosures (Azure Emissions Impact Dashboard, AWS Customer Carbon Footprint Tool, Google Environmental Report) are a separate research track not covered by this OEM study. They operate in a different role (downstream operator like Kyndryl, not upstream manufacturer), so their methodology choices may be more directly applicable to Kyndryl than the OEM sample.
- **Recycler / ITAD benchmarks** (Iron Mountain, Sims Lifecycle Services, TES-AMM, Relectronic-Remech). Their methodology for embodied-carbon credit on refurbished hardware is not covered here.
- **Policy / regulatory scan**. See the standards list above for what is and isn't in-scope from this research.

---

## Deliverable #3 — Opportunity Assessment & Prioritization Framework

**Format:** Excel model. **Due:** Final presentation, May 29 – June 4, 2026 (TBD).

**What it is:** Identify the highest-value areas for improvement based on environmental and financial impact.

### What this research gives it

The OEM research feeds #3 by identifying **where the methodology itself creates opportunities or constraints** — i.e., the gaps in OEM disclosure that either (a) block Kyndryl from computing an impact or (b) open up choices where Kyndryl can pick a preferred option. Every "gap vs Kyndryl draft" entry in a per-OEM summary is a candidate row in the Excel model.

The synthesis already groups these into a prioritized action list (`synthesis.md` §Recommendations summary), which can be lifted directly as the starting row set for the Excel model.

### Concrete content suggestions

**Structure the Excel model with at least these columns** (one row per opportunity):

| Column | Example value | Source |
|---|---|---|
| Opportunity ID | OPP-METHOD-001 | — |
| Category | Methodology / Vendor selection / Use-phase optimization / EoL / Standards | — |
| Description | Add PUE multiplier to use-phase model | `synthesis.md` rec #3 |
| Evidence OEMs | HPE p. 8 | `summaries/hpe.md` |
| Environmental impact potential | High (PUE is a 1.3–1.5× multiplier on use-phase emissions, which is >50% of total for most DC hardware) | Derived from WD p. 1 (use phase = 146.3 of 178.8 kgCO₂e) |
| Financial impact potential | Indirect (better data → better procurement) | Qualitative |
| Effort | Low (one parameter change) | — |
| Dependencies | Project North Star PUE data | — |
| Priority | High | — |

**Opportunity categories populated by this research:**

1. **Methodology gaps to close** (directly from `synthesis.md` §Recommendations summary → Add). 11 opportunities. Each has an evidence trail in the per-OEM files.
2. **Methodology choices to revisit** (from Recommendations → Modify). 3 opportunities: transport exclusion, economic allocation, energy/MJ categorization.
3. **Vendor selection opportunities** — derived from the OEM disclosure depth finding. Example rows:
   - "Prefer OEMs with standalone published methodology docs (HPE, Dell, Seagate, Samsung) over PCF-only disclosers (NVIDIA, WD)" — evidence: presence/absence of methodology doc in the sample
   - "Prefer OEMs with third-party verification" — evidence: 5/7 have verification
   - "Prefer OEMs conforming to ISO 14067" — evidence: HPE, NVIDIA, Samsung-cert
4. **Use-phase optimization opportunities** — these are the highest-value environmentally, since use phase dominates most PCF totals in the sample (WD: use = 82% of total; HPE notes use-phase emissions dominated by grid intensity; Dell shows Norway ~20 kg vs China ~240 kg for the same R750 server). Candidates:
   - PUE reduction at Kyndryl data centers (biggest single lever if site-measured)
   - Grid decarbonization / renewable procurement (direct lever on kg CO₂e/kWh)
   - Hardware utilization improvements (reduces absolute power draw per unit of service)
   - Lifetime extension (amortizes embodied carbon over more years)
5. **EoL opportunities** — the OEM sample gives thin evidence here. Only HPE quantifies EoL (80% recycle / 20% landfill, and even that is an assumption not a measurement). Kyndryl's parallel circularity workstream is better positioned to generate #3 rows in this category.

### What is still missing

- **Financial impact quantification.** The OEM research is entirely environmental; dollars are not in scope. #3 requires a cost-of-implementation and avoided-cost analysis layer on top of these findings.
- **Absolute impact magnitudes for Kyndryl's fleet.** This research tells you what each OEM discloses, not what Kyndryl's Canadian data center actually emits. Project North Star data and Kyndryl asset inventory are required to convert "opportunity identified" into "tCO₂e at stake."
- **Opportunities that live in operational practice** (e.g., right-sizing, workload consolidation, cooling optimization) rather than in methodology choices. These come from the data center operations workstream.

---

## Deliverable #4 — Business Case & Partner Engagement Strategy

**Format:** Word brief + PowerPoint summary. **Due:** Final presentation, May 29 – June 4, 2026 (TBD).

**What it is:** Quantification of economic + carbon benefits and a strategy to scale adoption across partner environments.

### What this research gives it

This is the weakest of the four mappings, but still real. The OEM research feeds #4 in two ways: (a) as **vendor selection criteria** for the partner engagement strategy (which OEMs to prioritize, on what grounds); and (b) as **carbon benefit quantification support** (how Kyndryl's methodology choices affect the numbers).

The research does NOT give #4 any financial numbers or partner relationship intelligence — those come from procurement and account management.

### Concrete content suggestions

**For the partner engagement strategy section, use this research to support:**

1. **Tiered OEM preference framework.** Build a ranking by disclosure quality using the synthesis matrix as the scoring rubric. Suggested tiers:
   - **Tier 1 (Preferred):** OEMs with standalone methodology doc + third-party verification + ISO 14067 conformance + named LCIA method. From this sample: HPE meets all four.
   - **Tier 2 (Acceptable):** Methodology doc + third-party verification, but lacks one of ISO 14067 / LCIA method. Dell, Seagate.
   - **Tier 3 (Conditional):** PCF only, some methodology disclosure. NVIDIA (has ISO 14067 + WSP review but no standalone methodology), WD (has TUV via Sluicebox tool but PCF-only).
   - **Tier 4 (Engagement target):** OEMs whose methodology is opaque or missing. Not represented in this sample, but any OEM Kyndryl encounters that publishes neither a methodology doc nor a verified PCF belongs here and should be the priority for engagement.
2. **Asks for partner engagement conversations.** When Kyndryl talks to OEMs about methodology disclosure, the synthesis tells you exactly what to ask for:
   - "Please provide a per-product PCF conformant to ISO 14067."
   - "Please disclose: allocation method, cut-off rule, LCIA characterization model, background database version, reference year, third-party review status." (These are the C-group dimensions where most OEMs are silent.)
   - "Please disclose use-phase assumptions explicitly: assumed lifetime, TDP, utilization, grid mix."
3. **Kyndryl's own credibility statement.** The business case is stronger if Kyndryl's methodology itself conforms to the same standards Kyndryl expects from OEMs. Recommendations #1, #2, #4, #9 from the synthesis (ISO conformance, named LCIA, EoL recipe, review status) directly serve this symmetry.

**For the carbon benefit quantification section:**

- **Sensitivity of the numbers to methodology choices.** Use Dell's regional variance example (R750 server: Norway ~20 kg CO₂e vs China ~240 kg CO₂e — 12× range from grid mix alone) to show that methodology and siting decisions can dominate the answer.
- **The use-phase dominance finding** (WD: use = 82% of total cradle-to-grave) to frame which levers have the highest carbon payoff.
- **The embodied-carbon distribution by component type** from NVIDIA (Memory 49%, ICs 28%, Thermals 12% for the HGX B200) to show where procurement-side interventions have the most upstream leverage.

### What is still missing

- **Cost data.** Procurement economics, renewable PPA pricing, refurbished-hardware price deltas, etc.
- **Partner relationship context.** Which OEMs Kyndryl has existing contracts with, which are open to engagement, which are regulatory-driven disclosers vs voluntary.
- **Adoption scaling strategy.** The OEM research tells you what good methodology looks like; it doesn't tell you how to get other partners to adopt it.
- **Stakeholder mapping.** Internal procurement, external OEM sustainability teams, regulators, customers.

---

## Deliverable #5 — Implementation Roadmap & KPIs

**Format:** PowerPoint + Excel KPI template. **Due:** Final presentation, May 29 – June 4, 2026 (TBD).

**What it is:** Phased roadmap with milestones, risks, required partnerships, and a starter KPI dashboard.

### What this research gives it

The OEM research informs #5 in two specific ways: (a) it defines **what measurable quantities OEMs actually disclose**, which bounds what Kyndryl can realistically put in a KPI dashboard using secondary data; and (b) it surfaces **risks** (methodology gaps, OEM disclosure inconsistencies) that should go in the roadmap as known issues.

### Concrete content suggestions

**Starter KPI candidates derived from the OEM sample.** These are quantities at least one OEM in the sample actually reports, so they are computable if Kyndryl consumes that OEM's PCFs:

| KPI | Unit | OEM precedent | Notes |
|---|---|---|---|
| Cradle-to-grave PCF per component | kg CO₂e / unit | HPE, WD, Seagate (all cradle-to-grave) | The flagship KPI. Requires OEM PCF consumption. |
| Cradle-to-gate embodied carbon per component | kg CO₂e / unit | NVIDIA, Samsung-cert (cradle-to-gate) | Available even when use/EoL not disclosed; Kyndryl extends with site-specific use phase. |
| Per-TB-year PCF (storage) | kg CO₂e / (TB·yr) | WD p. 1, Seagate p. 1 | Workload-normalized; enables generation-over-generation comparisons. |
| Use-phase share of total PCF | % | WD reports 82%; Dell shows regional variance; HPE shows dominance | Diagnostic, not a target. High use share → focus on PUE/grid; low use share → focus on embodied/procurement. |
| Contribution by lifecycle stage (materials / assembly / transport / use / EoL) | % | NVIDIA: 94/5.6/0.3; WD: itemized | Stage contribution breakdowns. |
| Contribution by component category (memory / ICs / thermals / PCBs / mechanicals) | % | NVIDIA p. 3 | Shows where embodied-carbon hotspots live; informs procurement engagement. |
| Fleet-weighted PUE | dimensionless | HPE uses PUE in use-phase model | Site-specific KPI; requires Project North Star data. |
| Grid carbon intensity at Kyndryl sites | kg CO₂e / kWh | HPE uses Ember Climate by country-year | Operational lever, not methodology lever. |
| % of procured OEM PCFs meeting minimum disclosure standard | % | Derived from synthesis rubric | Governance KPI. Set the bar at ISO 14067 + third-party verified + named LCIA method + stated allocation rule + reference year. |
| % of procurement (by $ or by unit count) from Tier 1 OEMs | % | From the vendor preference framework in #4 | Procurement-shift KPI. |
| Number of OEMs with a standalone methodology document | count | From the synthesis source list | Simple engagement-progress indicator. |

**Roadmap inputs from the research:**

1. **Phase 1 (early):** Close the high-priority methodology gaps from `synthesis.md` Recommendations — ISO conformance statement, LCIA method selection, PUE inclusion, EoL recipe. These are changes to the Kyndryl methodology document itself and can be done immediately, with no external dependencies.
2. **Phase 2 (mid):** OEM data acquisition. Build the intake process for OEM PCFs, define acceptance criteria (from the data-acceptance recommendation), and begin the OEM engagement conversations outlined in #4.
3. **Phase 3 (late):** Compute the KPI dashboard for a starter subset of Kyndryl's hardware fleet using acquired OEM PCFs + Project North Star use-phase data. Publish results internally, review, iterate.

**Known risks to flag in the roadmap:**

- **R1 — OEM disclosure inconsistency.** Each OEM reports to a different system boundary (cradle-to-grave vs cradle-to-gate), with different allocation procedures, different LCIA methods, and different functional units. Combining them into a Kyndryl-level KPI without harmonization will produce apples-to-oranges totals. Mitigation: require a minimum disclosure standard; normalize to Kyndryl's functional unit; document adjustments.
- **R2 — Missing PCFs.** Not every OEM publishes a PCF for every SKU. HPE's three-tier fallback (supplier PCF → custom attribute model → category average) is a proven template and should be adopted to handle gaps.
- **R3 — Methodology drift.** OEMs update their methodologies (HPE revision 3 is the latest; databases refresh annually). Any KPI built on today's OEM PCFs will need periodic refresh. Mitigation: pin the reference year in every Kyndryl calculation; re-baseline annually.
- **R4 — Transport exclusion could bias results.** Kyndryl's current draft excludes transport while 5 of 7 OEM PCFs include it. If Kyndryl consumes OEM values as-is, transport will be double-counted-out (the OEM included it but Kyndryl is "excluding" it — the PCF already has it baked in). This needs an explicit reconciliation rule.
- **R5 — Economic allocation mismatch.** Kyndryl states economic allocation but will be consuming OEM PCFs that use different (often unstated) allocation rules. Reconciliation is not possible without OEM disclosure.
- **R6 — Third-party review absent.** Kyndryl's methodology is not currently reviewed; 5/7 OEMs in the sample are. Reputational risk if the methodology is externally scrutinized. Mitigation: add a lightweight review step.
- **R7 — NVIDIA / PCF-only OEMs.** For these, Kyndryl cannot confirm methodology details; relying on their values means accepting opacity. Mitigation: flag in provenance metadata; weight results accordingly in sensitivity analysis.

### What is still missing

- **KPI targets.** The research suggests what to measure; it does not suggest where to set the target line. That requires Kyndryl-specific baselines and stakeholder agreement.
- **Implementation cost estimates** for each roadmap phase.
- **Governance structure** — who owns the KPI dashboard, cadence of updates, integration with existing sustainability reporting.
- **Tooling decisions** — OpenLCA, Sphera, ecoinvent licensing, etc.

---

## Cross-deliverable note: reusable artifacts

Three artifacts from this workstream are reusable across deliverables without modification:

1. **The 19-dimension comparison template** (`comparison_dimensions.md`) — rubric for any future OEM added to the benchmark.
2. **The synthesis matrix** (`synthesis.md` §Synthesis matrix) — the one-table benchmark view, drop-in for slides.
3. **The Recommendations tables** (`synthesis.md` §Recommendations summary) — drop-in for #2 (positioning Kyndryl vs industry), #3 (opportunity rows), #4 (methodology credibility statement), and #5 (Phase 1 roadmap items).

The seven per-OEM summary files are the citation library — every claim in every deliverable that references an OEM should cite back to the per-OEM file and its page reference.

## What to do next

Before starting any of deliverables 2–5:

1. **Commission the hyperscaler benchmarking pass** (AWS, Azure, Google, Meta). That research is the single biggest gap for #2. Operator-side methodology disclosures are more directly comparable to Kyndryl than vendor-side OEM PCFs and may reshape the recommendations.
2. **Commission the recycler / ITAD benchmarking pass** for #3 and #5.
3. **Resolve the open methodology decisions** flagged in the synthesis (transport exclusion, economic allocation, circularity handling) before the draft methodology goes into the benchmarking deck — otherwise #2 will benchmark Kyndryl against a moving target.
