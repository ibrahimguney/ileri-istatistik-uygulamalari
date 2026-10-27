"""Bölüm 4: Hipotez Testi; sabit kaynak kimliği 4."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b04-hipotez-testi'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
