# Bölüm 18 — Faktör Analizi

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- temel bileşenler analizi (PCA) ile açıklayıcı faktör analizini (AFA) ayırır;

- keşif ve doğrulama için veriyi önceden ikiye ayırmanın mantığını açıklar;

- aynı kayıtlar üzerinde korelasyon, kısmi korelasyon, KMO ve Bartlett hesabını izler;

- özdeğer kuralını iki paralel analiz sürümü ve içerik bilgisiyle karşılaştırır;

- temel eksenlerle faktör çıkarmayı, ortak varyans, özgüllük ve Heywood durumunu açıklar;

- eğik rotasyonda örüntü, yapı ve faktör korelasyon matrislerini birlikte okur;

- artık korelasyonları ve zayıf maddeleri raporlayıp ayrılmış yarıda sınanacak bir DFA planı kurar.

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
python bolumler/b18/analiz.py
```

Asıl analiz: [uygulamalar/b18-faktor-analizi/analiz.py](../../uygulamalar/b18-faktor-analizi/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b18-faktor-analizi/README.md).
R betiği: [analiz.R](../../uygulamalar/b18-faktor-analizi/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b18-faktor-analizi/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 21: faktör sayısı ve puan belirsizliği

[Uygulama açıklaması](../../uygulamalar/b18-faktor-analizi/puan-belirsizligi/README.md) ·
[Python kodu](../../uygulamalar/b18-faktor-analizi/puan-belirsizligi/analiz.py) ·
[Sonuçlar](../../uygulamalar/b18-faktor-analizi/puan-belirsizligi/sonuclar/ozet.json).
Eski ana analizler, gerçek IPIP verisi ve bölme korunur; yeni ek yalnız Python.
