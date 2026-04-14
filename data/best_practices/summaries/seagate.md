# Seagate — Methodology Extraction

**Source file:** seagate-methodolgy.pdf
**Source type:** methodology doc
**Document title:** Understanding life cycle assessment and embodied carbon
**Document date / version:** 2025 (copyright year shown; specific version not stated)
**Total pages reviewed:** 1

## Group A — Explicit in Kyndryl draft

### A1. Goal of the study
**OEM content:** "LCA is a systematic process used to evaluate the environmental impacts associated with all stages of a product's life." Seagate conducts LCAs for product families "to ensure the accuracy and reliability" and makes them available "empowering our customers to make informed purchasing decisions based on the environmental impact of our products" (p. 1). The goal encompasses both internal product assessment and public transparency/customer decision-support.
**Kyndryl draft:** Assess environmental impacts of IT hardware in Kyndryl's owned data centers, cradle-to-grave, to identify circularity improvement areas. Develop a baseline LCA methodology for IT data center hardware; inform Kyndryl's product sourcing decisions.
**Comparison:** Partially aligned. Both are cradle-to-grave and aim to inform product decisions, but Seagate's primary goal is customer transparency and purchasing support, while Kyndryl's is internal baseline development and circularity targeting.

### A2. Intended audience & commissioner
**OEM content:** "To ensure the accuracy and reliability of our Life Cycle Assessments (LCAs), we engage a third-party auditor to independently verify our findings. We produce LCAs for our product families and make them available on our website" (p. 1). The document states it is "intended that it be shared and disclosed publicly in the form presented" (p. 1, footer). Intended audience is public (customers, regulators). Commissioner is Seagate (internal initiative).
**Kyndryl draft:** Designed for Kyndryl Holdings, Inc. Initiated by Northwestern University.
**Comparison:** Different. Seagate is public disclosure with third-party verification; Kyndryl is internal with academic partnership.

### A3. Product system / scope of hardware
**OEM content:** "We produce LCAs for our product families" — specifically, the case study covers Seagate storage products (hard drives, SSDs, tape). The document discusses "Seagate Exos X22" (hard drive) and compares embodied carbon across "SSDs, hard drives, and tape" technologies (p. 1). Sub-components (drive, tape media) are treated separately in the comparison table.
**Kyndryl draft:** IT hardware in Kyndryl's owned data centers. In scope: GPUs, rack servers, HDDs, SSDs.
**Comparison:** Partially aligned. Both include HDDs and SSDs; Seagate also covers tape (out of scope for Kyndryl). Seagate does not address GPUs or rack servers.

### A4. Functional unit
**OEM content:** The document references "a 5-year period" and "5 years life cycle" in embodied carbon calculations and the storage media comparison table (p. 1). However, the specific functional unit is not stated as a formal definition. The implicit unit appears to be "per device" or "per TB" over 5 years, but no explicit statement like "1 unit operating for X years" is provided.
**Kyndryl draft:** One hardware component operating for five years.
**Comparison:** Partially aligned. Both assume 5-year lifetime, but Seagate does not state a formal functional unit definition; instead, it reports embodied carbon per device, per TB, and per TB/year.

### A5. System boundary — lifecycle stages
**OEM content:** "LCA covers raw material extraction, manufacturing, distribution, use, and end-of-life disposal or recycling" (p. 1). The four-phase framework is outlined: Goal and scope, Life cycle inventory (LCI), Life cycle impact assessment (LCIA), and Interpretation (p. 1). Embodied carbon is defined as "total GHG emissions associated with the upstream extraction, production, transport, manufacturing, packaging, and distribution stages of a product's life" — notably, this excludes use phase and end-of-life from the embodied carbon definition, though full LCA includes them (p. 1). The document mentions "recycling and disposal strategies" as end-of-life management (p. 1).
**Kyndryl draft:** Cradle-to-grave: raw materials extraction, manufacturing, operating use, end-of-life. Transportation explicitly excluded due to data collection complexity.
**Comparison:** Different. Seagate includes all cradle-to-grave stages plus transportation (within manufacturing/distribution). Kyndryl explicitly excludes transportation. Seagate's embodied carbon definition is narrower (excludes use and EoL), though full LCA covers them.

