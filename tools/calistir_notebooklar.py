from __future__ import annotations

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [ROOT / "bolumler" / f"b{i:02d}" / "calisma.ipynb" for i in range(1, 19)]


def main() -> int:
    failures: list[str] = []

    for path in NOTEBOOKS:
        rel = path.relative_to(ROOT)
        try:
            nb = nbformat.read(path, as_version=4)
            client = NotebookClient(
                nb,
                timeout=120,
                kernel_name="python3",
                allow_errors=False,
            )
            client.execute(cwd=str(path.parent))
            print(f"OK  {rel}")
        except Exception as exc:
            failures.append(f"{rel}: {type(exc).__name__}: {exc}")
            print(f"FAIL {rel}: {exc}", file=sys.stderr)

    print(f"\nÇalıştırılan notebook: {len(NOTEBOOKS)}")
    if failures:
        print("\nBaşarısız notebooklar:", file=sys.stderr)
        for item in failures:
            print(f"- {item}", file=sys.stderr)
        return 1

    print("Tüm notebooklar çalışma duman testinden geçti.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
