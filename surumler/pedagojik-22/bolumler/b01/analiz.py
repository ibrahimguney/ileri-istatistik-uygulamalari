"""Bölüm 1: İstatistiksel Düşünme: Sorudan Kanıta; sabit kaynak kimliği 1."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b01-istatistiksel-mekanizma'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
