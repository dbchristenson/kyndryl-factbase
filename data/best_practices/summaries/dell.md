# Dell — Methodology Extraction

**Source file:** dell-pcf-methodology.pdf
**Source type:** methodology doc
**Document title:** Product Carbon Footprint FAQs
**Document date / version:** March 2024
**Total pages reviewed:** 6

## Group A — Explicit in Kyndryl draft

### A1. Goal of the study
**OEM content:** PCF is output from a life cycle assessment (LCA) that can be broadly defined as the total greenhouse gas (GHG) emissions, or CO2-equivalent (CO2e), generated during the production or full lifecycle of a product. Goal is to evaluate environmental impact categories associated with all phases of a product's lifecycle. (p. 1–2)
**Kyndryl draft:** Assess environmental impacts of IT hardware in Kyndryl's owned data centers, cradle-to-grave, to identify circularity improvement areas. Sub-goals: develop a baseline LCA methodology for IT data center hardware; inform Kyndryl's product sourcing decisions.
**Comparison:** Partially aligned. Dell's goal is product carbon footprint disclosure and LCA study for internal product design and customer disclosure. Kyndryl's goal is broader (circularity improvement) and downstream-focused (informed sourcing decisions). Both are descriptive, not comparative.

### A2. Intended audience & commissioner
**OEM content:** Dell reports PCFs to customers, regulators (e.g., EPEAT), and internal stakeholders. Report notes that customers require reasonably accurate disclosures of GHG emissions (p. 2) and that Dell participates in sustainability impact reporting and industry consortia. Document is internal use marked "Confidential" but supports public disclosure via multiple channels. (p. 1–2)
**Kyndryl draft:** Designed for Kyndryl Holdings, Inc. Initiated by Northwestern University.
**Comparison:** Different. Dell's audience includes external (customers, regulators, EPEAT) and internal. Kyndryl's audience is internal. Dell's commissioner is Dell Technologies (corporate). Kyndryl's is initiated by university research partner.

### A3. Product system / scope of hardware
**OEM content:** Dell's PCF methodology covers multiple product categories: notebooks, desktops, workstations, and infrastructure hardware (servers, monitors). Document specifically covers servers (R750 referenced in example) (p. 4–5). Sub-components are itemized: display panels, LCD panels, graphics cards, memory, CPU, motherboards, storage capacity, PCBs. (p. 2, 4)
**Kyndryl draft:** IT hardware in Kyndryl's owned data centers. In scope: GPUs, rack servers, HDDs, SSDs.
**Comparison:** Partially aligned. Dell covers servers (match); Kyndryl also includes GPUs, HDDs, SSDs explicitly. Dell itemizes sub-components; Kyndryl's approach to sub-component treatment is not detailed in draft.

### A4. Functional unit
**OEM content:** Not explicitly stated in this document. The PCF tool documentation references "PCF per product" (p. 2–3) and "total PCF" without defining a functional unit per ISO 14040/14044. The use phase calculation references "energy consumption" and specific hardware configurations without normalizing to performance or duration. (p. 4–5)
**Kyndryl draft:** One hardware component operating for five years.
**Comparison:** Different / OEM silent on FU. Dell's PCF is stated as total product impact, not normalized to functional unit. No explicit lifetime assumption stated in this FAQ document.

### A5. System boundary — lifecycle stages
**OEM content:** Four key lifecycle stages: (1) Manufacturing phase—emissions related to raw materials and manufacturing of components; (2) Logistics or Transportation phase—transportation to country of use; (3) Use phase—energy consumption at customer locations in a given time frame; (4) End-of-Life (EOL) phase—recycling, refurbishing or disposal. (p. 2) Transportation and EOL phases are lower-priority than Manufacturing and Use for ICT industry focus (p. 5). Dell notes they will continue to focus on Use phase and Manufacturing phase improvements (p. 5).
**Kyndryl draft:** Cradle-to-grave: raw materials extraction, manufacturing, operating use, end-of-life. Transportation explicitly excluded due to data collection complexity.
**Comparison:** Partially aligned. Both include raw materials, manufacturing, use, EoL. Dell includes transportation (within scope); Kyndryl explicitly excludes it due to complexity. Both recognize Use and Manufacturing as primary impact drivers.

