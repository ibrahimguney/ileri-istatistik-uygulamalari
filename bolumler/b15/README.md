# Bölüm 15 — Doğrulayıcı Faktör Analizi (DFA/CFA)

Bu bölümde **doğrulayıcı faktör analizi (DFA/CFA)**, Bölüm 14'te incelenen A/C maddeleri üzerinde açıkça tanımlanmış ölçüm modellerinin sınanması üzerinden öğrenilir. Amaç yalnız uyum indeksleri üretmek değil; **modelin önceden tanımlanması, tanımlanabilirlik, parametre sayımı, model karşılaştırması, standartlaştırılmış yükler, belirsizlik, AVE/CR ve bağımsız doğrulama sınırlarını** birlikte değerlendirmektir.

**Önemli:** Bölüm 14 ile aynı 97 kayıt kullanılmaktadır. Bu nedenle burada AFA'dan DFA'ya geçiş öğretim açısından yararlı olsa da **bağımsız doğrulama değildir**. Yeni örneklem, Türkçe uyarlama verisi veya bağımsız ölçüm doğrulaması üretilmemektedir.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- AFA ile DFA arasındaki temel amaç farkını açıklayabilir,
- ölçüm modelini analizden önce açıkça tanımlayabilir,
- gözlenen kovaryans momentlerini ve serbest parametreleri sayabilir,
- serbestlik derecesini hesaplayabilir,
- pozitif serbestlik derecesi ile yerel tanımlanabilirliği ayırabilir,
- normal-kuram kovaryans ML/Wishart yaklaşımını tanımlayabilir,
- ki-kare, CFI, TLI, RMSEA, SRMR ve RMSR_off değerlerini yorumlayabilir,
- RMSEA güven aralığını nokta tahmininden ayırabilir,
- standartlaştırılmış faktör yükü, R² ve artık varyansını ilişkilendirebilir,
- AVE ve CR'nin farklı nicelikler olduğunu açıklayabilir,
- ilişkili ve ilişkisiz faktör modellerini karşılaştırabilir,
- çapraz yük eklenmesinin model uyumuna etkisini değerlendirebilir,
- AFA sonrası seçilmiş alternatifin nominal fark testini ölçülü yorumlayabilir,
- AIC*/BIC* ile yazılımın tam AIC/BIC değerlerini ayırabilir,
- aynı veriyle model değiştirmeyi bağımsız doğrulama olarak sunmamayı öğrenebilir,
- sonuçları akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` ile veri kaynağını ve sabit ön işlem kararlarını inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki D1–D3 sorularıyla DFA'nın varsayım ve kapsamını açıklayın.
3. `calisma.ipynb` içindeki hesapları tamamlayın.
4. M0, M1 ve M2 modellerinin parametre ve serbestlik derecelerini karşılaştırın.
5. Uyum indekslerini ve RMSEA belirsizliğini inceleyin.
6. Standartlaştırılmış yükler, R² ve artık varyanslarını değerlendirin.
7. AVE ve CR hesaplarını yorumlayın.
8. M0–M1 ve M1–M2 farklarını inceleyin.
9. AFA sonrası çapraz yük eklemenin doğrulama açısından sınırını tartışın.
10. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
11. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla DFA sonuçlarını bilimsel rapor diline dönüştürün.

## Veri ve ön işlem

Bölüm 13/14 ile aynı yerel ilk 100 A/C kaydı kullanılır. A1, C4 ve C5 bir kez `7−x` ile ters puanlanır. C1/satır 63, A2/satır 66 ve C3/satır 90'daki eksikler nedeniyle ortak tam kayıt örneklemi:

`n = 97`

olarak belirlenir.

Maddeler örneklem standart sapmasıyla (`ddof=1`) standartlaştırılır. Bu z-puanların `ddof=1` kovaryans matrisi aynı kişilerin Pearson korelasyon matrisidir.

Gözlenen madde varyanslarının 1 olması ile gizil faktör varyanslarının 1'e sabitlenmesi aynı işlem değildir. İkincisi model ölçekleme/tanımlama kararıdır. [Kitap, Bölüm 15](../../KITAP_ESLESMESI.md)

## Sınanan üç model

Aynı veri üzerinde üç açık model karşılaştırılır:

| Model | Tanım | Serbest parametre | sd |
|---|---|---:|---:|
| M0 | İlişkisiz iki faktör | 20 | 35 |
| M1 | İlişkili iki faktör | 21 | 34 |
| M2 | M1 + A2'nin C çapraz yükü | 22 | 33 |

On gözlenen değişken için benzersiz kovaryans momenti sayısı:

`10×11/2 = 55`

olur.

M0'da on birincil yük ve on artık varyansı serbesttir. M1'de bunlara faktör korelasyonu eklenir. M2'de ayrıca A2'nin C faktöründeki çapraz yükü serbest bırakılır.

Faktör varyansları 1'e sabitlenir; artık kovaryansları sıfırdır ve ortalama yapısı modellenmez.

Pozitif serbestlik derecesi tek başına tanımlanabilirlik kanıtı değildir. Kod yerel Jacobian rankını ayrıca denetler.

## Tahmin yöntemi

Bu bölümde yalnız **normal-kuram kovaryans maksimum olabilirlik (ML)** yaklaşımı kullanılır ve ki-kare hesabında Wishart `n−1` çarpanı uygulanır.

Bu pakette uygulanmayan yöntemler:

- sağlam ML/MLR,
- WLSMV,
- FIML,
- bootstrap,
- otomatik modifikasyon indeksi taraması,
- ölçüm değişmezliği,
- yeni veriyle DFA.

Tam kayıt seçimi FIML değildir. Bir rapor tablosuna “MLR”, “WLSMV” veya “FIML” yazmak bu analizlerin yapılmış olduğu anlamına gelmez.

## M1 — İlişkili iki faktör modeli

M1 için temel sonuçlar:

- `T = 45.138110`,
- `sd = 34`,
- CFI = `.935763`,
- RMSEA = `.058114`,
- %90 RMSEA GA = `[0, .099618]`,
- SRMR = `.078238`,
- RMSR_off = `.086495`.

Örnek raporlama biçimi:

`χ²(34)=45.14, CFI=.936, RMSEA=.058, %90 GA [0,.100], SRMR=.078`

Nokta RMSEA değerinin `.06` civarında olması modeli “doğru” yapmaz. Özellikle güven aralığının üst sınırı yaklaşık `.100` olduğundan belirsizlik ayrıca dikkate alınmalıdır.

SRMR burada köşegen dahil 55 alt üçgen hücre üzerinden, `RMSR_off` ise 45 benzersiz köşegen dışı çift üzerinden hesaplanır. Bunlar birbirinin yerine kullanılmamalıdır.

## CFI başlangıç modeli ile M0'ı ayırın

M0, iki faktörün birbiriyle ilişkisiz olduğu **iki faktörlü ölçüm modelidir**.

CFI hesaplamasındaki başlangıç/baseline model ise on göstergenin birbirinden bağımsız olduğu modeldir ve `sd=45`'tir.

M1 için başlangıç modelinin:

`T = 218.391072`

olduğu durumda:

`CFI = 1 − (45.138110−34)/(218.391072−45) = .935763`

elde edilir.

Dolayısıyla M0'ı CFI'nin bağımsız göstergeli başlangıç modeli olarak adlandırmayın.

## Standartlaştırılmış yük, R² ve artık varyansı — A1 örneği

M1'de A1'in standartlaştırılmış yükü:

`.304257`

olduğundan:

`R² = .304257² = .092572`

ve standartlaştırılmış artık varyansı:

`1 − R² = .907428`

olur.

A1 yükünün model-temelli %95 Wald aralığı:

`[.094327, .514187]`

şeklindedir.

Aralığın sıfırı dışlaması, maddenin faktörü güçlü temsil ettiğini kanıtlamaz. Model A1 varyansının yalnız yaklaşık `%9.3`'ünü temsil etmektedir. Ayrıca bu aralık sağlam değildir ve bütün yükler için eşzamanlı güven aralığı değildir.

## Faktör korelasyonu

M1'de faktör korelasyonu:

`Phi = .339936`

ve:

`Phi² ≈ .115556`

olarak bulunmuştur.

Phi için model-temelli %95 aralık:

`[.080523, .556219]`

şeklindedir.

Bu ilişki A ve C faktörlerinin tamamen bağımsız olmadığına işaret eder; ancak kültürel eşdeğerlik, Türkçe geçerlik veya nedensel ilişki kanıtı değildir.

## AVE ve CR

M1 için C alt ölçeğinde:

- AVE = `.361301`,
- CR = `.735159`.

A alt ölçeğinde:

- AVE = `.334323`,
- CR = `.689265`.

AVE'nin payında standartlaştırılmış yüklerin kareleri toplamı kullanılırken CR'nin payında yükler toplamının karesi yer alır. Bu nedenle AVE ve CR aynı nicelik değildir.

CR'nin görece yüksek olması düşük AVE'yi, zayıf madde temsilini veya içerik sorunlarını ortadan kaldırmaz. CR ham Cronbach alfa değildir ve burada CR/AVE için güven aralığı hesaplanmamıştır.

## M0 ve M1 karşılaştırması

M0 ve M1 arasında:

`ΔT = 51.252957 − 45.138110 = 6.114847`

ve:

`Δsd = 1`

bulunur.

Nominal fark testi:

`p = .013405`

verir.

Bu karşılaştırma, bu model ailesinde faktör korelasyonunun sıfıra sabitlenmesine karşı serbest bırakılmasını değerlendirir.

## M2 — A2 çapraz yük alternatifi

M2, M1'e A2'nin C faktöründeki çapraz yükünü ekler.

M2 sonuçları:

- `T = 37.526516`,
- `sd = 33`,
- `p = .269328`,
- CFI = `.973894`,
- TLI = `.964401`,
- RMSEA = `.037604`,
- %90 RMSEA GA = `[0, .086312]`,
- SRMR = `.067726`.

M1–M2 farkı:

- `ΔT = 7.611594`,
- `Δsd = 1`,
- nominal `p = .005799`.

A2'nin standartlaştırılmış C çapraz yükü:

`.302006`

olarak bulunmuştur.

Ancak bu alternatif **Bölüm 14'te aynı veride görülen AFA ipucundan sonra** seçilmiştir. Bu nedenle nominal fark testi p değeri, model seçimi sürecini hesaba katan bağımsız doğrulayıcı kanıt değildir.

M2'de A2'nin R²'si yalnız birincil yükün karesi değildir; iki yük ve faktör korelasyonundan gelen çapraz terim birlikte değerlendirilmelidir.

## AIC* ve BIC* karşılaştırmaları

Bu öğretim kodunda ortak olabilirlik sabiti çıkarılmış karşılaştırma ölçüleri kullanılır:

| Model | AIC* | BIC* |
|---|---:|---:|
| M0 | 91.252957 | 142.747177 |
| M1 | 87.138110 | 141.207041 |
| M2 | 81.526516 | 138.170158 |

Bu değerler aynı veri ve aynı tanım altında model karşılaştırması için kullanılabilir. Ancak **AMOS/lavaan gibi yazılımların tam AIC/BIC değerleriyle birebir aynı sayı oldukları iddia edilmemelidir**.

## Sayısal denetimler

Kod yalnız uyum indekslerini üretmez; çözümün sayısal davranışını da denetler. Bunlar arasında:

- birden fazla L-BFGS-B başlangıcı,
- ek BFGS karşılaştırması,
- küçük gradyan,
- aynı amaç/model kovaryansına yakınsama,
- parametre sınırlarından uzaklık,
- analitik türevlerin sonlu farklarla karşılaştırılması,
- yerel Jacobian rankı

bulunur.

Bu denetimler yararlıdır fakat global tek çözüm veya doğru ölçüm modeli kanıtı değildir.

## Python ile çalıştırma

Depo kökünden:

```sh
python bolumler/b15/analiz.py
```

Bölüm klasöründen:

```sh
python analiz.py
```

kullanabilirsiniz.

Kod kitap klasörlerine veya ağa ihtiyaç duymaz. `requirements.txt` doğrulama ortamındaki paket sürümlerini listeler; betikler paket kurmaz.

## R/lavaan ile çalışma

Önce Python ile puanlanmış CSV'yi üretin. Ardından depo kökünden:

```sh
Rscript bolumler/b15/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

