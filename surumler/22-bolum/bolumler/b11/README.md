# Bölüm 11 — Korelasyon Analizi

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- korelasyon analizinin amacını ve sınırlılıklarını açıklar,

- pozitif, negatif ve sıfıra yakın ilişkiyi grafik ve katsayı üzerinden yorumlar,

- Pearson ve Spearman korelasyonları arasında uygun seçimi yapar,

- korelasyon katsayısı, belirlilik katsayısı ve anlamlılık testini birlikte değerlendirir,

- korelasyon sonucunu nedensellikten ayırarak doğru raporlar,

- gerçek not verisinde bağlı değerlere ortalama sıra vererek Spearman katsayısını hesaplar,

- bir gözlemin çıkarılmasıyla oluşan değişimi, silme kararı vermeden değerlendirir,

- SPSS, R ve Python çıktılarını test yöntemi ve veri seçimiyle birlikte raporlar.

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
python bolumler/b11/analiz.py
```

Asıl analiz: [uygulamalar/b11-korelasyon/analiz.py](../../uygulamalar/b11-korelasyon/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b11-korelasyon/README.md).
R betiği: [analiz.R](../../uygulamalar/b11-korelasyon/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b11-korelasyon/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 14: birlikte belirsizlik ve uyum ayrımı

[Uygulama açıklaması](../../uygulamalar/b11-korelasyon/esli-bootstrap/README.md) ·
[Python kodu](../../uygulamalar/b11-korelasyon/esli-bootstrap/analiz.py) ·
[Sonuçlar](../../uygulamalar/b11-korelasyon/esli-bootstrap/sonuclar/ozet.json).
Eski ana analizler/veriler korunur; yeni ek yalnız Python.
