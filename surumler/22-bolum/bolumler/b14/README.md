# Bölüm 14 — Kovaryans Analizi (ANCOVA)

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- ANCOVA’yı grup göstergeleri ve sayısal kovaryat içeren bir doğrusal model olarak kurar;

- kovaryatın zamanını ve modeldeki rolünü, istatistiksel anlamlılığından ayırır;

- ortak eğim, ayrı eğim ve doğrusal olmayan ortalama yapısını karşılaştırır;

- belirli kovaryat düzeyindeki ortalamayı ve grup farkını doğrusal kontrastla hesaplar;

- güven aralığı, çoklu karşılaştırma ailesi ve etki büyüklüğünün tanımını açıklar;

- SPSS/R/Python ayarlarını eşleştirip analiz sınırlarını raporlar.

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
python bolumler/b14/analiz.py
```

Asıl analiz: [uygulamalar/b14-kovaryans-analizi/analiz.py](../../uygulamalar/b14-kovaryans-analizi/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b14-kovaryans-analizi/README.md).
R betiği: [analiz.R](../../uygulamalar/b14-kovaryans-analizi/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b14-kovaryans-analizi/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
