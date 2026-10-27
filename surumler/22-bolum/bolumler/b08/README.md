# Bölüm 8 — Tekrarlı Ölçümler ve Karma Desenler

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- aynı kişinin tekrar ölçülmesinin bağımsızlık varsayımını nasıl değiştirdiğini açıklar;

- tekrarlı ölçümler ANOVA’sında toplam değişkenliği kişi, zaman ve hata bileşenlerine ayırır;

- küreselliği tanımlar; Mauchly testini, Greenhouse–Geisser ve Huynh–Feldt düzeltmelerini yorumlar;

- tek değişkenli, çok değişkenli (Hotelling $T^2$) ve odaklı karşıtlık yaklaşımlarını karşılaştırır;

- kısmi ve genelleştirilmiş eta-kareyi ayırır;

- arası–içi (karma) desende etkileşimi, basit etkileri ve büyüme hızlarını raporlar;

- karma etkiler modelinin tekrarlı ölçümler ANOVA’sıyla ilişkisini ve üstünlüklerini açıklar.

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
python bolumler/b08/analiz.py
```

Asıl analiz: [uygulamalar/b08-tekrarli-olcumler/analiz.py](../../uygulamalar/b08-tekrarli-olcumler/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b08-tekrarli-olcumler/README.md).
R betiği: [analiz.R](../../uygulamalar/b08-tekrarli-olcumler/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b08-tekrarli-olcumler/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Yeni ileri uygulama: eksik izlem ve aynı model

Ayrı öğretim maskesinde tam/mevcut/tam kişi aynı eğim modeli, küçük örneklem
çıkarım sınırı ve dört yaşlık Holm ailesi eklendi. Yeni T1–T3 görevleri/çözümleri var.

[Açıklama ve komutlar](../../uygulamalar/b08-tekrarli-olcumler/eksik-izlem/README.md) ·
[Python kodu](../../uygulamalar/b08-tekrarli-olcumler/eksik-izlem/analiz.py) ·
[Sonuçlar](../../uygulamalar/b08-tekrarli-olcumler/eksik-izlem/sonuclar/ozet.json).
Özgün arşivde eksik yok; maskeli sonuçlar model üstünlüğü/gerçek MAR testi değildir.
Yeni ek yalnız Python; R/SPSS, MNAR veya küçük-örneklem sd düzeltmesi yok.
Kaynak: https://doi.org/10.1001/archpsyc.61.3.310 .

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b08/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
