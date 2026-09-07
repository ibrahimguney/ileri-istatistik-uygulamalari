# Bölüm 6 — Korelasyon

Bu bölümde korelasyon, yalnız iki değişken arasındaki tek bir katsayıyı hesaplama işlemi olarak değil, **ilişkinin yönünü, gücünü, biçimini, belirsizliğini ve tek tek kayıtların sonuca etkisini birlikte değerlendiren bir analiz süreci** olarak ele alınır.

Temel soru:

> Birinci dönem notu (G1) ile yıl sonu notu (G3) birlikte nasıl değişmektedir ve bu ilişki Pearson ile Spearman ölçüldüğünde ne kadar kararlıdır?

Bölüm 2'de kullanılan 80 kaydın ilk 60'ı ana analizdir. Son 20 kayıt ayrı bir öğrenci etkinliğidir; yeni veya bağımsız bir doğrulama örneklemi değildir. Veri tek okuldan alınmış sıralı bir alıntıdır ve temsili/rastgele örnek olarak yorumlanmamalıdır.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- korelasyon katsayısının yönünü ve büyüklüğünü yorumlayabilir,
- Pearson korelasyonunu merkezlenmiş çapraz çarpımlardan hesaplayabilir,
- bağlı değerlerde Spearman korelasyonunu ortalama sıralar üzerinden kurabilir,
- bağlı veride bağsız kısa sıra-farkı formülünün neden uygun olmadığını açıklayabilir,
- Pearson için klasik t testi ve yaklaşık Fisher güven aralığını hesaplayabilir,
- Pearson `r²` ile aynı kayıtlardaki sabit terimli basit OLS `R²` özdeşliğini gösterebilir,
- Spearman karesini ham veride açıklanan varyans oranı olarak yorumlamamayı öğrenebilir,
- ham ve sıra saçılım grafiklerini birlikte inceleyebilir,
- aynı koordinata düşen gözlemlerin üst üste gelebileceğini fark edebilir,
- birini-dışarıda-bırakma duyarlılık analizini yorumlayabilir,
- etkili gözlem ile hatalı gözlemi ayırabilir,
- Monte Carlo permütasyon p değerini ve çözünürlük sınırını açıklayabilir,
- klasik/asimptotik p değeri ile permütasyon p değerini ayırabilir,
- korelasyonun bireysel gelişme veya nedensellik kanıtı olmadığını açıklayabilir,
- sonuçları kaynak ve yöntem sınırlarıyla akademik olarak raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) dosyasından veri kaynağını ve analiz kapsamını okuyun.
2. Ana analiz için neden yalnız kaynak satırları 1–60'ın kullanıldığını açıklayın.
3. G1 ve G3 için saçılım grafiğini inceleyin.
4. `Sxx`, `Syy`, `Sxy` ve Pearson `r` değerini hesaplayın.
5. Bağlı notlara ortalama sıra vererek Spearman `r_s` değerini hesaplayın.
6. Pearson için t testi, iki yönlü p değeri ve yaklaşık Fisher %95 aralığını bulun.
7. Pearson `r²` ile aynı 60 kayıttaki basit OLS `R²` özdeşliğini denetleyin.
8. İlk kaydı yalnız bir kopyada dışlayarak Pearson ve Spearman değişimini inceleyin.
9. 60 ayrı birini-dışarıda-bırakma hesabıyla kayıt etkisini değerlendirin.
10. Son 20 kaydı ayrı etkinlik olarak analiz edin; bunu dış doğrulama diye sunmayın.
11. Monte Carlo permütasyon sonucunu klasik/asimptotik çıkarımdan ayrı raporlayın.
12. [COZUMLER.md](COZUMLER.md), `beklenen.json` ve [RAPORLAMA.md](RAPORLAMA.md) ile çalışmanızı kontrol edin.

## Veri ve araştırma sorusu

Veri, UCI Student Performance veri setinin Portekizce dersi bölümünden alınmış ilk 80 kaydın `school`, `G1` ve `G3` alanlarından oluşur.

- `G1`: birinci dönem notu,
- `G3`: yıl sonu notu,
- not aralığı: 0–20,
- bütün yerel kayıtlar GP okulundandır,
- sıfır not geçerli değerdir,
- eksik değer yoktur.

