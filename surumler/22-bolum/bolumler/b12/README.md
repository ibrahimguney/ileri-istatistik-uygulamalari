# Bölüm 12 — Regresyon Analizi

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- basit doğrusal regresyonun amacını ve korelasyondan farkını açıklar,

- bağımlı ve bağımsız değişken rollerini doğru biçimde tanımlar,

- regresyon doğrusunu, eğim ve sabit terimi bağlam içinde yorumlar,

- $R^2$, artık, güven aralığı ve tahmin mantığını birlikte değerlendirir,

- temel regresyon varsayımlarını ve tanısal kontrolleri açıklar,

- aynı veriyle SPSS, R ve Python sonuçlarını karşılaştırır,

- ortalama yanıtın güven aralığı ile bireysel tahmin aralığını ayırt eder,

- hatalı bir regresyon raporunu gerekçeleriyle düzeltir ve yeniden üretilebilir bir rapor hazırlar.

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
python bolumler/b12/analiz.py
```

Asıl analiz: [uygulamalar/b12-regresyon/analiz.py](../../uygulamalar/b12-regresyon/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b12-regresyon/README.md).
R betiği: [analiz.R](../../uygulamalar/b12-regresyon/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b12-regresyon/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 15: eğitim, kalibrasyon ve kontrol

[Uygulama açıklaması](../../uygulamalar/b12-regresyon/ayri-kalibrasyon/README.md) ·
[Python kodu](../../uygulamalar/b12-regresyon/ayri-kalibrasyon/analiz.py) ·
[Sonuçlar](../../uygulamalar/b12-regresyon/ayri-kalibrasyon/sonuclar/ozet.json).
Eski ana analizler/veriler korunur; yeni ek yalnız Python.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b12/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
