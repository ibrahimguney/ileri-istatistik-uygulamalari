# Bölüm 6 — Korelasyon

Pearson, bağlı sıralarla Spearman, kayıt etkisi ve Monte Carlo permütasyonu.
Önce [VERI.md](VERI.md) ve [GOREVLER.md](GOREVLER.md) okuyun.
Bölüm 2'nin aynı 80 kaydının burada ilk 60'ı ana analiz, son 20'si etkinliktir.

## Çalıştırma

Depo kökünden, öğrencinin kendi bilgisayarında:

```sh
python -m pip install -r bolumler/b06/requirements.txt
python bolumler/b06/analiz.py
```

Bölüm klasöründe `python analiz.py` çalışır; veri.csv aynı klasörde kalmalıdır.
Kitap veya Bölüm 7 dosyalarına bağımlılık yoktur. Sabit sürümler hazırlama
ortamının sürümleridir; bu ortamda yeni paket kurulmadı. `python -O` kullanmayın:
iç hesap denetimlerini kaldırır.

`calisma.ipynb` dosyasını Jupyter ortamında açın; depo kökünden veya bölüm
klasöründen çalışır. None alanlarını tamamlayıp [COZUMLER.md](COZUMLER.md) ve
[beklenen.json](beklenen.json) ile karşılaştırın. Jupyter analiz betiğinin
zorunlu bağımlılığı değildir ve requirements listesinde bulunmaz.

R: `Rscript bolumler/b06/analiz.R`; bölüm klasöründe `Rscript analiz.R`.
Temel R yeterlidir; sonuçlar ekrana, grafik `grafikler/grafikler-R.pdf` dosyasına
yazılır. R çalıştırılmadı. Bu pakette SPSS syntax/çıktısı yoktur. Aynı seed,
R ile NumPy'da aynı permütasyon dizisini garanti etmez.

## Çıktılar

- `sonuclar/ozet.json`: ana 60, ilk satırsız 59 ve son 20 için ayrı özetler.
- `sonuclar/siralar.csv`: ortalama sıralarıyla 60 kayıt.
- `sonuclar/duyarlilik.csv`: ana kümede 60 ayrı birini-dışarıda-bırakma hesabı.
- `grafikler/b06-uci-korelasyon.pdf`: ham notlar ve sıralar; nokta büyüklüğü
  aynı koordinattaki kayıt sayısıyla orantılıdır, ilk kayıt ayrıca işaretlenir.

Ham 80 kayıt değişmez; yeniden çalıştırma üretilen dosyaları yeniler. Kendi
raporunuzu çıktı klasörlerinden ayrı tutun. Hash denetimi başka bölümün
sonuç dosyasına bağlı değildir. Aynı 60 kayıtta sabit terimli OLS özdeşliği
korunur; dış Bölüm 7 dosyasının çalıştırıldığı iddia edilmez.
Çalıştırma kaydı: [DOGRULAMA.json](DOGRULAMA.json).

Pearson klasik p'si ve yaklaşık Fisher aralığı model koşullarına bağlıdır.
Spearman yaklaşık/asimptotik p'si ile seed 202606, B=19999 rastgele permütasyonun
`(uç+1)/(B+1)` p'si ayrı etiketlenir. Bu Monte Carlo hesabı tam kesin test değildir.