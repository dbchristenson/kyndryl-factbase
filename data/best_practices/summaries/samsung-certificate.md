# Samsung Independent Verification Certificate — Methodology Extraction

**Source file:** samsung-pcf-methodology-independent-certificate.pdf
**Source type:** Third-party verification certificate
**Verifier organization:** DNV Business Assurance Korea Ltd.
**Document title:** Independent Validation Opinion
**Document date / version:** 28 August 2025
**Total pages reviewed:** 1

> **Source-type note:** This document is a verification statement — it certifies that Samsung Semiconductor's DS-PCF System meets specified standards, rather than describing the methodology itself. Most dimensions of the comparison template will be `Not stated`, because the verifier reports on what was checked and their conclusions, not on the underlying methodology details. The most useful rows are C1 (standards verified against), C7 (third-party verification details), and C3 (cut-off rules mentioned in validation scope).

## Group A — Explicit in Kyndryl draft

### A1. Goal of the study
**OEM content:** The validation assesses the DS-PCF System of Samsung Semiconductor, which was developed in accordance with principles and requirements of footprint calculation considering the LCA of the products, and the DS-PCF System (p. 1).
**Kyndryl draft:** Assess environmental impacts of IT hardware in Kyndryl's owned data centers, cradle-to-grave, to identify circularity improvement areas. Sub-goals: develop a baseline LCA methodology for IT data center hardware; inform Kyndryl's product sourcing decisions.
**Comparison:** Different scope. OEM validation covers Samsung's DS-PCF System methodology and data for semiconductor products; Kyndryl's goal is to assess IT hardware (GPUs, servers, drives) in owned data centers.

### A2. Intended audience & commissioner
**OEM content:** DNV Business Assurance Korea Ltd. was commissioned by Samsung Electronics Co., Ltd. Device Solutions to perform validation of Product Carbon Footprint Calculation and its Reporting System (p. 1). The validation is described as a third-party independent verification.
**Kyndryl draft:** Designed for Kyndryl Holdings, Inc. Initiated by Northwestern University.
**Comparison:** Different. This is a third-party verification commissioned by Samsung for independent credibility. Kyndryl's study is internal to Kyndryl, initiated by Northwestern University.

### A3. Product system / scope of hardware
**OEM content:** The validation assesses the DS-PCF System for semiconductor products: Functional Unit is "Water (per 8" and 12" wafer) and Die" and covers FAB, Water and Chemical Module; Process: Semiconductor Manufacturing Process; System Boundary: Cradle-to-Gate (p. 1).
**Kyndryl draft:** IT hardware in Kyndryl's owned data centers. In scope: GPUs, rack servers, HDDs, SSDs.
**Comparison:** Different. OEM covers semiconductor wafer and die manufacturing (upstream component); Kyndryl covers finished IT hardware products.

### A4. Functional unit
**OEM content:** "Water (per 8" and 12" wafer) and Die" (p. 1).
**Kyndryl draft:** "One hardware component operating for five years."
**Comparison:** Different. OEM's FU is component quantity (wafer/die); Kyndryl's includes temporal and operational dimensions (5-year operation).

### A5. System boundary — lifecycle stages
**OEM content:** System Boundary listed as "Cradle-to-Gate" (p. 1). The validation scope includes "Functional Unit" assessment and "System Boundary: Cradle-to-Gate" (p. 1). The validations assessed the DS-PCF System based on the LCA Report and the conversion (procedures for PCF calculation) and reporting by assessing actual and projected data (p. 1).
**Kyndryl draft:** Cradle-to-grave: raw materials extraction, manufacturing, operating use, end-of-life. Transportation explicitly excluded due to data collection complexity.
**Comparison:** Different. OEM's system boundary is Cradle-to-Gate (manufacturing only, no use phase or EoL); Kyndryl includes cradle-to-grave but excludes transportation.

### A6. Geographic boundary
**OEM content:** Not stated explicitly in the validation certificate. Geographic location mentioned only in the signature block: "Seoul, Korea" and reference to Samsung Semiconductor sites in Korea and USA (p. 1, footnote).
**Kyndryl draft:** Kyndryl-owned data center in Canada. Site-specific data from Project North Star.
**Comparison:** Not directly comparable. OEM geographic data not disclosed in this validation document.

### A7. Allocation procedure
**OEM content:** Not stated in the validation certificate.
**Kyndryl draft:** Economic allocation, based on market price of co-products.
**Comparison:** OEM silent on allocation procedure in this document.

