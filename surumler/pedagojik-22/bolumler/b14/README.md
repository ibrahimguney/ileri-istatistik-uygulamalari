# Bölüm 14 — Çok Değişkenli Varyans Analizi (MANOVA)

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- birden çok bağımlı değişkeni birlikte sınamanın ne zaman anlamlı, ne zaman gereksiz olduğunu ayırır;

- kareler ve çapraz çarpımlar (SSCP) matrislerini ve $\mathbf E^{-1}\mathbf H$ özdeğerlerini yorumlar;

- Wilks, Pillai, Hotelling–Lawley ve Roy istatistiklerini hesaplar ve aralarında seçim yapar;

- iki grup için Hotelling $T^2$ ve Mahalanobis uzaklığını tek değişkenli t-testleriyle karşılaştırır;

- çok değişkenli normallik, uç değer ve kovaryans eşitliği (Box M) varsayımlarını değerlendirir;

- anlamlı bir MANOVA’yı ayırma fonksiyonları ve düzeltilmiş tek değişkenli testlerle izler;

- dengesiz iki faktörlü MANOVA’da Tip II kareler toplamının anlamını açıklar.

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
python bolumler/b09/analiz.py
```

Asıl analiz: [uygulamalar/b09-manova/analiz.py](../../uygulamalar/b09-manova/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b09-manova/README.md).
R betiği: [analiz.R](../../uygulamalar/b09-manova/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b09-manova/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 12: hedef, birim ve birlikte belirsizlik

[Uygulama açıklaması](../../uygulamalar/b09-manova/hedef-aralik/README.md) ·
[Python kodu](../../uygulamalar/b09-manova/hedef-aralik/analiz.py) ·
[Sonuçlar](../../uygulamalar/b09-manova/hedef-aralik/sonuclar/ozet.json).
Ortak tersinir dönüşüm, Bonferroni/Hotelling aralıkları ve iki grup asimptotik
Wald hesabı. Eski ana kod/veri korunur; yeni ek yalnız Python.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/pedagojik-22/bolumler/b09/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.

## Öğrenme ve teslim rotası

Üç çekirdek kazanım, ileri rota ve Ç1 sorusu [görevlerde](GOREVLER.md),
yerel puanların ortak çatıyla bağlantısı [RUBRIK.md](RUBRIK.md) içindedir.
Colab kararı ve kısa savunma çıktı ZIP’ine ayrıca kaydedilir.
[Ortak ön koşul haritası](../../ON-KOSULLAR.md) temel okuma sırasını gösterir.
