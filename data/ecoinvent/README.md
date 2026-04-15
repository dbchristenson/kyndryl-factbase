# Importing ecoinvent 3.11 ecoSpold02 into openLCA 2.6

Step-by-step guide for loading the raw ecoinvent 3.11 cutoff ecoSpold02
release into openLCA 2.6 without access to the Nexus `.zolca` bundle,
with all formula fixes applied in a single paste-and-run pass.

Verified on openLCA 2.6.1 (released 2025-12-12) and ecoinvent 3.11 cutoff ecoSpold02.
Works identically on macOS and Windows.

---

## The short version

openLCA 2.6 does **not** expose EcoSpold 2 import in its `File -> Import`
menu, but the underlying Java import code still ships with the
application. We reach it through openLCA's built-in Jython editor
(`Tools -> Developer tools -> Python`) and call
`org.openlca.io.ecospold2.input.EcoSpold2Import` directly, pointing it
at the `datasets/` folder of the extracted release. The same script
then sweeps the imported database for formulas openLCA's parser or
scope resolver cannot handle and clears them, so the result is
immediately usable for validation and JSON-LD export.

You do **not** need the `MasterData/` folder or `MasterData.zip`. The
.spold files inline every flow name, unit, classification and location,
and the importer derives reference data by iterating the .spold files
themselves (see `RefDataImport.java` in olca-modules).

---

## Why the file menu doesn't work

In `olca-app/plugin.xml` on the current `master` branch, the EcoSpold 2
import wizard registration is commented out:

```xml
<!--
<wizard
    category="import.category.otherLCA"
    class="org.openlca.app.wizards.io.EcoSpold2ImportWizard"
    ...
    name="EcoSpold 2">
</wizard>
-->
```

So `File -> Import -> Other` shows EcoSpold 1, ILCD, SimaPro CSV, Excel,
JSON, zolca, HSC Sim, and GeoJSON — but no EcoSpold 2. The wizard
**class** is still there (`EcoSpold2ImportWizard.java`), and the core
Java API (`org.openlca.io.ecospold2.input.EcoSpold2Import`) is still
maintained in `olca-modules/olca-io` (last commit 2026-04-07). It's just
hidden from the GUI.

The Jython path is the supported way to reach it: openLCA bundles
`jython-standalone-2.7.4.jar`, the Python editor pre-binds `db` to the
active database, and its host pre-imports every public class from
`olca-modules` so Java classes are callable from the script as if they
were Python classes.

---

## Why the fix phase is needed

ecoinvent ships formulas that openLCA's own `olca-formula` parser
rejects and the JSON-LD exporter refuses to serialize. Five broken
classes observed in the 3.11 cutoff release:

1. **Commas**: `UnitConversion(a,b,c)`, `POWER(a,b)`, `LiveLink(...)`,
   `Average(...)`, European decimals like `1,23e-6`. openLCA uses `;`
   as the function argument separator.
2. **2-arg `IF(x;y)`**: ecoinvent's co-product allocation idiom.
   openLCA's `If.java` requires 3 args (condition; then; else).
3. **Unknown function names** (`power`, `livelink`, `average`) — these
   resolve as variable references, fail the scope check, and get
   cleared along with class 1.
4. **Scope-bind failures**: variables missing from the process's
   parameter scope. Most common cause is ecoinvent's multi-output
   allocation: one parent process explodes into N sibling processes
   and the importer binds parameters to some siblings but all N
   inherit the exchange formulas referencing those parameters.
5. **`%` literals**: `12900*10^6*75%`, `0.0016503*1.5%`. openLCA's
   lexer emits `TokenMgrError: Encountered "%"`.

