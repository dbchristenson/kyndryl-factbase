# Update `models.py` — Schema Refinement for Circularity Analysis

## Context

This is a **data center circularity analysis project** for a consulting engagement. The database schema in `models.py` uses SQLAlchemy ORM with joined-table polymorphic inheritance (`Component` → `Mainframe`, `RackServer`, `GPU`). The system evaluates vendor hardware across four dimensions: **TCO, ownership structure, Scope 2/3 emissions, and circularity program value**.

This update implements decisions from a schema review session. The changes add fields required for **cross-generational energy efficiency comparison**, **emissions data provenance tracking**, and a **migration scenario modeling layer** that supports side-by-side TCO and LCA analysis of competing hardware solutions.

**Do not populate any data. This is a schema-only update.**

After all changes are applied, produce a `POST_UPDATE.md` file documenting the final state of the schema.

---

## Part 1: Modifications to Existing Tables

Follow the existing code style exactly:
- Use `mapped_column()` with explicit SQLAlchemy types (`INTEGER`, `REAL`, `VARCHAR`, `TEXT`, `Boolean`)
- Include `info={}` dicts with `"label"` and `"description"` keys on every new column
- Use parenthesized string concatenation for long descriptions
- Keep line length under ~55 characters inside `mapped_column()` blocks
- Use the existing constants: `CHAR_LIMIT_SHORT = 50`, `CHAR_LIMIT_LONG = 255`, `PRECISION = 2`
- All new numeric/string columns should be `nullable=True` unless specified otherwise
- Do **not** modify any existing columns or relationships unless explicitly instructed

### 1a. `Component` Base Class — Add Columns

**Add `product_family`** — Place in the "Basic Info" section, after `release_year` and before `type`.

```python
product_family: Mapped[str | None] = mapped_column(
    VARCHAR(CHAR_LIMIT_SHORT),
    nullable=True,
    info={
        "label": "Product Family",
        "description": (
            "Groups generations together "
            "(e.g., 'IBM z', 'Power E', "
            "'ThinkSystem SR')."
        ),
    },
)
```

**Add `power_draw_watts_typical`** — Place in the "Power" section, between `power_draw_watts_tdp` and `power_draw_watts_idle`.

```python
power_draw_watts_typical: Mapped[
    float | None
] = mapped_column(
    REAL(precision=PRECISION),
    nullable=True,
    info={
        "label": "Typical Power (Watts)",
        "description": (
            "Power draw under typical "
            "operating load. Primary "
            "denominator for efficiency "
            "calculations."
        ),
    },
)
```

**Add `pcf_source`** — Place in the "Emissions" section, after `pcf_assumptions`.

```python
pcf_source: Mapped[str | None] = mapped_column(
    VARCHAR(CHAR_LIMIT_LONG),
    nullable=True,
    info={
        "label": "PCF Data Source",
        "description": (
            "Where the PCF value was "
            "obtained (e.g., vendor report "
            "URL, internal estimate)."
        ),
    },
)
```

**Add `pcf_confidence`** — Place immediately after `pcf_source`.

```python
pcf_confidence: Mapped[str | None] = mapped_column(
    VARCHAR(CHAR_LIMIT_SHORT),
    nullable=True,
    info={
        "label": "PCF Confidence Level",
        "description": (
            "Data quality indicator. "
            "Valid values: "
            "'vendor_published', "
            "'vendor_requested', "
            "'third_party', "
            "'estimated', "
            "'unavailable'."
        ),
    },
)
```

### 1b. `Component` Base Class — Remove Column

**Delete `circularity_score` entirely.** Remove the full `mapped_column()` block and its preceding comment (`# Circularity Metric`). This field had no defensible methodology; circularity is assessed at the vendor program level via the `CircularityProgram` table instead.

### 1c. `Mainframe` Subclass — Add Columns

**Add `msu_rating`** — Place immediately after `mips_rating`.

```python
msu_rating: Mapped[int | None] = mapped_column(
    INTEGER,
    nullable=True,
    info={
        "label": "MSU Rating",
        "description": (
            "Million Service Units. "
            "IBM standard capacity and "
            "licensing metric. More "
            "stable than MIPS for "
            "cross-generational comparison."
        ),
    },
)
```

**Add `num_cps`** — Place after `msu_rating`.

```python
num_cps: Mapped[int | None] = mapped_column(
    INTEGER,
    nullable=True,
    info={
        "label": "Configurable CPs",
        "description": (
            "Number of configurable "
            "Central Processors. "
            "Required for per-core "
            "efficiency normalization."
        ),
    },
)
```

**Add `num_ifls`** — Place after `num_cps`, before `floor_space_sqft`.

