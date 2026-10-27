"""Bölüm 14: Çok Değişkenli Varyans Analizi (MANOVA); sabit kaynak kimliği 9."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b09-manova'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
