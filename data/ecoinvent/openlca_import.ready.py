# -*- coding: utf-8 -*-
# openlca_import.py
#
# PASTE THIS SCRIPT INTO OPENLCA 2.6's Python editor
#   (Tools -> Developer tools -> Python)
# and press the Run button in the editor toolbar.
#
# Before running, edit DATASETS_DIR below to the absolute path of the
# `datasets` folder inside your extracted ecoinvent ecoSpold02 release.
# Or run `generate_import_script.py` next to this file to produce a
# version with the absolute path already filled in.
#
# This is Jython 2.7 (bundled with openLCA 2.x), not CPython 3.
# Do not run it with `uv run` / `python3`; it only works inside openLCA.

import os
from jarray import array
from java.io import File
from org.openlca.io.ecospold2.input import EcoSpold2Import, ImportConfig

# ---- EDIT THIS ----
# Absolute path of the `datasets/` folder that contains the .spold files.
# macOS  example: "/Users/you/factbase/data/ecoinvent/ecoinvent 3.11_cutoff_ecoSpold02/datasets"
# Windows example: "C:/Users/you/factbase/data/ecoinvent/ecoinvent 3.11_cutoff_ecoSpold02/datasets"
DATASETS_DIR = "/Users/dbchristenson/Desktop/python/kyndryl-factbase/data/ecoinvent/ecoinvent 3.11_cutoff_ecoSpold02/datasets"

# Optional: stop after this many .spold files for a smoke test.
# Set to None to import everything. Try 50 first if you want to dry-run.
LIMIT = None


def collect_spold_files(folder):
    if not os.path.isdir(folder):
        raise RuntimeError("DATASETS_DIR does not exist: " + folder)
    names = sorted(os.listdir(folder))
    out = []
    for name in names:
        if name.lower().endswith(".spold"):
            out.append(File(os.path.join(folder, name)))
            if LIMIT is not None and len(out) >= LIMIT:
                break
    return out


def preflight(db_ref):
    # `db` is pre-bound by openLCA's Jython host to the currently active database.
    if db_ref is None:
        raise RuntimeError(
            "No active database. In openLCA's Navigation pane, double-click "
            "the target database so its name goes bold, then re-run.")

    name = db_ref.getName()
    loc = db_ref.getFileStorageLocation()
    loc_path = loc.getAbsolutePath() if loc is not None else "<unknown>"
    print("Active database : %s" % name)
    print("Database folder : %s" % loc_path)

    if loc is None or not loc.isDirectory():
        raise RuntimeError(
            "Database folder does not exist on disk: %s\n"
            "The `db` reference is stale. Fully quit openLCA (File -> Exit), "
            "reopen it, double-click the database in the Navigation pane, "
            "and run this script again." % loc_path)

    # Verify Derby/HikariCP can actually give us a connection before we
    # spend hours in the importer.
    conn = db_ref.createConnection()
    try:
        conn.close()
    except:
        pass
    print("Connection check: OK")


def main():
    preflight(db)

    files = collect_spold_files(DATASETS_DIR)
    print("Found %d .spold files under %s" % (len(files), DATASETS_DIR))
    if not files:
        return

    file_array = array(files, File)

    conf = ImportConfig(db)
    # Leave defaults unless you have a reason to override. The public fields
    # (skipNullExchanges, withParameters, withParameterFormulas, checkFormulas)
    # can be toggled here if needed.

    imp = EcoSpold2Import(conf)
    imp.setFiles(file_array)

    print("Starting EcoSpold2 import. This will take a while.")
    print("Pass 1/2: reference data (flows, units, locations, categories).")
    print("Pass 2/2: processes + exchanges.")
    imp.run()
    print("Import finished. Close and reopen the database to see everything.")


main()