### A8. Impact categories
**OEM content:** Impact Category listed as "Global Warming Potential (GWP100)" and "Impact Assessment Methodology: IPCC 2021 AR6" (p. 1).
**Kyndryl draft:** Water use (m³), resource/energy use (MJ), climate change (kg CO₂e).
**Comparison:** Partially aligned. OEM reports climate change only (GWP via IPCC 2021 AR6); Kyndryl includes water and energy as well.

---

## Group B — Implied or partial in Kyndryl draft

### B1. Data sources — primary vs secondary
**OEM content:** The validation assessed data input, conversion (procedures for PCF calculation) and output based on the LCA Report. DNV does not offer guarantee of reliability of PCF result of the DS-PCF System; actual PCF output result will depend on accuracy of the data input provided by Samsung Semiconductor (p. 1).
**Kyndryl draft:** Implied secondary. Kyndryl leverages existing Product Carbon Footprints.
**Comparison:** Partially stated. Document implies Samsung provides data inputs; verifier assessed the data processing but did not guarantee data accuracy.

### B2. Use-phase assumptions
**OEM content:** Not stated in the validation certificate. System boundary is Cradle-to-Gate, so no use-phase assumptions apply to the scope being verified.
**Kyndryl draft:** Partial. 5-year lifetime stated via FU. Use-phase grid mix implied via Canada/Project North Star, but no explicit utilization rate, TDP, or workload assumption.
**Comparison:** OEM's Cradle-to-Gate boundary excludes use phase; not comparable to Kyndryl's cradle-to-grave with explicit use-phase assumptions.

### B3. End-of-life modeling approach
**OEM content:** Not stated in the validation certificate. System boundary is Cradle-to-Gate; EoL is not included.
**Kyndryl draft:** EoL is in scope, but the modeling approach (cut-off vs recycled content vs avoided burden) is not specified.
**Comparison:** OEM's Cradle-to-Gate boundary excludes EoL; not comparable to Kyndryl's inclusion of EoL.

---

## Group C — Not addressed in Kyndryl draft

### C1. Standards conformance
**OEM content:** The validation assessed the DS-PCF System "in accordance with the principles and requirements of ISO 14040 and ISO 14067 2020; ISO 14067 2018 and 'LCA Report'." Also references "GreenHouse Gas (GHG) calculation principles of ISO 14064-3:2019 (Part 3) Specification" and "General principles and requirements: IPCC 2021 AR6" (p. 1).
**Kyndryl draft:** [NOT STATED]
**Comparison:** Aligned—OEM claims conformance to ISO 14040, ISO 14067 (2020 and 2018), ISO 14064-3, and IPCC 2021 AR6. These are third-party verified.

### C2. LCIA method (characterization model)
**OEM content:** Impact Assessment Methodology: IPCC 2021 AR6 (p. 1).
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM explicitly uses IPCC 2021 AR6 for GWP characterization. Kyndryl draft does not specify a characterization model.

### C3. Cut-off / completeness rules
**OEM content:** Not explicitly stated as a cut-off threshold in the validation certificate. However, the scope mentions "actual and projected data of 2024 such as amount of raw materials input, energy use, waste and energy consumption of Outsourced Semiconductor Foundry and Test processing" (p. 1), implying data inclusion is based on material flows and energy consumption captured in 2024 data.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM's cut-off rule not explicitly stated in this validation document.

### C4. Temporal boundary / data vintage
**OEM content:** Data vintage of 2024 is mentioned: "actual and projected data of 2024" (p. 1). Validation date is 28 August 2025.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM uses 2024 as reference year for foreground data; Kyndryl's temporal boundary is not stated.

### C5. Data quality assessment
**OEM content:** Not stated in the validation certificate. The verifier notes that "DNV assurance engagement is based on the engagement for the data and information provided by Samsung" and states responsibility for gathering and processing activity data, but no formal data quality assessment methodology (pedigree matrix or narrative) is described (p. 1, "Responsibilities" box).
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM's data quality assessment methodology not disclosed in this validation document.

### C6. Uncertainty & sensitivity analysis
**OEM content:** Not stated in the validation certificate.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM's uncertainty or sensitivity analysis not disclosed in this validation document.

### C7. Critical review / third-party verification
**OEM content:** This document IS the third-party verification. DNV Business Assurance Korea Ltd. performed the independent validation. The validation assessed the DS-PCF System's validity "based on the LCA Report. On the basis of the work undertaken, nothing comes to our attention to support that the assumptions, methods and approach in establishing the DS-PCF system have material errors, and therefore it is our opinion that the DS-PCF system was established on a rational basis" (p. 1). DNV validated in accordance with "General principles and requirements: IPCC 2021 AR6" and "Assessment Requirements for validation and verification using alternative methodologies and non-ISO 14040/14044 based EPDs or PCRs" (p. 1, "Responsibilities" box).
**Kyndryl draft:** [NOT STATED]
**Comparison:** This document demonstrates Samsung pursued third-party verification. Verifier: DNV Business Assurance Korea Ltd. Scope: validation of DS-PCF System methodology, data conversion, and reporting. Conclusion: "rational basis" for the system, no material errors identified.

