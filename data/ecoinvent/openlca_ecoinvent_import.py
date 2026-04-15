# -*- coding: utf-8 -*-
# openlca_ecoinvent_import.py
#
# PASTE THIS SCRIPT INTO OPENLCA 2.6's Python editor
#   (Tools -> Developer tools -> Python)
# and press the Run button in the editor toolbar.
#
# One-shot pipeline: imports the ecoinvent 3.11 ecoSpold02 release into
# the active openLCA database AND clears every formula that openLCA's
# parser or scope resolver cannot handle, in a single paste-and-run.
# Replaces the old four-script workflow (openlca_import.py,
# fix_formulas.py, nullify_unresolved.py, fix_parse_errors.py).
#
# This is Jython 2.7 (bundled with openLCA 2.x), not CPython 3. Do not
# run it with `uv run` / `python3`; it only works inside openLCA.
#
# -----------------------------------------------------------------
# SAFETY CHECKLIST (READ BEFORE RUNNING)
# -----------------------------------------------------------------
#   1. In openLCA's Navigation pane, double-click the target database
#      so its name goes bold. The script targets the active DB.
#   2. Back up the database first if it already has data:
#        Navigation pane -> right-click the database -> Backup
#      The backup is a .zolca file; keep it somewhere safe.
#   3. Close any editors you have open on processes in this DB so
#      the entity-manager state is clean.
#   4. Set LIMIT below to a small number (e.g. 50) for a smoke test
#      before committing to the multi-hour full import.
# -----------------------------------------------------------------
#
# What the fix phase clears (stored numerical values are NEVER touched,
# so every amount keeps its ecoinvent-provided number):
#
#   * Any formula that openLCA's own parser rejects. This is the same
#     entry point JSON-LD export hits:
#       org.openlca.util.Formula.getVariables
#         -> org.openlca.expressions.FormulaParser.parse
#     Covers commas (UnitConversion, POWER, LiveLink, Average, European
#     decimals), 2-arg IF(x;y), '%' literals, and anything else that
#     breaks the lexer.
#   * Any formula whose variable references are not in its owning
#     process's parameter scope (out-of-scope cascades from multi-output
#     allocation and broken upstream parameters).
#
#   Broken parameters are flipped to is_input_param = 1 so the stored
#   value keeps the row self-consistent and downstream formulas that
#   referenced them resolve to the stored number.

import os
from jarray import array
from java.io import File
from java.lang import Throwable
from org.openlca.io.ecospold2.input import EcoSpold2Import, ImportConfig
from org.openlca.util import Formula


# ---- EDIT THIS ----
# Absolute path of the `datasets/` folder that contains the .spold
# files. Or run `generate_import_script.py` next to this file from your
# shell to produce a version with the absolute path already filled in.
#
# macOS  example: "/Users/you/factbase/data/ecoinvent/ecoinvent 3.11_cutoff_ecoSpold02/datasets"
# Windows example: "C:/Users/you/factbase/data/ecoinvent/ecoinvent 3.11_cutoff_ecoSpold02/datasets"
DATASETS_DIR = "REPLACE_WITH_ABSOLUTE_PATH_TO_datasets_FOLDER"


# ---- PHASE FLAGS ----
# Flip any off to resume partway or re-run a single phase.
RUN_IMPORT = True       # run EcoSpold2Import over DATASETS_DIR
RUN_FIXES = True        # scan + NULL broken formulas after import
DRY_RUN_FIXES = False   # True = roll back the fix transaction (counts only)

# Smoke-test cap on .spold file count. None = import everything (~25k).
LIMIT = None


# openLCA built-in functions and constants from olca-formula. Anything
# else in a formula that isn't one of these is a variable reference
# that must be in the owning scope.
BUILTINS = set([
    "abs", "acos", "and", "asin", "atan", "avg", "ceil", "cos", "cosh",
    "cotan", "e", "exp", "false", "floor", "frac", "if", "int", "ln",
    "log", "max", "min", "not", "or", "pi", "pow", "random", "round",
    "sin", "sinh", "sqr", "sqrt", "sum", "tan", "tanh", "true", "ipow",
])


# -------------------------------------------------------------------
# Preflight
# -------------------------------------------------------------------

def preflight(db_ref):
    if db_ref is None:
        raise RuntimeError(
            "No active database. In openLCA's Navigation pane, "
            "double-click the target database so its name goes bold, "
            "then re-run.")

    name = db_ref.getName()
    loc = db_ref.getFileStorageLocation()
    loc_path = loc.getAbsolutePath() if loc is not None else "<unknown>"
    print("Active database : %s" % name)
    print("Database folder : %s" % loc_path)

    if loc is None or not loc.isDirectory():
        raise RuntimeError(
            "Database folder does not exist on disk: %s\n"
            "The `db` reference is stale. Fully quit openLCA (File -> "
            "Exit), reopen it, double-click the database in the "
            "Navigation pane, and run this script again." % loc_path)

    # Verify Derby/HikariCP can actually give us a connection before we
    # spend hours in the importer.
    conn = db_ref.createConnection()
    try:
        conn.close()
    except:
        pass
    print("Connection check: OK")


