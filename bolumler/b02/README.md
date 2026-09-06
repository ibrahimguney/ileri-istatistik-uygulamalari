# Bölüm 2 — Betimsel İstatistik

Bu klasör kitabın Bölüm 2 uygulamasının bağımsız öğrenci kopyasıdır.
Başka bir bölüm klasörüne veya kitabın LaTeX dosyalarına gereksinim duymaz.

## Başlangıç

1. [Veri sözlüğünü](VERI.md) okuyun; sıfırı ve eksik kodunu ayırın.
2. [Görevleri](GOREVLER.md) çözün veya `calisma.ipynb` defterinde cevaplarınızı yazın.
3. Depo kökünde `python bolumler/b02/analiz.py` çalıştırın.
   Bu klasöre geçtiyseniz `python analiz.py` de çalışır.
4. [Çözümler](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.

Paketler depo kökündeki `requirements.txt` dosyasındadır.
Python betiği CSV'nin şema, sıra, değer aralığı ve hash'ini kontrol eder.
Hata varsa kaynağı düzeltmeden devam etmeyin; Python'u `-O` ile çalıştırmayın.
Ana veri 80 satırdır. Kaynak satırı 1 yalnız ayrı duyarlılık dosyasında dışlanır.

R kodu temel R kullanır. Depo kökünde `Rscript bolumler/b02/analiz.R`,
bu klasörde `Rscript analiz.R` çalıştırılabilir. RStudio'da bu klasörü çalışma
dizini yapıp dosyayı açın. R bu hazırlama oturumunda çalıştırılmamıştır.

## Hesap sözleşmesi

- Varyans ve kovaryans: n−1 böleni; kapalı çerçeve varyansı n böleniyle ayrıca gösterilir.
- Çeyrekler: NumPy `linear`, R `type=7`; histogram sınıfları bir puan genişliğindedir.
- Bıyıklar: 1.5 IQR sınırları içinde kalan gözlenen uçlar.
- MAD: ham medyan mutlak sapma, ölçek çarpanı uygulanmaz.
- İki dönem: aynı 80 kayıt; 160 bağımsız kişi değildir.
- CV: notlar için göreli yetenek ölçüsü olarak yorumlanmaz.
- Güven aralığı, normallik testi, bootstrap veya hipotez testi bu betikte yapılmaz.

## Çıktılar

`sonuclar/betimsel_ozet.csv`, `frekanslar.csv`, `ceyrek_yontemleri.csv`,
`isaretli_kayitlar.csv`, `duyarlilik_satir1_haric.csv`, `ozet.json`;
`grafikler/b02-gercek-betimsel.pdf` ve türetilmiş `notlar.csv`.
Bunlar çalışma sırasında üretilir; kaynak `veri.csv` üzerine yazılmaz.
Grafik kitabın çizimiyle aynı veri ve tanımları kullanır; görsel yerleşimi aynı olmak zorunda değildir.