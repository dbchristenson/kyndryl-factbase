# NVIDIA — Methodology Extraction (PCF source)

**Source file:** nvidia-gpu-example-product-pcf-with-methodology-explained.pdf
**Source type:** PCF with embedded methodology
**Product covered:** NVIDIA HGX B200 GPU baseboard
**Document title:** Product Carbon Footprint (PCF) Summary for NVIDIA HGX B200
**Document date / version:** July 24, 2025
**Total pages reviewed:** 4

---

**Extraction note:** This document is a PCF product report with embedded methodology explanation, not a standalone methodology document. NVIDIA was included in this study because no formal standalone NVIDIA LCA/PCF methodology document could be located. The extraction below reflects this source type: some dimensions are explicitly addressed (because methodology must be disclosed in a PCF), while others remain silent. Absence of content in Group C sections is expected and does not indicate a finding gap — it reflects the PCF format's focus on results over methodological detail.

---

## Group A — Explicit in Kyndryl draft

### A1. Goal of the study
**OEM content:** "At NVIDIA, we're working to reduce the greenhouse gases (GHGs) associated with our products. Carefully determining the impact of our products is a critical step in that process. This summary provides insights into the emissions associated with one NVIDIA HGX B200 baseboard, from raw material extraction, material transport, production of components to final assembly of the GPU baseboard (cradle-to-gate)." (p. 1)

**Kyndryl draft:** Assess environmental impacts of IT hardware in Kyndryl's owned data centers, cradle-to-grave, to identify circularity improvement areas. Sub-goals: develop a baseline LCA methodology for IT data center hardware; inform Kyndryl's product sourcing decisions.

**Comparison:** Partially aligned. Both study GHG impacts of hardware, but NVIDIA's goal is to reduce and disclose GHGs for sustainability reporting; Kyndryl's goal is to inform sourcing and identify circularity improvements. NVIDIA's scope is cradle-to-gate (excludes use and EoL); Kyndryl's is cradle-to-grave. Alignment on environmental assessment intent; divergence on boundary and decision-making context.

### A2. Intended audience & commissioner
**OEM content:** Document states "This summary is based on an ISO-conformant, third-party-reviewed product carbon footprint (PCF) commissioned by NVIDIA and performed by WSP." (p. 1)

**Kyndryl draft:** Designed for Kyndryl Holdings, Inc. Initiated by Northwestern University.

**Comparison:** Different. NVIDIA's PCF is commissioned by NVIDIA (internal sustainability initiative), reviewed by third party (WSP), and intended for public disclosure (PCF summaries are typically public-facing). Kyndryl's study is commissioned by an external academic institution (Northwestern). NVIDIA's audience is not explicitly stated but is inferred to be public/stakeholders; Kyndryl's is internal (Kyndryl Holdings).

### A3. Product system / scope of hardware
**OEM content:** "NVIDIA HGX B200 propels the data center into a new era of accelerating computing and generative artificial intelligence (AI), integrating NVIDIA Blackwell GPUs with a high-speed interconnect to accelerate AI performance at scale. It features eight NVIDIA Blackwell B200 GPUs, each with 180 GB of HBM3E memory, and uses NVLINK and NVLINK-2 interfaces for high-speed interconnections." (p. 1) Product specifications include Form Factor (8x NVIDIA Blackwell SMXs), FP* Tensor Core, FP8/FP6 Tensor Core, INT8 Tensor Core, FP16/BF16 Tensor Core, TF32 Tensor Core, FP32 (600 FLOPS), FP64/FP64 Tensor Core (296 TFLOPS), Total Memory (up to 1.4 TB), Total Memory Bandwidth (up to 62 TB/s), NVLink (fifth generation), NVSwitch (fifth generation). (p. 1, product specifications table)

**Kyndryl draft:** IT hardware in Kyndryl's owned data centers. In scope: GPUs, rack servers, HDDs, SSDs.

**Comparison:** Partially aligned. NVIDIA covers one specific GPU product (HGX B200 baseboard as a system); Kyndryl's scope includes GPUs as a category, plus servers, HDDs, SSDs. NVIDIA treats the baseboard as an integrated product; does not isolate sub-components separately in reporting (methodology shows they model components, but results aggregate to the baseboard level).

