# Bölüm 8 — Tekrarlı Ölçümler ve Karma Desenler

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- aynı kişinin tekrar ölçülmesinin bağımsızlık varsayımını nasıl değiştirdiğini açıklar;

- tekrarlı ölçümler ANOVA’sında toplam değişkenliği kişi, zaman ve hata bileşenlerine ayırır;

- küreselliği tanımlar; Mauchly testini, Greenhouse–Geisser ve Huynh–Feldt düzeltmelerini yorumlar;

- tek değişkenli, çok değişkenli (Hotelling $T^2$) ve odaklı karşıtlık yaklaşımlarını karşılaştırır;

- kısmi ve genelleştirilmiş eta-kareyi ayırır;

- arası–içi (karma) desende etkileşimi, basit etkileri ve büyüme hızlarını raporlar;

- karma etkiler modelinin tekrarlı ölçümler ANOVA’sıyla ilişkisini ve üstünlüklerini açıklar.

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
python bolumler/b08/analiz.py
```

Asıl analiz: [uygulamalar/b08-tekrarli-olcumler/analiz.py](../../uygulamalar/b08-tekrarli-olcumler/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b08-tekrarli-olcumler/README.md).
R betiği: [analiz.R](../../uygulamalar/b08-tekrarli-olcumler/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b08-tekrarli-olcumler/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