### A6. Geographic boundary
**OEM content:** Geographic location is a major factor in Use phase emissions. Dell's PCF depends on country/region of use due to variation in grid energy mix and electricity source (renewable, coal, nuclear, etc.). Document shows R750 server PCF varies dramatically across regions (Norway ~20 kg CO2e, China ~240 kg CO2e). Manufacturing and Transportation phases remain static regardless of use location. Geographic boundary for manufacturing not explicitly stated but implied to be global average or regional default. (p. 4–5)
**Kyndryl draft:** Kyndryl-owned data center in Canada. Site-specific data from Project North Star.
**Comparison:** Aligned on principle, different in practice. Both recognize geography matters for use phase (grid mix). Dell uses country-averaged grid data; Kyndryl uses site-specific data from project. Dell does not specify manufacturing geography in this document.

### A7. Allocation procedure
**OEM content:** Not explicitly stated. The PCF calculations reference "developing detailed information on manufacturing impact areas (hotspots)" and use of bill-of-materials and material composition, but no allocation procedure (subdivision, physical, economic) is described. (p. 4)
**Kyndryl draft:** Economic allocation, based on market price of co-products.
**Comparison:** OEM silent. Dell's allocation method is not described in this FAQ document.

### A8. Impact categories
**OEM content:** Dell PCF focuses on climate change (carbon footprint) as primary impact. The document states PCF is "carbon emissions at a product level" (p. 2). However, Dell notes that beyond PCF, a full LCA evaluates "a range of multiple potential environmental impact categories associated with all phases of a product's lifecycle" including water consumption, acidification, ozone depletion, and resource depletion (p. 3). Dell's PCF tool currently covers climate only; they anticipate adding other environmental impact categories in the future. (p. 6)
**Kyndryl draft:** Water use (m³), resource/energy use (MJ), climate change (kg CO₂e).
**Comparison:** Different scope. Dell's current PCF is climate-only; Kyndryl draft plans for water, energy, and climate. Dell notes intention to expand beyond climate in future, aligning with Kyndryl's multi-category approach.

---

## Group B — Implied or partial in Kyndryl draft

### B1. Data sources — primary vs secondary
**OEM content:** Dell's PCF Calculator is built on "comprehensive LCA models" where "all parameters of the models are updated" and it can execute full LCA (p. 2). Dell conducted "full LCAs on numerous products with help of third-party consultants, built a custom, energy-optimized PCF tool that complies with ISO 14040" (p. 2). Dell uses PAIA (Product Attribute Impact Algorithm) as an alternative, which is "based on IEC TR 62921" (p. 2–3). For PAIA, data is "typically depicted by an average value, along with the appropriate standard deviation" (p. 2). Dell also uses bill-of-materials (BoM) and obtaining "detailed information on manufacturing impact areas from ODMs and suppliers" (p. 4). Background database used not explicitly named in this document.
**Kyndryl draft:** Implied secondary. Leverages existing Product Carbon Footprints.
**Comparison:** Aligned in approach. Both use secondary data. Dell's ratio of primary (supplier-specific BoM, manufacturing hotspots) to secondary (standard PAIA, third-party LCA) not quantified. Background database not named in Dell document.

### B2. Use-phase assumptions
**OEM content:** Use phase assumes "energy consumption" by equipment in a given time frame at customer location (p. 2). Energy sourcing and grid carbon intensity are critical: Dell shows dramatic variance in PCF based on "energy mix and the specific hardware configuration" including geographic location and electricity source (renewable, coal, nuclear) (p. 4–5). Use phase is typically higher for infrastructure products than client products (p. 4). Dell references "energy sourcing decisions like variations in the power grid and the electricity source" as a major driver. No explicit power draw (TDP), utilization rate, or lifetime assumption is stated in this document beyond country-specific grid mix variation.
**Kyndryl draft:** Partial. 5-year lifetime stated (via FU). Use-phase grid mix implied via Canada/Project North Star site data, but no explicit utilization rate, TDP, or workload assumption.
**Comparison:** Partially aligned. Both recognize grid mix drives use phase. Neither document specifies utilization rate, TDP, or explicit lifetime. Kyndryl assumes 5-year FU; Dell's lifetime assumption not stated in this FAQ.

### B3. End-of-life modeling approach
**OEM content:** EOL phase is described as "recycling, refurbishing or disposal of the product" (p. 2) and is included in PCF scope. However, the specific modeling approach (credit vs burden, recycled content, avoided burden) is not detailed in this FAQ. Transportation and EOL phases are noted as "relatively lower for the ICT industry than they are for the other two phases" and Dell will "focus on emissions related to Transport and EOL for overall improvement" (p. 5).
**Kyndryl draft:** EoL is in scope, but the modeling approach (cut-off vs recycled content vs avoided burden) is not specified.
**Comparison:** Aligned on silence. Both include EoL in scope but neither document specifies the modeling approach (system expansion, avoided burden, recycled content credit, PEF Circular Footprint Formula, etc.).

