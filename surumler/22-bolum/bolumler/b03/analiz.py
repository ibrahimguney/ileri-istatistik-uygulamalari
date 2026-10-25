"""Bölüm 3: Veri Hazırlama ve Analize Hazırlık; ortak uygulamayı sürüm kökünde çalıştırır."""
from pathlib import Path
import subprocess, sys
root = Path(__file__).resolve().parents[2]
subprocess.run([sys.executable, str(root / 'uygulamalar/b03-veri-hazirlama' / "analiz.py"), *sys.argv[1:]], cwd=root, check=True)
