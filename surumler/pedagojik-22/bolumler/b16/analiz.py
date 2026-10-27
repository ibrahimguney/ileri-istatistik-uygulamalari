"""Bölüm 16: Çok Düzeyli Modeller; sabit kaynak kimliği 16."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b16-cok-duzeyli-modeller'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
