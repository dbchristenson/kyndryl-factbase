"""
Generates a stakeholder-friendly Excel workbook from
the SQLAlchemy schema.

Column labels and descriptions are read directly from
the `info` dict on each mapped_column in models.py, so
the workbook stays in sync with the schema automatically
- no separate mapping to maintain.
"""

import models
from sqlalchemy import inspect as sa_inspect

# Columns to exclude from data-entry sheets
_SKIP_COLUMNS = {"id", "type", "component_id", "program_id"}

OUTPUT_FILE = "Kyndryl_Hardware_Data_Collection.xlsx"


def get_entry_columns(model_class):
    """Return column info for user-facing columns.

    Returns [(db_name, label, description), ...].

    Reads ``info["label"]`` and ``info["description"]``
    from each ``mapped_column``.  Falls back to a
    title-cased version of the column name when no
    ``info`` is set.
    """
    mapper = sa_inspect(model_class)
    columns = []
    for attr in mapper.column_attrs:
        col = attr.columns[0]
        if col.key in _SKIP_COLUMNS:
            continue
        info = col.info or {}
        label = info.get(
            "label",
            col.key.replace("_", " ").title(),
        )
        description = info.get("description", "")
        columns.append((col.key, label, description))
    return columns


def _merge_columns(*column_lists):
    """Merge column lists, deduplicating by db_name."""
    seen = set()
    merged = []
    for col_list in column_lists:
        for entry in col_list:
            if entry[0] not in seen:
                seen.add(entry[0])
                merged.append(entry)
    return merged


def _write_sheet(
    workbook, sheet_name, columns,
    header_fmt, highlight_fmt,
):
    """Create a worksheet and write the header row."""
    worksheet = workbook.add_worksheet(sheet_name)
    for col_num, (_, label, _desc) in enumerate(columns):
        if label == "Emissions Scope":
            fmt = highlight_fmt
        else:
            fmt = header_fmt
        worksheet.write(0, col_num, label, fmt)
        worksheet.set_column(
            col_num, col_num,
            max(20, len(label) + 4),
        )
    return worksheet


def generate_excel_template():
    import xlsxwriter

    workbook = xlsxwriter.Workbook(OUTPUT_FILE)

    # --- Formats ---
    header_fmt = workbook.add_format(
        {"bold": True, "bg_color": "#DCE6F1", "border": 1}
    )
    highlight_fmt = workbook.add_format(
        {"bold": True, "bg_color": "#FFFF00", "border": 1}
    )

    # --- Collect columns from models ---
    base_cols = get_entry_columns(models.Component)
    mainframe_cols = get_entry_columns(models.Mainframe)
    rack_cols = get_entry_columns(models.RackServer)
    gpu_cols = get_entry_columns(models.GPU)
    program_cols = get_entry_columns(
        models.CircularityProgram
    )
    source_cols = get_entry_columns(models.DataSource)

    # Merge base + subclass columns
    sheets = [
        ("Mainframes", _merge_columns(
            base_cols, mainframe_cols,
        )),
        ("Rack Servers", _merge_columns(
            base_cols, rack_cols,
        )),
        ("GPUs (AI)", _merge_columns(
            base_cols, gpu_cols,
        )),
        ("Vendor Programs", program_cols),
        ("Data Sources", source_cols),
    ]

    # --- Tab 0: Data Dictionary ---
    all_columns = _merge_columns(
        base_cols, mainframe_cols,
        rack_cols, gpu_cols, program_cols,
        source_cols,
    )
    dict_ws = workbook.add_worksheet(
        "READ ME - Definitions"
    )
    dict_headers = [
        "Field Name", "Description", "DB Column",
    ]
    for col_num, h in enumerate(dict_headers):
        dict_ws.write(0, col_num, h, header_fmt)
    for row, (_, label, desc) in enumerate(
        all_columns, start=1,
    ):
        dict_ws.write(row, 0, label)
        dict_ws.write(row, 1, desc)
        dict_ws.write(row, 2, _)
    dict_ws.set_column(0, 0, 30)
    dict_ws.set_column(1, 1, 65)
    dict_ws.set_column(2, 2, 25)

    # --- Entry sheets ---
    for sheet_name, columns in sheets:
        _write_sheet(
            workbook, sheet_name, columns,
            header_fmt, highlight_fmt,
        )

    workbook.close()
    print(
        f"Success! '{OUTPUT_FILE}' has been generated."
    )


if __name__ == "__main__":
    generate_excel_template()