---

## Group C — Not addressed in Kyndryl draft

### C1. Standards conformance
**OEM content:** Dell PCF Calculator "is built with ISO 14040, which is a voluntary certification and an overarching standard that encompasses all four phases of an LCA, defining a life cycle assessment and how to conduct it" (p. 3). Dell states compliance with ISO 14040. PAIA methodology "is not ISO compliant" but "has provided the IT industry with a reasonable and transparent baseline" and is "based on IEC TR 62921" (p. 3). Dell notes "third-party expert" involvement to ensure "established best practices" and is "currently discussing being ISO 14044 compliant will give customers greater assurance about our approach" (p. 3).
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM explicit. Dell claims ISO 14040 compliance for PCF Calculator. PAIA uses IEC TR 62921 (not ISO 14040/44). Third-party review mentioned informally but verification status not fully clear in this document.

### C2. LCIA method (characterization model)
**OEM content:** Not stated. The document describes "carbon emissions" and reference to "greenhouse gas emissions" and "CO2-equivalent" but does not name a characterization model (IPCC AR5, IPCC AR6, ReCiPe, CML-IA, EF 3.1, TRACI, etc.). The methodology is described as "comprehensive LCA models" but the specific LCIA method is not disclosed in this FAQ.
**Kyndryl draft:** [NOT STATED]
**Comparison:** Both silent. Neither document specifies LCIA characterization method.

### C3. Cut-off / completeness rules
**OEM content:** Not explicitly stated. The document references "obtaining detailed information on manufacturing impact areas (hotspots)" which implies a cut-off or materiality threshold, but no explicit rule (e.g., <1% mass, <1% energy, <5% cumulative) is stated.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM silent. Dell's cut-off rule not described in this document.

### C4. Temporal boundary / data vintage
**OEM content:** Document is dated March 2024. Dell references updating PCF tool as "suppliers improve their processes, use more recycled materials and switch to renewable energy sources" (p. 5). PAIA is based on "a product's lifecycle and is typically depicted by an average value, along with the appropriate standard deviation" (p. 2). No explicit reference year for background data or BoM vintage is provided.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM partially stated. Document date is March 2024. Data vintage/reference year not explicitly stated. Implication that data is updated dynamically (no fixed baseline year apparent).

### C5. Data quality assessment
**OEM content:** Not stated. The document mentions "standard deviation" for PAIA method (p. 2) as a measure of uncertainty but does not describe a pedigree matrix, qualitative narrative, or ISO 14044 data quality criteria (time-, geographic-, technology-representativeness; precision; completeness; consistency).
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM mostly silent. Dell mentions standard deviation as uncertainty representation but no formal data quality assessment described.

### C6. Uncertainty & sensitivity analysis
**OEM content:** Limited. PAIA provides "the PCF value at the 5th and 95th percentile to account for possible uncertainties" (p. 2). Dell notes that "comparisons from generation to generation or between models of the manufacturer could be explored. However, a comparison between different brands will be uncertain due to the use of different data and assumptions. The discrepancies introduced through differences in primary data, tools and modeling will not be large, so results are always given with a deviation channel and/or formulated as an estimated impact." (p. 3) Geographic variation and configuration-dependence are acknowledged as sources of variance, but no formal sensitivity analysis is described.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM partial. Dell provides 5th/95th percentile bounds for PAIA, mentions deviation channel, but no systematic sensitivity analysis to key parameters (lifetime, grid mix, utilization) is described.

### C7. Critical review / third-party verification
**OEM content:** Dell mentions "third-party expert" involvement: "In addition, being compliant will give customers greater assurance about our approach" and notes a plan toward "ISO 14044 compliant will give customers greater assurance" (p. 3). However, no specific third-party reviewer name, scope of review (methodology only vs data vs both), or verification credentials are provided in this FAQ. The statement suggests third-party review is planned or in discussion but not yet fully implemented.
**Kyndryl draft:** [NOT STATED]
**Comparison:** OEM partial/planned. Dell references third-party review as planned but not fully described. No independent reviewer named; scope and completion status unclear.

### C8. Reporting transparency
**OEM content:** Dell discloses methodology at a high level (lifecycle stages, factors, geographic variation) in this FAQ but does not publish detailed inventory data, BoM, or itemized flows in this document. The document references "obtaining detailed information on manufacturing impact areas (hotspots)" and customized models for product categories (p. 2, 4) but does not provide numerical bill-of-materials, energy values per component, or EoL recovery rates publicly in this document. Dell notes expansion of PCF Calculator to more categories and "one standard approach to all product categories" in the future (p. 6).
**Kyndryl draft:** [NOT STATED]
**Comparison:** Medium transparency. Dell publishes FAQ and references PCF values for specific products (e.g., R750 regional variation) but detailed inventory and parameters appear proprietary or in supplementary tools (Dell PCF Calculator, PAIA white papers referenced but not included here).

