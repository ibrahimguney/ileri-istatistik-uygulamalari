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

## Yeni ileri uygulama: Welch kalibrasyonu ve Yuen duyarlılığı

Dengesiz gruplarda normal null modelinin hata oranı ve gerçek doz1 verisinde
kırpılmış ortalama için Yuen eklendi. T1–T3 görevleri ve çözümleri ilgili dosyalardadır.

[Açıklama ve komutlar](../../uygulamalar/b06-parametrik-testler/welch-saglamlik/README.md) ·
[Python kodu](../../uygulamalar/b06-parametrik-testler/welch-saglamlik/analiz.py) ·
[Sonuçlar](../../uygulamalar/b06-parametrik-testler/welch-saglamlik/sonuclar/ozet.json).
Ana Welch sıradan ortalama farkını, Yuen kırpılmış ortalama farkını hedefler.
Yeni ek yalnız Python'da sınandı; R/SPSS eşdeğeri yok.
Kaynak: https://doi.org/10.1093/biomet/61.1.165 .

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b06/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.

## Öğrenme ve teslim rotası

Üç çekirdek kazanım, ileri rota ve Ç1 sorusu [görevlerde](GOREVLER.md),
yerel puanların ortak çatıyla bağlantısı [RUBRIK.md](RUBRIK.md) içindedir.
Colab kararı ve kısa savunma çıktı ZIP’ine ayrıca kaydedilir.
[Ortak ön koşul haritası](../../ON-KOSULLAR.md) temel okuma sırasını gösterir.
