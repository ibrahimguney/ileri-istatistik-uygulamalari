# Bölüm 13 — Çoklu ve Lojistik Regresyon

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- çoklu doğrusal regresyonun basit regresyondan farkını açıklar,

- kısmi regresyon katsayılarını ve standartlaştırılmış katsayıları yorumlar,

- çoklu doğrusal regresyon varsayımlarını değerlendirir,

- ikili lojistik regresyonun olasılık ve odds mantığını açıklar,

- odds oranı, sınıflandırma ve model uyumu çıktılarının temel yorumunu yapar,

- gerçek veride yaş için düzeltilmiş not katsayısını ve değişim testini hesaplar,

- olay tanımını, olasılık eşiğini ve eğitim performansını birbirinden ayırır,

- gözlem etkisini, belirsizliği ve veri seçimini belgeleyerek iki modeli raporlar.

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
python bolumler/b13/analiz.py
```

Asıl analiz: [uygulamalar/b13-coklu-lojistik/analiz.py](../../uygulamalar/b13-coklu-lojistik/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b13-coklu-lojistik/README.md).
R betiği: [analiz.R](../../uygulamalar/b13-coklu-lojistik/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b13-coklu-lojistik/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
