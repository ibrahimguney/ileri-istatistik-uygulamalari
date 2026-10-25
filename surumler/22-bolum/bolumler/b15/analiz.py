"""Bölüm 15: Aracılık ve Düzenleyicilik Analizleri; ortak uygulamayı sürüm kökünde çalıştırır."""
from pathlib import Path
import subprocess, sys
root = Path(__file__).resolve().parents[2]
subprocess.run([sys.executable, str(root / 'uygulamalar/b15-aracilik-duzenleyicilik' / "analiz.py"), *sys.argv[1:]], cwd=root, check=True)
