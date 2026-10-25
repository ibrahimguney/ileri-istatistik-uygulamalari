# Bölüm 2 — Betimsel istatistik

## Kaynak
Cortez, P. (2008). Student Performance [Veri seti]. UCI Machine Learning Repository.
DOI: 10.24432/C5TG7T. CC BY 4.0.
https://archive.ics.uci.edu/dataset/320/student+performance
https://creativecommons.org/licenses/by/4.0/

Bölüm 12'nin `../b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv` arşivi
kullanılır. İlk 80 Portekizce dersi kaydı, tamamı GP okulundan; kaynak sıra,
school, G1 ve G3 alanları. Notlar 0–20; G1 birinci dönem, G3 yıl sonudur.
Kaynağın 649 kaydının tümü veya temsili örneklem değildir. Türkiye verisi değildir.
Kaynak atfı, aktarım ve lisans ayrıntıları Bölüm 12'de korunur.
Normalize tek terminal LF SHA-256:
`51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9`.
Kaynak hash'i, dosyanın değişmediğini denetler; uzaktaki kaynakla eşitliği kanıtlamaz.

## Çalıştırma
Kitap kökünden:
```sh
python uygulamalar/b02-betimsel-istatistik/analiz.py
```
NumPy/pandas/matplotlib kullanılır (bkz. `uygulamalar/requirements.txt`).
`analiz.R` temel R ile bağımsız hesap betiğidir ve Python ile aynı sonuçları verir.
`analiz.sps` Python'un ürettiği `notlar.csv` dosyasını okur.

## Hesaplama sözleşmesi
- Ana analiz 80 kaydın tamamını içerir. İlk satır G1=0, G3=11; eksik değildir.
- Varyans/kovaryans `ddof=1`, bölen 79. Kapalı 80 kayıt için bölen 80 varyansı ayrıca verilir.
- Çeyrekler NumPy `method="linear"` = R `type=7`; elle ara değer formülüyle doğrulanır.
- Kutu grafikleri `bxp` ile aynı çeyrekleri kullanır. Bıyıklar 1.5 IQR sınırları
  içindeki gözlenen uçlardır; sınır değerlerinin kendisi değildir.
- Ham MAD kullanılır; 1.4826 çarpanı yok. R `mad(..., constant=1)` ile eşleştirilir.
- Yarı-medyan yöntemi yalnız bu çift n=80 veride ilk/son 40'ın medyanıdır;
  bütün n'ler için genel bir kutu algoritması olarak sunulmaz.
- CV sayıları yalnız keyfî sıfırın etkisini gösteren aritmetik karşı örnektir;
  notlar için göreli yetenek değişkenliği diye yorumlanmaz.
- İlk satır dışlama yalnız duyarlılık kopyasıdır; ana kayıtlardan hiçbiri silinmez.
- Korelasyon, kovaryans ve dönem farkı aynı 80 eşleşmiş kayıttadır. Güven aralığı,
  bootstrap, normallik veya anlamlılık testi Python'da yapılmaz.

## Çıktılar ve beklenen sonuçlar
`notlar.csv`: gerçek 80 kayıt ve fark_G3_G1. `sonuclar/betimsel_ozet.csv`:
konum/yayılım; `frekanslar.csv`: 0–20 puan frekansları; `ceyrek_yontemleri.csv`:
tip 7 ve yarı-medyan tanımı; `isaretli_kayitlar.csv`: taranan kayıtlar;
`duyarlilik_satir1_haric.csv`: 79-kayıt kopyası; `ozet.json`: bütün hesaplar,
sürüm ve kaynak bilgileri. Şekil `../../assets_figures/b02-gercek-betimsel.pdf`.

G1: ortalama 12.175, s=2.427558, Q1=11, Q3=13.25, IQR=2.25.
G3: ortalama 12.6375, s=2.026681, Q1=11, Q3=14, IQR=3.
G3 SS=324.4875, varyans (n−1)=4.107437, varyans (n)=4.056094.
İki medyan da 12, ham MAD'ler 1; modlar G1=13 ve G3=12.
G1 tip 7 sınırları 7.625/16.625, bıyıklar 8/16; işaretler 1,16,48,61.
Yarı-medyan Q3=13.5, üst sınır 17.25; yalnız 1. kayıt işaretlenir.
G3 sınırları 6.5/18.5, bıyıklar 7/17; işaret yoktur.

Kovaryans 3.456646, r=.702586. Fark ortalaması .4625, s=1.757038;
32 artış, 31 eşitlik, 17 azalış. 79-kayıt duyarlılığı G1 ortalama 12.329114,
s=2.011005 ve r=.793762 verir. Bunlar silme gerekçesi değildir.
İlk60/son20 ortalamaları 12.783333 ve 12.2; kişi-sayılı birleşim 12.6375,
eşit ağırlıklı birleşim 12.491667. Ağırlıklar örnekleme ağırlığı değildir.

## Yazılımlar arası karşılaştırma
SPSS EXAMINE `HAVERAGE` burada açıkça istenir ama tip 7 diye etiketlenmez;
varsayılan çeyrek/kutu yöntemleri farklı olabilir. G1'in sıralı 60/61 değerleri
13/14'tür; tip 7 Q3=13+.25*(14−13)=13.25 elle yeniden hesaplanabilir.
SPSS CORRELATIONS çıktıdaki p değerleri kitapta hesaplanmış veya yorumlanmış
sonuç olarak sunulmaz; bu bölüm betimsel katsayıyı kullanır. Filtre, ağırlık ve
split-file kapatılır; G1=0 eksik tanımlanmaz. TEMPORARY dışlamalar kalıcı değildir.
R/SPSS betiklerinin bulunması bu yazılımların çalıştırıldığı anlamına gelmez.

İç denetimler: frekans-ağırlıklı ortalama, açık SS hesabı, elle tip 7,
NumPy kovaryans/korelasyon, fark varyansı özdeşliği, ölçek/öteleme dönüşümleri.
Küçük alıştırma dizileri ve +%10/−%10 çarpanları açıkça kurgusal örneklerdir;
gerçek notlarla karıştırılmaz. İleri 3 korelasyonu 0.9647638212'dir.

Yöntem belgeleri, erişim 6 Eylül 2026:
- https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
- https://stat.ethz.ch/R-manual/R-devel/library/stats/html/quantile.html
- https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm
- https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/coefvari.htm
- https://www.ibm.com/docs/en/spss-statistics/30.0.0?topic=examine-percentiles-subcommand-command

## Revizyon 6 — Özet seçimi

`ozet-secimi/` ek modülü ortalama/medyan/kırpılmış ortalama hedeflerini, ampirik
dağılım ve eşik eşitsizliklerini, tip 7–ters ampirik çeyrek ayrımını ve eşleşmiş
farkların dağılımını inceler. Ana veri ve yukarıdaki analiz değişmedi. Üç yeni
matematik/girdi denetimi Python'da geçti; bu ek için R/SPSS kodu hazırlanmadı.
Komut ve sınırlar ek modül README'sindedir.
