"""Gerçek R yürütmesini B18 Python çıktısı ve sabit referansla karşılaştır."""
import csv
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / 'bolumler/b18'
OUT = CHAPTER / 'sonuclar/R'


def flatten(value, prefix=''):
    if isinstance(value, dict):
        return {k: v for key, item in value.items() for k, v in flatten(item, f'{prefix}.{key}' if prefix else key).items()}
    if isinstance(value, list):
        return {k: v for i, item in enumerate(value) for k, v in flatten(item, f'{prefix}.{i}').items()}
    return {prefix: value}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(CHAPTER/'analiz.py')], cwd=ROOT, check=True)
    command = ['Rscript', 'bolumler/b18/analiz.R']
    with (OUT/'yurutme.log').open('w') as log:
        subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    expected = flatten(json.loads((CHAPTER/'beklenen.json').read_text()))
    actual = flatten(json.loads((CHAPTER/'sonuclar/ozet.json').read_text()))
    prefixes = ('uyku_esli.', 'ToothGrowth_doz1.', 'durum_deneyi.')
    required = {key for key in expected if key.startswith(prefixes) and 'filtre_kapatilinca' not in key}
    with (OUT/'sayisal_kontrol.csv').open() as handle:
        rows = list(csv.DictReader(handle))
    keys = [row['metric'] for row in rows]
    assert len(keys) == len(set(keys)), 'Tekrarlı R ölçütü'
    assert set(keys) == required, f'Eksik/fazla R ölçütü: {set(keys)^required}'
    max_delta = 0.0
    for row in rows:
        key = row['metric']; value = float(row['value'])
        assert math.isfinite(value), key
        for reference in (expected, actual):
            assert math.isclose(value, reference[key], rel_tol=1e-7, abs_tol=1e-8), (key,value,reference[key])
        max_delta = max(max_delta, abs(value-actual[key]))
    report = {'bolum':'B18','tarih_UTC':datetime.now(timezone.utc).isoformat(),
              'komut':command,'R_gercek_yurutme':True,'SPSS_gercek_yurutme':False,
              'sayisal_kontrol_sayisi':len(rows),'sonuc':'başarılı','rtol':1e-7,'atol':1e-8,
              'Python_ile_en_buyuk_mutlak_fark':max_delta,
              'sha256':{name:hashlib.sha256((CHAPTER/name).read_bytes()).hexdigest()
                        for name in ('analiz.R','analiz.py','beklenen.json','sleep.csv','ToothGrowth.csv')},
              'R_surumu':subprocess.check_output(['Rscript','--version'],text=True).strip()}
    (OUT/'dogrulama.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