### A4. Functional unit
**OEM content:** Not explicitly stated. The PCF is reported per "one HGX B200 GPU baseboard" (32 kg total weight, p. 1), implying the functional unit is the physical product unit, not a performance metric or service metric.

**Kyndryl draft:** One hardware component operating for five years.

**Comparison:** OEM silent on functional unit definition. NVIDIA reports results per physical product (baseboard), not normalized to performance (FLOPS-years, compute-years) or time (per 5 years of operation). NVIDIA's cradle-to-gate scope means no operational lifetime is relevant; Kyndryl's cradle-to-grave scope requires explicit lifetime assumption (5 years).

### A5. System boundary — lifecycle stages
**OEM content:** "The PCF was performed using the cradle-to-gate Life Cycle Assessment (LCA) methodology, covering emissions from raw material extraction to the point where it leaves the manufacturing facility." (p. 2, footnote 2) Stages included: (1) Raw Material Extraction and Refinement, (2) Component Manufacturing [including Semiconductor Manufacturing Fabrication, Transportation, Packaging Testing; Printed Circuit Board Manufacturing; Thermal and Mechanical Component Manufacturing], (3) Assembly [GPU Assembly, Baseboard Assembly]. (p. 2, Scope and Methodology diagram) Transportation is "accounts for only 0.3%" (p. 3). Use phase and end-of-life are intentionally excluded: "This PCF summary intentionally excludes use-phase and end-of-life emissions due to the variability in those emissions based on customer usage." (p. 1)

**Kyndryl draft:** Cradle-to-grave: raw materials extraction, manufacturing, operating use, end-of-life. Transportation explicitly excluded due to data collection complexity.

**Comparison:** Significantly different. NVIDIA uses cradle-to-gate (raw materials, manufacturing, assembly, inbound transport). Kyndryl plans cradle-to-grave (includes use and EoL). Both exclude outbound/distribution transport. NVIDIA explicitly justifies exclusion of use and EoL due to customer variability; Kyndryl plans to include both but excludes transportation due to data complexity. This is a fundamental boundary divergence.

### A6. Geographic boundary
**OEM content:** Not stated in document. No geographic assumptions disclosed for use phase (N/A: cradle-to-gate). No grid mix or regional data specified for manufacturing stage. Implicitly assumes global/average for secondary data (ecoinvent, Sphera).

**Kyndryl draft:** Kyndryl-owned data center in Canada. Site-specific data from Project North Star.

**Comparison:** OEM silent. NVIDIA does not disclose geographic assumptions for the manufacturing/extraction stages. Kyndryl's geographic boundary is specific to Canadian data center use-phase impact. Not comparable (NVIDIA cradle-to-gate does not have use-phase geography).

### A7. Allocation procedure
**OEM content:** Not stated in document.

**Kyndryl draft:** Economic allocation, based on market price of co-products.

**Comparison:** OEM silent. No allocation method disclosed.

### A8. Impact categories
**OEM content:** Single impact category: climate change (kg CO₂e). "The PCF quantifies the total greenhouse gas (GHG) emissions associated with a product throughout its lifecycle, potentially encompassing emissions from raw material extraction, manufacturing, usage, and end-of-life disposal or recycling. The results are typically expressed in terms of carbon dioxide equivalents (CO₂e), which account for all relevant GHGs based on their Global Warming Potential (GWP)." (p. 1, footnote 1) Result: "2,274 kg CO₂e" for one HGX B200 baseboard. (p. 3)

**Kyndryl draft:** Water use (m³), resource/energy use (MJ), climate change (kg CO₂e).

**Comparison:** Narrower than Kyndryl draft. NVIDIA reports climate change (GWP 100-year) only. Kyndryl plans three categories (water, resource/energy, climate). NVIDIA does not report water use or energy/resource depletion.

---

## Group B — Implied or partial in Kyndryl draft

### B1. Data sources — primary vs secondary
**OEM content:** "To calculate the carbon footprint, we developed custom PCF models based on primary data from suppliers of critical components (GPU and networking chip fabrication and packaging, thermals, PCBs, interconnects, key ICs, GPU and baseboard assembly). We collected primary data, including material composition data and production energy consumption, for components representing over 90% of the product by weight. This data was combined with secondary data sources, including imec's net.zero tool for fabrication-related emissions, as well as ecoinvent 3.10 and Sphera's LCA databases (Professional Database 2024 and Extension Database XI: Electronics 2024) for modeling materials, transportation, and energy." (p. 2)

