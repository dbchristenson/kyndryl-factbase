"""
generate_import_script.py

Cross-platform helper that resolves the local absolute path to the
ecoinvent 3.11 ecoSpold02 `datasets/` folder and writes a ready-to-paste
Jython script next to itself.

Usage (macOS / Linux / Windows):
    uv run python data/ecoinvent/generate_import_script.py

Or pass a custom root if your extracted folder is named differently:
    uv run python data/ecoinvent/generate_import_script.py --root "path/to/ecoinvent 3.11_cutoff_ecoSpold02"

Output:
    data/ecoinvent/openlca_import.ready.py

Copy that file's contents into openLCA's Python editor
(Tools -> Developer tools -> Python) and press Run.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_RELEASE_DIR = HERE / "ecoinvent 3.11_cutoff_ecoSpold02"
TEMPLATE_PATH = HERE / "openlca_import.py"
OUTPUT_PATH = HERE / "openlca_import.ready.py"
PLACEHOLDER = "REPLACE_WITH_ABSOLUTE_PATH_TO_datasets_FOLDER"


def find_datasets_dir(root: Path) -> Path:
    datasets = root / "datasets"
    if not datasets.is_dir():
        raise FileNotFoundError(
            f"No 'datasets' folder at {datasets}. "
            f"Point --root at the extracted ecoSpold02 release."
        )
    return datasets


def count_spold(datasets: Path) -> int:
    return sum(1 for p in datasets.iterdir() if p.suffix.lower() == ".spold")


def to_jython_literal(path: Path) -> str:
    # Forward slashes are accepted by java.io.File on both Windows and macOS,
    # so we normalize to them to keep the string simple and free of backslash
    # escaping.
    return path.as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_RELEASE_DIR,
        help="Path to the extracted ecoinvent ecoSpold02 release folder "
        "(the one that contains `datasets/` and `MasterData/`).",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: release folder not found: {root}", file=sys.stderr)
        return 1

    datasets = find_datasets_dir(root)
    n = count_spold(datasets)
    if n == 0:
        print(f"error: no .spold files found in {datasets}", file=sys.stderr)
        return 1

    if not TEMPLATE_PATH.is_file():
        print(f"error: template not found: {TEMPLATE_PATH}", file=sys.stderr)
        return 1

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if PLACEHOLDER not in template:
        print(
            f"error: template {TEMPLATE_PATH} has no {PLACEHOLDER} placeholder",
            file=sys.stderr,
        )
        return 1

    resolved = template.replace(PLACEHOLDER, to_jython_literal(datasets))
    OUTPUT_PATH.write_text(resolved, encoding="utf-8")

    print(f"ecoSpold02 release : {root}")
    print(f"datasets folder    : {datasets}")
    print(f".spold files found : {n}")
    print(f"wrote              : {OUTPUT_PATH}")
    print()
    print("Next steps:")
    print("  1. Open openLCA 2.6 and create or open the target database.")
    print("  2. Tools -> Developer tools -> Python.")
    print(f"  3. Paste the contents of {OUTPUT_PATH.name} into the editor.")
    print("  4. Click the Run button in the editor toolbar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