### A6. Geographic boundary
**OEM content:** Not stated in document. The case study discusses Seagate Exos X22 and a storage media comparison, but does not specify whether global average, regional, or site-specific data is used for manufacturing, grid mix, or end-of-life.
**Kyndryl draft:** Kyndryl-owned data center in Canada. Site-specific data from Project North Star.
**Comparison:** OEM silent. Seagate does not disclose geographic assumptions for manufacturing, grid mix, or EoL.

### A7. Allocation procedure
**OEM content:** Not stated in document. No mention of allocation rules for co-products or byproducts is provided.
**Kyndryl draft:** Economic allocation, based on market price of co-products.
**Comparison:** OEM silent. Seagate does not disclose allocation methodology.

### A8. Impact categories
**OEM content:** "Seagate assess our products' environmental impacts across several key categories relevant to storage products": Global Warming (measured in CO₂e using ReCiPe characterization and Greenhouse Gas Protocol flows), Human Toxicity (DALYs), Water Consumption (m³), and Mineral Resource Scarcity (kg Cu equivalent) (p. 1). The document notes "Although our analysis encompasses 18 impact areas, our sustainability reports concentrate on the previously mentioned categories, as these are of greatest importance to our stakeholders" (p. 1).
**Kyndryl draft:** Water use (m³), resource/energy use (MJ), climate change (kg CO₂e).
**Comparison:** Partially aligned. Both include water use and climate change (as CO₂e). Seagate also includes human toxicity and mineral resource scarcity (not in Kyndryl draft). Seagate assesses 18 total impact areas but reports only four to stakeholders. Kyndryl includes resource/energy use (MJ), which is not listed as a separate category by Seagate.

---

## Group B — Implied or partial in Kyndryl draft

### B1. Data sources — primary vs secondary
**OEM content:** Not stated in document. The document does not disclose whether Seagate uses primary supplier data, industry databases (ecoinvent, GaBi, Idemat), or a mix. No database name, cutoff year, or primary/secondary ratio is provided.
**Kyndryl draft:** Implied secondary. Draft says it "leverages existing Product Carbon Footprints for climate change impact calculations" — i.e., Kyndryl is a downstream user of OEM PCFs, not a primary data collector.
**Comparison:** OEM silent. Seagate does not disclose data sources or background databases.

### B2. Use-phase assumptions
**OEM content:** The case study example includes "5 years" as an operating period (p. 1). Operating power is provided for the storage media comparison: "Operating power in watt" and "Watt/TB" are reported for SSD (15W, 0.5 W/TB), hard drive (9.6W, 0.32 W/TB), and LTO tape (37W, 1.1 W/TB) (p. 1). However, utilization rate (duty cycle), grid carbon intensity, thermal efficiency (PUE), or lifetime assumptions beyond the 5-year period are not stated.
**Kyndryl draft:** Partial. 5-year lifetime stated (via FU). Use-phase grid mix implied via Canada/Project North Star site data, but no explicit utilization rate, TDP, or workload assumption.
**Comparison:** Partially aligned. Both assume 5-year operating period. Seagate provides operating power (watts and W/TB) but does not state utilization, grid carbon intensity, or cooling overhead. Kyndryl's site-specific grid data is not mentioned by Seagate.

### B3. End-of-life modeling approach
**OEM content:** The document mentions "effective recycling and disposal strategies" as a best practice (p. 1) and references "The Seagate Circularity program" which "aims to prolong the life of our products through reuse, refurbishment, and recycling, thereby reducing waste and increasing resource efficiency" (p. 1). However, the specific EoL modeling approach (cut-off, avoided burden, recycled content credit, or PEF Circular Footprint Formula) is not stated. No recycling rates or credit assumptions are disclosed.
**Kyndryl draft:** EoL is in scope, but the modeling approach (cut-off vs recycled content vs avoided burden) is not specified.
**Comparison:** OEM silent on modeling approach. Seagate mentions recycling and a circularity program but does not disclose how EoL impacts are quantified in the LCA or PCF.

---