**Kyndryl draft:** Implied secondary. Draft says it "leverages existing Product Carbon Footprints for climate change impact calculations" — i.e., Kyndryl is a downstream user of OEM PCFs, not a primary data collector.

**Comparison:** Aligned on approach (leveraging secondary databases) but different on role. NVIDIA collected primary data from suppliers for 90% of product weight, supplemented with secondary databases. Kyndryl is planning to be a downstream user of OEM PCFs (entirely secondary). Both use secondary databases (ecoinvent, Sphera). NVIDIA's primary data collection for critical components (wafer fab, packaging, assembly) is beyond Kyndryl's scope.

### B2. Use-phase assumptions
**OEM content:** Not applicable. Document excludes use phase: "This PCF summary intentionally excludes use-phase and end-of-life emissions due to the variability in those emissions based on customer usage." (p. 1)

**Kyndryl draft:** Partial. 5-year lifetime stated (via FU). Use-phase grid mix implied via Canada/Project North Star site data, but no explicit utilization rate, TDP, or workload assumption.

**Comparison:** OEM silent. NVIDIA's cradle-to-gate scope excludes use entirely, so no use-phase assumptions (power draw, utilization, lifetime, grid mix) are disclosed. Not comparable.

### B3. End-of-life modeling approach
**OEM content:** Not disclosed. Document excludes EoL: "This PCF summary intentionally excludes use-phase and end-of-life emissions due to the variability in those emissions based on customer usage." (p. 1)

**Kyndryl draft:** EoL is in scope, but the modeling approach (cut-off vs recycled content vs avoided burden) is not specified.

**Comparison:** OEM silent. NVIDIA explicitly excludes EoL due to customer-dependent variability. Kyndryl plans to include EoL but has not finalized the modeling approach.

---

## Group C — Not addressed in Kyndryl draft

### C1. Standards conformance
**OEM content:** "The PCF was critically reviewed in conformance to ISO Standard 14067 on carbon footprints and is aligned with ISO standards 14040 and 14044 on life cycle assessments (LCA)." (p. 2)

**Kyndryl draft:** [NOT STATED]

**Comparison:** NVIDIA conforms to ISO 14067 (carbon footprint of products), ISO 14040 (LCA principles), ISO 14044 (LCA requirements). Conformance is stated; verification by third party (WSP) is noted. Kyndryl's draft does not yet specify standards alignment.

### C2. LCIA method (characterization model)
**OEM content:** Implicit but not explicitly named. Document refers to "Global Warming Potential (GWP)" for GHG accounting (p. 1, footnote 1), consistent with IPCC AR5 or AR6 GWP 100-year method, but the specific characterization model version is not disclosed.

**Kyndryl draft:** [NOT STATED] — categories listed but no characterization method named.

**Comparison:** OEM implicitly uses GWP (likely IPCC AR5/AR6) for climate change but does not name the exact LCIA method. Kyndryl's draft does not yet specify.

### C3. Cut-off / completeness rules
**OEM content:** Implied: "We collected primary data, including material composition data and production energy consumption, for components representing over 90% of the product by weight." (p. 2) Infers a cut-off rule of approximately 10% by mass, but not formally stated.

**Kyndryl draft:** [NOT STATED]

**Comparison:** OEM uses approximate 90% mass coverage (implying ~10% cut-off), but no formal cut-off rule is documented. Kyndryl's draft does not specify.

### C4. Temporal boundary / data vintage
**OEM content:** Stated in references: "Professional Database 2024 and Extension Database XI: Electronics 2024" (p. 2). Implies 2024 is the reference year for background databases. Document creation date: July 24, 2025 (PDF metadata). No foreground data vintage stated.

**Kyndryl draft:** [NOT STATED]

**Comparison:** NVIDIA uses 2024 background database versions; no explicit foreground data vintage. Kyndryl's draft does not specify data vintage expectations.

### C5. Data quality assessment
**OEM content:** Not formally disclosed. No pedigree matrix, qualitative narrative on data representativeness, or quality rating provided.

**Kyndryl draft:** [NOT STATED]

**Comparison:** OEM silent. No documented data quality assessment methodology.