Ana analiz:

`kaynak_satir = 1–60`, `n=60`.

`kaynak_satir` kişi kimliği değil, aktarım sırasıdır. Kaynak 61–80 yalnız ayrı bir etkinliktir. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Araştırma sorusu:

> İlk 60 kayıtta G1 ile G3 arasında ne ölçüde doğrusal ve sıralı birliktelik vardır?

Bu soru “G1, G3'e neden olur mu?” sorusu değildir.

## Pearson korelasyonu

Ana 60 kayıtta merkezlenmiş çapraz çarpımlar:

- `Sxx = 385.4`,
- `Syy = 234.1833333333`,
- `Sxy = 224.3`.

Bunlardan Pearson korelasyonu:

`r = .746612792`

elde edilir. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Bu değer, ana örneklemde G1 ile G3 arasında güçlü pozitif doğrusal birliktelik bulunduğunu gösterir.

Ancak katsayının büyüklüğü:

- nedensellik,
- bireysel not artışı,
- temsil edilebilirlik,
- ölçüm geçerliği

kanıtı değildir.

## Pearson için klasik çıkarım

Ana analizde:

`t(58) = 8.547100`

ve iki yönlü klasik p değeri yaklaşık:

`p = 7.46694 × 10⁻¹²`

olarak hesaplanır.

Yaklaşık Fisher %95 güven aralığı:

`[.607944246, .841082238]`.

Bu test ve aralık klasik model koşullarına dayanır. Küçük p değeri örnekleme, temsil veya nedensellik sorunlarını ortadan kaldırmaz. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

## Pearson r² neyi gösterir?

Ana örneklemde:

`r² = .557430662`.

Aynı 60 kayıtla, sabit terimli ve tek yordayıcılı OLS regresyonda:

`R² = r²`.

Bu matematiksel özdeşlik aynı gözlemler ve aynı iki değişken için geçerlidir. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Bunu “G1, G3'ün %55.7'sine neden olur” diye yorumlamayın.

## Spearman korelasyonu

Notlarda bağlar bulunduğundan, her değişkende bağlı değerlere **ortalama sıra** verilir ve bu sıraların Pearson korelasyonu hesaplanır.

Ana sonuç:

`r_s = .831085662`.

Bu değer SciPy Spearman hesabıyla aynıdır. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Bağlı değerler bulunduğu için bağ düzeltmesi içermeyen kısa `1−6Σd²/[n(n²−1)]` formülü doğrudan kullanılmamalıdır.

## Pearson ve Spearman neden farklı olabilir?

Ana örneklemde:

- Pearson = `.7466`,
- Spearman = `.8311`.

Pearson ham değerlerdeki doğrusal birlikteliğe, Spearman ise sıralardaki monoton birlikteliğe odaklanır.

Spearman'ın daha yüksek olması tek başına Pearson'ın “yanlış” olduğu anlamına gelmez. İki katsayı ilişkinin farklı yönlerini özetler.

Spearman `r_s²`, ham G3 notlarındaki açıklanan varyans oranı olarak raporlanmamalıdır. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

## Grafiklerin rolü

Korelasyon katsayısını grafikten bağımsız yorumlamayın.

Ham not grafiğinde:

- ilişkinin yönünü,
- yaklaşık doğrusallığını,
- uç veya etkili olabilecek kayıtları,
- aynı koordinatta üst üste gelen gözlemleri

inceleyin.

Sıra grafiği ise Spearman'ın hangi bilgi üzerinden hesaplandığını görünür kılar.

Aynı koordinattaki noktaların üst üste gelmesi, grafikte görülen nokta sayısının kişi sayısına eşit olmamasına yol açabilir.

## İlk kaydın etkisi

Ana 60 kayıt korunarak hesaplanan Pearson:

`.746612792`.

Yalnız bir duyarlılık kopyasında kaynak 1 dışlandığında:

- `n=59`,
- Pearson = `.865833531`,
- Spearman = `.826699998`.

Pearson'ın artması ilk kaydın hatalı olduğunu kanıtlamaz. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Bu kayıt:

