# Bölüm 7 — Regresyon

Birinci dönem notundan yıl sonu notunu yordama: basit OLS, ortalama güven
aralığı/bireysel tahmin aralığı, etki tanıları, HC3 ve LOOCV.
Önce [VERI.md](VERI.md), sonra [GOREVLER.md](GOREVLER.md) okuyun.

## Çalıştırma

Öğrencinin bilgisayarında, öğrenci deposunun kökünden:

```sh
python -m pip install -r bolumler/b07/requirements.txt
python bolumler/b07/analiz.py
```

Bölüm klasöründe `python analiz.py` yeterlidir. Ham `veri.csv` kodla aynı
klasörde kalmalıdır. Kitap/Bölüm 6 dosyaları gerekmez. Sürümler hazırlama
ortamının sürümleridir; burada paket kurulmadı. `python -O` kullanmayın:
assert denetimlerini kapatır.

`calisma.ipynb` defterini Jupyter ortamında açın; depo kökü veya bölüm
klasöründen çalışır. None alanları öğrencinin tamamlayacağı görevlerdir.
Jupyter, analiz betiği için gerekli değildir ve requirements listesinde yoktur.
Çözümleri [COZUMLER.md](COZUMLER.md), sayısal hedefleri [beklenen.json](beklenen.json)
ile karşılaştırın; yuvarlanmamış değerlerde küçük kayan nokta farkları olabilir.

R: `Rscript bolumler/b07/analiz.R`; bölüm klasöründe `Rscript analiz.R`.
Temel R yeterlidir; önceden Python çalıştırmak gerekmez. R sonuçları ekrana,
tanı grafiklerini `grafikler/tani-R.pdf` dosyasına yazar. R çalıştırılmadı.
Bu öğrenci paketinde SPSS syntax/çıktısı yoktur.

## Üretilen dosyalar

- `sonuclar/not_basari.csv`: ilk 60 kaydın ana analiz kopyası.
- `sonuclar/aktarim.csv`: son 20 kaydın ayrı model kurma etkinliği.
- `sonuclar/ozet.json`: katsayı, aralık, HC3, RMSE ve ayrı etkinlik sonuçları.
- `sonuclar/tani.csv`: ana kayıtlar, tahmin, artık, kaldıraç ve Cook uzaklığı.
- `sonuclar/araliklar.csv`: G1=12 için klasik ortalama ve bireysel aralıklar.
- `sonuclar/duyarlilik.csv`: çıkarılan kayıt, 59 kayıtla eğim ve LOOCV hatası.
- `grafikler/b07-ogrenme-senaryosu.pdf`: ham notlar, regresyon doğrusu ve
  klasik ortalama güven bandı; yanında artık grafiği.

Ham 80 kayıt değişmez; yeniden çalıştırma üretilen dosyaları yeniler.
Kendi raporunuzu bu çıktı klasörlerinden ayrı saklayın. Doğrulama kapsamı
[DOGRULAMA.json](DOGRULAMA.json) dosyasındadır. Yerel hash kaynağın
bozulmadığını denetler; otomatik çevrimiçi kaynak karşılaştırması yapılmaz.
Öğrenci betiği ağ bağlantısı gerektirmez.

## Yorum sınırı

Ana n=60, son 20 ise yeniden model kurulan ayrı etkinliktir; bu dosyada ana
modelin dış test performansı hesaplanmaz. LOOCV yalnız ana 60 kayıtta yapılır.
HC3 katsayı belirsizliğini değiştirir, OLS nokta tahminlerini değiştirmez;
klasik bireysel tahmin aralığını kendiliğinden sağlamlaştırmaz. Klasik ve HC3
eğim aralıkları t(58) referansıyla raporlanır. Kaynak seçimi, kümelenme ve
nedensellik sorunları yalnız bu hesaplarla çözülmez.