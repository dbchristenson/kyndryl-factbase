# Schema Update — Post-Update Reference

## Section 1: Changelog

| Table | Change Type | Column / Entity | Description |
|---|---|---|---|
| `component` | Added | `product_family` | Groups hardware generations for filtering/grouping |
| `component` | Added | `pcf_source` | Records where the PCF value was obtained |
| `component` | Added | `pcf_confidence` | Data quality indicator for emissions values |
| `component` | Added | `power_draw_watts_typical` | Typical operating power for efficiency calculations |
| `component` | Removed | `circularity_score` | Subjective metric removed; circularity assessed at program level |
| `mainframe` | Added | `msu_rating` | IBM standard capacity metric for cross-generational comparison |
| `mainframe` | Added | `num_cps` | Configurable Central Processors for per-core normalization |
| `mainframe` | Added | `num_ifls` | IFL count for Linux-dedicated capacity tracking |
| `rack_server` | Added | `num_cores` | Total physical CPU cores for per-core normalization |
| `rack_server` | Added | `benchmark_score` | Standardized benchmark score (throughput numerator) |
| `rack_server` | Added | `benchmark_type` | Identifies which benchmark standard was used |
| `gpu` | Added | `tflops_fp16` | Half-precision throughput for AI inference performance |
| `gpu` | Added | `tflops_fp32` | Single-precision throughput for general compute |
| `data_source` | New table | — | Per-field data provenance tracking for components and programs |
| `scenario_option_component` | New table | — | Association table linking scenario options to components with quantity and role |
| `migration_scenario` | New table | — | Parent entity for migration pilot evaluations with shared assumptions |
| `scenario_option` | New table | — | Individual options within a migration scenario |

---

## Section 2: Complete Schema Reference

### `company`

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | INTEGER | PK | — |
| `name` | VARCHAR(50) | No | Vendor Name |

### `circularity_program`

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | INTEGER | PK | — |
| `company_id` | FK → company.id | No | Vendor |
| `name` | VARCHAR(50) | No | Program Name |
| `program_type` | VARCHAR(50) | No | Program Type |
| `description` | TEXT | No | Description |
| `eligibility_criteria` | TEXT | No | Eligibility Criteria |
| `avg_reimbursement_rate` | REAL | Yes | Avg Reimbursement Rate |

### `component`

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | INTEGER | PK | — |
| `company_id` | FK → company.id | No | Vendor |
| `name` | VARCHAR(50) | No | Product Name |
| `release_year` | INTEGER | No | Release Year |
| `product_family` | VARCHAR(50) | Yes | Product Family |
| `type` | VARCHAR(50) | No | *(polymorphic discriminator)* |
| `pcf_value` | REAL | Yes | Reported Emissions (kgCO2e) |
| `pcf_boundary` | VARCHAR(50) | Yes | Emissions Scope |
| `pcf_assumptions` | TEXT | Yes | Emissions Assumptions |
| `pcf_source` | VARCHAR(255) | Yes | PCF Data Source |
| `pcf_confidence` | VARCHAR(50) | Yes | PCF Confidence Level |
| `power_draw_watts_tdp` | REAL | Yes | Max Power (Watts TDP) |
| `power_draw_watts_typical` | REAL | Yes | Typical Power (Watts) |
| `power_draw_watts_idle` | REAL | Yes | Idle Power (Watts) |
| `list_price_capex` | REAL | No | List Price (CAPEX) |
| `is_lease_available` | Boolean | No (default False) | Lease Available? |
| `monthly_lease_opex` | REAL | Yes | Monthly Lease (OPEX) |
| `lease_term_months` | INTEGER | Yes | Lease Term (Months) |

### `mainframe` *(inherits `component`)*

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | FK → component.id | PK | — |
| `mips_rating` | INTEGER | Yes | MIPS (Performance) |
| `msu_rating` | INTEGER | Yes | MSU Rating |
| `num_cps` | INTEGER | Yes | Number of CPs |
| `num_ifls` | INTEGER | Yes | Number of IFLs |
| `floor_space_sqft` | REAL | No | Floor Space (sqft) |

### `rack_server` *(inherits `component`)*

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | FK → component.id | PK | — |
| `size_u` | INTEGER | No | Rack Size (U) |
| `socket_count` | INTEGER | No | Socket Count |
| `num_cores` | INTEGER | Yes | Total CPU Cores |
| `benchmark_score` | REAL | Yes | Benchmark Score |
| `benchmark_type` | VARCHAR(50) | Yes | Benchmark Type |

### `gpu` *(inherits `component`)*

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | FK → component.id | PK | — |
| `vram_gb` | INTEGER | No | VRAM (GB) |
| `tflops_fp16` | REAL | Yes | TFLOPS (FP16) |
| `tflops_fp32` | REAL | Yes | TFLOPS (FP32) |
| `interconnect_type` | VARCHAR(50) | No | Interconnect |

### `data_source`

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | INTEGER | PK | — |
| `component_id` | FK → component.id | Yes | Component |
| `program_id` | FK → circularity_program.id | Yes | Program |
| `field_name` | VARCHAR(255) | No | Field Name |
| `url` | TEXT | Yes | Source URL |
| `notes` | TEXT | Yes | Notes |

