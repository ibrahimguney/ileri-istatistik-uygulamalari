"""Bölüm 5: Parametrik Testler; sabit kaynak kimliği 6."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b06-parametrik-testler'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