> “Sonucu etkileyen bir gözlem olabilir.”

şeklinde değerlendirilebilir; fakat veri hatası olduğuna ilişkin bağımsız kanıt olmadan silinmemelidir.

## Birini-dışarıda-bırakma duyarlılığı

Ana 60 kayıt için her seferinde bir kayıt dışarıda bırakılmıştır.

Pearson aralığı:

`[.727846069, .865833531]`.

- en düşük: kaynak 48 çıkarıldığında,
- en yüksek: kaynak 1 çıkarıldığında,
- ana katsayıdan mutlak değişim ölçütüyle en etkili: kaynak 1.

Spearman aralığı:

`[.822255639, .849831028]`.

- en düşük: kaynak 16 çıkarıldığında,
- en yüksek: kaynak 40 çıkarıldığında,
- ana katsayıdan mutlak değişim ölçütüyle en etkili: kaynak 40. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Bu aralıklar **güven aralığı değildir**. Bunlar 60 farklı duyarlılık hesabının sonuç aralığıdır.

Ayrıca en yüksek korelasyonu veren alt kümeyi seçmek geçerli bir analiz stratejisi değildir.

## Son 20 kayıt

Kaynak 61–80 için:

- `n=20`,
- Pearson = `.627307114`,
- Spearman = `.570535504`.

Bu katsayıların ana 60 kayıttan farklı olması tek başına anakütle korelasyonlarının farklı olduğunu göstermez. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Bu son 20 kayıt:

- aynı yerel alıntının devamıdır,
- bağımsız örnekleme sürecinden gelmez,
- dış doğrulama örneklemi değildir,
- doğrudan korelasyon farkı testi değildir. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

## Monte Carlo permütasyon hesabı

Spearman ilişkisi için Python'da:

- seed = `202606`,
- `B=19999` rastgele permütasyon,
- iki yönlü mutlak uçluk,
- uç permütasyon sayısı = `0`

elde edilmiştir.

Monte Carlo p değeri:

`p_MC = (0+1)/(19999+1) = .00005`.

Bu değer **p=0 değildir**. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Aynı zamanda:

- bütün olası permütasyonları tarayan tam kesin test değildir,
- Monte Carlo çözünürlük sınırını yansıtır,
- Spearman'ın asimptotik p değerinden farklı bir çıkarım yöntemidir.

Permütasyon yaklaşımı da bağımsızlık altında eşleşmelerin değiştirilebilirliği varsayımına dayanır; kümelenme ve örneklem seçimi sorunlarını çözmez. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

## Aynı seed neden R ve Python'da aynı sonucu garanti etmez?

R ve NumPy farklı rastgele sayı üreticileri ve permütasyon uygulamaları kullanabilir.

Bu nedenle aynı `seed=202606` yazılması iki ortamda aynı permütasyon dizisinin üretileceğini garanti etmez.

Yeniden üretilebilirlik raporunda yalnız seed değil, yazılım ve yöntem de belirtilmelidir.

## Ölçekleme deneyi

Pozitif doğrusal ölçekleme Pearson ve Spearman katsayılarını korur.

Örneğin bir değişkeni pozitif bir sabitle çarpmak ilişkinin yönünü değiştirmez.

Negatif sabitle çarpma ise sıralama/yön tersine döndüğü için korelasyon işaretini değiştirir. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

Bu özellik korelasyonun ölçü biriminden bağımsızlığını anlamak için yararlıdır.

## Korelasyon bireysel gelişme değildir

G1 ile G3 arasındaki yüksek pozitif korelasyon:

> G1'i yüksek olan öğrencilerin G3'ünün de genellikle yüksek olma eğiliminde olduğunu

gösterir.

Şunu göstermez:

> Her öğrencinin notu G1'den G3'e yükselmiştir.

Bireysel gelişme için `G3−G1` gibi kişi-içi değişim ayrı bir araştırma sorusudur. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

## Korelasyon nedensellik değildir

Bu bölümde gözlenen ilişki:

`G1 ↔ G3`

birlikteliğidir.

Tek başına korelasyon:

- G1'in G3'e neden olduğunu,
- arada başka değişken olmadığını,
- müdahalenin G3'ü değiştireceğini

