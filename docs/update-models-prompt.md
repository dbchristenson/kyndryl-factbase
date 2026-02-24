# Update `models.py` — Add Efficiency & Generational Comparison Fields

## Context

This project is a **data center circularity analysis tool** for Kyndryl. The database schema in `models.py` uses SQLAlchemy ORM with joined-table polymorphic inheritance (`Component` → `Mainframe`, `RackServer`, `GPU`). The system evaluates vendor hardware across four dimensions: **TCO, ownership structure (buy vs. lease), Scope 2/3 emissions, and circularity program value**.

We need to extend the schema so it can support **energy efficiency comparisons across hardware generations** — especially IBM mainframes (z13 → z14 → z15 → z16) — and **cross-platform efficiency comparisons** between mainframes and rack servers, normalized to work-per-kWh.

## Key Metric Background

- **Mainframes** use **MIPS** (Millions of Instructions Per Second) and **MSUs** (Million Service Units) as capacity measures. MSUs are IBM's licensing standard and are more stable for cross-generational comparison. Both are needed.
- **Rack servers** use benchmarks like **SPECint rate** or **transactions per second**. Since benchmark types vary, we need a generic score field plus a field identifying the benchmark standard used.
- **GPUs** use **TFLOPS** (Tera Floating-Point Operations Per Second) as their primary throughput metric.
- The normalized efficiency metric is **capacity per kWh** (e.g., MIPS/kWh, MSUs/kWh, TFLOPS/kWh). This requires a **typical operating power** value in addition to the existing TDP and idle fields.

## Required Changes

### 1. Add to `Component` (base class)

Add these columns to the base `Component` model. Follow the existing code style exactly — use `mapped_column()` with explicit SQLAlchemy types, include `info={}` dicts with `label` and `description` keys, and use the existing `CHAR_LIMIT_SHORT`, `CHAR_LIMIT_LONG`, `PRECISION` constants.

| Column | Type | Nullable | Purpose |
|---|---|---|---|
| `product_family` | `VARCHAR(CHAR_LIMIT_SHORT)` | `True` | Groups generations together (e.g., `"IBM z"`, `"Power E"`, `"ThinkSystem SR"`). Used for filtering/grouping generational queries. |
| `power_draw_watts_typical` | `REAL(precision=PRECISION)` | `True` | Typical operating power draw in watts. Represents realistic workload power, not worst-case TDP or best-case idle. This is the denominator for efficiency calculations. |

Place `product_family` in the "Basic Info" section after `release_year`. Place `power_draw_watts_typical` in the "Power" section between `power_draw_watts_tdp` and `power_draw_watts_idle`.

### 2. Add to `Mainframe` subclass

| Column | Type | Nullable | Purpose |
|---|---|---|---|
| `msu_rating` | `INTEGER` | `True` | Million Service Units — IBM's standard capacity/licensing metric. More stable than MIPS for cross-generational comparison. |
| `num_cps` | `INTEGER` | `True` | Number of configurable Central Processors (CPs). Required for per-core efficiency normalization. |
| `num_ifls` | `INTEGER` | `True` | Number of Integrated Facility for Linux engines. Tracks Linux-dedicated capacity separately. |

Place `msu_rating` directly after `mips_rating`. Place `num_cps` and `num_ifls` together after `msu_rating`, before `floor_space_sqft`.

### 3. Add to `RackServer` subclass

| Column | Type | Nullable | Purpose |
|---|---|---|---|
| `num_cores` | `INTEGER` | `True` | Total physical CPU cores. Needed for per-core efficiency normalization (parallel to mainframe `num_cps`). |
| `benchmark_score` | `REAL(precision=PRECISION)` | `True` | Performance score from a standardized benchmark. The throughput numerator for efficiency calculations. |
| `benchmark_type` | `VARCHAR(CHAR_LIMIT_SHORT)` | `True` | Identifies which benchmark standard was used (e.g., `"SPECint_rate2017"`, `"SPECpower_ssj2008"`, `"TPC-C"`). Required for apples-to-apples comparisons — only compare rows with matching `benchmark_type`. |

Place `num_cores` after `socket_count`. Place `benchmark_score` and `benchmark_type` together after `num_cores`.

### 4. Add to `GPU` subclass

| Column | Type | Nullable | Purpose |
|---|---|---|---|
| `tflops_fp16` | `REAL(precision=PRECISION)` | `True` | Half-precision floating-point throughput (TFLOPS). Primary AI inference performance metric. |
| `tflops_fp32` | `REAL(precision=PRECISION)` | `True` | Single-precision floating-point throughput (TFLOPS). Standard compute performance metric. |

Place both after `vram_gb`, before `interconnect_type`.

## Style Rules — Follow Exactly

- Use the **existing code conventions** already in `models.py`. Do not introduce new patterns.
- All new `mapped_column()` calls must include an `info={}` dict with `"label"` and `"description"` keys, matching the style of existing columns.
- Use parenthesized string concatenation for long description strings, exactly as existing columns do:
  ```python
  info={
      "label": "Short Label",
      "description": (
          "First part of the description "
          "continued on the next line."
      ),
  }
  ```
- Keep line length under ~55 characters inside the `mapped_column()` blocks (matching the existing formatting — this code uses aggressive wrapping for readability).
- All new numeric columns should be `nullable=True` since historical data may not have these values.
- Do **not** add any computed properties, hybrid properties, or helper methods. This is a schema-only change.
- Do **not** modify any existing columns, relationships, or the association table.
- Do **not** change any imports unless a new SQLAlchemy type is needed (it shouldn't be).
- Preserve all existing comments and docstrings.

## Validation

After making changes, verify that:

1. The file has no syntax errors (`python -c "import models"` or equivalent).
2. All new columns are properly typed and nullable.
3. The polymorphic inheritance still works (no conflicting column names across the hierarchy).
4. The `info={}` dicts are present on every new column.

## Files to Modify

- `models.py` — this is the only file that needs changes.