R betiği sistemde kurulu `lavaan` paketini gerektirir; paket yoksa durur ve kurulum yapmaz.

**Bu dağıtım hazırlanırken R/lavaan çalıştırılarak doğrulanmamıştır.** Python sonuçlarını lavaan sonucu olarak sunmayın.

## AMOS yolu

`amos-kontrol-listesi.md` öğrencinin modeli AMOS'ta yeniden kurabilmesi için hazırlanmış bir kontrol listesidir. **Çalıştırılmış AMOS çıktısı değildir.**

Python sonuçlarını AMOS tarafından doğrulanmış gibi sunmayın. Yazılımlar arası karşılaştırmada en azından:

- standartlaştırma,
- kovaryans böleni,
- ML/Wishart tanımı,
- ki-kare çarpanı,
- bilgi matrisi,
- güven aralığı tanımı

eşleştirilmelidir.

## Analizde inceleyeceğiniz temel kavramlar

- AFA ve DFA ayrımı,
- ölçüm modeli,
- gözlenen kovaryans momentleri,
- serbest parametre,
- serbestlik derecesi,
- tanımlanabilirlik,
- normal-kuram ML,
- Wishart düzeltmesi,
- model ki-karesi,
- CFI ve TLI,
- RMSEA ve güven aralığı,
- SRMR ve RMSR_off,
- standartlaştırılmış yük,
- gösterge R²'si,
- artık varyansı,
- faktör korelasyonu,
- AVE,
- CR,
- iç içe model karşılaştırması,
- çapraz yük,
- model seçimi yanlılığı,
- bağımsız doğrulama.