```python
num_ifls: Mapped[int | None] = mapped_column(
    INTEGER,
    nullable=True,
    info={
        "label": "IFL Count",
        "description": (
            "Integrated Facility for "
            "Linux engines. Tracks "
            "Linux-dedicated capacity "
            "separately from CPs."
        ),
    },
)
```

### 1d. `RackServer` Subclass — Add Columns

**Add `num_cores`** — Place after `socket_count`.

```python
num_cores: Mapped[int | None] = mapped_column(
    INTEGER,
    nullable=True,
    info={
        "label": "Total Cores",
        "description": (
            "Total physical CPU cores. "
            "For per-core efficiency "
            "normalization."
        ),
    },
)
```

**Add `benchmark_score`** — Place after `num_cores`.

```python
benchmark_score: Mapped[
    float | None
] = mapped_column(
    REAL(precision=PRECISION),
    nullable=True,
    info={
        "label": "Benchmark Score",
        "description": (
            "Performance score from a "
            "standardized benchmark. "
            "Throughput numerator for "
            "efficiency calculations."
        ),
    },
)
```

**Add `benchmark_type`** — Place after `benchmark_score`, before `__mapper_args__`.

```python
benchmark_type: Mapped[
    str | None
] = mapped_column(
    VARCHAR(CHAR_LIMIT_SHORT),
    nullable=True,
    info={
        "label": "Benchmark Standard",
        "description": (
            "Which benchmark was used "
            "(e.g., 'SPECint_rate2017', "
            "'SPECpower_ssj2008', "
            "'TPC-C'). Only compare "
            "rows with matching type."
        ),
    },
)
```

### 1e. `GPU` Subclass — Add Columns (Draft)

**Add `tflops_fp16`** — Place after `vram_gb`, before `interconnect_type`.

```python
tflops_fp16: Mapped[
    float | None
] = mapped_column(
    REAL(precision=PRECISION),
    nullable=True,
    info={
        "label": "FP16 TFLOPS",
        "description": (
            "Half-precision throughput. "
            "Primary AI inference "
            "performance metric."
        ),
    },
)
```

**Add `tflops_fp32`** — Place after `tflops_fp16`, before `interconnect_type`.

```python
tflops_fp32: Mapped[
    float | None
] = mapped_column(
    REAL(precision=PRECISION),
    nullable=True,
    info={
        "label": "FP32 TFLOPS",
        "description": (
            "Single-precision throughput. "
            "Standard compute performance "
            "metric."
        ),
    },
)
```

---

## Part 2: New Tables

Add these after the `GPU` class at the end of `models.py`. Follow the same style conventions.

### 2a. `ScenarioOptionComponent` Association Table

Place this immediately after the existing `component_program_association` table, before the `Company` class. Add a comment block explaining its purpose.

```python
# Association table for Many-to-Many relationship
# between ScenarioOptions and Components.
# Each option in a migration scenario may include
# multiple components (e.g., rack servers + GPUs),
# each with a quantity and a role in the solution.
scenario_option_component = Table(
    "scenario_option_component",
    Base.metadata,
    Column(
        "option_id",
        ForeignKey("scenario_option.id"),
        primary_key=True,
    ),
    Column(
        "component_id",
        ForeignKey("component.id"),
        primary_key=True,
    ),
    Column(
        "quantity",
        INTEGER,
        default=1,
    ),
    Column(
        "role",
        VARCHAR(CHAR_LIMIT_SHORT),
        nullable=True,
    ),
)
```

### 2b. `MigrationScenario` Class

Place after the `GPU` class.

