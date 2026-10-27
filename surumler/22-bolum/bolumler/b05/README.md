# Bölüm 5 — Güç Analizi ve Örneklem Büyüklüğü Planlama

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- hedef parametreyi, önemli farkı ve planlamada kullanılan etkiyi ayırır;

- merkezi olmayan t dağılımından test gücünü hesaplar;

- grup başına kişi, toplam kişi ve tam çift sayısını doğru raporlar;

- tamsayı örneklem sonucunu bir önceki n’nin gücüyle denetler;

- pilot yayılımı, kayıp oranı ve kaynak sınırı için duyarlılık planı kurar;

- güç, hassasiyet ve yeterli kayıt kalma olasılığını birbirinden ayırır;

- modele uygun yazılım ayarlarıyla denetlenebilir örneklem gerekçesi yazar.

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
python bolumler/b05/analiz.py
```

Asıl analiz: [uygulamalar/b05-guc-analizi/analiz.py](../../uygulamalar/b05-guc-analizi/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b05-guc-analizi/README.md).
R betiği: [analiz.R](../../uygulamalar/b05-guc-analizi/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b05-guc-analizi/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Yeni ileri uygulama: eşdeğerlik gücü ve genişlik olasılığı

TOST gücünde sınır ile beklenen gerçek fark, %95 aralık kapsaması ile genişlik
olasılığı ayrıldı. T1–T3 görevleri ve çözümleri ilgili dosyalardadır.

[Açıklama ve komutlar](../../uygulamalar/b05-guc-analizi/esdegerlik-hassasiyet/README.md) ·
[Python kodu](../../uygulamalar/b05-guc-analizi/esdegerlik-hassasiyet/analiz.py) ·
[Sonuçlar](../../uygulamalar/b05-guc-analizi/esdegerlik-hassasiyet/sonuclar/ozet.json).
Varsayımsal bağımsız normal/eşit varyanslı gruplar; klinik sınır, gerçek pilot veya
kayıpla ortak güç hesabı yoktur. Ek yalnız Python'da sınandı; R/SPSS eşdeğeri yok.
Kaynak: https://doi.org/10.1146/annurev.psych.59.103006.093735 .

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b05/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
