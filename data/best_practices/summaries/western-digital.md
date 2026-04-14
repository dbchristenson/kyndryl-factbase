# Western Digital — Methodology Extraction (PCF source)

**Source file:** western-digital-hdd-example-pcf-with-methodology-explained.pdf
**Source type:** PCF with embedded methodology
**Product covered:** Ultrastar DC HC555 HDD (18 TB capacity)
**Document title:** Executive Summary - Ultrastar DC HC555 HDD
**Document date / version:** Not stated
**Total pages reviewed:** 1

---

## Note on source type

This extraction is from a PCF summary document (Product Carbon Footprint), not a standalone methodology document. Western Digital was included in this study because no dedicated methodology disclosure could be located. This single-page executive summary presents the PCF results with embedded methodology statements. Empty cells in the extraction below reflect the expected thinness of a PCF vs. a full methodology report and are findings about WD's disclosure depth.

---

## Group A — Explicit in Kyndryl draft

### A1. Goal of the study
**OEM content:** Support sustainability reporting and regulatory compliance efforts through transparent, ISO-14040/14044-compliant carbon footprint calculation. The document states the study "support[s] sustainability reporting and regulatory compliance efforts, providing transparency and accuracy essential for meeting current and future environmental regulations." (p. 1)
**Kyndryl draft:** Assess environmental impacts of IT hardware in Kyndryl's owned data centers, cradle-to-grave, to identify circularity improvement areas. Sub-goals: develop a baseline LCA methodology for IT data center hardware; inform Kyndryl's product sourcing decisions.
**Comparison:** Different. OEM goal is regulatory/compliance-driven disclosure; Kyndryl's goal is sourcing and circularity improvement. Both are descriptive (not comparative).

### A2. Intended audience & commissioner
**OEM content:** Calculated by Sluicebox (third-party tool provider); primary activity data supplied by Western Digital (product owner/manufacturer). Implied audience: regulatory, sustainability reporting, customer disclosure. No explicit commissioner named, but implicit commissioner is WD management. (p. 1)
**Kyndryl draft:** Designed for Kyndryl Holdings, Inc. Initiated by Northwestern University.
**Comparison:** Partially aligned on audience (both public/disclosure-facing), but different commissioners (WD vs. Kyndryl/Northwestern).

### A3. Product system / scope of hardware
**OEM content:** Ultrastar DC HC555 HDD — a data storage solution engineered for demanding environments of modern data centers. Treated as a single product unit, not decomposed into sub-components. (p. 1)
**Kyndryl draft:** IT hardware in Kyndryl's owned data centers. In scope: GPUs, rack servers, HDDs, SSDs.
**Comparison:** Aligned. Both cover HDDs as discrete products; WD's product is one specific HDD model.

### A4. Functional unit
**OEM content:** "One Ultrastar DC HC555 HDD with an 18 terabyte (TB) capacity and lifetime of five years. Results are provided per functional unit and 1 TB-year." (p. 1)
**Kyndryl draft:** "One hardware component operating for five years."
**Comparison:** Aligned on the 5-year lifetime and component-level FU. WD adds storage capacity (18 TB) and offers normalized results per TB-year as an alternative reference, which Kyndryl does not explicitly state.

### A5. System boundary — lifecycle stages
**OEM content:** "The system boundary follows a cradle-to-grave approach. The system boundaries encompass emissions from raw material extraction and processing, manufacturing of individual components, product assembly, upstream transportation to the factory gate, product use (based on 5-year product warranty), and end-of-life treatment and disposal. Key insights: the electricity using use phase and raw materials and manufacturing processes in the product phase contribute notably to the overall emissions." (p. 1)
**Kyndryl draft:** Cradle-to-grave: raw materials extraction, manufacturing, operating use, end-of-life. **Transportation explicitly excluded** due to data collection complexity.
**Comparison:** Different. OEM includes "upstream transportation to the factory gate"; Kyndryl explicitly excludes all transportation. Both include raw materials, manufacturing, use, and EoL. This is a material difference in scope.

### A6. Geographic boundary
**OEM content:** Not stated in document. Use-phase grid mix and manufacturing geography are not disclosed.
**Kyndryl draft:** Kyndryl-owned data center in Canada. Site-specific data from Project North Star.
**Comparison:** OEM silent. WD does not disclose geographic assumptions for grid mix or supply chain.

### A7. Allocation procedure
**OEM content:** Not stated in document.
**Kyndryl draft:** Economic allocation, based on market price of co-products.
**Comparison:** OEM silent. No allocation methodology disclosed.