```python
class MigrationScenario(Base):
    """
    Parent entity for a migration pilot evaluation.
    Carries shared assumptions (electricity cost,
    carbon intensity, PUE, discount rate) and
    references the source system being replaced.
    Each scenario contains one or more
    ScenarioOptions representing competing
    solutions.
    """

    __tablename__ = "migration_scenario"

    id: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_LONG),
        info={
            "label": "Scenario Name",
            "description": (
                "Title for this evaluation "
                "(e.g., 'Banking Fraud "
                "Inference Pilot')."
            ),
        },
    )
    description: Mapped[str | None] = mapped_column(
        TEXT,
        nullable=True,
        info={
            "label": "Description",
            "description": (
                "Narrative context and "
                "scope of the evaluation."
            ),
        },
    )

    # Source system being replaced
    source_component_id: Mapped[int] = mapped_column(
        ForeignKey("component.id"),
        info={
            "label": "Source System",
            "description": (
                "The component being "
                "replaced or upgraded "
                "(e.g., the existing z14)."
            ),
        },
    )
    source_quantity: Mapped[int] = mapped_column(
        INTEGER,
        default=1,
        info={
            "label": "Source Quantity",
            "description": (
                "How many source systems "
                "are being replaced."
            ),
        },
    )

    # Shared evaluation parameters
    evaluation_years: Mapped[int] = mapped_column(
        INTEGER,
        default=5,
        info={
            "label": "Evaluation Period (Years)",
            "description": (
                "Timeframe for TCO and "
                "LCA calculations."
            ),
        },
    )
    electricity_cost_kwh: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        info={
            "label": "Electricity Cost ($/kWh)",
            "description": (
                "Assumed electricity rate "
                "for energy cost modeling."
            ),
        },
    )
    grid_carbon_intensity: Mapped[
        float
    ] = mapped_column(
        REAL(precision=PRECISION),
        info={
            "label": "Grid Carbon Intensity",
            "description": (
                "kgCO2e per kWh. Used for "
                "Scope 2 emissions "
                "calculation."
            ),
        },
    )
    pue: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        default=1.5,
        info={
            "label": "PUE",
            "description": (
                "Power Usage Effectiveness "
                "of the data center "
                "facility."
            ),
        },
    )
    discount_rate: Mapped[float] = mapped_column(
        REAL(precision=PRECISION),
        default=0.08,
        info={
            "label": "Discount Rate",
            "description": (
                "For NPV calculations. "
                "Default 8% (standard "
                "corporate IT rate)."
            ),
        },
    )
    operating_hours_year: Mapped[int] = mapped_column(
        INTEGER,
        default=8760,
        info={
            "label": "Operating Hours/Year",
            "description": (
                "Annual operating hours. "
                "Default 8760 (24/7)."
            ),
        },
    )
    assumptions: Mapped[str | None] = mapped_column(
        TEXT,
        nullable=True,
        info={
            "label": "Assumptions",
            "description": (
                "Free-text documentation "
                "of all assumptions "
                "(workload portability, "
                "exclusions, etc.)."
            ),
        },
    )

    # Relationships
    source_component: Mapped["Component"] = relationship(
        foreign_keys=[source_component_id],
    )
    options: Mapped[
        List["ScenarioOption"]
    ] = relationship(
        back_populates="scenario",
    )
```

### 2c. `ScenarioOption` Class

Place after `MigrationScenario`.

```python
class ScenarioOption(Base):
    """
    One option within a migration scenario.
    (e.g., 'Upgrade to z17' or
    'Dell Rack Servers + NVIDIA GPUs')
    References components via the
    scenario_option_component association table.
    """

    __tablename__ = "scenario_option"

    id: Mapped[int] = mapped_column(
        INTEGER, primary_key=True
    )
    scenario_id: Mapped[int] = mapped_column(
        ForeignKey("migration_scenario.id"),
        info={
            "label": "Parent Scenario",
            "description": (
                "The migration scenario "
                "this option belongs to."
            ),
        },
    )
    name: Mapped[str] = mapped_column(
        VARCHAR(CHAR_LIMIT_LONG),
        info={
            "label": "Option Name",
            "description": (
                "Label for this option "
                "(e.g., 'z17 Upgrade', "
                "'Dell + NVIDIA Cluster')."
            ),
        },
    )
    description: Mapped[str | None] = mapped_column(
        TEXT,
        nullable=True,
        info={
            "label": "Description",
            "description": (
                "Solution architecture "
                "narrative for this option."
            ),
        },
    )
    financing_model: Mapped[
        str | None
    ] = mapped_column(
        VARCHAR(CHAR_LIMIT_SHORT),
        nullable=True,
        info={
            "label": "Financing Model",
            "description": (
                "How this option is funded. "
                "Valid values: "
                "'capex_purchase', "
                "'lease_fmv', "
                "'lease_buyout', "
                "'tailored_fit', "
                "'as_a_service'."
            ),
        },
    )

    # Circularity & residual value
    circularity_program_id: Mapped[
        int | None
    ] = mapped_column(
        ForeignKey("circularity_program.id"),
        nullable=True,
        info={
            "label": "Takeback Program",
            "description": (
                "End-of-life disposition "
                "program for this option's "
                "equipment."
            ),
        },
    )
    residual_value_estimate: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Residual Value ($)",
            "description": (
                "Estimated recovery value "
                "at end of term via the "
                "circularity program."
            ),
        },
    )

    # Catch-all for unmodeled costs
    additional_infra_cost: Mapped[
        float | None
    ] = mapped_column(
        REAL(precision=PRECISION),
        nullable=True,
        info={
            "label": "Additional Infra Cost ($)",
            "description": (
                "Costs not captured in "
                "component pricing "
                "(middleware, networking, "
                "API gateways, etc.)."
            ),
        },
    )
    notes: Mapped[str | None] = mapped_column(
        TEXT,
        nullable=True,
        info={
            "label": "Notes",
            "description": (
                "Any additional context "
                "relevant to this option."
            ),
        },
    )

    # Relationships
    scenario: Mapped[
        "MigrationScenario"
    ] = relationship(
        back_populates="options",
    )
    circularity_program: Mapped[
        "CircularityProgram" | None
    ] = relationship()
    components: Mapped[
        List["Component"]
    ] = relationship(
        secondary=scenario_option_component,
    )
```

