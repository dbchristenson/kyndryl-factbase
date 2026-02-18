import models
import pandas as pd
from sqlalchemy.inspection import inspect

# --- CONFIGURATION: Friendly Names & Tooltips ---
# This dictionary maps your database column names to "Stakeholder Friendly" headers
# and provides a tooltip/description for the Data Dictionary tab.
FIELD_META = {
    "name": ("Product Name", "The specific model name (e.g., z16, H100)."),
    "company_id": ("Vendor", "The manufacturer providing the component."),
    "release_year": (
        "Release Year",
        "Used to calculate vintage and efficiency gains.",
    ),
    "pcf_value": (
        "Reported Emissions (kgCO2e)",
        "The raw carbon footprint number provided by the vendor.",
    ),
    "pcf_boundary": (
        "Emissions Scope",
        "Crucial: Does the reported number include use-phase? (Cradle-to-Gate vs. Cradle-to-Grave).",
    ),
    "pcf_assumptions": (
        "Emissions Assumptions",
        "If Cradle-to-Grave, what grid/usage did they assume?",
    ),
    "power_draw_watts_tdp": (
        "Max Power (Watts)",
        "Thermal Design Power. Used to calculate worst-case Scope 2 emissions.",
    ),
    "list_price_capex": (
        "List Price (CAPEX)",
        "Upfront purchase cost (MSRP).",
    ),
    "monthly_lease_opex": (
        "Monthly Lease (OPEX)",
        "Cost per month if leased (As-a-Service model).",
    ),
    "circularity_score": (
        "Circularity Score (0-1)",
        "Internal metric: 1.0 = Fully Recyclable/Circular.",
    ),
    "mips_rating": (
        "MIPS (Performance)",
        "Millions of Instructions Per Second (Mainframe specific).",
    ),
    "vram_gb": (
        "VRAM (GB)",
        "Video Memory size (Critical for AI model weights).",
    ),
    "interconnect_type": (
        "Interconnect",
        "Speed of connection between chips (e.g., NVLink).",
    ),
}


def get_columns_for_model(model_class):
    """Inspects a SQLAlchemy model and returns a list of column names."""
    return [c.key for c in inspect(model_class).attrs if hasattr(c, "key")]


def generate_excel_template():
    output_file = "Kyndryl_Hardware_Data_Collection.xlsx"

    # 1. Prepare Dataframes for the "Entry Sheets"
    # We create empty dataframes with columns derived from your schema

    # Generic Component Columns
    base_cols = get_columns_for_model(models.Component)

    # Specific Columns (filtering out duplicates that exist in base)
    mainframe_cols = [
        c
        for c in get_columns_for_model(models.Mainframe)
        if c not in base_cols
    ]
    rack_cols = [
        c
        for c in get_columns_for_model(models.RackServer)
        if c not in base_cols
    ]
    gpu_cols = [
        c for c in get_columns_for_model(models.GPU) if c not in base_cols
    ]

    # Combine for the specific tabs
    df_mainframe = pd.DataFrame(columns=base_cols + mainframe_cols)
    df_rack = pd.DataFrame(columns=base_cols + rack_cols)
    df_gpu = pd.DataFrame(columns=base_cols + gpu_cols)
    df_programs = pd.DataFrame(
        columns=get_columns_for_model(models.CircularityProgram)
    )

    # 2. Rename Columns using our Friendly Mapping
    def rename_cols(df):
        new_names = {k: v[0] for k, v in FIELD_META.items() if k in df.columns}
        return df.rename(columns=new_names)

    df_mainframe = rename_cols(df_mainframe)
    df_rack = rename_cols(df_rack)
    df_gpu = rename_cols(df_gpu)
    df_programs = rename_cols(df_programs)

    # 3. Create the "Data Dictionary" Dataframe
    # This explains to stakeholders *why* we are asking for this data.
    dict_data = []
    for col, (friendly_name, description) in FIELD_META.items():
        dict_data.append(
            {
                "Field Name": friendly_name,
                "Description": description,
                "DB Column": col,
            }
        )
    df_dictionary = pd.DataFrame(dict_data)

    # 4. Write to Excel with formatting
    try:
        with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:

            # --- Tab 0: Data Dictionary ---
            df_dictionary.to_excel(
                writer, sheet_name="READ ME - Definitions", index=False
            )
            worksheet = writer.sheets["READ ME - Definitions"]
            worksheet.set_column("A:A", 25)  # Width for Field Name
            worksheet.set_column("B:B", 60)  # Width for Description

            # Add a title format
            header_fmt = writer.book.add_format(
                {"bold": True, "bg_color": "#DCE6F1", "border": 1}
            )
            for col_num, value in enumerate(df_dictionary.columns.values):
                worksheet.write(0, col_num, value, header_fmt)

            # --- Tab 1: Mainframes ---
            sheet_name = "Mainframes"
            df_mainframe.to_excel(writer, sheet_name=sheet_name, index=False)
            format_sheet(writer, df_mainframe, sheet_name, header_fmt)

            # --- Tab 2: Rack Servers ---
            sheet_name = "Rack Servers"
            df_rack.to_excel(writer, sheet_name=sheet_name, index=False)
            format_sheet(writer, df_rack, sheet_name, header_fmt)

            # --- Tab 3: GPUs (AI Workloads) ---
            sheet_name = "GPUs (AI)"
            df_gpu.to_excel(writer, sheet_name=sheet_name, index=False)
            format_sheet(writer, df_gpu, sheet_name, header_fmt)

            # --- Tab 4: Circularity Programs ---
            sheet_name = "Vendor Programs"
            df_programs.to_excel(writer, sheet_name=sheet_name, index=False)
            format_sheet(writer, df_programs, sheet_name, header_fmt)

        print(f"Success! '{output_file}' has been generated.")
        print(
            "You can send this file to vendors or use it to present the schema to stakeholders."
        )

    except Exception as e:
        print(f"Error generating Excel: {e}")


def format_sheet(writer, df, sheet_name, header_fmt):
    """Helper function to format the data entry sheets nicely."""
    worksheet = writer.sheets[sheet_name]

    # Set generous column width
    worksheet.set_column("A:Z", 20)

    # Write the header with the custom format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_fmt)

        # Highlight "Emissions Scope" column in yellow to draw attention (it's critical)
        if "Emissions Scope" in str(value):
            yellow_fmt = writer.book.add_format(
                {"bg_color": "#FFFF00", "bold": True, "border": 1}
            )
            worksheet.write(0, col_num, value, yellow_fmt)


if __name__ == "__main__":
    generate_excel_template()
