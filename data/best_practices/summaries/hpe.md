# HPE — Methodology Extraction

**Source file:** hpe-methodology.pdf
**Source type:** methodology doc
**Document title:** HPE product carbon footprint methodology
**Document date / version:** Revision 3 (a0014417GENW, Rev. 3), Copyright 2025
**Total pages reviewed:** 12

## Group A — Explicit in Kyndryl draft

### A1. Goal of the study
**OEM content:** "The goal of HPE PCFs is to accurately estimate the cradle-to-grave GHG emissions of HPE products. The reason for carrying out this study is to provide PCF results to customers upon request and satisfy regulatory requirements. The intended audience includes sustainability experts and life cycle analysis (LCA) practitioners." (p. 3) HPE also states the study supports data transparency and accuracy improvements. (p. 3)
**Kyndryl draft:** Assess environmental impacts of IT hardware in Kyndryl's owned data centers, cradle-to-grave, to identify circularity improvement areas. Sub-goals: develop a baseline LCA methodology for IT data center hardware; inform Kyndryl's product sourcing decisions.
**Comparison:** Partially aligned. Both aim for cradle-to-grave emissions quantification, but HPE emphasizes customer disclosure and regulatory compliance, while Kyndryl emphasizes internal baseline-building and sourcing decisions. Both are descriptive rather than comparative.

### A2. Intended audience & commissioner
**OEM content:** "The intended audience includes sustainability experts and life cycle analysis (LCA) practitioners." (p. 3) HPE is the commissioner and manufacturer. The document is a technical white paper, implicitly for public/customer disclosure given the PCF reporting framework and DEKRA verification (p. 10).
**Kyndryl draft:** Designed for Kyndryl Holdings, Inc. Initiated by Northwestern University.
**Comparison:** Different. HPE targets external audiences (customers, sustainability practitioners) and is self-commissioned; Kyndryl is internal with external (university) initiation.

