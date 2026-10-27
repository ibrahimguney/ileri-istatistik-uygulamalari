"""Bölüm 13: Kovaryans Analizi (ANCOVA); sabit kaynak kimliği 14."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b14-kovaryans-analizi'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
