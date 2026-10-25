# Bölüm 10 — Parametrik Olmayan Testler

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- bağımsız grupları, eşleştirilmiş çiftleri ve tam blokları ayırır;

- ortalama, konum ve sıra hipotezlerinin aynı olmadığını açıklar;

- bağları ve sıfır farkları işleyerek U, işaretli sıra ve H istatistiklerini hesaplar;

- kesin sayım, Monte Carlo ve asimptotik p değerlerini ayırır;

- Dunn ve eşleştirilmiş karşılaştırmalarda Holm ailesini tanımlar;

- gerçek veri, kaynak sınırı ve yeniden üretilebilir kodla sonuç raporlar.

## Çalışma sırası

1. [Veri açıklamasını](VERI.md) okuyun.
2. [Görevleri](GOREVLER.md) kendi çözümünüzle tamamlayın.
3. [Defteri](calisma.ipynb) veya Python analizini çalıştırın.
4. [Raporlama rehberiyle](RAPORLAMA.md) bulguları yazın.
5. [Çözümlerle](COZUMLER.md) karşılaştırın.

## Çalıştırma

Komutlar `surumler/22-bolum/` klasöründen:

```sh
python -m pip install -r requirements.txt
python bolumler/b10/analiz.py
```

Asıl analiz: [uygulamalar/b10-parametrik-olmayan/analiz.py](../../uygulamalar/b10-parametrik-olmayan/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b10-parametrik-olmayan/README.md).
R betiği: [analiz.R](../../uygulamalar/b10-parametrik-olmayan/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b10-parametrik-olmayan/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 13: üstünlük belirsizliği ve eşli medyan

[Uygulama açıklaması](../../uygulamalar/b10-parametrik-olmayan/ustunluk-belirsizlik/README.md) ·
[Python kodu](../../uygulamalar/b10-parametrik-olmayan/ustunluk-belirsizlik/analiz.py) ·
[Sonuçlar](../../uygulamalar/b10-parametrik-olmayan/ustunluk-belirsizlik/sonuclar/ozet.json).
Eski ana analizler/veriler korunur; yeni ek yalnız Python.
