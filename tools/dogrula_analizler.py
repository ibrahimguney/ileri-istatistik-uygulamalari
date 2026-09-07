from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RTOL = 1e-7
ATOL = 1e-8


def fail(message: str) -> None:
    raise AssertionError(message)


def compare(expected, actual, path="root"):
    """Beklenen JSON'u, üretilen özetin zorunlu alt-kümesi olarak doğrula."""
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            fail(f"{path}: beklenen dict, bulunan {type(actual).__name__}")
        for key, value in expected.items():
            if key not in actual:
                fail(f"{path}.{key}: alan sonuclar/ozet.json içinde yok")
            compare(value, actual[key], f"{path}.{key}")
        return

    if isinstance(expected, list):
        if not isinstance(actual, list):
            fail(f"{path}: beklenen list, bulunan {type(actual).__name__}")
        if len(expected) != len(actual):
            fail(f"{path}: liste uzunluğu {len(actual)}, beklenen {len(expected)}")
        for i, (e, a) in enumerate(zip(expected, actual)):
            compare(e, a, f"{path}[{i}]")
        return

    if isinstance(expected, bool) or expected is None:
        if actual is not expected:
            fail(f"{path}: {actual!r}, beklenen {expected!r}")
        return

    if isinstance(expected, (int, float)) and not isinstance(expected, bool):
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            fail(f"{path}: sayısal değer bekleniyordu, bulunan {actual!r}")
        if not math.isclose(float(actual), float(expected), rel_tol=RTOL, abs_tol=ATOL):
            fail(f"{path}: {actual!r}, beklenen {expected!r} (rtol={RTOL}, atol={ATOL})")
        return

    if actual != expected:
        fail(f"{path}: {actual!r}, beklenen {expected!r}")


def run_chapter(chapter: str) -> None:
    directory = ROOT / "bolumler" / chapter
    analysis = directory / "analiz.py"
    expected_file = directory / "beklenen.json"
    output_file = directory / "sonuclar" / "ozet.json"

    for required in (analysis, expected_file):
        if not required.exists():
            fail(f"{chapter}: gerekli dosya yok: {required.relative_to(ROOT)}")

    print(f"\n=== {chapter.upper()} analiz.py çalıştırılıyor ===", flush=True)
    subprocess.run([sys.executable, "analiz.py"], cwd=directory, check=True)

    if not output_file.exists():
        fail(f"{chapter}: analiz sonrası sonuclar/ozet.json üretilmedi")

    expected = json.loads(expected_file.read_text(encoding="utf-8"))
    actual = json.loads(output_file.read_text(encoding="utf-8"))
    compare(expected, actual, chapter)
    print(f"✓ {chapter.upper()}: analiz çalıştı ve beklenen.json ile eşleşti", flush=True)


def main() -> None:
    chapters = [f"b{i:02d}" for i in range(2, 18)]
    failures = []

    for chapter in chapters:
        try:
            run_chapter(chapter)
        except Exception as exc:
            failures.append((chapter, str(exc)))
            print(f"✗ {chapter.upper()}: {exc}", file=sys.stderr, flush=True)

    print("\n=== Toplu analiz doğrulama özeti ===")
    print(f"Başarılı: {len(chapters) - len(failures)}/{len(chapters)}")
    if failures:
        for chapter, message in failures:
            print(f"- {chapter.upper()}: {message}")
        raise SystemExit(1)

    print("B02-B17: 16/16 analiz başarıyla çalıştı ve beklenen.json sözleşmeleri doğrulandı.")


if __name__ == "__main__":
    main()
