# Bölüm 19 — Doğrulayıcı Faktör Analizi

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- DFA modelinde serbest parametreleri ve sıfır kısıtlarını açıkça tanımlar;

- ölçeklendirme, tanımlanabilirlik ve serbestlik derecesini ayırır;

- AFA’da keşfedilen yapıyı dokunulmamış yarıda sınamanın mantığını ve sınırını açıklar;

- yükler, standart hatalar, faktör ilişkisi ve yerel artıklarla birlikte uyum indekslerini yorumlar;

- AVE ve bileşik güvenirlik hesabının model ve puan tanımına bağlılığını gösterir;

- önceden yazılmış alternatif ile veriye bakarak yapılan modifikasyonu ayırır;

- yeniden üretilebilir bir DFA raporu ve bağımsız doğrulama planı hazırlar.

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
python bolumler/b19/analiz.py
```

Asıl analiz: [uygulamalar/b19-dogrulayici-faktor/analiz.py](../../uygulamalar/b19-dogrulayici-faktor/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b19-dogrulayici-faktor/README.md).
R betiği: [analiz.R](../../uygulamalar/b19-dogrulayici-faktor/analiz.R).
SPSS sözdizimi: bu bölüm için ayrı dosya yok; varsa Amos rehberini uygulama klasöründe inceleyin.

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 22: puan hedefi ve delta belirsizliği

[Uygulama açıklaması](../../uygulamalar/b19-dogrulayici-faktor/puan-guvenirligi/README.md) ·
[Python kodu](../../uygulamalar/b19-dogrulayici-faktor/puan-guvenirligi/analiz.py) ·
[Sonuçlar](../../uygulamalar/b19-dogrulayici-faktor/puan-guvenirligi/sonuclar/ozet.json).
Eski ana analizler ve gerçek IPIP verisi ve bölme korunur; yeni ek yalnız Python.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/pedagojik-22/bolumler/b19/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.

## Öğrenme ve teslim rotası

Üç çekirdek kazanım, ileri rota ve Ç1 sorusu [görevlerde](GOREVLER.md),
yerel puanların ortak çatıyla bağlantısı [RUBRIK.md](RUBRIK.md) içindedir.
Colab kararı ve kısa savunma çıktı ZIP’ine ayrıca kaydedilir.
[Ortak ön koşul haritası](../../ON-KOSULLAR.md) temel okuma sırasını gösterir.
