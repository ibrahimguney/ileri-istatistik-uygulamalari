"""Bölüm 21: Yapısal Eşitlik Modeli; sabit kaynak kimliği 21."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b21-yapisal-esitlik'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
