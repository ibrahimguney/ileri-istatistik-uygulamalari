# Bölüm 6 — Parametrik Testler

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- parametrik testlerin temel mantığını ve hangi koşullarda tercih edildiğini açıklar,

- bir örneklem, bağımsız örneklem ve eşleşmiş örneklem t-testleri arasında doğru seçimi yapar,

- normallik, bağımsızlık ve varyans homojenliği varsayımlarını değerlendirir,

- t-istatistiği, serbestlik derecesi, $p$-değeri ve güven aralığını birlikte yorumlar,

- parametrik test sonuçlarını araştırma bağlamında akademik dille raporlar,

- IBM SPSS Statistics ortamında temel parametrik test çıktılarını yorumlar,

- aynı kişileri ID ile eşleştirir ve fark yönünü açıkça tanımlar,

- Welch ve Student sonuçlarını standart hata ve serbestlik derecesi bakımından karşılaştırır,

- ham fark, güven aralığı ve tasarıma uygun etki büyüklüğünü birlikte raporlar.

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
python bolumler/b06/analiz.py
```

Asıl analiz: [uygulamalar/b06-parametrik-testler/analiz.py](../../uygulamalar/b06-parametrik-testler/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b06-parametrik-testler/README.md).
R betiği: [analiz.R](../../uygulamalar/b06-parametrik-testler/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b06-parametrik-testler/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
