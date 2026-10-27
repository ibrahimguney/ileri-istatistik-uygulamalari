# Bölüm 1 — İstatistiksel Düşünme: Sorudan Kanıta

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- araştırma sorusu, hedef anakütle, örnekleme çerçevesi ve eldeki kayıtları birbirinden ayırır;

- gözlem birimi, değişken, ölçüm ve satır sayısını doğru tanımlar;

- sayısal kod ile sayısal ölçümü; nominal, ordinal, aralık ve oran düzeylerini ayırt eder;

- basit rastgele, sistematik, tabakalı ve küme örneklemenin seçim mantığını açıklar;

- frekans ve yüzdeyi doğru payda üzerinden hesaplar;

- veri türüne uygun grafik seçer ve kaynak sınırlarını belirten kısa bir rapor yazar.

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
python bolumler/b01/analiz.py
```

Asıl analiz: [uygulamalar/b01-istatistiksel-mekanizma/analiz.py](../../uygulamalar/b01-istatistiksel-mekanizma/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b01-istatistiksel-mekanizma/README.md).
R betiği: [analiz.R](../../uygulamalar/b01-istatistiksel-mekanizma/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b01-istatistiksel-mekanizma/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Yeni ileri uygulama: hedef parametre ve tasarım belirsizliği

Hedef parametre, kestirici ve kestirim ayrımı; SRS ve sistematik seçimde tam
tasarım varyansı; 20.000 tekrarlı deney ile Monte Carlo hatası ayrımı eklendi.
Yeni T1–T3 görevleri ve yanıtları yukarıdaki dosyalardadır.

[Açıklama ve komutlar](../../uygulamalar/b01-istatistiksel-mekanizma/tasarim-belirsizligi/README.md) ·
[Python kodu](../../uygulamalar/b01-istatistiksel-mekanizma/tasarim-belirsizligi/analiz.py) ·
[Sonuçlar](../../uygulamalar/b01-istatistiksel-mekanizma/tasarim-belirsizligi/sonuclar/ozet.json).
Bu ek yalnız Python'da sınandı; R/SPSS eşdeğeri hazırlanmadı.

Kuramsal dayanaklar: Lundberg, Johnson ve Stewart (2021),
https://doi.org/10.1177/00031224211004187 ; Meng (2018),
https://doi.org/10.1214/18-AOAS1161SF . Kaynak künyeleri ve yazar özetleri kontrol edildi.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b01/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.

## Öğrenme ve teslim rotası

Üç çekirdek kazanım, ileri rota ve Ç1 sorusu [görevlerde](GOREVLER.md),
yerel puanların ortak çatıyla bağlantısı [RUBRIK.md](RUBRIK.md) içindedir.
Colab kararı ve kısa savunma çıktı ZIP’ine ayrıca kaydedilir.
[Ortak ön koşul haritası](../../ON-KOSULLAR.md) temel okuma sırasını gösterir.