## Group C — Not addressed in Kyndryl draft

### C1. Standards conformance
**OEM content:** "The LCA framework Seagate is using is structured around four key phases, as outlined in ISO 14040 and ISO 14044" (p. 1). No other standards are cited (e.g., ISO 14067, GHG Protocol Product Standard, PAS 2050, PEF). The document notes conformance to ISO 14040/14044 but does not claim independent verification of conformance or third-party audit scope.
**Kyndryl draft:** [NOT STATED]
**Comparison:** Seagate cites ISO 14040 and ISO 14044. Verification mentioned but audit scope not detailed.

### C2. LCIA method (characterization model)
**OEM content:** "We assess our products' global warming impacts across the 213 elementary flows ReCiPe characterizes as GHGs, including the seven GHGs specified in the Greenhouse Gas Protocol Product Standard" (p. 1). For human toxicity, water consumption, and mineral resource scarcity, no characterization model is explicitly named, though the language suggests ReCiPe is used for at least global warming. The document does not name a version of ReCiPe or state whether other impact categories use the same method.
**Kyndryl draft:** [NOT STATED] — categories listed but no characterization method named.
**Comparison:** Seagate names ReCiPe for global warming (version not stated) and references GHG Protocol. Other impact categories are not attributed to a named method.

### C3. Cut-off / completeness rules
**OEM content:** Not stated in document. No threshold for mass, energy, cumulative impact, or other exclusion rule is disclosed.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. Seagate does not disclose cut-off rules.

### C4. Temporal boundary / data vintage
**OEM content:** The document is dated 2025 (copyright). No reference year for foreground data, background database vintage, or update frequency is provided.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. Seagate does not disclose data reference year or update schedule.

### C5. Data quality assessment
**OEM content:** Not stated in document. No pedigree matrix, data quality narrative, or evaluation against ISO 14044 quality criteria is provided.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. Seagate does not disclose data quality assessment.

### C6. Uncertainty & sensitivity analysis
**OEM content:** Not stated in document. No Monte Carlo analysis, ± ranges, or sensitivity to key parameters (lifetime, grid mix, utilization, capacity) is provided.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. Seagate does not disclose uncertainty or sensitivity analysis.

### C7. Critical review / third-party verification
**OEM content:** "To ensure the accuracy and reliability of our Life Cycle Assessments (LCAs), we engage a third-party auditor to independently verify our findings" (p. 1). The document states the white paper "has been prepared for the purpose of summarizing the methodologies and assumptions used to calculate the life cycle impacts of Seagate's storage products" and disclaims that "Due and customary care has been exercised in preparing this report, but we have not, save as specifically stated, independently verified information provided by others" (p. 1, footer). The reviewer name and audit scope (methodology, data, or both) are not disclosed in this white paper.
**Kyndryl draft:** [NOT STATED]
**Comparison:** Seagate states that LCAs are third-party verified but does not name the reviewer or detail the scope of review in this document.

### C8. Reporting transparency
**OEM content:** This white paper is a high-level overview and case study. It provides narrative explanations of LCA framework, a worked example for Exos X22 embodied carbon calculation (formula provided: p. 1), and a comparison table of embodied carbon per device, per TB, and per TB/year for SSDs, hard drives, and tape (p. 1). However, detailed bill-of-materials, lifecycle inventory flows by stage, or process-level energy/water values are not itemized. The document points readers to "our website" and "www.seagate.com/circularity" for additional details but does not provide full transparency in this document.
**Kyndryl draft:** [NOT STATED]
**Comparison:** Low to medium transparency. The white paper includes framework description and a worked example but lacks itemized BOM, inventory flows, and process-level inputs. Full LCA data is stated to be available on Seagate's website (not in this document).