The fix phase clears every formula `org.openlca.util.Formula.getVariables`
rejects (that's the same parser path JSON-LD export uses) and every
formula referencing out-of-scope variables. **Stored numerical values
are never touched** — every amount keeps its ecoinvent-provided number.
Parameters with broken formulas are flipped to `is_input_param = 1` so
the stored value makes the row self-consistent and downstream formulas
that referenced them resolve cleanly.

---

## Prerequisites

- **openLCA 2.6** or newer, installed from <https://openlca.org/download/>.
- **ecoinvent 3.11 ecoSpold02** extracted on disk. After extraction you
  should have a folder like:
  ```
  ecoinvent 3.11_cutoff_ecoSpold02/
    datasets/              <- 25412 *.spold files
    MasterData/            <- unused by this guide
    MasterData.zip         <- unused by this guide
    FilenameToActivityLookup.csv
  ```
- ~**10 GB free disk** for the resulting openLCA database.
- A few hours of wall-clock time for the import to finish. The full
  release is around 3.8 GB and 25k processes; expect the import to
  take hours on a typical laptop. The fix phase afterwards is fast
  (seconds to low minutes) thanks to parser-result caching.

---

## Step 1 — Install openLCA and create an empty database

1. Install openLCA 2.6 and launch it.
2. In the `Navigation` pane on the left, right-click and choose
   `New database`.
3. Name it something like `ecoinvent_311_cutoff`.
4. Pick `Empty database` (no reference data). Click `Finish`.
5. openLCA opens the new database and marks it as the active one.
   Confirm it is bold in the Navigation pane — the Jython script
   targets whichever database is currently active.

## Step 2 — Generate the ready-to-paste script

From the project root, run:

```bash
uv run python data/ecoinvent/generate_import_script.py
```

This reads `data/ecoinvent/openlca_ecoinvent_import.py` (the Jython
template), finds `data/ecoinvent/ecoinvent 3.11_cutoff_ecoSpold02/datasets`
on your disk, counts the .spold files, and writes a ready-to-paste
version to:

```
data/ecoinvent/openlca_ecoinvent_import.ready.py
```

If your release folder lives elsewhere, pass `--root` explicitly:

```bash
uv run python data/ecoinvent/generate_import_script.py \
  --root "/path/to/ecoinvent 3.11_cutoff_ecoSpold02"
```

The helper uses forward slashes for the embedded path, which
`java.io.File` accepts on both macOS and Windows, so the same generated
script works on either OS.

**Prefer not to run the helper?** Open `openlca_ecoinvent_import.py`
directly and replace `REPLACE_WITH_ABSOLUTE_PATH_TO_datasets_FOLDER`
with the absolute path of your `datasets/` folder.

## Step 3 — Paste and run

1. In openLCA: `Tools -> Developer tools -> Python`. A new tab opens
   titled `Python` with an empty editor and a green Run button in the
   toolbar.
2. Open `data/ecoinvent/openlca_ecoinvent_import.ready.py` in any text
   editor and copy its entire contents.
3. Paste into openLCA's Python editor.
4. Click the green Run button.

The script prints progress to the openLCA Console (which pops up
automatically when the script runs):

- `Active database : ...` / `Connection check: OK`
- `Found 25412 .spold files ...`
- `Starting EcoSpold2 import. This will take a while.`
- `Pass 1/2: reference data ...` / `Pass 2/2: processes + exchanges.`
- (multi-hour import runs, log lines from the importer itself)
- `Import finished.`
- `Building parameter scope...` with counts
- `Scanning formulas (parser + scope)...` with per-column
  `scanned N, parser-broken P, scope-broken S` lines
- `Total formulas to clear: ...`
- `COMMITTED.` + per-column cleared counts
- `Entity cache evicted.`
- `Done. Next steps: ...`

Leave openLCA alone while the import runs. The UI may be unresponsive
at times; that is normal — it's all on the JVM UI thread. The fix
phase afterwards is much faster.

## Step 4 — Verify

When the script finishes:

1. Close the database (right-click -> Close) and reopen it to flush
   any editor-local caches. The script's `evictAll()` call clears the
   JPA L2 cache, but a reopen is the 100%-clean path for GUI
   validation.
2. Right-click the database -> **Validate**. Formula errors should be
   gone. Remaining warnings about elementary flows used as both input
   and output (waste heat, landfill carbon) are ecoinvent modeling
   choices, not formula bugs.
3. Spot-check: open a process like `tin production | tin | cutoff, U`
   and confirm it has a reference product, inputs/outputs, and
   elementary flows. Processes that historically had broken formulas
   — e.g. `rare earth oxides production | terbium oxide` or anything
   under `sugarcane production` — should now open cleanly with
   amounts intact.
4. `File -> Export -> JSON-LD` (include Processes) should succeed.

---

## Dry run first (recommended)

Before committing to a multi-hour import, try a small subset. Edit the
generated `openlca_ecoinvent_import.ready.py` and set:

```python
LIMIT = 50
```

Run it against an empty database. You'll get ~50 processes plus
whatever reference data they touch, in about a minute, followed by a
fast fix pass. If that looks right, delete the database, create a
fresh empty one, set `LIMIT = None`, and run the full import.

You can also flip `DRY_RUN_FIXES = True` to get counts-only fix output
(the fix transaction rolls back). Useful for iterating on the fix
logic against an already-imported database.

---

## Partial re-runs

Three top-level flags in the script let you skip phases:

```python
RUN_IMPORT = True       # run EcoSpold2Import
RUN_FIXES = True        # build scope + scan + NULL broken formulas
DRY_RUN_FIXES = False   # True = rollback the fix transaction
```

Common modes:

- **`RUN_IMPORT=True, RUN_FIXES=True`** — the default end-to-end run.
- **`RUN_IMPORT=False, RUN_FIXES=True`** — re-run the fix pass against
  an already-imported database, e.g. after restoring a backup.
- **`RUN_IMPORT=True, RUN_FIXES=False`** — import only, skip the fix
  pass (useful if you want to poke at the raw state in validation
  first).

---

## Troubleshooting

**`No active database. ...`**
You ran the script with no database selected. Open the target database
in the Navigation pane so it becomes the active (bold) one, then run
again.

**`DATASETS_DIR does not exist: ...`**
The path in the script doesn't match your disk. Re-run
`generate_import_script.py`, or hand-edit the `DATASETS_DIR` line.

**`OutOfMemoryError: Java heap space`**
openLCA ships with a default heap cap. For 25k processes bump it by
editing `openLCA.ini` (next to the openLCA executable):

- macOS: right-click `openLCA.app` -> `Show Package Contents` -> `Contents/Eclipse/openLCA.ini`
- Windows: in the install folder, `openLCA.ini`

Find the `-Xmx` line and raise it to something like `-Xmx8g`. Restart
openLCA and run the import again against a fresh empty database.

**The import stopped partway through.**
`EcoSpold2Import` has no resume — partial imports leave a dirty
database. Delete the database, create a new empty one, and run again.

**The fix phase threw an error.**
The fix phase runs inside a single JDBC transaction with
`autoCommit=False`, so any error rolls back automatically and the
database state is unchanged. Fix the cause and re-run with
`RUN_IMPORT=False, RUN_FIXES=True` to retry the fix pass only.

**`ImportConfig` looks wrong / imports the ILCD one.**
openLCA's auto-generated Jython bindings expose every class under its
short name, and `ImportConfig` is ambiguous. The script avoids this by
importing the fully-qualified class:

```python
from org.openlca.io.ecospold2.input import EcoSpold2Import, ImportConfig
```

Don't replace that with `from org.openlca.io.ecospold2.input import *`.

---

## Files in this folder

- `README.md` — this guide.
- `openlca_ecoinvent_import.py` — the Jython template (Jython 2.7, for
  openLCA only — not runnable with `uv` / CPython). Contains the
  import phase, the parser + scope fix phase, and the entity cache
  eviction, all in one paste-and-run script.
- `generate_import_script.py` — CPython 3, run with `uv run`. Resolves
  the absolute path to `datasets/` and writes
  `openlca_ecoinvent_import.ready.py` next to itself.
- `openlca_ecoinvent_import.ready.py` — generated by the helper,
  ignored by git if you add it. This is what you copy into openLCA.

The ecoinvent release files themselves (`ecoinvent 3.11_cutoff_ecoSpold02/`
and `MasterData.zip`) are not committed — `.gitignore` already excludes
`*.spold`, `*.xml`, `*.zip`, `*.csv`.

---

## Sources

Everything above is grounded in these primary sources. If any of this
drifts in a future openLCA release, re-check:

- openLCA 2 manual, supported import formats — <https://greendelta.github.io/openLCA2-manual/databases/importing_and_combining_databases.html>
- openLCA Jython manual (confirms Jython 2.7 bundling and Java-API access) — <https://greendelta.github.io/openLCAJython-manual/>
- `olca-modules/olca-io` README (EcoSpold2Import API) — <https://github.com/GreenDelta/olca-modules/tree/master/olca-io>
- `EcoSpold2Import.java` — <https://github.com/GreenDelta/olca-modules/blob/master/olca-io/src/main/java/org/openlca/io/ecospold2/input/EcoSpold2Import.java>
- `RefDataImport.java` (confirms MasterData/ is not read) — <https://github.com/GreenDelta/olca-modules/blob/master/olca-io/src/main/java/org/openlca/io/ecospold2/input/RefDataImport.java>
- `EcoSpold2ImportWizard.java` (still in the source tree) — <https://github.com/GreenDelta/olca-app/blob/master/olca-app/src/org/openlca/app/wizards/io/EcoSpold2ImportWizard.java>
- `olca-app/plugin.xml` (wizard registration is commented out) — <https://github.com/GreenDelta/olca-app/blob/master/olca-app/plugin.xml>
- `Jython.java` and `app_bindings.py` (confirms `db` pre-binding and auto-generated olca-modules imports) — <https://github.com/GreenDelta/olca-app/tree/master/olca-app/src/org/openlca/app/devtools/python>
- `RcpActionBarAdvisor.java` (Tools -> Developer tools -> Python menu wiring) — <https://github.com/GreenDelta/olca-app/blob/master/olca-app/src/org/openlca/app/rcp/RcpActionBarAdvisor.java>
- `olca-formula` function/grammar sources (BUILTINS set + IF arity + tokenizer rules) — <https://github.com/GreenDelta/olca-modules/tree/master/olca-formula>
- `Formula.java` (the parser entry point the fix phase uses) — <https://github.com/GreenDelta/olca-modules/blob/master/olca-core/src/main/java/org/openlca/util/Formula.java>
- GreenDelta's official position ("we do not support the EcoSpold2 format any more ... essentially removed it from openLCA") — <https://ask.openlca.org/5602/how-to-import-datasets-in-ecospold2-format-onto-openlca> and <https://ask.openlca.org/7718/how-to-use-ecospold2-to-openlca2-1>
- Community confirmation that the Jython path is the workaround — <https://ask.openlca.org/2581/how-to-import-ecospold-file-from-external-python-script>
- Jython example from GreenDelta's own tutorial repo (uses the same `db` global and Java API pattern) — <https://github.com/GreenDelta/openlca-python-examples/blob/main/Jython/ecoinvent_38_to_39_migration.py>
- Jython `jarray.array` reference for creating `File[]` — <https://www.jython.org/jython-old-sites/archive/21/docs/jarray.html>
- ecoinvent's own data-formats page (confirms only GreenDelta is tooled to integrate the database into openLCA) — <https://support.ecoinvent.org/data-formats>