## Üretilen dosyalar

`sonuclar/ozet.json` model, uyum, belirsizlik ve sayısal denetim özetlerini içerir.

Ayrıca on iki CSV üretilir:

- `puanlanmis.csv`,
- `standartlastirilmis.csv`,
- `orneklem_kovaryans.csv`,
- her model için `_model`, `_artik` ve `_yukler` dosyaları.

`puanlanmis.csv` zaten ters kodlanmıştır; yeniden terslemeyin. `standartlastirilmis.csv` yalnız on maddeyi içerir; satır kimliği gerektiğinde puanlanmış dosyadan eşlenir. Matris CSV'lerinin ilk sütunu satır etiketidir.

`grafikler/b15-yuk-araliklari.pdf`, M1 standartlaştırılmış yüklerinin model-temelli, sağlam olmayan tekil %95 Wald aralıklarını gösterir.

Ham kaynak dosyası değiştirilmez.

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- Aynı 97 kayıtta AFA sonrası DFA'yı bağımsız doğrulama saymayın.
- Pozitif sd'yi tek başına tanımlanabilirlik kanıtı olarak sunmayın.
- Tam kayıt analizini FIML olarak adlandırmayın.
- Normal-kuram ML sonucunu MLR/WLSMV sonucu gibi sunmayın.
- Anlamsız ki-kareyi “model doğrudur” şeklinde yorumlamayın.
- RMSEA nokta değerini güven aralığından bağımsız değerlendirmeyin.
- CFI'yi bütün maddelerin iyi temsil edildiğinin kanıtı saymayın.
- M0'ı CFI'nin bağımsız göstergeli başlangıç modeliyle karıştırmayın.
- SRMR ve RMSR_off'u birbirinin yerine kullanmayın.
- Yük aralığının sıfırı dışlamasını güçlü madde temsilinin kanıtı saymayın.
- CR'yi ham alfa olarak adlandırmayın.
- Yüksek CR'nin düşük AVE'yi ortadan kaldırdığını söylemeyin.
- M2'nin daha iyi uyumunu bağımsız doğrulama olarak sunmayın.
- AFA sonrası seçilen M2 için nominal p değerini model seçimi için düzeltilmiş p olarak sunmayın.
- AIC*/BIC* değerlerini tam lavaan/AMOS AIC/BIC değerleri olarak sunmayın.
- `amos-kontrol-listesi.md` dosyasını AMOS çıktısı olarak göstermeyin.
- Bu pakette yapılmayan WLSMV, MLR, FIML, bootstrap, değişmezlik veya yeni-veri DFA sonuçlarını rapora eklemeyin.

