# Bölüm 15 — Aracılık ve düzenleyicilik

Kitap kökünden:

    python uygulamalar/b15-aracilik-duzenleyicilik/analiz.py
    Rscript uygulamalar/b15-aracilik-duzenleyicilik/analiz.R

SPSS: `analiz.sps` (çalışma dizini kitap kökü; önce Python betiği `veri.csv`
dosyasını üretir).

## Veri

Gerçek katılımcı verisi değildir; üretim kodu `analiz.py` içindedir.
160 kayıt, üretim tohumu 202609 (NumPy `default_rng`). Sırayla `x`, `w`, `e_M`,
`e_Y`, `e_D` standart normal olarak çekilir:

- `araci = .6 x + e_M`
- `y_aracilik = .2 x + .7 araci + e_Y`
- `y_duzenleyicilik = .3 x + .2 w + .5 x w + e_D`

İki yanıt ayrı öğretim örnekleridir; tek bir koşullu aracılık modeli gibi
birleştirilmez.

## Çıktılar

- `veri.csv`: üretilen veri (id, x, w, araci, y_aracilik, y_duzenleyicilik)
- `sonuclar/ozet.json`: a, b, c′, c yolları; dolaylı etki; 5000 tekrarlı
  persentil bootstrap aralığı (tohum 202610); düzenleyicilik katsayıları ve
  basit eğimler
- `sonuclar/basit_egimler.csv`: W ortalama ve ±1 SS düzeylerinde basit eğimler
- `assets_figures/b13m-bootstrap-egimler.pdf`: kitaptaki şekil

## Denetimler

Betik şunları sayısal olarak doğrular: `c = c′ + ab` özdeşliği; kitapta
raporlanan ab = .521844 ve %95 GA [.368530, .698101]; merkezlenmiş ve ham
modellerde etkileşim katsayısının eşitliği; basit eğim standart hatasının
kovaryans formülü ile yeniden merkezlenmiş model arasında aynı çıkması.

R betiği aynı nokta tahminlerini verir. R'nin rastgele sayı üreteci NumPy'den
farklı olduğu için bootstrap aralığının son basamakları farklıdır
([.367, .692]); bu Monte Carlo belirsizliğidir. SPSS betiği yol katsayılarını
ve basit eğimler için gereken katsayı kovaryanslarını verir; dolaylı etkinin
bootstrap aralığı için PROCESS makrosu (Model 4) veya Python/R kullanılır.

## Revizyon 18 — tanımlama ve bölgeler

[Yeni ek](duyarlilik-bolgeler/README.md): aynı tam duyarlıklı simülasyonda
varsayımsal hata korelasyonu ve ayrı düzenleyicilik yanıtında noktasal/eşzamanlı
eğim bölgeleri. Eski 5000 bootstrap hesabı korunur; yeni ek yalnız Python.
