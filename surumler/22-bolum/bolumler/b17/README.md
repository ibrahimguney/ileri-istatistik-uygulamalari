# Bölüm 17 — Ölçek Uyarlama ve Güvenirlik

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- güvenirliği puan, örneklem ve kullanım bağlamıyla tanımlar;

- iç tutarlılığı geçerlik, zamansal kararlılık ve ölçüm eşdeğerliğinden ayırır;

- puanlama anahtarına göre ters kodlama yapar, eksik madde kararını belgeler;

- ham/standart alfa, düzeltilmiş madde–kalan korelasyonu ve bootstrap aralığını hesaplar;

- madde silme kararında sayısal değişim ile içerik kaybını birlikte değerlendirir;

- bir Türkçe uyarlama için gerekli kanıtları ve henüz yapılmamış işlemleri açıklar.

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
python bolumler/b17/analiz.py
```

Asıl analiz: [uygulamalar/b17-guvenirlik/analiz.py](../../uygulamalar/b17-guvenirlik/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b17-guvenirlik/README.md).
R betiği: [analiz.R](../../uygulamalar/b17-guvenirlik/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b17-guvenirlik/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 20: model ve belirsizlik

[Uygulama açıklaması](../../uygulamalar/b17-guvenirlik/model-belirsizlik/README.md) ·
[Python kodu](../../uygulamalar/b17-guvenirlik/model-belirsizlik/analiz.py) ·
[Sonuçlar](../../uygulamalar/b17-guvenirlik/model-belirsizlik/sonuclar/ozet.json).
Eski ana analizler ve gerçek IPIP verisi korunur; yeni ek yalnız Python.
