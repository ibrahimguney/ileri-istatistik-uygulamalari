"""Bölüm 11: Regresyon Analizi; sabit kaynak kimliği 12."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b12-regresyon'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
