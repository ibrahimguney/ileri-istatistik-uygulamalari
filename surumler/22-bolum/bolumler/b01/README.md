# Bölüm 1 — İstatistiksel Düşünme: Sorudan Kanıta

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- araştırma sorusu, hedef anakütle, örnekleme çerçevesi ve eldeki kayıtları birbirinden ayırır;

- gözlem birimi, değişken, ölçüm ve satır sayısını doğru tanımlar;

- sayısal kod ile sayısal ölçümü; nominal, ordinal, aralık ve oran düzeylerini ayırt eder;

- basit rastgele, sistematik, tabakalı ve küme örneklemenin seçim mantığını açıklar;

- frekans ve yüzdeyi doğru payda üzerinden hesaplar;

- veri türüne uygun grafik seçer ve kaynak sınırlarını belirten kısa bir rapor yazar.

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
python bolumler/b01/analiz.py
```

Asıl analiz: [uygulamalar/b01-istatistiksel-mekanizma/analiz.py](../../uygulamalar/b01-istatistiksel-mekanizma/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b01-istatistiksel-mekanizma/README.md).
R betiği: [analiz.R](../../uygulamalar/b01-istatistiksel-mekanizma/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b01-istatistiksel-mekanizma/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