## Bağımsız doğrulamaya geçiş

Bu bölümün en önemli bilimsel sonucu yalnız M1 veya M2'nin uyum değerleri değildir. Asıl amaç, **yeni veride hangi modelin nasıl sınanacağını önceden tanımlamaktır**.

Gelecek bir bağımsız DFA çalışmasında en azından:

1. hedef grup tanımlanmalı,
2. örneklem planı önceden belirlenmeli,
3. madde puanlama ve eksik veri yaklaşımı önceden yazılmalı,
4. temel ölçüm modeli sonuçlar görülmeden tanımlanmalı,
5. A2 çapraz yükü gibi alternatifler önceden kuramsal gerekçeye bağlanmalı,
6. ordinal/sağlam tahmin gereksinimi değerlendirilmelidir,
7. modifikasyon sınırları önceden belirlenmeli,
8. mümkünse bağımsız örneklem kullanılmalı,
9. sonraki aşamada ölçüm değişmezliği değerlendirilmelidir.

## Akademik raporlama

DFA sonuçlarının yöntem ve bulgu bölümünde nasıl raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi bir DFA raporu yalnız `χ²`, CFI ve RMSEA değerlerini sıralamaz. **Modelin nereden geldiğini, hangi veride sınandığını, tahmin yöntemini, model tanımını, yükleri ve belirsizliklerini, artık uyumunu, model karşılaştırmalarını, alternatif modelin nasıl seçildiğini ve bağımsız doğrulama sınırlarını** açıkça belirtir.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Gerçekte hangi araçların ve denetimlerin çalıştırıldığı `DOGRULAMA.json` dosyasında belirtilmiştir.

Yerel hash ve sayısal optimizasyon denetimleri yeniden üretilebilirliği destekler; veri temsiliyeti, kültürel geçerlik veya bağımsız ölçüm doğrulaması anlamına gelmez.