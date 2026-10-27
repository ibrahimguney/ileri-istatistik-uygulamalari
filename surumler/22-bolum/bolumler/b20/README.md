# Bölüm 20 — Ölçme Değişmezliği

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- grup karşılaştırmasının neden ölçme değişmezliği varsayımına dayandığını açıklar;

- biçimsel, metrik, skaler ve katı değişmezlik düzeylerini ve her birinin izin verdiği karşılaştırmayı ayırır;

- ortalama yapılı çok gruplu DFA’yı tanımlar; ölçekleme ve serbestlik derecesini hesaplar;

- ki-kare fark testi ile $\Delta$CFI ve $\Delta$RMSEA ölçütlerini birlikte yorumlar;

- kısmi değişmezliği önceden belirlenmiş bir kuralla kurar ve sınırlarını raporlar;

- gizil ortalama farklarını gözlenen ölçek puanı farklarıyla karşılaştırır.

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
python bolumler/b20/analiz.py
```

Asıl analiz: [uygulamalar/b20-olcme-degismezligi/analiz.py](../../uygulamalar/b20-olcme-degismezligi/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b20-olcme-degismezligi/README.md).
R betiği: [analiz.R](../../uygulamalar/b20-olcme-degismezligi/analiz.R).
SPSS sözdizimi: bu bölüm için ayrı dosya yok; varsa Amos rehberini uygulama klasöründe inceleyin.

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 23: çıpa duyarlılığı ve gizil fark

[Uygulama açıklaması](../../uygulamalar/b20-olcme-degismezligi/capa-duyarliligi/README.md) ·
[Python kodu](../../uygulamalar/b20-olcme-degismezligi/capa-duyarliligi/analiz.py) ·
[Sonuçlar](../../uygulamalar/b20-olcme-degismezligi/capa-duyarliligi/sonuclar/ozet.json).
Eski ana analizler ve gerçek IPIP verisi ve bölme korunur; yeni ek yalnız Python.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b20/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