### C6. Uncertainty & sensitivity analysis
**OEM content:** Not disclosed. No Monte Carlo ranges, ± bounds, or sensitivity analysis (e.g., to lifetime, grid mix, utilization) reported.

**Kyndryl draft:** [NOT STATED]

**Comparison:** OEM silent. Results reported as point values (2,274 kg CO₂e) with no quantified uncertainty.

### C7. Critical review / third-party verification
**OEM content:** "This summary is based on an ISO-conformant, third-party-reviewed product carbon footprint (PCF) commissioned by NVIDIA and performed by WSP." (p. 1) Reviewer: WSP. Scope of review: stated as "ISO-conformant" and "critically reviewed in conformance to ISO Standard 14067," but details on what was reviewed (methodology, data, both) are not disclosed.

**Kyndryl draft:** [NOT STATED]

**Comparison:** NVIDIA had third-party review (WSP) against ISO 14067 conformance. Scope of review (full vs partial) not detailed. Kyndryl's draft does not yet specify third-party review plans.

### C8. Reporting transparency
**OEM content:** Medium-to-high transparency for a PCF. Strengths: Bill of materials is disclosed (product specs, p. 1; material breakdown by component type, p. 3). Lifecycle stages explicitly listed (p. 2, diagram). Contribution breakdown (94% materials/components, 5.6% assembly, 0.3% transport) shown. Key data sources named (imec net.zero, ecoinvent 3.10, Sphera 2024). Limitations: Primary data collection rate (90% by weight) disclosed, but specific bill of materials not itemized numerically; material composition per component not given; energy values by stage not broken down (only final result shown); EoL flows not discussed (N/A: cradle-to-gate).

**Kyndryl draft:** [NOT STATED]

**Comparison:** NVIDIA provides above-average transparency for a PCF: process diagram, materials list, component contribution breakdown, and data sources. Less detailed than a full methodology document or EPD (e.g., no pedigree, no sensitivity). Suitable for customer disclosure and sourcing comparison. Kyndryl's draft does not yet specify reporting transparency expectations.

### C9. Circularity-specific metrics (opportunistic — covered by parallel workstream)
**OEM content:** Not stated in document. No recycled content %, recyclability %, reuse/refurbishment rate, design-for-disassembly, or take-back program coverage disclosed.

**Kyndryl draft:** [NOT STATED in goal/scope doc] — circularity is the study's purpose but is being addressed through a separate qualitative analysis of vendor take-back programs and annual sustainability reports, not through PCFs/LCAs.

**Comparison:** OEM silent. Document is intentionally cradle-to-gate and excludes EoL, so circularity metrics are outside scope. Absence is expected and is not a finding.

---

## Gaps vs Kyndryl draft

- **A4 (Functional unit):** Kyndryl specifies "one hardware component operating for five years"; NVIDIA reports per physical product (baseboard) with no temporal dimension. Kyndryl's 5-year assumption is not disclosed or justified in NVIDIA PCF.
- **A7 (Allocation procedure):** Kyndryl plans economic allocation; NVIDIA does not disclose allocation approach.
- **B1 (Primary data strategy):** NVIDIA collected primary data from suppliers for 90% of product weight; Kyndryl plans to use secondary OEM PCFs only. NVIDIA's primary data collection approach is a model that Kyndryl may not replicate (lacks direct supplier relationships).
- **B2, B3 (Use phase and EoL modeling):** NVIDIA cradle-to-gate excludes both; Kyndryl cradle-to-grave requires assumptions on both. NVIDIA's PCF cannot inform Kyndryl's use-phase grid mix or EoL modeling.
- **C2 (LCIA method):** Kyndryl lists impact categories but does not name characterization model; NVIDIA implicitly uses GWP but does not name method explicitly.
- **C4 (Temporal boundary):** Kyndryl does not state data vintage expectations; NVIDIA uses 2024 databases.

---

## Goes beyond Kyndryl draft

