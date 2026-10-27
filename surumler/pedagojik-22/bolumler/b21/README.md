# Bölüm 21 — Yapısal Eşitlik Modeli

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- ölçüm denklemlerini gizil değişkenler arasındaki yapısal denklemlerden ayırır;

- gösterge hatası, yapısal artık, toplam gizil varyans ve $R^2$’yi ilişkilendirir;

- marker ölçeklemesiyle standartlaştırılmış katsayıların farkını açıklar;

- serbest parametre sayısını, yerel tanımlanabilirliği ve tahmin denetimlerini yorumlar;

- aynı kovaryansı üreten modellerden nedensel yön seçilemeyeceğini gösterir;

- gizil aracılık modelinde dolaylı etkiyi bütün YEM’i yeniden kestiren bootstrap ile raporlar;

- gerçek veri, model varsayımı ve nedensel iddia arasındaki sınırı açıkça yazar.

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
python bolumler/b21/analiz.py
```

Asıl analiz: [uygulamalar/b21-yapisal-esitlik/analiz.py](../../uygulamalar/b21-yapisal-esitlik/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b21-yapisal-esitlik/README.md).
R betiği: [analiz.R](../../uygulamalar/b21-yapisal-esitlik/analiz.R).
SPSS sözdizimi: bu bölüm için ayrı dosya yok; varsa Amos rehberini uygulama klasöründe inceleyin.

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 24: ölçüm ve yapısal varsayım duyarlılığı

[Uygulama açıklaması](../../uygulamalar/b21-yapisal-esitlik/olcum-yapi-duyarliligi/README.md) ·
[Python kodu](../../uygulamalar/b21-yapisal-esitlik/olcum-yapi-duyarliligi/analiz.py) ·
[Sonuçlar](../../uygulamalar/b21-yapisal-esitlik/olcum-yapi-duyarliligi/sonuclar/ozet.json).
Eski ana analizler ve gerçek IPIP verisi ve bölme korunur; yeni ek yalnız Python.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/pedagojik-22/bolumler/b21/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.

## Öğrenme ve teslim rotası

Üç çekirdek kazanım, ileri rota ve Ç1 sorusu [görevlerde](GOREVLER.md),
yerel puanların ortak çatıyla bağlantısı [RUBRIK.md](RUBRIK.md) içindedir.
Colab kararı ve kısa savunma çıktı ZIP’ine ayrıca kaydedilir.
[Ortak ön koşul haritası](../../ON-KOSULLAR.md) temel okuma sırasını gösterir.
