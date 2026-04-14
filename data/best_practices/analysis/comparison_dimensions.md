# OEM Methodology Comparison — Dimensions

This document defines the dimensions used to compare OEM LCA/PCF methodologies against Kyndryl's draft goal & scope statement (`data/best_practices/kyndryl_goal_scope_definition.md`). It is the extraction template for Step 2 (per-OEM summaries) and the column spec for the synthesis matrix in Step 3.

For each dimension below:
- **Definition** — what the dimension means and why it matters for an LCA methodology.
- **Kyndryl draft** — verbatim or paraphrased content from the current draft. `[NOT STATED]` means the draft is silent on this dimension.
- **What to extract from each OEM** — the specific facts the per-OEM summary should record, with page citations.

Dimensions are grouped: (A) covered explicitly in Kyndryl's draft, (B) implied/partial, (C) not addressed.

---

## Group A — Explicit in Kyndryl draft

### A1. Goal of the study
- **Definition:** The decision the LCA is meant to support and the question it answers. ISO 14040 requires this be stated unambiguously.
- **Kyndryl draft:** Assess environmental impacts of IT hardware in Kyndryl's owned data centers, cradle-to-grave, to identify circularity improvement areas. Sub-goals: develop a baseline LCA methodology for IT data center hardware; inform Kyndryl's product sourcing decisions.
- **Extract:** OEM's stated goal (sustainability reporting, regulatory compliance, customer disclosure, internal product design, marketing claim?). Note whether the goal is comparative or descriptive.

### A2. Intended audience & commissioner
- **Definition:** Who the report is written for and who paid for it. Affects required rigor (third-party disclosure ≠ internal study).
- **Kyndryl draft:** Designed for Kyndryl Holdings, Inc. Initiated by Northwestern University.
- **Extract:** Audience (public, customers, regulators, internal). Commissioner. Whether the report is intended to support comparative assertions disclosed to the public (ISO 14044 §6.1 triggers stricter requirements if yes).

### A3. Product system / scope of hardware
- **Definition:** Which products/components are inside the system being studied.
- **Kyndryl draft:** IT hardware in Kyndryl's owned data centers. In scope: GPUs, rack servers, HDDs, SSDs.
- **Extract:** Which product(s) the OEM covers. Whether they treat sub-components separately (board, chassis, drives) or as one black box.

### A4. Functional unit
- **Definition:** The quantified performance of the product system, used as the reference for normalizing inputs and outputs. Must include performance, duration, and quality.
- **Kyndryl draft:** "One hardware component operating for five years."
- **Extract:** OEM's functional unit verbatim. Note whether it specifies (a) a service delivered (e.g., "1 TB-year of storage"), (b) a piece of equipment, or (c) is missing entirely. Flag mismatch with Kyndryl's 5-year assumption.

### A5. System boundary — lifecycle stages
- **Definition:** Which cradle-to-grave stages are included vs cut off.
- **Kyndryl draft:** Cradle-to-grave: raw materials extraction, manufacturing, operating use, end-of-life. **Transportation explicitly excluded** due to data collection complexity.
- **Extract:** Which stages OEM includes. Specifically check: raw materials, manufacturing, inbound transport, distribution transport, use phase, maintenance/spares, EoL collection, EoL processing. Flag any cut-offs and the OEM's stated reason.

### A6. Geographic boundary
- **Definition:** The geography assumed for grid mix, supply chain, and EoL infrastructure.
- **Kyndryl draft:** Kyndryl-owned data center in Canada. Site-specific data from Project North Star.
- **Extract:** Geography assumed for use phase (grid mix region) and for manufacturing supply chain. Whether OEM uses average global, regional, or site-specific data.

### A7. Allocation procedure
- **Definition:** How environmental burdens are split between co-products from the same process. ISO 14044 hierarchy: avoid by subdivision/expansion → physical relationships → other (e.g., economic).
- **Kyndryl draft:** Economic allocation, based on market price of co-products.
- **Extract:** OEM's stated allocation method. Whether they follow the ISO hierarchy or jump straight to economic. Whether they apply different rules at different lifecycle stages.

### A8. Impact categories
- **Definition:** The environmental indicators quantified. A full LCA covers many; a PCF covers only climate.
- **Kyndryl draft:** Water use (m³), resource/energy use (MJ), climate change (kg CO₂e).
- **Extract:** Full list of categories OEM reports. Note whether they go beyond climate (water, eutrophication, acidification, resource depletion, toxicity, land use). Note which LCIA characterization model they use (see C2).

---

## Group B — Implied or partial in Kyndryl draft

### B1. Data sources — primary vs secondary
- **Definition:** Whether the inventory data comes from supplier-measured (primary) or database-derived (secondary) sources. ISO 14044 requires this be reported.
- **Kyndryl draft:** Implied secondary. Draft says it "leverages existing Product Carbon Footprints for climate change impact calculations" — i.e., Kyndryl is a downstream user of OEM PCFs, not a primary data collector.
- **Extract:** OEM's primary/secondary data ratio. Background database used (ecoinvent v3.x, GaBi/Sphera, Idemat, IDEA). Cutoff year of data. Whether supplier-specific data is used for key inputs (e.g., wafer fab, PCB).

### B2. Use-phase assumptions
- **Definition:** Power draw, utilization rate, lifetime, grid carbon intensity — drivers of use-phase impact.
- **Kyndryl draft:** Partial. 5-year lifetime stated (via FU). Use-phase grid mix implied via Canada/Project North Star site data, but no explicit utilization rate, TDP, or workload assumption.
- **Extract:** OEM's assumed lifetime, average power draw, utilization/duty cycle, grid mix (kg CO₂e/kWh), and any thermal/cooling overhead (PUE-style multiplier).