# -------------------------------------------------------------------
# Import phase
# -------------------------------------------------------------------

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


def run_import(db_ref):
    files = collect_spold_files(DATASETS_DIR)
    print("Found %d .spold files under %s" % (len(files), DATASETS_DIR))
    if not files:
        return

    file_array = array(files, File)

    conf = ImportConfig(db_ref)
    # Leave defaults. Public fields (skipNullExchanges, withParameters,
    # withParameterFormulas, checkFormulas) can be toggled here if
    # needed.

    imp = EcoSpold2Import(conf)
    imp.setFiles(file_array)

    print("Starting EcoSpold2 import. This will take a while.")
    print("Pass 1/2: reference data (flows, units, locations, categories).")
    print("Pass 2/2: processes + exchanges.")
    imp.run()
    print("Import finished.")


# -------------------------------------------------------------------
# Fix phase
# -------------------------------------------------------------------

def build_scope(conn):
    """Build the parameter-name scope map from tbl_parameters.name.
    Returns process_scope: {f_owner -> set(lowercase names)} with
    global parameters already unioned in, so scope lookup is a single
    dict lookup."""
    process_scope = {}
    global_scope = set()
    st = conn.createStatement()
    st.setFetchSize(5000)
    rs = st.executeQuery(
        "SELECT f_owner, name FROM tbl_parameters WHERE name IS NOT NULL")
    try:
        while rs.next():
            owner = rs.getLong(1)
            owner_null = rs.wasNull()
            name = rs.getString(2)
            if name is None:
                continue
            lc = name.lower()
            if owner_null:
                global_scope.add(lc)
            else:
                s = process_scope.get(owner)
                if s is None:
                    s = set()
                    process_scope[owner] = s
                s.add(lc)
    finally:
        rs.close()
        st.close()

    # Precompute union with global_scope so the scan loop does a
    # single difference instead of re-computing the union per row.
    if global_scope:
        for owner in process_scope:
            process_scope[owner] |= global_scope
    return process_scope, global_scope


def make_parser_check():
    """Return a closure (ok, refs) = check(formula) that caches parser
    results by formula string. ecoinvent has heavy duplication
    (UnitConversion('MJ','kWh')*1000 appears in dozens of processes),
    so caching saves ~80% of Formula.getVariables calls."""
    cache = {}

    def check(formula):
        hit = cache.get(formula)
        if hit is not None:
            return hit
        try:
            java_vars = Formula.getVariables(formula)
        except Throwable:
            result = (False, None)
            cache[formula] = result
            return result
        refs = set()
        if java_vars is not None:
            # Jython iterates java.util.Set directly as a Python iterable.
            for v in java_vars:
                if v is None:
                    continue
                lc = v.lower()
                if lc in BUILTINS:
                    continue
                refs.add(lc)
        result = (True, refs)
        cache[formula] = result
        return result

    return check


def scan_column(conn, sel_sql, label, process_scope, global_scope, parser_check):
    """Single-pass scan over a formula column. Every row is checked
    with Formula.getVariables (cached) and then against the owning
    scope. Returns ids to NULL (union of parser-broken + scope-broken).
    Parser/scope counts are printed for sanity."""
    sel = conn.createStatement()
    sel.setFetchSize(5000)
    rs = sel.executeQuery(sel_sql)
    broken_parse = []
    broken_scope = []
    scanned = 0
    try:
        while rs.next():
            scanned += 1
            rid = rs.getLong(1)
            owner = rs.getLong(2)
            owner_null = rs.wasNull()
            formula = rs.getString(3)
            if formula is None:
                continue
            ok, refs = parser_check(formula)
            if not ok:
                broken_parse.append(rid)
                continue
            if not refs:
                continue
            if owner_null:
                scope = global_scope
            else:
                scope = process_scope.get(owner)
                if scope is None:
                    scope = global_scope
            if refs - scope:
                broken_scope.append(rid)
    finally:
        rs.close()
        sel.close()
    print("%-40s: scanned %d, parser-broken %d, scope-broken %d"
          % (label, scanned, len(broken_parse), len(broken_scope)))
    return broken_parse + broken_scope


