"""Bölüm 12: Çoklu ve Lojistik Regresyon; sabit kaynak kimliği 13."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b13-coklu-lojistik'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
