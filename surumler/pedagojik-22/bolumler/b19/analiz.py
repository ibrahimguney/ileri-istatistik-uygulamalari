"""Bölüm 19: Doğrulayıcı Faktör Analizi; sabit kaynak kimliği 19."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/'uygulamalar/b19-dogrulayici-faktor'/"analiz.py"),*sys.argv[1:]],cwd=root,check=True)