### C9. Circularity-specific metrics (opportunistic — covered by parallel workstream)
**OEM content:** Not stated in this document. EOL phase is mentioned as "recycling, refurbishing or disposal" (p. 2) but no metrics such as recycled content %, recyclability %, reuse/refurb rate, or design-for-disassembly are provided. Dell notes "suppliers improve their processes, use more recycled materials and switch to renewable energy sources" (p. 5) implying use of recycled materials in supply chain but no quantitative metrics.
**Kyndryl draft:** [NOT STATED in goal/scope doc]
**Comparison:** OEM silent. No explicit circularity metrics. Absence is expected per instructions.

---

## Gaps vs Kyndryl draft
- **B2 Use-phase assumptions:** Dell provides explicit grid carbon intensity data (kg CO2e/kWh by country); Kyndryl draft mentions site-specific data but no grid mix values disclosed in draft document.
- **C1 Standards conformance:** Dell explicitly cites ISO 14040 compliance and references IEC TR 62921 for PAIA; Kyndryl draft is silent on standards.
- **C4 Temporal boundary:** Dell updates PCF as supplier data changes; Kyndryl draft does not specify data vintage or update schedule.

---

## Goes beyond Kyndryl draft
- **Dual methodology approach:** Dell uses two PCF calculation methods (Dell PCF Calculator via ISO 14040 and PAIA via IEC TR 62921) to enable consistency across product categories and flexibility; Kyndryl's approach is single-method.
- **Geographic variance quantification:** Dell quantifies use-phase PCF by grid mix (shows R750 variance from ~20 kg CO2e in Norway to ~240 kg CO2e in China); Kyndryl assumes single site (Canada Project North Star).
- **Percentile-based uncertainty:** PAIA provides 5th and 95th percentile bounds; Kyndryl draft does not describe uncertainty.
- **Configuration-dependent modeling:** Dell notes PCF varies with hardware configuration, capacity, and energy draw; Kyndryl draft treats component as black box.
- **Future multi-category expansion:** Dell explicitly plans to expand PCF tool to keyboards, mice, docking stations, data center products, and additional environmental impact categories beyond climate; Kyndryl is currently climate + water + energy.

---

## Notable absences in OEM doc
- **A7 Allocation procedure:** No explicit allocation method (subdivision, physical, economic) stated.
- **C2 LCIA characterization model:** No specific model name (IPCC AR5/AR6, ReCiPe, CML, EF, TRACI) disclosed.
- **C3 Cut-off rules:** No materiality threshold or completeness rule described.
- **C5 Data quality assessment:** No pedigree matrix or ISO 14044 data quality criteria documented.
- **C7 Third-party verification:** Mentioned as planned but no specific reviewer, scope, or status provided.
- **C9 Circularity metrics:** No recycled content %, recyclability %, or refurbishment rate quantified.

---

## Direct quotes for citation
1. "The product carbon footprint (PCF) of a product in a cradle-to-grave assessment and includes emissions related to four key product lifecycle stages: Manufacturing phase; Logistics or Transportation phase; Use phase; EOL phase." (p. 2)

2. "The Dell PCF Calculator is built with ISO 14040, which is a voluntary certification and an overarching standard that encompasses all four phases of an LCA, defining a life cycle assessment and how to conduct it." (p. 3)

3. "No. As depicted in the graph below, the emissions for the Manufacturing, Transportation and End-of-Life phases remain static no matter where the configuration is being used. However, a variety of factors—including the geographic location's energy mix and the specific hardware configuration—have a significant impact on the Use phase of the product carbon footprint." (p. 4)

4. "Emissions in the ICT industry are mainly driven by the Manufacturing and Use phases of products...On an end-to-end basis, estimates of total PCF (across all four lifecycle stages) for infrastructure products are typically much larger than estimates for client products." (p. 4)

5. "Although the PAIA methodology is not ISO compliant, it has provided the IT industry with a reasonable and transparent baseline PCF. PAIA, which follows IEC TR 62921 and is a quantification method for greenhouse gas emissions for ICT systems to estimate product carbon footprints." (p. 3)

6. "Yes. As our suppliers improve their processes, use more recycled materials and switch to renewable energy sources, the manufacturing footprint of the products they support may change." (p. 5)