- **Product-specific bill of materials:** NVIDIA discloses detailed product specifications (8x B200 GPUs, 180 GB HBM3E per GPU, NVLink interconnects, memory bandwidth, thermal/compute specs). Kyndryl's draft does not specify BoM requirements; NVIDIA's transparency on hardware composition is a model for other OEMs.
- **Material contribution breakdown by component:** NVIDIA quantifies contribution by category (Memory 49%, ICs 28%, Thermal Components 12%, Electromechanical 2%, PCBs 1.7%, Common Components 1%, Mechanical 0.3%, Interconnects 0.3%, p. 3). Kyndryl's draft does not require this level of itemization.
- **Lifecycle stage contribution breakdown:** NVIDIA shows 94% materials/components, 5.6% assembly, 0.3% transport (p. 3). Kyndryl's draft does not specify reporting of stage-level contributions.
- **Third-party verification:** NVIDIA's PCF was reviewed by WSP for ISO 14067 conformance. Kyndryl's draft does not yet plan third-party review; NVIDIA's approach is a model for future Kyndryl verification requirements.
- **Justification for scope boundaries:** NVIDIA explicitly justifies exclusion of use and EoL ("due to the variability in those emissions based on customer usage," p. 1). Kyndryl's draft does not justify its inclusion of use/EoL; NVIDIA's reasoning is a useful reference for scope sensitivity.

---

## Notable absences in OEM doc

- **Use-phase environmental impact:** Intentionally excluded. No power draw, utilization rate, grid mix, or operating lifetime disclosed.
- **End-of-life environmental impact:** Intentionally excluded. No recycling rate, material recovery, or disposal-related burdens disclosed.
- **Allocation procedure:** Not disclosed. No explanation of how environmental burdens are split among co-products if any arise in manufacturing.
- **Formal cut-off rule:** Not documented. Primary data covers "over 90%" by weight, but no formal cut-off threshold stated (e.g., 1% mass, 1% energy).
- **Data quality assessment:** No pedigree matrix, representativeness narrative, or quality ratings provided.
- **Uncertainty or sensitivity analysis:** No ranges, Monte Carlo results, or sensitivity to key parameters (lifetime, grid mix, utilization, primary data assumptions) reported.
- **LCIA characterization method:** Implicit (GWP), but specific method name and version (e.g., IPCC AR5 GWP 100) not stated.
- **Detailed material composition per component:** Product specs and component categories listed, but detailed BoM (material types, quantities) not provided.
- **Temporal boundary / foreground data vintage:** Reference year for primary data not stated; only background database year (2024) mentioned.
- **Reporting on transportation scope:** While transport is mentioned as "0.3%" of total, inbound vs. outbound transport not distinguished; transportation assumptions (distance, mode, load factor) not detailed.
- **Circularity metrics:** No recycled content, recyclability rate, design-for-disassembly score, or take-back program information disclosed. (Expected, given cradle-to-gate scope.)

These absences reflect the PCF format (product disclosure summary rather than full methodology document) and NVIDIA's intentional exclusion of use and EoL phases. Absence should not be interpreted as methodological oversight, but rather as a strategic scope decision and format limitation.

---

## Direct quotes for citation

1. "At NVIDIA, we're working to reduce the greenhouse gases (GHGs) associated with our products. Carefully determining the impact of our products is a critical step in that process." (p. 1)

2. "This summary is based on an ISO-conformant, third-party-reviewed product carbon footprint (PCF) commissioned by NVIDIA and performed by WSP." (p. 1)

3. "This PCF summary intentionally excludes use-phase and end-of-life emissions due to the variability in those emissions based on customer usage." (p. 1)

4. "The PCF was performed using the cradle-to-gate Life Cycle Assessment (LCA) methodology, covering emissions from raw material extraction to the point where it leaves the manufacturing facility." (p. 2)

5. "We collected primary data, including material composition data and production energy consumption, for components representing over 90% of the product by weight. This data was combined with secondary data sources, including imec's net.zero tool for fabrication-related emissions, as well as ecoinvent 3.10 and Sphera's LCA databases." (p. 2)

6. "The PCF was critically reviewed in conformance to ISO Standard 14067 on carbon footprints and is aligned with ISO standards 14040 and 14044 on life cycle assessments (LCA)." (p. 2)

7. "Our PCF determined that the carbon footprint from cradle-to-gate for one HGX B200 GPU baseboard is 2,274 kg CO₂e. The central contributors to these emissions are materials and components, accounting for 94% of the total emissions." (p. 3)

8. "The production of high bandwidth memory (49%), integrated circuits (28%) and thermal components (12%) are significant drivers of the carbon footprint." (p. 3)

