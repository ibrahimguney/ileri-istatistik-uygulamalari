# Bölüm 16 — Çok Düzeyli Modeller

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- iç içe (hiyerarşik) veride bağımsızlık varsayımının neden bozulduğunu açıklar;

- boş modelden sınıf içi korelasyonu (ICC), tasarım etkisini ve etkili örneklem büyüklüğünü hesaplar;

- naif, küme-sağlam ve çok düzeyli standart hataları karşılaştırır;

- grup ortalamasına ve genel ortalamaya merkezlemeyi ayırır; grup içi, gruplar arası ve bağlamsal etkileri yorumlar;

- rastgele eğimi ve sınırda olabilirlik oranı testini açıklar;

- düzeyler arası etkileşimi kurar ve açıklanan varyans ölçülerinin sınırlarını tartışır;

- ML ve REML kestirimlerini, yakınsama denetimini ve raporlama unsurlarını uygular.

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
python bolumler/b16/analiz.py
```

Asıl analiz: [uygulamalar/b16-cok-duzeyli-modeller/analiz.py](../../uygulamalar/b16-cok-duzeyli-modeller/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b16-cok-duzeyli-modeller/README.md).
R betiği: [analiz.R](../../uygulamalar/b16-cok-duzeyli-modeller/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b16-cok-duzeyli-modeller/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 19: hedef, okul büyüklüğü ve tahmin

[Uygulama açıklaması](../../uygulamalar/b16-cok-duzeyli-modeller/okul-tahmini/README.md) ·
[Python kodu](../../uygulamalar/b16-cok-duzeyli-modeller/okul-tahmini/analiz.py) ·
[Sonuçlar](../../uygulamalar/b16-cok-duzeyli-modeller/okul-tahmini/sonuclar/ozet.json).
Eski ana analizler ve gerçek HSB verisi korunur; yeni ek yalnız Python.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b16/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
