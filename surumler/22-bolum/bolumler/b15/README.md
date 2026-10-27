# Bölüm 15 — Aracılık ve Düzenleyicilik Analizleri

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- aracılık ve düzenleyicilik kavramlarını birbirinden ayırır,

- doğrudan, dolaylı ve toplam etki mantığını açıklar,

- etkileşim terimi üzerinden düzenleyici etkiyi yorumlar,

- bootstrap güven aralığı yaklaşımının aracılık analizindeki önemini açıklar,

- merkezleme ve basit eğim analizinin ne işe yaradığını belirtir,

- aracılık ve düzenleyicilik sonuçlarını akademik biçimde raporlar.

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
python bolumler/b15/analiz.py
```

Asıl analiz: [uygulamalar/b15-aracilik-duzenleyicilik/analiz.py](../../uygulamalar/b15-aracilik-duzenleyicilik/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b15-aracilik-duzenleyicilik/README.md).
R betiği: [analiz.R](../../uygulamalar/b15-aracilik-duzenleyicilik/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b15-aracilik-duzenleyicilik/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 18: tanımlama, duyarlılık ve bölgeler

[Uygulama açıklaması](../../uygulamalar/b15-aracilik-duzenleyicilik/duyarlilik-bolgeler/README.md) ·
[Python kodu](../../uygulamalar/b15-aracilik-duzenleyicilik/duyarlilik-bolgeler/analiz.py) ·
[Sonuçlar](../../uygulamalar/b15-aracilik-duzenleyicilik/duyarlilik-bolgeler/sonuclar/ozet.json).
Eski ana analizler/simülasyon korunur; yeni ek yalnız Python.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b15/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