### `migration_scenario`

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | INTEGER | PK | — |
| `name` | VARCHAR(255) | No | Scenario Name |
| `description` | TEXT | Yes | Description |
| `source_component_id` | FK → component.id | No | Source System |
| `source_quantity` | INTEGER | No (default 1) | Source Quantity |
| `evaluation_years` | INTEGER | No (default 5) | Evaluation Period (Years) |
| `electricity_cost_kwh` | REAL | No | Electricity Cost ($/kWh) |
| `grid_carbon_intensity` | REAL | No | Grid Carbon Intensity |
| `pue` | REAL | No (default 1.5) | PUE |
| `discount_rate` | REAL | No (default 0.08) | Discount Rate |
| `operating_hours_year` | INTEGER | No (default 8760) | Operating Hours/Year |
| `assumptions` | TEXT | Yes | Assumptions |

### `scenario_option`

| Column | Type | Nullable | Label |
|---|---|---|---|
| `id` | INTEGER | PK | — |
| `scenario_id` | FK → migration_scenario.id | No | Parent Scenario |
| `name` | VARCHAR(255) | No | Option Name |
| `description` | TEXT | Yes | Description |
| `financing_model` | VARCHAR(50) | Yes | Financing Model |
| `circularity_program_id` | FK → circularity_program.id | Yes | Takeback Program |
| `residual_value_estimate` | REAL | Yes | Residual Value ($) |
| `additional_infra_cost` | REAL | Yes | Additional Infra Cost ($) |
| `notes` | TEXT | Yes | Notes |

### Association Tables

**`component_program_association`**

| Column | Type |
|---|---|
| `component_id` | FK → component.id (PK) |
| `program_id` | FK → circularity_program.id (PK) |

**`scenario_option_component`**

| Column | Type |
|---|---|
| `option_id` | FK → scenario_option.id (PK) |
| `component_id` | FK → component.id (PK) |
| `quantity` | INTEGER (default 1) |
| `role` | VARCHAR(50), nullable |

---

## Section 3: Relationship Map

- `Company` 1:N `Component`
- `Company` 1:N `CircularityProgram`
- `Component` N:M `CircularityProgram` (via `component_program_association`)
- `Component` → `Mainframe`, `RackServer`, `GPU` (polymorphic inheritance)
- `Component` 1:N `DataSource`
- `CircularityProgram` 1:N `DataSource`
- `MigrationScenario` N:1 `Component` (source system)
- `MigrationScenario` 1:N `ScenarioOption`
- `ScenarioOption` N:M `Component` (via `scenario_option_component`, with `quantity` and `role`)
- `ScenarioOption` N:1 `CircularityProgram` (optional)

---

## Section 4: Design Assumptions

1. **Max configuration baseline** — All hardware comparisons use max CPs/cores at full speed with standardized memory and I/O. Exact memory/IO counts are TBD but held constant across generations within a product family.
2. **Pricing approach** — `list_price_capex` on `Component` represents the most readily available price for a max configuration. Rack servers and GPUs use vendor MSRP; mainframes use refurbished dealer pricing or public procurement records. No bottom-up component-level cost decomposition.
3. **Workload portability** — Assumed. The `MigrationScenario.assumptions` field must document this for every scenario.
4. **PCF data provenance** — `pcf_confidence` tracks data quality because emissions data availability varies significantly by vendor and generation. IBM publishes PCF reports for z16/z17 but not older generations. This field ensures the analysis transparently distinguishes vendor-published values from internal estimates.
5. **Circularity at the program level** — The former `circularity_score` (a subjective 0-1 float on `Component`) was removed. Circularity is now assessed entirely through the `CircularityProgram` table and its relationship to `ScenarioOption`, which links end-of-life disposition to specific vendor programs with documented terms.
6. **GPU table is draft** — The `GPU` subclass and its fields (`tflops_fp16`, `tflops_fp32`) are provisional. The GPU analysis is lower priority and the table may change when that workstream begins.
7. **ORM retained deliberately** — The SQLAlchemy ORM with `info={}` annotations serves as both the database definition and machine-readable documentation. The schema should be frozen after this update.
8. **Scenario modeling is solution-level** — `MigrationScenario` and `ScenarioOption` model a solution comparison (e.g., 1 mainframe vs. N rack servers + M GPUs), not individual hardware benchmarks. The `scenario_option_component` association table's `quantity` and `role` columns capture the bill of materials for each option.
9. **Per-field data provenance** — The `DataSource` table documents the origin of individual data fields rather than whole records. If the same URL covers 3 fields, that's 3 rows. This keeps provenance queries simple with no arrays or JSON needed.

---

## Section 5: Open Items

| Item | Status |
|---|---|
| Memory & I/O standardization for max-config comparisons | TBD — use Redbook reference configs |
| Workload equivalence ratio (MSU -> SPECint) | TBD — research Gartner / Arcati sources |
| Rack server vendor selection for mock pilot | TBD — Dell recommended as primary |
| GPU system definition (card vs. full server) | TBD — full server recommended |
| z17 data availability (LSPR, IMPP, PCF) | TBD — check immediately; fall back to z16 if unavailable |
