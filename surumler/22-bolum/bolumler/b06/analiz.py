"""Bölüm 6: Parametrik Testler; ortak uygulamayı sürüm kökünde çalıştırır."""
from pathlib import Path
import subprocess, sys
root = Path(__file__).resolve().parents[2]
subprocess.run([sys.executable, str(root / 'uygulamalar/b06-parametrik-testler' / "analiz.py"), *sys.argv[1:]], cwd=root, check=True)