### A8. Impact categories
**OEM content:** Climate change (kg CO₂e) explicitly reported. Document states "Results on the other impact categories are available in the full ISO report," implying water use, eutrophication, acidification, resource depletion, and/or other categories are calculated but not disclosed in this summary. (p. 1)
**Kyndryl draft:** Water use (m³), resource/energy use (MJ), climate change (kg CO₂e).
**Comparison:** Partially aligned. OEM reports climate (aligned with Kyndryl) and implies additional categories beyond Kyndryl's scope, but does not itemize them in this summary.

---

## Group B — Implied or partial in Kyndryl draft

### B1. Data sources — primary vs secondary
**OEM content:** "This study was calculated by Sluicebox, acting as the independent tool provider, using primary activity data supplied by Western Digital, the product owner and manufacturer of the product." (p. 1) Sluicebox uses a combination of primary data (from WD) and secondary data (background databases); the ratio is not disclosed. Database name not specified.
**Kyndryl draft:** Implied secondary. Kyndryl leverages existing OEM PCFs, not primary data collection.
**Comparison:** Different. WD uses primary data for foreground (product-level specs) + unspecified secondary data for background (supply chain, electricity). Kyndryl is downstream secondary user only.

### B2. Use-phase assumptions
**OEM content:** "Use phase emissions are modeled based on conventional energy usage in HDD applications. Actuals will vary depending on REC/CFE usage." Lifetime: 5 years (per functional unit). Power draw, grid mix (kg CO₂e/kWh), and utilization rate are not disclosed in this summary. (p. 1)
**Kyndryl draft:** Partial. 5-year lifetime stated. Implied Canada grid mix via Project North Star, but no explicit utilization rate, TDP, or workload assumption.
**Comparison:** Partially aligned on 5-year lifetime. Both leave power draw and grid mix unspecified in their primary documents. OEM adds a caveat about REC/CFE impact but no numbers.

### B3. End-of-life modeling approach
**OEM content:** "End-of-life treatment and disposal" is stated as in scope (p. 1), but the modeling approach—whether cut-off, avoided burden, recycled content credit, or PEF Circular Footprint Formula—is not disclosed in this summary.
**Kyndryl draft:** EoL is in scope, but the modeling approach (cut-off vs. recycled content vs. avoided burden) is not specified.
**Comparison:** Aligned. Both are silent on the specific EoL method; both confirm EoL is included.

---

## Group C — Not addressed in Kyndryl draft

### C1. Standards conformance
**OEM content:** "Sluicebox has been independently evaluated by TUV for ISO 14040 and ISO 14044. In this PCF summary, all values comply with ISO standards, ensuring that the carbon footprint calculations meet international requirements for product-level greenhouse gas (GHG) emissions assessments." (p. 1)
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM discloses. Conforms to ISO 14040 and ISO 14044; verified by TUV. No mention of ISO 14067 (PCF standard) explicitly, though the claim to GHG standards suggests alignment.

### C2. LCIA method (characterization model)
**OEM content:** Not stated in document. The model used to convert inventory to impact category scores is not named.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. No LCIA method name disclosed (e.g., IPCC AR5, ReCiPe, etc.).

### C3. Cut-off / completeness rules
**OEM content:** Not stated in document.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. No threshold (% mass, % energy, % cumulative) disclosed.

### C4. Temporal boundary / data vintage
**OEM content:** Not stated in document. Reference year of data is not disclosed.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. No data vintage or update cycle disclosed.

### C5. Data quality assessment
**OEM content:** Not stated in document. No pedigree matrix, qualitative narrative on data quality along ISO criteria, or commentary on time/geographic/technology representativeness is provided.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. WD relies on the TUV verification (C1) as implicit quality assurance but does not detail data quality assessment.

### C6. Uncertainty & sensitivity analysis
**OEM content:** Not stated in document. No Monte Carlo uncertainty, ± ranges, or sensitivity analysis disclosed.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. No quantified uncertainty or sensitivity results reported.

### C7. Critical review / third-party verification
**OEM content:** "Sluicebox has been independently evaluated by TUV for ISO 14040 and ISO 14044." (p. 1) TUV verification is mentioned; scope of review (methodology, data, both) is not specified. Reviewer name is TUV.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM discloses. Third-party verification present (TUV); review scope unclear.

### C8. Reporting transparency
**OEM content:** Transparency rating: **Low to Medium**. The executive summary provides high-level lifecycle stage breakdown (raw materials 8.2 kgCO₂e, manufacturing 14.4, packaging 0.3, distribution 9.4, use 146.3, EoL 0.1) and functional unit definition, but omits detailed bill-of-materials, specific power consumption values, grid mix assumptions, and background database details. Document states "Results on the other impact categories are available in the full ISO report," indicating detailed data exists but is not disclosed here.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM provides moderate transparency. Lifecycle breakdown is itemized numerically; broader assumptions are withheld or referred to fuller report.

