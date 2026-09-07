from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [ROOT / "bolumler" / f"b{i:02d}" / "calisma.ipynb" for i in range(1, 18)]

HERE_REF = re.compile(r"HERE\s*/\s*[\"']([^\"']+)[\"']")


def fail(message: str) -> None:
    raise AssertionError(message)


def validate_notebook(path: Path) -> list[str]:
    notes: list[str] = []
    if not path.exists():
        fail(f"Eksik notebook: {path.relative_to(ROOT)}")

    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Geçersiz JSON: {path.relative_to(ROOT)} — {exc}")

    if nb.get("nbformat") != 4:
        fail(f"nbformat 4 değil: {path.relative_to(ROOT)}")
    if not isinstance(nb.get("cells"), list) or not nb["cells"]:
        fail(f"Hücre yok: {path.relative_to(ROOT)}")

    kernelspec = nb.get("metadata", {}).get("kernelspec", {})
    if kernelspec.get("name") != "python3":
        fail(f"python3 kernelspec yok: {path.relative_to(ROOT)}")

    code_count = 0
    for idx, cell in enumerate(nb["cells"]):
        cell_type = cell.get("cell_type")
        source = cell.get("source", [])
        if isinstance(source, list):
            source_text = "".join(source)
        elif isinstance(source, str):
            source_text = source
        else:
            fail(f"Geçersiz source alanı: {path.relative_to(ROOT)} hücre {idx}")

        if cell_type == "code":
            code_count += 1
            if cell.get("execution_count") is not None:
                fail(f"Execution count temiz değil: {path.relative_to(ROOT)} hücre {idx}")
            if cell.get("outputs", []) != []:
                fail(f"Kayıtlı çıktı var: {path.relative_to(ROOT)} hücre {idx}")
            try:
                ast.parse(source_text or "pass")
            except SyntaxError as exc:
                fail(f"Python sözdizimi hatası: {path.relative_to(ROOT)} hücre {idx} — {exc}")

            for ref in HERE_REF.findall(source_text):
                target = path.parent / ref
                if not target.exists():
                    fail(
                        f"Notebook yerel dosya yolu bulunamadı: "
                        f"{path.relative_to(ROOT)} -> {ref}"
                    )

        elif cell_type not in {"markdown", "raw"}:
            fail(f"Bilinmeyen hücre tipi: {path.relative_to(ROOT)} hücre {idx}: {cell_type}")

    if code_count == 0:
        fail(f"Kod hücresi yok: {path.relative_to(ROOT)}")

    text = path.read_text(encoding="utf-8")
    for required in ("GOREVLER.md", "COZUMLER.md", "RAPORLAMA.md"):
        if required not in text:
            notes.append(f"uyarı: {required} notebook metninde geçmiyor")

    return notes


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for path in EXPECTED:
        try:
            notes = validate_notebook(path)
            rel = path.relative_to(ROOT)
            print(f"OK  {rel}")
            warnings.extend(f"{rel}: {note}" for note in notes)
        except AssertionError as exc:
            failures.append(str(exc))
            print(f"FAIL {exc}", file=sys.stderr)

    print(f"\nKontrol edilen notebook: {len(EXPECTED)}")
    if warnings:
        print("Uyarılar:")
        for item in warnings:
            print(f"- {item}")

    if failures:
        print(f"\nBaşarısız kontrol: {len(failures)}", file=sys.stderr)
        return 1

    print("Tüm notebooklar statik teknik kontrolden geçti.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