def batched_update(conn, sql, ids, label):
    if not ids:
        return 0
    upd = conn.prepareStatement(sql)
    in_batch = 0
    total = 0
    try:
        for rid in ids:
            upd.setLong(1, rid)
            upd.addBatch()
            in_batch += 1
            if in_batch >= 2000:
                total += len(upd.executeBatch())
                in_batch = 0
        if in_batch > 0:
            total += len(upd.executeBatch())
    finally:
        upd.close()
    print("  updated %d rows [%s]" % (total, label))
    return total


def run_fixes(db_ref):
    print("")
    print("---- fix phase ----")
    print("DRY_RUN_FIXES: %s" % DRY_RUN_FIXES)
    print("")

    conn = db_ref.createConnection()
    old_auto = conn.getAutoCommit()
    conn.setAutoCommit(False)

    try:
        print("Building parameter scope...")
        process_scope, global_scope = build_scope(conn)
        total_entries = sum(len(s) for s in process_scope.values())
        print("  processes with parameters: %d" % len(process_scope))
        print("  total parameter entries  : %d" % total_entries)
        print("  global parameters        : %d" % len(global_scope))
        print("")

        parser_check = make_parser_check()

        print("Scanning formulas (parser + scope)...")
        p_ids = scan_column(
            conn,
            "SELECT id, f_owner, formula FROM tbl_parameters "
            "WHERE formula IS NOT NULL",
            "tbl_parameters.formula",
            process_scope, global_scope, parser_check)
        a_ids = scan_column(
            conn,
            "SELECT id, f_owner, resulting_amount_formula FROM tbl_exchanges "
            "WHERE resulting_amount_formula IS NOT NULL",
            "tbl_exchanges.resulting_amount_formula",
            process_scope, global_scope, parser_check)
        c_ids = scan_column(
            conn,
            "SELECT id, f_owner, cost_formula FROM tbl_exchanges "
            "WHERE cost_formula IS NOT NULL",
            "tbl_exchanges.cost_formula",
            process_scope, global_scope, parser_check)

        total = len(p_ids) + len(a_ids) + len(c_ids)
        print("")
        print("Total formulas to clear: %d" % total)
        print("")

        if DRY_RUN_FIXES:
            conn.rollback()
            print("DRY RUN -- nothing committed.")
            print("If these counts look right, set DRY_RUN_FIXES = False")
            print("at the top of this script and run it again.")
            return

        batched_update(
            conn,
            "UPDATE tbl_parameters "
            "SET formula = NULL, is_input_param = 1 "
            "WHERE id = ?",
            p_ids,
            "tbl_parameters formula=NULL, is_input_param=1")

        batched_update(
            conn,
            "UPDATE tbl_exchanges "
            "SET resulting_amount_formula = NULL WHERE id = ?",
            a_ids,
            "tbl_exchanges.resulting_amount_formula=NULL")

        batched_update(
            conn,
            "UPDATE tbl_exchanges "
            "SET cost_formula = NULL WHERE id = ?",
            c_ids,
            "tbl_exchanges.cost_formula=NULL")

        conn.commit()
        print("")
        print("COMMITTED.")
        print("  parameter formulas cleared       : %d" % len(p_ids))
        print("  exchange amount formulas cleared : %d" % len(a_ids))
        print("  exchange cost formulas cleared   : %d" % len(c_ids))
        print("")
        print("Numerical amounts (parameter.value, exchange.")
        print("resulting_amount_value, exchange.cost_value) were NOT")
        print("modified.")
    except Throwable as ex:
        conn.rollback()
        print("ERROR -- rolled back. %s" % str(ex))
        raise
    finally:
        try:
            conn.setAutoCommit(old_auto)
        except:
            pass
        try:
            conn.close()
        except:
            pass

    # Flush the JPA L2 cache so subsequent validation/export in the
    # same openLCA session sees the fix. This is usually sufficient,
    # but a full close/reopen is the 100%-clean path for GUI
    # validation because editor-local L1 caches remain.
    try:
        db_ref.getEntityFactory().getCache().evictAll()
        print("Entity cache evicted.")
    except Throwable:
        print("Could not evict entity cache -- close and reopen the "
              "database manually before validating.")


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------

def main():
    preflight(db)

    if RUN_IMPORT:
        run_import(db)
    else:
        print("RUN_IMPORT = False -- skipping import phase.")

    if RUN_FIXES:
        run_fixes(db)
    else:
        print("RUN_FIXES = False -- skipping fix phase.")

    print("")
    print("Done. Next steps:")
    print("  1. Close the database (right-click -> Close) and re-open")
    print("     it so the entity cache fully refreshes.")
    print("  2. Right-click database -> Validate. Formula errors should")
    print("     be gone. Remaining warnings about elementary flows used")
    print("     as both input and output are ecoinvent modeling choices,")
    print("     not formula bugs.")
    print("  3. File -> Export -> JSON-LD should now succeed.")


main()