göstermez.

Zamansal sıra bulunsa bile gözlemsel korelasyon tek başına nedensel tanımlama sağlamaz.

## Python ile çalıştırma

Depo kökünden:

```sh
python -m pip install -r bolumler/b06/requirements.txt
python bolumler/b06/analiz.py
```

Bölüm klasöründen:

```sh
python analiz.py
```

kullanabilirsiniz.

`veri.csv` aynı klasörde kalmalıdır. `python -O` kullanmayın; iç hesap denetimleri devre dışı kalabilir.

`calisma.ipynb` içindeki `None` alanlarını tamamlayın ve sonuçları `COZUMLER.md` ile karşılaştırın.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b06/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

Temel R yeterlidir; sonuçlar ekrana, grafik `grafikler/grafikler-R.pdf` dosyasına yazılır.

**R bu paket hazırlanırken çalıştırılmamıştır.** Bu pakette SPSS syntax veya SPSS çıktısı yoktur. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

## Üretilen dosyalar

- `sonuclar/ozet.json`: ana 60, ilk kayıt dışlanmış 59 ve son 20 için özetler,
- `sonuclar/siralar.csv`: ortalama sıralarıyla 60 kayıt,
- `sonuclar/duyarlilik.csv`: 60 ayrı birini-dışarıda-bırakma hesabı,
- `grafikler/b06-uci-korelasyon.pdf`: ham not ve sıra grafikleri.

Grafikte nokta büyüklüğü aynı koordinattaki kayıt sayısıyla orantılıdır; ilk kayıt ayrıca işaretlenir. [Kitap, Bölüm 6](../../KITAP_ESLESMESI.md)

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- 80 kaydın tamamını ana analizmiş gibi sunmayın; ana n=60'tır.
- Son 20 kaydı bağımsız dış doğrulama örneklemi diye adlandırmayın.
- `kaynak_satir` alanını kişi kimliği sanmayın.
- Sıfır notu otomatik veri hatası saymayın.
- Korelasyonu bireysel not artışı olarak yorumlamayın.
- Korelasyonu nedensellik olarak yorumlamayın.
- Bağlı notlarda bağsız kısa Spearman sıra-farkı formülünü kullanmayın.
- Pearson ve Spearman'ı “hangisi daha yüksekse o doğrudur” şeklinde seçmeyin.
- Spearman karesini ham notlarda açıklanan varyans oranı diye raporlamayın.
- İlk kaydı çıkarınca Pearson arttığı için kaydı hatalı ilan etmeyin.
- Birini-dışarıda-bırakma aralığını güven aralığı sanmayın.
- En yüksek korelasyonu veren alt kümeyi ana sonuç olarak seçmeyin.
- Son 20'deki katsayı farkını doğrudan korelasyon farkı testi diye yorumlamayın.
- Permütasyonda sıfır uç gözlenmesini `p=0` diye raporlamayın.
- Monte Carlo permütasyonunu tam kesin test diye sunmayın.
- Aynı seed'in R ve NumPy'da aynı permütasyonları üreteceğini varsaymayın.
- Küçük p değerinin temsili örnekleme veya nedensellik sağladığını düşünmeyin.

## Akademik raporlama

Sonuçları bilimsel bir metne dönüştürmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi bir korelasyon raporu yalnız `r=.75, p<.001` yazmaz. En azından:

**değişkenler → analiz örneklemi → katsayı türü → katsayı → belirsizlik/test → grafik → duyarlılık → veri kaynağı → yöntem sınırı → nedensellik sınırı**

zincirini görünür kılar.

## Çözüm ve teknik doğrulama

Önce [GOREVLER.md](GOREVLER.md) içindeki soruları kendiniz çözün. Ardından [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.

Çalıştırma bilgileri [DOGRULAMA.json](DOGRULAMA.json) dosyasında tutulur.

Bu bölümün ana öğrenme zinciri:

**Araştırma sorusu → Veri ve eşleşme → Grafik → Pearson → Spearman → Belirsizlik → Duyarlılık → Permütasyon → Yorum → Sınırlılık → Akademik raporlama**