"""B01/B18 için kitaptan okunan seçili sayıları yerel hesaplarla denetle.

Kitap: ileri-istatistik-izü6.pdf; basılı sayfa numaraları kullanılır.
Bütün kitabın doğrulaması değildir. PDF ayrıştırıcısı değildir.
Önce B01 ve B18 analiz.py betikleri çalıştırılmalıdır.
"""
import json
import math
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def value(data, path):
    for key in path.split('.'):
        data = data[int(key)] if isinstance(data, list) else data[key]
    return data


def main():
    b01 = json.loads((ROOT/'bolumler/b01/sonuclar/ozet.json').read_text())
    b18 = json.loads((ROOT/'bolumler/b18/sonuclar/ozet.json').read_text())
    # (basılı sayfa, çıktı alanı, kitapta görünen değer, ondalık basamak)
    checks1 = [(5,'veri.n',80,0),(5,'sistematik_secim.n',10,0),
               (5,'sistematik_secim.aralik',8,0),(5,'sistematik_secim.baslangic',3,0),
               (6,'sistematik_secim.G3_ortalama',12.2,1),(6,'G3.ortalama',12.6375,4)]
    checks18 = [(271,'uyku_esli.kosul1.ortalama',.75,2),
        (271,'uyku_esli.kosul1.s',1.789010,6),(271,'uyku_esli.kosul2.ortalama',2.33,2),
        (271,'uyku_esli.kosul2.s',2.002249,6),(271,'uyku_esli.korelasyon.r',.795170,6),
        (271,'uyku_esli.korelasyon.p',.005965,6)]
    prefix='uyku_esli.fark_kosul2_eksi_kosul1.'
    checks18 += [(271,prefix+k,v,d) for k,v,d in [
        ('n',10,0),('ortalama',1.58,2),('s',1.229995,6),('SH',.388959,6),
        ('t',4.062128,6),('sd',9,0),('p_iki_yonlu',.002832890,9),
        ('GA95.0',.700114,6),('GA95.1',2.459886,6),('dz',1.284558,6)]]
    prefix='ToothGrowth_doz1.'
    checks18 += [(272,prefix+k,v,d) for k,v,d in [
        ('OJ.ortalama',22.70,2),('OJ.s',3.910953,6),('VC.ortalama',16.77,2),('VC.s',2.515309,6),
        ('Levene_ortalama_merkezli.F',2.271451,6),('Levene_ortalama_merkezli.p',.149126,6),
        ('Welch.fark',5.93,2),('Welch.SH',1.470453,6),('Welch.t',4.032770,6),
        ('Welch.sd',15.357672,6),('Welch.p_iki_yonlu',.001038,6),
        ('Welch.GA95.0',2.802148,6),('Welch.GA95.1',9.057852,6),
        ('Student.sd',18,0),('Student.p_iki_yonlu',.000781,6),
        ('Student.GA95.0',2.840692,6),('Student.GA95.1',9.019308,6)]]
    checks18.append((273,prefix+'d_pooled',1.803509,6))
    checks18 += [(273,'durum_deneyi.ID_1_5_filtresi.'+k,v,d) for k,v,d in [
        ('n',5,0),('ortalama',1.24,2),('t',3.260900,6),('sd',4,0),
        ('p_iki_yonlu',.031054,6),('GA95.0',.184220,6),('GA95.1',2.295780,6)]]
    for name,data,checks in [('B01',b01,checks1),('B18',b18,checks18)]:
        for page,key,expected,digits in checks:
            actual=value(data,key)
            tolerance=0 if digits==0 else .5*10**(-digits)+1e-12
            assert math.isclose(actual,expected,rel_tol=0,abs_tol=tolerance),(name,page,key,actual,expected)
        print(f'{name}: {len(checks)} kitap sayısı, basılı yuvarlama hassasiyetinde doğrulandı.')
    x=pd.read_csv(ROOT/'bolumler/b01/veri.csv')
    assert b01['sistematik_secim']['kaynak_satirlar']==[3,11,19,27,35,43,51,59,67,75]
    selected=x.iloc[np.sort(np.random.default_rng(20260906).choice(80,10,replace=False))]
    assert selected.kaynak_satir.tolist()==[21,23,26,34,40,44,56,59,60,62]
    assert math.isclose(selected.G3.mean(),13.2)
    assert math.isclose(x.iloc[:10].G3.mean(),13.0)
    np.testing.assert_allclose([x.iloc[r::8].G3.mean() for r in range(8)],
                               [12.8,13.1,12.2,12.4,12.4,13.0,12.2,13.0],rtol=0,atol=1e-12)
    print('B01: ayrıca iki seçim dizisi, rastgele/ilk-10 ortalamaları ve sekiz başlangıç doğrulandı (s.5–6).')

if __name__ == '__main__': main()
