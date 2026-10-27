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

## Yeni ileri uygulama: birleştirme denetimi ve bilgi sınırı

Veri sözleşmesi, eksik nedeninin saklanması, gerçek A/C puanlarında birleşim
paydaları ve tahmin değerlendirmesinde ön işlem sızıntısı genişletildi.
T1–T3 görevleri ve çözümleri ilgili dosyalardadır.

[Açıklama ve komutlar](../../uygulamalar/b03-veri-hazirlama/birlesim-denetimi/README.md) ·
[Python kodu](../../uygulamalar/b03-veri-hazirlama/birlesim-denetimi/analiz.py) ·
[Sonuçlar](../../uygulamalar/b03-veri-hazirlama/birlesim-denetimi/sonuclar/ozet.json).
Mevcut çoklu atama simülasyonu korunmuştur; yeni ek yalnız Python'da sınandı.
Kaynaklar: https://doi.org/10.18637/jss.v059.i10 ; https://doi.org/10.1002/sim.4067 .

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b03/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
