# Bölüm 22 — IBM SPSS Uygulamaları

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- veri kaynağını, analiz birimini ve etkin oturum ayarlarını birlikte denetler;

- veri sözlüğünü CSV içe aktarma komutlarıyla eşleştirir;

- eşli testte doğru tabloyu, bağımsız testte doğru model satırını belirler;

- filtre, ağırlık, eksik kod ve fark yönünün sonuç üzerindeki etkisini gösterir;

- SPSS ile hesaplanmış sonucu, başka yazılımla üretilmiş kontrol değerinden ayırır;

- sözdizimi (syntax), veri, çıktı ve akademik raporu denetlenebilir bir teslim dosyasında birleştirir.

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
python bolumler/b22/analiz.py
```

Asıl analiz: [uygulamalar/b22-spss-uygulamalar/analiz.py](../../uygulamalar/b22-spss-uygulamalar/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b22-spss-uygulamalar/README.md).
R betiği: [analiz.R](../../uygulamalar/b22-spss-uygulamalar/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b22-spss-uygulamalar/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 25

[Yeni uygulama ve kapsamı](../../uygulamalar/b22-spss-uygulamalar/cikti-sozlesmesi/README.md). Ana analiz korunur; yeni ek yalnız Python. SPSS yürütme veya bağımsız hakemlik iddiası yoktur.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b22/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
