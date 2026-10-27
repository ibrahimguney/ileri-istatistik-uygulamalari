# Bölüm 2 — Betimsel İstatistik

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- ortalama, medyan ve modu aynı veride hesaplayıp farklı sorulara yanıt verdiklerini açıklar;

- varyans bölenini, standart sapmayı ve standart hatayı birbirinden ayırır;

- çeyrek algoritmasını belirterek IQR, tarama sınırları ve kutu grafiğini üretir;

- uç kayıtların etkisini ana veriyi değiştirmeden duyarlılık analiziyle gösterir;

- ağırlıklı/geometrik ortalamanın ve varyasyon katsayısının kullanım koşullarını belirtir;

- aynı kayıtlardaki iki değişkenin kovaryansını, korelasyonunu ve fark dağılımını yorumlar.

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
python bolumler/b02/analiz.py
```

Asıl analiz: [uygulamalar/b02-betimsel-istatistik/analiz.py](../../uygulamalar/b02-betimsel-istatistik/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b02-betimsel-istatistik/README.md).
R betiği: [analiz.R](../../uygulamalar/b02-betimsel-istatistik/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b02-betimsel-istatistik/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Yeni ileri uygulama: özet seçimi ve ampirik dağılım

Ortalama/medyan/kırpılmış ortalama farklı hedeflerdir. Eşik oranında >= ve >
ayrımı, ters ampirik çeyrek–tip 7 ayrımı ve eşleşmiş fark grafiği eklendi.
Yeni T1–T3 görevleri ve çözümleri ilgili dosyalardadır.

[Açıklama ve komutlar](../../uygulamalar/b02-betimsel-istatistik/ozet-secimi/README.md) ·
[Python kodu](../../uygulamalar/b02-betimsel-istatistik/ozet-secimi/analiz.py) ·
[Sonuçlar](../../uygulamalar/b02-betimsel-istatistik/ozet-secimi/sonuclar/ozet.json).
Bu ek yalnız Python'da sınandı; R/SPSS eşdeğeri yok.

Kaynaklar: https://doi.org/10.1080/00031305.1996.10473566 ;
https://doi.org/10.1371/journal.pbio.1002128 .

## GitHub + Colab pilotu

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b02/colab.ipynb) · [Adım adım rehber](COLAB.md) · [Defteri indir](colab.ipynb).

Colab defteri bağımsız çalışır; tüm paketi bilgisayarınıza açmanız gerekmez. Veri
GitHub'ın sabit bir commit'inden alınır ve SHA256 ile doğrulanır. Mevcut
`calisma.ipynb` tam paketle yerel çalışma içindir; iki defterin amacı farklıdır.

## Öğrenme ve teslim rotası

Üç çekirdek kazanım, ileri rota ve Ç1 sorusu [görevlerde](GOREVLER.md),
yerel puanların ortak çatıyla bağlantısı [RUBRIK.md](RUBRIK.md) içindedir.
Colab kararı ve kısa savunma çıktı ZIP’ine ayrıca kaydedilir.
[Ortak ön koşul haritası](../../ON-KOSULLAR.md) temel okuma sırasını gösterir.
