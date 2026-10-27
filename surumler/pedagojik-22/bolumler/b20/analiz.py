"""Bölüm 20: Ölçme Değişmezliği; sabit kaynak kimliği 20."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b20-olcme-degismezligi'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
