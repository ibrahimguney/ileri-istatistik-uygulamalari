"""Bölüm 17: Ölçek Uyarlama ve Güvenirlik; sabit kaynak kimliği 17."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b17-guvenirlik'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
