"""Bölüm 10: Korelasyon Analizi; sabit kaynak kimliği 11."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b11-korelasyon'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