---

## Part 3: Validation

After all changes are applied, verify:

1. `python -c "from models import *"` runs without errors.
2. All new columns have `info={}` dicts with `label` and `description`.
3. `circularity_score` no longer exists on `Component`.
4. The polymorphic inheritance chain (`Component` → `Mainframe`, `RackServer`, `GPU`) still works.
5. Both association tables (`component_program_association`, `scenario_option_component`) are correctly defined.
6. `MigrationScenario.source_component` relationship resolves correctly.
7. `ScenarioOption.components` relationship through `scenario_option_component` resolves correctly.
8. `ScenarioOption.circularity_program` relationship resolves correctly.

---

## Part 4: Generate `POST_UPDATE.md`

After the schema changes pass validation, create a `POST_UPDATE.md` file in the same directory as `models.py`. This file documents the final state of the schema for the team. It should contain:

### Section 1: Changelog

A table listing every change made, organized by table. Format:

| Table | Change Type | Column / Entity | Description |
|---|---|---|---|
| `component` | Added | `product_family` | Groups hardware generations for filtering |
| ... | ... | ... | ... |

Include additions, removals, and new tables.

### Section 2: Complete Schema Reference

For every table in the final schema, list all columns with their type, nullability, and the `label` from the `info={}` dict. Organize by table in this order: `Company`, `CircularityProgram`, `Component`, `Mainframe`, `RackServer`, `GPU`, `MigrationScenario`, `ScenarioOption`. Include both association tables with their columns.

### Section 3: Relationship Map

A plain-text description of all relationships in the schema:
- `Company` 1:N `Component`
- `Company` 1:N `CircularityProgram`
- `Component` N:M `CircularityProgram` (via `component_program_association`)
- `Component` → `Mainframe`, `RackServer`, `GPU` (polymorphic inheritance)
- `MigrationScenario` N:1 `Component` (source system)
- `MigrationScenario` 1:N `ScenarioOption`
- `ScenarioOption` N:M `Component` (via `scenario_option_component`, with `quantity` and `role`)
- `ScenarioOption` N:1 `CircularityProgram` (optional)

### Section 4: Design Assumptions

Document these decisions so future contributors understand why the schema looks the way it does:

1. **Max configuration baseline** — All hardware comparisons use max CPs/cores at full speed with standardized memory and I/O. Exact memory/IO counts are TBD but held constant across generations within a product family.
2. **Pricing approach** — `list_price_capex` on `Component` represents the most readily available price for a max configuration. Rack servers and GPUs use vendor MSRP; mainframes use refurbished dealer pricing or public procurement records. No bottom-up component-level cost decomposition.
3. **Workload portability** — Assumed. The `MigrationScenario.assumptions` field must document this for every scenario.
4. **PCF data provenance** — `pcf_confidence` tracks data quality because emissions data availability varies significantly by vendor and generation. IBM publishes PCF reports for z16/z17 but not older generations. This field ensures the analysis transparently distinguishes vendor-published values from internal estimates.
5. **Circularity at the program level** — The former `circularity_score` (a subjective 0–1 float on `Component`) was removed. Circularity is now assessed entirely through the `CircularityProgram` table and its relationship to `ScenarioOption`, which links end-of-life disposition to specific vendor programs with documented terms.
6. **GPU table is draft** — The `GPU` subclass and its fields (`tflops_fp16`, `tflops_fp32`) are provisional. The GPU analysis is lower priority and the table may change when that workstream begins.
7. **ORM retained deliberately** — The SQLAlchemy ORM with `info={}` annotations serves as both the database definition and machine-readable documentation. The schema should be frozen after this update.
8. **Scenario modeling is solution-level** — `MigrationScenario` and `ScenarioOption` model a solution comparison (e.g., 1 mainframe vs. N rack servers + M GPUs), not individual hardware benchmarks. The `scenario_option_component` association table's `quantity` and `role` columns capture the bill of materials for each option.

### Section 5: Open Items

List these as unresolved items requiring team decisions:

| Item | Status |
|---|---|
| Memory & I/O standardization for max-config comparisons | TBD — use Redbook reference configs |
| Workload equivalence ratio (MSU → SPECint) | TBD — research Gartner / Arcati sources |
| Rack server vendor selection for mock pilot | TBD — Dell recommended as primary |
| GPU system definition (card vs. full server) | TBD — full server recommended |
| z17 data availability (LSPR, IMPP, PCF) | TBD — check immediately; fall back to z16 if unavailable |

---

## Files to Modify

- `models.py` — Apply all changes from Parts 1–2.

## Files to Create

- `POST_UPDATE.md` — Generate after validation passes, following the specification in Part 4.
