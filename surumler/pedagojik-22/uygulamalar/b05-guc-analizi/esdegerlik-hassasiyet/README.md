# Bölüm 5 — Eşdeğerlik gücü ve aralık genişliği olasılığı

İki bağımsız normal, ortak varyanslı ve eşit büyüklüklü grup için öğretim eki.
Ana güç analizi ve sleep arşivi değiştirilmez. Yeni gerçek kişi/pilot verisi yoktur.

Kitap kökünden; öğrenci deposunda `surumler/22-bolum/` klasöründen:

```sh
python uygulamalar/b05-guc-analizi/esdegerlik-hassasiyet/dogrula.py
python uygulamalar/b05-guc-analizi/esdegerlik-hassasiyet/analiz.py
```

Ortak NumPy/pandas/SciPy bağımlılıkları kullanılır. Üst ana modül yalnız `power_t`
karşılaştırması için yüklenir; `main` çağrılmaz. Ek yalnız Python'da doğrulandı;
R/SPSS eşdeğeri veya G*Power çalıştırma kanıtı yoktur.

## TOST gücü

Delta=5 puan, sigma=10, alfa=.05. Gerçek fark 0 varsayımında minimum70 kişi/grup,
önceki69'da güç .798512, 70'te .805931. Gerçek fark2.5 için 198'de .799080,
199'da .800840; minimum199 kişi/grup. Toplamlar140 ve398'dir.

Normal ortalama farkı ile bağımsız ki-kare pooled varyans kullanılır. Varyansa
koşullu normal aralık olasılığı, ki-kare CDF'sinin tersinden uniform olasılık
ölçeğinde sayısal bütünleştirilir. İki TOST bileşeninin güçleri çarpılmaz.
Sınırlar yalnız öğretim tercihleridir; klinik/alan standardı değildir.

n64'te fark testinin gerçek fark5 için gücü .801460; TOST'un gerçek fark0/2.5
için güçleri .757328/.400835. Farklı test/alternatif varsayımları karıştırılmamalıdır.
TOST'un gerçek fark sınırında .80 güçlü olması beklenmez; orada H0 doğrudur.

## Aralık genişliği

%95 Student fark aralığında rastgele yarı genişlik H için sabit sigma10 altında
P(H<=2) ki-kare CDF'sinden hesaplanır. n194'te .530073; n210'da .893633,
n211'de .906617. En az .90 olasılığı sağlayan minimum211 kişi/grup, toplam422.
Bu olasılık aralık kapsaması, test gücü veya bilinmeyen sigma için önsel üzerinden
bütünleştirilmiş Bayesçi güvence değildir. Kayıp modeli de bütünleştirilmemiştir.

## Denetim ve çıktılar

Beş test: TOST işaret/birim simetrisi ve null sınırı, bilgi/sınır etkisi,
genişlik CDF özdeşliği, tamsayı araması ve geçersiz girdiler. Ana kod minimum n
ile önceki n'yi yeniden denetler. Sayısal integrale ait hata tahmini sınanır.

Ek olarak 100.000 yeterli istatistik çekilişi kullanılır (NumPy default_rng,
seed20261025). Normal ortalama farkı ve ki-kare varyans bağımsız üretilir;
ham kişi tablosu üretilmez. n64'te gerçek fark0/2.5 için MC güçleri .75568/.39944;
MC SH .001356/.001550. n211 genişlik olasılığı MC=.90646. Bunlar gerçek veri
sonucu veya varsayım kanıtı değildir. Daha çok tekrar sadece MC hatasını azaltır.

`sonuclar/esdegerlik-planlari.csv`, `genislik-plani.csv`, `MC-denetimi.csv`,
`ozet.json` üretilir. Ortalama etki, sigma, sınırlar ve alfa varsayımsaldır.
Kaynaklar: Lakens (2017), https://doi.org/10.1177/1948550617697177 ;
Maxwell, Kelley ve Rausch (2008), https://doi.org/10.1146/annurev.psych.59.103006.093735 .
