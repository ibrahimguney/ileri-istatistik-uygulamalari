# Bölüm 3 ileri uygulaması — sürekli yanıtta çoklu atama

Bu paket, gerçek `bfi` maddelerine atama yapmaz. Ayrı bir simülasyonda tek sürekli
sonuç değişkeninin eksikliğini ve anakütle ortalamasının tahminini öğretir.
Normal regresyon ataması ordinal maddelere doğrudan önerilmez.

## Çalıştırma

Kitap kökünden, mevcut NumPy/SciPy/pandas ortamında:

```sh
python uygulamalar/b03-veri-hazirlama/coklu-atama/analiz.py
python uygulamalar/b03-veri-hazirlama/coklu-atama/dogrula.py
```

Ayrı bir çıktı klasörü için `analiz.py --output /istenen/yol` kullanılabilir.
Kod ağdan veri almaz veya paket kurmaz. Çıktılar kendi `sonuclar/` klasöründedir.
Kaynak BFI dosyası ve mevcut bölüm 3 hazırlama sonuçları değişmez.

## Tasarım ve hedef

240 kayıt için X~N(0,1), Y=50+8X+e, e~N(0,6²). Hedef üretim anakütlesinin Y
ortalaması, yani 50'dir. Tam simülasyonun örneklem ortalaması bu hedefin kendisi
veya gerçek araştırmada ulaşılabilir bir bilgi değildir; öğretim karşılaştırmasıdır.

Y eksikliği olasılığı expit(-0.4+0.9X)'tir. Maskeleme için ayrı rastgele sayı
akışı kullanılır. Böylece X'e koşullandığımızda eksiklik Y'ye ayrıca bağlı değildir:
MAR, üretim tasarımından bilinir; bir mekanizma testiyle saptanmış değildir.
Veri, maske ve atama tohumları sırasıyla 20261025, 20261026, 20261027'dir.
104/240 Y eksiktir (%43,33); X tüm kayıtlarda gözlenir.

## Atama modeli

Y|X için sabit terimli, doğrusal, normal ve eş varyanslı regresyon kullanılır.
Model gözlenen Y'lerden tahmin edilir. Önsel p(beta,sigma²) ∝ 1/sigma² altında:

1. nu=n_gözlenen−2 ve RSS gözlenen regresyonundan hesaplanır.
2. Her atamada sigma²=RSS/chi²_nu çekilir.
3. beta, N(beta_OLS, sigma²(X'X)^−1) dağılımından çekilir.
4. Y eksikleri N(X_eksik beta, sigma²)'den üretilir; gözlenenler değişmez.

Bu özel tek-değişkenli modelde posterior öngörü çekilişleri bağımsızdır;
MICE zinciri veya burn-in yoktur. Çok değişkenli/ordinal/kümeli gerçek verilere
aynen taşınmaz. Katsayıları sabit tutup yalnız hata eklemek, burada uygulanan
parametre belirsizliğini taşıyan çoklu atama ile aynı değildir.

## Birleştirme ve raporlama

Her tamamlanmış dosyada Q_j=ortalama(Y), U_j=s_j²/n hesaplanır. Birincil m=200:

- Qbar=49.467076; Ubar=.447825; B=.162112.
- T=Ubar+(1+1/m)B=.610748; SH=.781504.
- Barnard–Rubin sd=163.627; %95 t aralığı [47.923944,51.010208].
- lambda=.266759 toplam varyansa atamalar arası katkının oranıdır. Eksik kayıt
  oranı veya genel anlamda FMI ile özdeşleştirilmemelidir.
- Ortalama tahmininin yaklaşık Monte Carlo SH'si sqrt(B/m)=.028470'tir.

m=1000 kontrolünde ortalama49.481999, SH=.777665, Monte Carlo SH=.012591 olur.
200 sihirli yeterlik sınırı değildir; hedeflenen raporlama hassasiyetine göre
çekiliş sayısı ve Monte Carlo hatası değerlendirilir. Bu örnekte 200'lük seri,
1000'lik serinin ilk 200 bağımsız çekilişidir.

`yontemler.csv`: tam simülasyon karşılaştırması, yalnız gözlenen yanıtlar,
ortalama tek atama ve çoklu atama. Tek atamanın naif SH'si belirsizliği küçültür.
MAR altında tam kayıt analizinin her hedef için mutlaka yanlı olduğu söylenmez;
burada yalnız gözlenen Y ortalaması, X'e bağlı seçilimi hesaba katmaz.

## MNAR için delta duyarlılığı

Aynı MAR atamalarının yalnız eksik Y hücrelerine sabit delta=−6,0,+6 eklenir.
Bunlar veriden tahmin edilmiş düzeltmeler değil, Y'nin özgün biriminde varsayımsal
sapmalardır. Uygulamada değerler konu bilgisiyle gerekçelendirilmelidir. Ortalama
kayması tam olarak delta×104/240'tır; delta=±6 için ±2.6. Aralıklar verilen sabit
deltaya koşulludur; delta belirsizliği veya MAR/MNAR'ı ayırt eden bir test değildir.

## Dosyalar ve denetim sınırı

- `veri_gozlenen.csv`: yalnız id, X ve gözlenen/eksik Y; atamanın girdisi.
- `veri_tam_simulasyon.csv`: gizlenmeden önceki Y ve maske üretimi; atamaya girmez.
- `cekimler.csv`: 1000 atamanın katsayı/varyans çekilişleri, Q_j ve U_j.
- `yontemler.csv`, `delta_duyarlilik.csv`, `ozet.json`, `veri_sozlugu.csv`.
- `dogrula.py`: el hesabı fikstürü, MICE'nin yayımladığı bağımsız sd biçimi,
  geçersiz atamaların reddi ve gözlenen değerlerin korunması.

Tek simülasyon yanlılık veya güven aralığı kapsama çalışması değildir. FIML,
MICE zinciri, ordinal atama ve R/SPSS ile sayısal çapraz doğrulama yapılmadı.
R'deki MICE belgeleri yalnız kaynak ve sd formülü kontrolü için incelendi.

Kaynaklar: Rubin (1987), DOI10.1002/9780470316696; Barnard ve Rubin (1999),
DOI10.1093/biomet/86.4.948; Little ve Rubin (2019). MICE `pool` ve
`barnard.rubin` kaynak belgeleri: https://github.com/amices/mice (kontrol:25 Ekim 2026).
