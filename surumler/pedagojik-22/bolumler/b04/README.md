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

## Yeni ileri uygulama: eşdeğerlik ve çoklu karşılaştırma

TOST ile hedef/sınır/aralık eşleşmesi, belirsiz sonuç ile eşdeğerlik ayrımı ve
planlı ailede Holm düzeltmesi eklendi. T1–T3 görevleri/çözümleri ilgili dosyalardadır.

[Açıklama ve komutlar](../../uygulamalar/b04-hipotez-testi/esdegerlik-cokluk/README.md) ·
[Python kodu](../../uygulamalar/b04-hipotez-testi/esdegerlik-cokluk/analiz.py) ·
[Sonuçlar](../../uygulamalar/b04-hipotez-testi/esdegerlik-cokluk/sonuclar/ozet.json).
Sleep delta1/3 sınırları öğretim içindir; klinik standart veya gerçek önkayıt yok.
Holm p ailesi ayrı kurgudur. Ek yalnız Python'da sınandı; R/SPSS eşdeğeri yok.
Kaynak: Lakens (2017), https://doi.org/10.1177/1948550617697177 ; Holm (1979).

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/pedagojik-22/bolumler/b04/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.

## Öğrenme ve teslim rotası

Üç çekirdek kazanım, ileri rota ve Ç1 sorusu [görevlerde](GOREVLER.md),
yerel puanların ortak çatıyla bağlantısı [RUBRIK.md](RUBRIK.md) içindedir.
Colab kararı ve kısa savunma çıktı ZIP’ine ayrıca kaydedilir.
[Ortak ön koşul haritası](../../ON-KOSULLAR.md) temel okuma sırasını gösterir.