### A3. Product system / scope of hardware
**OEM content:** "HPE sells a wide array of hardware including infrastructure, server, storage, and networking products. These products are sold as build to order (BTO), configured to order (CTO), or individual option kits. Configured to order allows the customer to customize their product by selecting multiple part numbers that are preassembled and tested." (p. 3) The PCF is measured per piece. The system boundary is cradle-to-grave including manufacturing, transportation, use, and end-of-life. (p. 4–5)
**Kyndryl draft:** IT hardware in Kyndryl's owned data centers. In scope: GPUs, rack servers, HDDs, SSDs.
**Comparison:** Aligned. HPE covers hardware including servers and storage (overlapping with Kyndryl's scope) and treats products modularly. HPE goes broader (includes networking); Kyndryl is narrower (specific component types in owned DC).

### A4. Functional unit
**OEM content:** "The PCF declared unit (also known as a unit of analysis) is measured per piece and defined within the PCF report by the category and description for each part number." (p. 3) HPE defines the declared unit per individual product piece/SKU.
**Kyndryl draft:** One hardware component operating for five years.
**Comparison:** Different. HPE's FU is "per piece" (one unit of that SKU) with no explicit lifetime assumption in the PCF report; Kyndryl explicitly specifies a 5-year operational lifetime as part of the FU. HPE's lifetime is implicit in use-phase modeling (see B2).

### A5. System boundary — lifecycle stages
**OEM content:** Includes manufacturing (base unit, commodity, assembly), transportation (freight, distribution), use phase, and end-of-life. (p. 4–5) GHG emissions are subdivided by lifecycle stage: manufacturing, transportation, use, and EoL. (p. 4, Figure 1) Service and repair processes are excluded due to irregularity. (p. 5)
**Kyndryl draft:** Cradle-to-grave: raw materials extraction, manufacturing, operating use, end-of-life. Transportation explicitly excluded due to data collection complexity.
**Comparison:** Partially aligned. HPE includes all four stages (manufacturing, transport, use, EoL) whereas Kyndryl explicitly excludes transportation. Both cover raw materials through manufacturing and EoL. Service/repair excluded by both.

### A6. Geographic boundary
**OEM content:** "The choice of FY 2020 is in alignment with the baseline year for our value chain net-zero commitments. The geographic scope is generally global except for the calculation of manufacturing and energy use emissions which are country specific." (p. 3) Use-phase emissions use country-specific grid mix. Manufacturing is global average except for category-specific details.
**Kyndryl draft:** Kyndryl-owned data center in Canada. Site-specific data from Project North Star.
**Comparison:** Different. HPE uses global scope (except country-specific grid mix for use phase); Kyndryl is site-specific to Canada/Project North Star. HPE's approach is broader for comparability; Kyndryl's is granular for accuracy at a specific facility.

### A7. Allocation procedure
**OEM content:** "HPE uses allocation models for the assembly unit process by dividing the annual GHG emissions from energy use by the yearly quantity of products produced by each factory. In cases where the commodity and base unit manufacturing locations serve multiple customers, the energy and emissions data is allocated to represent HPE related values." (p. 5)
**Kyndryl draft:** Economic allocation, based on market price of co-products.
**Comparison:** Different. HPE allocates by production volume (mass/quantity) at the assembly stage; Kyndryl uses economic allocation (market price). No mention in HPE of economic allocation or broader co-product handling.

### A8. Impact categories
**OEM content:** HPE reports climate change (GHG emissions, kg CO2e) only. The document is titled "product carbon footprint methodology" and focuses exclusively on kg CO2e per item. (p. 3, and throughout)
**Kyndryl draft:** Water use (m³), resource/energy use (MJ), climate change (kg CO₂e).
**Comparison:** Different. HPE reports only climate (PCF scope); Kyndryl plans a full LCA with three impact categories including water and resource use. HPE is narrower, more focused; Kyndryl is broader.

---

## Group B — Implied or partial in Kyndryl draft

### B1. Data sources — primary vs secondary
**OEM content:** "HPE digitally collects relevant carbon data for each part number from our internal operations, sales, engineering, and other databases. HPE also digitally collects emissions from our IT supply chain. In addition, we also rely on several external emission factors databases including IEA, ecoinvent, Ember Climate, U.S. Environmental Protection Agency (EPA), and others." (p. 6) For manufacturing, HPE uses component PCFs from suppliers (primary where available), custom attribute models, and category-average models. (p. 6–7, Table 1–2) Background databases: IEA 2021 (2023 edition), ecoinvent v3.10, Ember Climate. (p. 6–7) Primary data includes bill of materials, annual energy consumption, production volumes, and supplier PCFs. (p. 6)
**Kyndryl draft:** Implied secondary. Draft says it "leverages existing Product Carbon Footprints for climate change impact calculations" — i.e., Kyndryl is a downstream user of OEM PCFs, not a primary data collector.
**Comparison:** Aligned. Both rely primarily on secondary data (external databases and supplier PCFs). HPE collects primary data for specific activities (energy, production volume) but dominantly uses secondary sources. Kyndryl is purely secondary by design.

### B2. Use-phase assumptions
**OEM content:** "Average power consumption is obtained from system measurements during the use of the product or estimated by HPE internal power estimates. Lifetime: average power consumption times the number of years in a product's lifetime. Emissions are estimated from grid emissions factors in the country where the product is used during the years of operation." (p. 8, Table 4) Grid emissions intensity (grams of CO2e per kWh) sourced from Ember Climate by country and per year. (p. 8) Power usage effectiveness (PUE) is applied: "After scaling the power consumption by PUE, the emissions calculation proceeds in the same manner." (p. 8) Lifetime is variable (not specified in methodology as fixed), PUE-style multiplier is applied for data center equipment. (p. 8)
**Kyndryl draft:** Partial. 5-year lifetime stated (via FU). Use-phase grid mix implied via Canada/Project North Star site data, but no explicit utilization rate, TDP, or workload assumption.
**Comparison:** HPE more explicit. HPE specifies lifetime as a product input parameter (variable by product), grid mix by country/year (Ember), and includes PUE multiplier for data center use. Kyndryl fixes lifetime at 5 years but does not disclose TDP, utilization, or PUE assumptions yet.

### B3. End-of-life modeling approach
**OEM content:** "The End-of-life life cycle stage includes emissions associated with recycling and disposing of the item at the end of its useful life, including transportation and disposal processing such as landfilling or recycling. We estimate emissions associated with transportation based on the volumetric weight of the product and assuming it is transported 1000 km by truck to its disposal location. We estimate emissions associated with the disposal end-of-life processing by assuming that 20% of weight of products will be disposed in landfill and 80% of weight of products will be recycled. The result of the LCIA for this unit process is emissions in kg CO2e per item." (p. 8, Table 5)
**Kyndryl draft:** EoL is in scope, but the modeling approach (cut-off vs recycled content vs avoided burden) is not specified.
**Comparison:** HPE explicit and transparent. HPE uses cut-off approach with fixed assumptions: 20% landfill, 80% recycled by mass, 1000 km transport to disposal. No avoided burden or recycled-content credits claimed. Kyndryl has not yet specified the approach.

---

## Group C — Not addressed in Kyndryl draft

### C1. Standards conformance
**OEM content:** "This document follows the GHG Protocol Product Standard, which requires the reporting entity (in this case HPE) to disclose the following methodology information: general information and scope, boundary setting, allocation, data collection and quality, uncertainty, inventory results, and assurance. HPE collects data from our value chain using the Partnership for Carbon Transparency (PACT) Methodology. Our carbon footprint implements the CFP systematic approach defined by ISO 14067 and the PCF models follow the streamlined CFP methodology defined by IEC 62921. The PCF is further guided by IEC 62725, ISO 14040 and ISO 14044." (p. 3)
**Kyndryl draft:** [NOT STATED]
**Comparison:** HPE explicitly cites GHG Protocol Product Standard, ISO 14067, IEC 62231, ISO 14040, ISO 14044. Conformance is claimed and verified by DEKRA (third-party assurance, p. 10).

### C2. LCIA method (characterization model)
**OEM content:** "Component PCFs from Suppliers complying with PACT Methodology include mandatory attributes such as secondary emission factors, IPCC AR5, and AR6 100-yr global warming potential (GWP) factors." (p. 6) "IPCC AR5, and AR6 100-yr global warming potential (GWP) factors" for GHG. (p. 6) Grid emissions intensity from Ember Climate. EoL uses IPCC AR6 global warming potential (GWP). (p. 8)
**Kyndryl draft:** [NOT STATED] — categories listed but no characterization method named.
**Comparison:** HPE specifies IPCC AR5 and AR6 GWP (100-year) for climate impact characterization. Method is clear and standard.

### C3. Cut-off / completeness rules
**OEM content:** "HPE currently does not include any nonattributable processes in the PCF calculations. We also exclude service and repair processes due to the irregularity of when this process is required, the diversity of repair activities, and the assumption that this process would yield a negligible impact well below the allowed 5% cut-off criterion." (p. 5)
**Kyndryl draft:** [NOT STATED]
**Comparison:** HPE states a 5% cut-off threshold and excludes service/repair processes as below that threshold.

### C4. Temporal boundary / data vintage
**OEM content:** "The choice of FY 2020 is in alignment with the baseline year for our value chain net-zero commitments." (p. 3) Background databases: IEA 2021 (2023 edition), ecoinvent v3.10. (p. 6) Grid emissions data from Ember Climate: "per year" by country, implying annual updates. (p. 8) No explicit statement about annual updates to PCF reports, but data vintage is FY 2020 baseline with rolling database updates (e.g., IEA 2023 edition).
**Kyndryl draft:** [NOT STATED]
**Comparison:** HPE references year FY 2020 for baseline, uses up-to-date databases (IEA 2023 edition, ecoinvent v3.10), and grid data by year. Data is kept current via rolling database updates.

### C5. Data quality assessment
**OEM content:** "Data quality checks are applied at every stage of our data collection and PCF calculation process. Understanding the sensitivity of calculations to the inputs applied, HPE carefully reviews and validates each input before insertion into the respective formulas... Data quality checks at the product, component, and assembly level include reviewing the correct classification of all materials, category assignments, attributes, weight, and volume... Grid data are gathered and quality checked at the transportation phase include verifying the applied emission factor for GLEC, weight/distance/mode validation is done by reviewing the same products shipped across the same factory to customers within the same region/country." (p. 9)
**Kyndryl draft:** [NOT STATED]
**Comparison:** HPE employs a qualitative data quality framework: manual review and machine learning validation at multiple stages (product, component, assembly, transport). No formal pedigree matrix reported, but systematic checks are documented.

### C6. Uncertainty & sensitivity analysis
**OEM content:** "HPE uses the first-order error propagation method (or Gaussian method) based on the uncertainties of the individual inputs to aggregate statistical uncertainty. This approach conforms to the 1st Tier IEC PCR Guidance and Uncertainty Management. Each unit process provides a mean value and percent uncertainty of the GHG emissions. When multiple unit processes are sourcing GHG emissions, the uncertainties are assimilated in such a way as uncorrelated among unit processes, and thus the total uncertainty is calculated from the square root of the sum of the squares of each unit process uncertainty (that is, uncertainties summed in quadrature)... Uncertainty of the carbon footprint for each unit process is estimated based on knowledge of the process and understanding of the data quality for that process. Uncertainty can stem from use of secondary data, allocation, temporal, geographic, completeness, or reliability of the data. For example, uncertainty from use stage emissions occurs from yearly country level grid intensities (both temporal and geographic uncertainty). To mitigate this uncertainty, customers are allowed to use their own custom-defined grid intensity." (p. 9)
**Kyndryl draft:** [NOT STATED]
**Comparison:** HPE reports quantitative uncertainty using first-order error propagation (Gaussian method). Each unit process outputs a mean and percent uncertainty. Allows customers to input custom grid intensity to reduce geographic/temporal uncertainty.

### C7. Critical review / third-party verification
**OEM content:** "Our product carbon footprint methodology has been verified and assured by DEKRA. During the assurance process, the DEKRA team performed a thorough review of our calculation methodology, major assumptions, inputs, data quality and governance and verified several standards including ISO 14067, ISO 14040, ISO 14044, and GHG Protocol Product Standard. As a result of this process DEKRA has provided a limited assurance certificate available at the end of this document." (p. 10) Verification statement is included (p. 11).
**Kyndryl draft:** [NOT STATED]
**Comparison:** HPE had independent third-party review and verification by DEKRA (May 8, 2025, per verification statement, p. 11). Scope includes methodology, major assumptions, inputs, data quality, governance, and standards alignment.

### C8. Reporting transparency
**OEM content:** Rating: Medium-High. The document provides detailed descriptions of data sources, calculation methodologies, and key assumptions for each lifecycle stage. Tables 1–5 itemize primary data collected and emission factors used (bill of materials, energy consumption, production volumes, transport parameters, power draw, lifetime, EoL split). Inventory results (Section 7, p. 9) lists detailed output format including company name, unique PCF ID, GHG emissions by lifecycle stage, uncertainty, product configuration, part number, category, description, quantity, settings, product lifetime dates, PUE, location, and average power. However, numerical values for specific products are not provided in this methodology document (expected in actual PCF reports). The methodology itself is transparent and reproducible.
**Kyndryl draft:** [NOT STATED]
**Comparison:** HPE reports medium-high transparency. The methodology document is detailed and systematic; actual PCF reports will contain itemized data. This document does not include proprietary product-specific inventory details (expected in individual PCF disclosures).

### C9. Circularity-specific metrics (opportunistic — covered by parallel workstream)
**OEM content:** End-of-life modeling includes recycling rate assumption (80% recycled by mass, 20% landfilled) (p. 8, Table 5). No separate recycled content input, reuse rate, design-for-disassembly score, or take-back program coverage metrics are reported in this PCF methodology document.
**Kyndryl draft:** [NOT STATED in goal/scope doc] — circularity is the study's purpose but is being addressed through a separate qualitative analysis of vendor take-back programs and annual sustainability reports, not through PCFs/LCAs.
**Comparison:** HPE includes a basic recycling rate assumption (80% recycled) in EoL modeling but does not report circularity-specific metrics beyond that. Absence of deeper circularity data (e.g., design-for-disassembly, take-back coverage) is expected and aligns with C9 scope — belongs in parallel sustainability workstream, not here.

---

## Gaps vs Kyndryl draft

- **B2 (Use-phase assumptions):** HPE explicitly documents power draw, product lifetime (variable), PUE multiplier for data centers, and country-specific grid mix by year. Kyndryl draft is silent on TDP, utilization, and PUE; these are candidates for addition to Kyndryl's methodology.
- **B3 (End-of-life modeling):** HPE specifies EoL approach (cut-off method with 20% landfill / 80% recycled by mass, 1000 km transport). Kyndryl draft is silent; this approach is a concrete candidate for Kyndryl adoption or comparison.
- **C1 (Standards conformance):** HPE cites GHG Protocol, ISO 14067, ISO 14040, ISO 14044, IEC 62921, IEC 62725. Kyndryl draft silent; standards citation is expected for formal methodology.
- **C2 (LCIA method):** HPE specifies IPCC AR5 and AR6 GWP (100-yr). Kyndryl draft lists impact categories but not characterization method; IPCC AR5/AR6 is a standard candidate.
- **C3 (Cut-off rules):** HPE explicitly states 5% cut-off and excludes service/repair. Kyndryl draft silent.
- **C4 (Temporal boundary / data vintage):** HPE references FY 2020 baseline and uses rolling database updates (IEA 2023 edition). Kyndryl draft silent.
- **C5 (Data quality assessment):** HPE describes multi-stage quality checks (manual and machine learning). Kyndryl draft silent.
- **C6 (Uncertainty & sensitivity):** HPE reports first-order error propagation with quantified percent uncertainty per process. Kyndryl draft silent.
- **C7 (Critical review):** HPE had DEKRA third-party verification. Kyndryl draft silent; verification is a governance best practice.

---

## Goes beyond Kyndryl draft

- **Supplier primary PCF collection:** HPE actively collects component-level PCFs from suppliers (compliant with PACT Methodology) and evaluates them against data quality standards before use. Kyndryl draft is silent on whether it will request primary PCFs from OEMs or accept secondary data only.
- **Attribute modeling for missing PCFs:** HPE has developed attribute models (custom-built based on key product features like PCB size, die sizes, NAND flash for SSDs) to fill gaps when supplier PCFs are unavailable. Table 2 shows SSD and Server/Storage models. This is a structured fallback not mentioned in Kyndryl draft.
- **Category-average fallback:** HPE uses LCA-based category-average models as a third-tier fallback when both primary PCF and attribute models are unavailable. (p. 7)
- **Dynamic grid mix by country and year:** HPE uses Ember Climate data to source grid intensity by specific country and year, allowing customers to override with site-specific grids. Kyndryl specifies Canada/Project North Star but doesn't mention annual grid data updates.
- **PUE scaling for data center use:** HPE includes a Power Usage Effectiveness (PUE) multiplier to account for cooling and auxiliary infrastructure in data centers. (p. 8) Kyndryl's methodology does not yet address PUE.
- **First-order error propagation uncertainty:** HPE quantifies uncertainty at the unit process level and aggregates in quadrature. Kyndryl draft silent on uncertainty quantification.
- **Allowable customer override for grid intensity:** HPE documentation states customers may provide their own custom grid intensity to reduce uncertainty. (p. 9) This enables flexibility that Kyndryl may or may not adopt.

---

## Notable absences in OEM doc

- **Water and resource/energy impact categories:** HPE reports only climate (PCF scope); does not quantify water use, resource depletion, or MJ energy per the Kyndryl draft goal. This is expected for a PCF-focused methodology, not a full LCA.
- **Recycled content input tracking:** HPE EoL model assumes 80% recycled by mass but does not track recycled content percentages in input materials. No avoided-burden credit for pre-consumer recycled content is mentioned.
- **Comparative assertions / benchmark reporting:** HPE's methodology supports product disclosure but the document does not discuss how individual PCFs would be compared or ranked (e.g., per watt, per TB, per service-year).
- **Sensitivity analysis results:** The methodology describes uncertainty propagation but does not present sensitivity results (e.g., "carbon footprint varies ±X% if lifetime changes").
- **Transportation detail vs. Kyndryl:** HPE includes inbound and distribution transportation (p. 4–5, Section 3.1.2, Table 3); Kyndryl explicitly excludes transportation due to data complexity. This is an acknowledged methodological difference.
- **Cradle-to-grave specifics for raw materials:** HPE references IEA and ecoinvent for material emissions but does not detail ore extraction, refining, or material processing assumptions. (p. 6)

---

## Direct quotes for citation

1. "The goal of HPE PCFs is to accurately estimate the cradle-to-grave GHG emissions of HPE products." (p. 3)

2. "HPE uses allocation models for the assembly unit process by dividing the annual GHG emissions from energy use by the yearly quantity of products produced by each factory." (p. 5)

3. "HPE digitally collects relevant carbon data for each part number from our internal operations, sales, engineering, and other databases. HPE also digitally collects emissions from our IT supply chain... we also rely on several external emission factors databases including IEA, ecoinvent, Ember Climate, U.S. Environmental Protection Agency (EPA)." (p. 6)

4. "Average power consumption is obtained from system measurements during the use of the product or estimated by HPE internal power estimates... Emissions are estimated from grid emissions factors in the country where the product is used." (p. 8)

5. "We estimate emissions associated with the disposal end-of-life processing by assuming that 20% of weight of products will be disposed in landfill and 80% of weight of products will be recycled." (p. 8)

6. "HPE uses the first-order error propagation method (or Gaussian method) based on the uncertainties of the individual inputs to aggregate statistical uncertainty." (p. 9)

7. "Our product carbon footprint methodology has been verified and assured by DEKRA... DEKRA has provided a limited assurance certificate." (p. 10)

8. "This document follows the GHG Protocol Product Standard... implements the CFP systematic approach defined by ISO 14067 and the PCF models follow the streamlined CFP methodology defined by IEC 62921... further guided by IEC 62725, ISO 14040 and ISO 14044." (p. 3)
