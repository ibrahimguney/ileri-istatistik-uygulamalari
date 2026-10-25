# Bölüm 3 — Veri Hazırlama ve Analize Hazırlık

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- ham arşivi, doğrulanmış veriyi ve analize özel dosyayı birbirinden ayırır;

- gözlem birimi, anahtar, veri sözlüğü ve geçerli değer kurallarını tanımlar;

- hücre, kayıt ve puan düzeyindeki eksikliği farklı paydalarla raporlar;

- ters kodlamayı ve asgari madde sayısını açık bir puanlama kuralına dönüştürür;

- geniş–uzun dönüşümünü ve birleştirmeyi veri kaybı/çoğalma kontrolleriyle yürütür;

- temizleme kararlarını ve yapılmamış analizleri denetlenebilir biçimde belgeler;

- ileri uygulamada çoklu atama belirsizliğini Rubin kurallarıyla birleştirir ve delta duyarlılığının varsayımsal niteliğini açıklar.

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
python bolumler/b03/analiz.py
```

Asıl analiz: [uygulamalar/b03-veri-hazirlama/analiz.py](../../uygulamalar/b03-veri-hazirlama/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b03-veri-hazirlama/README.md).
R betiği: [analiz.R](../../uygulamalar/b03-veri-hazirlama/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b03-veri-hazirlama/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
