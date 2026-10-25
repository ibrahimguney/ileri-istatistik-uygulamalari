# Bölüm 4 — Hipotez Testi

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- araştırma hedefini, parametreyi ve sıfır hipotezini açıkça tanımlar;

- test istatistiğini sıfır hipotezi altındaki referans dağılımla ilişkilendirir;

- tek/iki yönlü p değerini, anlamlılık düzeyini ve hata olasılıklarını ayırır;

- eşli ölçümlerde farkın standart hatasını ve güven aralığını hesaplar;

- istatistiksel anlamlılığı etki büyüklüğü, eşdeğerlik ve nedensellikten ayırır;

- çoklu deneme, yön seçimi ve durdurma kararlarının hata oranına etkisini gösterir.

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
python bolumler/b04/analiz.py
```

Asıl analiz: [uygulamalar/b04-hipotez-testi/analiz.py](../../uygulamalar/b04-hipotez-testi/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b04-hipotez-testi/README.md).
R betiği: [analiz.R](../../uygulamalar/b04-hipotez-testi/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b04-hipotez-testi/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.