### C8. Reporting transparency
**OEM content:** The validation certificate provides limited transparency into the underlying methodology. It confirms that Samsung's DS-PCF System includes FAB, Water and Chemical Module, Process: Semiconductor Manufacturing Process, and uses IPCC 2021 AR6, but does not publish bill-of-materials, energy values, or itemized EoL flows (p. 1). The document itself is a one-page opinion, not a full methodology report.
**Kyndryl draft:** [NOT STATED]
**Comparison:** Reporting transparency is low. The certificate confirms the existence and standards conformance of Samsung's DS-PCF System but does not provide the detail required to reproduce results.

### C9. Circularity-specific metrics (opportunistic — covered by parallel workstream)
**OEM content:** Not stated in the validation certificate. The system boundary is Cradle-to-Gate (manufacturing only); no recycling, reuse, take-back, design-for-disassembly, or recycled content metrics are mentioned.
**Kyndryl draft:** [NOT STATED in goal/scope doc] — circularity is addressed through a separate qualitative workstream.
**Comparison:** Absence expected and not a finding. OEM's Cradle-to-Gate system does not address circularity metrics.

---

## Gaps vs Kyndryl draft

- **C1 (Standards conformance):** Kyndryl draft is silent; Samsung's validation certificate explicitly confirms conformance to ISO 14040, ISO 14067 (2020/2018), ISO 14064-3, and IPCC 2021 AR6.
- **C2 (LCIA method):** Kyndryl draft lists impact categories but does not name a characterization model; Samsung uses IPCC 2021 AR6.
- **C4 (Temporal boundary / data vintage):** Kyndryl draft does not specify reference year; Samsung uses 2024 data (as of validation date 28 August 2025).

---

## Goes beyond Kyndryl draft

- **Standards verification by independent third party:** Samsung underwent formal DNV validation; Kyndryl's draft does not mention third-party review. This is evidence that third-party verification is a real-world practice in semiconductor industry and may be worth considering for Kyndryl's own LCA.

---

## Notable absences in OEM doc

- **A6 (Geographic boundary):** Not explicitly stated for the verified system.
- **A7 (Allocation procedure):** Not stated.
- **B1 (Primary vs secondary data breakdown):** Not quantified; document confirms data input responsibility but not the ratio or sources.
- **B3 (End-of-life modeling approach):** Not applicable; system boundary is Cradle-to-Gate only.
- **C3 (Cut-off / completeness rules):** Not explicitly stated as a threshold.
- **C5 (Data quality assessment):** Methodology not described.
- **C6 (Uncertainty & sensitivity analysis):** Not stated.
- **C8 (Reporting transparency):** Low; this is a one-page opinion, not a full methodology disclosure.
- **C9 (Circularity metrics):** Not stated; expected given Cradle-to-Gate boundary.

---

## Direct quotes for citation

1. "DNV Business Assurance Korea Ltd. has been commissioned by Samsung Electronics Co., Ltd. Device Solutions to perform validation of Product Carbon Footprint Calculation and its Reporting System." (p. 1)

2. "The validation assesses the DS-PCF System of Samsung Semiconductor that was developed in accordance with principles and requirements of ISO 14040 and ISO 14067 2020; ISO 14067 2018 and 'LCA Report'." (p. 1)

3. "Functional Unit: Water (per 8\" and 12\" wafer) and Die; System Boundary: Cradle-to-Gate; Impact Category: Global Warming Potential (GWP100); Impact Assessment Methodology: IPCC 2021 AR6." (p. 1)

4. "The validation assessed the DS-PCF System's validity based on the LCA Report. On the basis of the work undertaken, nothing comes to our attention to support that the assumptions, methods and approach in establishing the DS-PCF system have material errors, and therefore it is our opinion that the DS-PCF system was established on a rational basis." (p. 1)

5. "DNV validation was performed in accordance with the GreenHouse Gas (GHG) calculation principles of ISO 14064-3:2019 (Part 3) Specification and General principles and requirements: IPCC 2021 AR6." (p. 1)

6. "The measurement is limited to the DS-PCF System described in the 'LCA Report' by Samsung Semiconductor; hence it does not guarantee reliability of PCF result of the DS-PCF System. The assessment result will depend on accuracy of the data input provided by Samsung Semiconductor at a limited scope on a sampling basis." (p. 1, Limitations section)
