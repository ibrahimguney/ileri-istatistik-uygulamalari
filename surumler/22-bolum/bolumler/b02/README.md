# Bölüm 2 — Betimsel İstatistik

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- ortalama, medyan ve modu aynı veride hesaplayıp farklı sorulara yanıt verdiklerini açıklar;

- varyans bölenini, standart sapmayı ve standart hatayı birbirinden ayırır;

- çeyrek algoritmasını belirterek IQR, tarama sınırları ve kutu grafiğini üretir;

- uç kayıtların etkisini ana veriyi değiştirmeden duyarlılık analiziyle gösterir;

- ağırlıklı/geometrik ortalamanın ve varyasyon katsayısının kullanım koşullarını belirtir;

- aynı kayıtlardaki iki değişkenin kovaryansını, korelasyonunu ve fark dağılımını yorumlar.

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
python bolumler/b02/analiz.py
```

Asıl analiz: [uygulamalar/b02-betimsel-istatistik/analiz.py](../../uygulamalar/b02-betimsel-istatistik/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b02-betimsel-istatistik/README.md).
R betiği: [analiz.R](../../uygulamalar/b02-betimsel-istatistik/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b02-betimsel-istatistik/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
