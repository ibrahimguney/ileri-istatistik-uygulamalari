"""Bölüm 7: Varyans Analizi (ANOVA); sabit kaynak kimliği 7."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b07-varyans-analizi'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