### C9. Circularity-specific metrics (opportunistic — covered by parallel workstream)
**OEM content:** The document mentions "The Seagate Circularity program" which "aims to prolong the life of our products through reuse, refurbishment, and recycling, thereby reducing waste and increasing resource efficiency" and states "By choosing Seagate Circularity, customers support a brand dedicated to environmental stewardship and contributing to a circular economy" (p. 1). However, no quantified metrics (recycled content %, recyclability %, reuse/refurb rate, design-for-disassembly indices, take-back program coverage %) are provided in this white paper. The document points to "www.seagate.com/circularity" for "further details about Seagate Circularity" but does not include specific metrics here.
**Kyndryl draft:** [NOT STATED in goal/scope doc] — circularity is the study's purpose but is being addressed through a separate qualitative analysis of vendor take-back programs and annual sustainability reports, not through PCFs/LCAs.
**Comparison:** Seagate's circularity program is mentioned qualitatively but no quantified metrics appear in this document. Absence is expected (see instructions).

---

## Gaps vs Kyndryl draft
- **B1 (Data sources):** Seagate does not disclose whether primary or secondary data is used, which background database (ecoinvent, GaBi, Idemat), or cutoff year. This is a candidate for Kyndryl to require from OEM submissions.
- **B3 (EoL modeling):** Seagate does not specify cut-off, avoided burden, or recycled content credit approach. Kyndryl should clarify this requirement.
- **A6 (Geographic boundary):** Seagate does not state whether global average, regional, or site-specific grid/supply chain data is used. Kyndryl's emphasis on site-specific data (Canada, Project North Star) is not addressed.
- **A7 (Allocation procedure):** Seagate does not disclose allocation rules for co-products. This is a gap that affects reproducibility.

---

## Goes beyond Kyndryl draft
- **Impact categories (A8):** Seagate assesses 18 impact areas total (vs Kyndryl's three: water, energy, climate). Seagate reports four to stakeholders (global warming, human toxicity, water consumption, mineral resource scarcity). Human toxicity and mineral resource scarcity are not in Kyndryl's draft, offering potential expansions.
- **Third-party verification (C7):** Seagate explicitly engages third-party auditors. Kyndryl's draft does not mention verification; Seagate's approach could inform a future verification plan.
- **Characterization model clarity (C2):** Seagate names ReCiPe for global warming and Greenhouse Gas Protocol, providing specificity beyond Kyndryl's draft.
- **Functional unit examples:** Seagate provides multiple reporting units (per device, per TB, per TB/year), which could help Kyndryl communicate results at different scales (e.g., per-device vs per-service-delivered).

---

## Notable absences in OEM doc
- No allocation procedure disclosed (A7).
- No geographic boundary for manufacturing, grid mix, or EoL (A6).
- No data sources or background database named (B1).
- No data quality assessment (C5).
- No uncertainty or sensitivity analysis (C6).
- No specific reviewer name or critical review scope (C7).
- No cut-off rules or completeness thresholds (C3).
- No temporal boundary or data vintage (C4).
- No quantified circularity metrics despite program mention (C9).

---

## Direct quotes for citation

1. "LCA is a systematic process used to evaluate the environmental impacts associated with all stages of a product's life. Often termed as a 'cradle-to-grave' analysis, LCA covers raw material extraction, manufacturing, distribution, use, and end-of-life disposal or recycling." (p. 1)

2. "The LCA framework Seagate is using is structured around four key phases, as outlined in ISO 14040 and ISO 14044: Goal and scope, Life cycle inventory (LCI), Life cycle impact assessment (LCIA), Interpretation." (p. 1)

3. "We assess our products' global warming impacts across the 213 elementary flows ReCiPe characterizes as GHGs, including the seven GHGs specified in the Greenhouse Gas Protocol Product Standard." (p. 1)

4. "Embodied carbon—also known as embodied greenhouse gas (GHG) emissions—refers to the total GHG emissions associated with the upstream extraction, production, transport, manufacturing, packaging, and distribution stages of a product's life." (p. 1)

5. "To ensure the accuracy and reliability of our Life Cycle Assessments (LCAs), we engage a third-party auditor to independently verify our findings." (p. 1)

6. "The Seagate Circularity program is another key element of our sustainability strategy. It aims to prolong the life of our products through reuse, refurbishment, and recycling, thereby reducing waste and increasing resource efficiency." (p. 1)

7. "Although our analysis encompasses 18 impact areas, our sustainability reports concentrate on the previously mentioned categories, as these are of greatest importance to our stakeholders." (p. 1)

