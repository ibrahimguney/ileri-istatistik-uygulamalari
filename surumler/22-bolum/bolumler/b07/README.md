# Bölüm 7 — Varyans Analizi (ANOVA)

Bu paket 22 bölümlük güncel kitap sırasına aittir. Eski 18 bölümlük sürümün
aynı numaralı klasörü farklı bir konu olabilir; iki sürümü karıştırmayın.

## Öğrenme hedefleri

Bu bölümün sonunda okuyucu:

- ANOVA’nın neden çoklu t-testlerine tercih edildiğini açıklar,

- tek yönlü ve iki yönlü ANOVA arasında uygun seçimi yapar,

- gruplar arası ve gruplar içi değişkenlik kavramlarını yorumlar,

- F istatistiği, $p$-değeri ve etki büyüklüğünü birlikte değerlendirir,

- anlamlı ANOVA sonucundan sonra uygun post-hoc yaklaşımı belirler,

- SPSS, R ve Python çıktılarında temel ANOVA tablolarını yorumlar,

- karşılaştırma ailesini tanımlar ve tekil/eşzamanlı aralıkları ayırır,

- etkileşim ile koşullu ortalama farklarını birlikte raporlar,

- aynı gerçek veriden kareler toplamlarını ve sonuçları yeniden üretir.

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
python bolumler/b07/analiz.py
```

Asıl analiz: [uygulamalar/b07-varyans-analizi/analiz.py](../../uygulamalar/b07-varyans-analizi/analiz.py).
Ayrıntılı paket belgesi: [uygulama README](../../uygulamalar/b07-varyans-analizi/README.md).
R betiği: [analiz.R](../../uygulamalar/b07-varyans-analizi/analiz.R).
SPSS sözdizimi: [analiz.sps](../../uygulamalar/b07-varyans-analizi/analiz.sps).

18. bölüm bölme dosyalarını üretir; 19–21. bölümler bu kaynakları kullanır.
Tüm paketi indirmeniz dosya yollarını ve gerekli ortak kaynakları korur.

## Doğrulama

[Bölüm kaydı](DOGRULAMA.json) Python, R ve SPSS/Amos durumlarını ayırır.
Dosyanın bulunması o yazılımda yürütme kanıtı değildir. [Beklenen sonuçlar](beklenen.json)
önceki sürümlenmiş sayısal dayanakları taşır; kod başarısız olunca bu dosyayı
sonuca uydurarak değiştirmeyin.

## Revizyon 25

[Yeni uygulama ve kapsamı](../../uygulamalar/b07-varyans-analizi/dengesiz-hedef/README.md). Ana analiz korunur; yeni ek yalnız Python. SPSS yürütme veya bağımsız hakemlik iddiası yoktur.

## Revizyon 25

[Yeni uygulama ve kapsamı](../../uygulamalar/b07-varyans-analizi/dengesiz-hedef/README.md). Ana analiz korunur; yeni ek yalnız Python. SPSS yürütme veya bağımsız hakemlik iddiası yoktur.

## Tarayıcıda Colab ile çalıştırma

[Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/22-bolum/bolumler/b07/colab.ipynb) · [Rehber](COLAB.md) · [Defter](colab.ipynb).

Sabit sürümdeki kaynaklar hash denetimiyle alınır. Ana analiz ve ileri ekler
yeniden yürütülür; sonuçlar referanslarla karşılaştırılır. Grafikler defterde
görünür ve sonuçlar ZIP olarak indirilebilir. Mevcut `calisma.ipynb` yerel paketle
çalışma içindir. Google Colab arayüzü ve Jupyter çekirdeği testleri ayrı kaydedilir.
