"""Bölüm 5: Güç Analizi ve Örneklem Büyüklüğü Planlama; ortak uygulamayı sürüm kökünde çalıştırır."""
from pathlib import Path
import subprocess, sys
root = Path(__file__).resolve().parents[2]
subprocess.run([sys.executable, str(root / 'uygulamalar/b05-guc-analizi' / "analiz.py"), *sys.argv[1:]], cwd=root, check=True)