### C9. Circularity-specific metrics
**OEM content:** Not stated in document. No recycled content %, recyclability %, reuse/refurbishment rate, design-for-disassembly, or take-back program disclosure in this PCF summary.
**Kyndryl draft:** [NOT STATED in goal/scope doc] — circularity is addressed through a separate qualitative analysis of vendor take-back programs.
**Comparison:** OEM silent. Absence is expected and is not a finding for this extraction.

---

## Gaps vs Kyndryl draft

- **B1 (Data sources):** WD discloses primary + secondary split and names the tool provider (Sluicebox); Kyndryl does not yet specify background database or data provenance ratios.
- **C1 (Standards conformance):** WD explicitly cites ISO 14040, ISO 14044, and third-party verifier (TUV); Kyndryl draft is silent on conformance claims.
- **C7 (Critical review / third-party verification):** WD reports TUV verification; Kyndryl draft does not yet address independent review.

---

## Goes beyond Kyndryl draft

- **A4 (Functional unit):** WD normalizes results to both per-unit and per-TB-year, providing flexibility for different use contexts (storage capacity scaling). Kyndryl's FU is per-component only.
- **B2 (Use-phase assumptions):** WD acknowledges REC/CFE impact variability on use-phase emissions, a nuance not yet in Kyndryl's draft.
- **C1 + C7 combined:** WD's dual disclosure of ISO conformance *and* independent TUV verification exceeds Kyndryl's current silence on audit-ability and trust mechanisms.

---

## Notable absences in OEM doc

- **A5 (System boundary — transportation):** OEM includes "upstream transportation to the factory gate," contradicting Kyndryl's explicit exclusion. This is a material methodological difference.
- **A6 (Geographic boundary):** No disclosure of grid mix region, manufacturing geography, or site-specific supply chain data. Kyndryl plans Canada/Project North Star site specificity, which is much more granular.
- **A7 (Allocation procedure):** No mention of how co-product burdens are split across lifecycle.
- **C2 (LCIA method):** No LCIA characterization model (IPCC AR5, ReCiPe, etc.) is named. Method used by Sluicebox is opaque.
- **C3 (Cut-off rules):** No threshold stated for inclusion/exclusion of minor flows.
- **C4 (Temporal boundary / data vintage):** No reference year or data currency disclosed. Unknown when WD's primary data was collected and when background databases were last updated.
- **C5 (Data quality assessment):** No qualitative or pedigree-based assessment of data representativeness provided beyond TUV's audit.
- **C6 (Uncertainty & sensitivity analysis):** No uncertainty ranges or sensitivity to key parameters reported.
- **B3 (EoL modeling approach specifics):** While EoL is in scope, whether WD uses avoided burden, recycled content credit, or cut-off is not stated.

---

## Direct quotes for citation

1. "One Ultrastar DC HC555 HDD with an 18 terabyte (TB) capacity and lifetime of five years. Results are provided per functional unit and 1 TB-year." (p. 1) — Functional unit definition.

2. "The system boundary follows a cradle-to-grave approach. The system boundaries encompass emissions from raw material extraction and processing, manufacturing of individual components, product assembly, upstream transportation to the factory gate, product use (based on 5-year product warranty), and end-of-life treatment and disposal." (p. 1) — System boundary (note: includes upstream transport).

3. "This study was calculated by Sluicebox, acting as the independent tool provider, using primary activity data supplied by Western Digital, the product owner and manufacturer of the product." (p. 1) — Data sources (primary from WD, tool by Sluicebox).

4. "Sluicebox has been independently evaluated by TUV for ISO 14040 and ISO 14044. In this PCF summary, all values comply with ISO standards, ensuring that the carbon footprint calculations meet international requirements for product-level greenhouse gas (GHG) emissions assessments." (p. 1) — Standards and third-party verification.

5. "The total carbon footprint for this product is 178.8 kgCO₂e, with the highest impact attributed to the use phase." (p. 1) — Primary result and lifecycle stage dominance (use phase).

6. "Use phase emissions are modeled based on conventional energy usage in HDD applications. Actuals will vary depending on REC/CFE usage." (p. 1) — Use-phase assumptions and variability caveat.

7. "Results on the other impact categories are available in the full ISO report." (p. 1) — Indication of other impact categories beyond climate, but no detail in this summary.

8. "Key insights: the electricity using use phase and raw materials and manufacturing processes in the product phase contribute notably to the overall emissions." (p. 1) — Lifecycle stage insights and dominance of manufacturing + use.