### B3. End-of-life modeling approach
- **Definition:** How EoL credits and burdens are handled — cut-off, avoided burden / system expansion, or PEF Circular Footprint Formula.
- **Kyndryl draft:** EoL is in scope, but the modeling approach (cut-off vs recycled content vs avoided burden) is not specified.
- **Extract:** OEM's EoL approach. Recycling rate assumed. Whether they take credit for recycled content in inputs, recycling at EoL, or both (double-counting risk).

---

## Group C — Not addressed in Kyndryl draft

*If the analysis is complete and none of the OEMs include information about one of these categories, we can just remove the category I believe. Because Kyndryl will be almost entirely using secondary data, there is no way to get certain information if it is left out of reports.*

### C1. Standards conformance
- **Definition:** Which published standards/protocols the methodology claims to follow. Drives audit-ability and comparability.
- **Kyndryl draft:** [NOT STATED]
- **Extract:** Which of the following the OEM cites: ISO 14040, ISO 14044, ISO 14067 (carbon footprint of products), ISO 14025 (EPDs), GHG Protocol Product Standard, PAS 2050, PEF (Product Environmental Footprint), PCRs (product category rules). Note whether conformance is claimed vs verified.

### C2. LCIA method (characterization model)
- **Definition:** The model used to convert inventory flows into impact category scores. Different models give different numbers for the same inventory.
- **Kyndryl draft:** [NOT STATED] — categories listed but no characterization method named.
- **Extract:** Method name and version: IPCC AR5/AR6 GWP100, ReCiPe 2016, CML-IA, EF 3.1, TRACI 2.1, etc.

### C3. Cut-off / completeness rules
- **Definition:** Threshold below which inputs/outputs are excluded (e.g., <1% mass, <1% energy, <5% cumulative). Required by ISO 14044.
- **Kyndryl draft:** [NOT STATED]
- **Extract:** OEM's stated cut-off rule and any specifically excluded flows.

### C4. Temporal boundary / data vintage
- **Definition:** The reference year for foreground data and background databases. Distinct from the FU's 5-year operating period.
- **Kyndryl draft:** [NOT STATED]
- **Extract:** Reference year of OEM data. Whether they update annually.

### C5. Data quality assessment
- **Definition:** Documented evaluation of data along ISO 14044's quality criteria (time-, geographic-, technology-representativeness; precision; completeness; consistency).
- **Kyndryl draft:** [NOT STATED]
- **Extract:** Whether OEM uses a pedigree matrix, qualitative narrative, or nothing.

### C6. Uncertainty & sensitivity analysis
- **Definition:** Quantification of how uncertain the results are and which assumptions drive the answer.
- **Kyndryl draft:** [NOT STATED]
- **Extract:** Whether OEM reports Monte Carlo uncertainty, ± ranges, sensitivity to key parameters (lifetime, grid mix, utilization), or nothing.

### C7. Critical review / third-party verification
- **Definition:** Independent review of the LCA. ISO 14044 requires it for studies disclosed to the public with comparative assertions.
- **Kyndryl draft:** [NOT STATED]
- **Extract:** Whether OEM had the study reviewed. Reviewer name. Whether the review covers methodology, data, or both.

### C8. Reporting transparency
- **Definition:** Whether the OEM publishes the inventory, parameters, and assumptions in enough detail that the result could be reproduced.
- **Kyndryl draft:** [NOT STATED]
- **Extract:** Subjective rating (high / medium / low) with evidence. Specifically: are bill-of-materials, energy values, and EoL flows numerical and itemized, or only narrative?

### C9. Circularity-specific metrics (opportunistic — covered by parallel workstream)
- **Definition:** Metrics beyond impact categories that speak to circularity: recycled content %, recyclability %, reuse/refurb rate, design-for-disassembly, take-back program coverage.
- **Kyndryl draft:** [NOT STATED in goal/scope doc] — circularity is the study's purpose but is being addressed through a separate qualitative analysis of vendor take-back programs and annual sustainability reports, not through PCFs/LCAs.
- **Extract:** Record any circularity metrics that *happen* to appear in the PCF/LCA, but absence is expected and is **not** a finding. Anything substantive belongs in the parallel sustainability-report analysis, not here.

---

## How this becomes the synthesis matrix (Step 3)

For Step 3, this dimension list becomes the rows of a matrix; OEMs become the columns. Kyndryl's draft is column 1 (already filled in above). Each cell is a short tag (e.g., "ISO 14067, verified" / "not stated" / "ReCiPe 2016 H/A") with a citation back to the per-OEM summary.

The synthesis output answers three questions per dimension:
1. What's the consensus across OEMs?
2. Does Kyndryl's draft already match it?
3. Add / modify / remove recommendation, with evidence.

---

## Resolved scoping decisions

- **Group B (B1–B3) stays as "implied/partial."** All three are research targets — extraction should treat them with the same rigor as Group A.
- **C9 (circularity metrics) stays in Group C as opportunistic.** Circularity is being addressed through a parallel qualitative analysis of vendor take-back programs and annual sustainability reports. Absence in a PCF/LCA is expected and is not a finding.
- **PCF-only sources go through the same template as methodology docs.** Thinner extraction is expected; empty cells become evidence about that OEM's disclosure depth, not a template failure.
- **Pruning Group C dimensions:** If, after all OEM extractions are complete, no OEM reports a given Group C dimension, that dimension can be dropped from the final synthesis matrix. Rationale: Kyndryl will use almost entirely secondary data, so a dimension absent from every available report is unrecoverable and not actionable.
