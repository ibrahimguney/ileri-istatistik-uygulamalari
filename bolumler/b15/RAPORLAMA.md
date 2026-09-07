# Bölüm 15 — Doğrulayıcı Faktör Analizini Akademik Raporlama

Bu rehber, Bölüm 15'teki doğrulayıcı faktör analizinin (DFA/CFA) bilimsel bir raporda doğru ve ölçülü biçimde sunulmasına yardımcı olur.

Temel raporlama zinciri:

**Kuramsal model → Veri ve örneklem → Ön işlem → Model tanımı → Tahmin yöntemi → Tanımlanabilirlik → Global uyum → Yüklar ve belirsizlik → Faktör ilişkisi → AVE/CR → Alternatif modeller → Sınırlılıklar → Bağımsız doğrulama**

## 1. Önce doğrulanan modelin nereden geldiğini açıklayın

Bu bölümde iki faktörlü A/C yapısı Bölüm 14'te aynı 97 kayıt üzerinde AFA ile incelenmiştir. Dolayısıyla DFA öğretim amacıyla açık kısıtlı modelleri sınasa da yeni veride bağımsız doğrulama değildir.

Uygun ifade:

> DFA, önceki AFA örneğiyle aynı 97 tam kayıt üzerinde, serbest keşifsel örüntü ile açık ölçüm kısıtlarını karşılaştırmayı öğretmek amacıyla yürütülmüştür. Aynı verinin yeniden kullanılması nedeniyle sonuçlar bağımsız doğrulama olarak yorumlanmamıştır.

## 2. Veri ve ön işlemi raporlayın

Yerel ilk 100 kayıttan A1–A5 ve C1–C5 maddeleri kullanılmıştır. A1, C4 ve C5 bir kez `7−x` ile ters puanlanmış; üç farklı eksik satır nedeniyle ortak tam kayıt örneklemi `n=97` olmuştur.

Maddeler örneklem standart sapmasıyla (`ddof=1`) standartlaştırılmıştır.

Örnek ifade:

> Analiz, on A/C maddesinin ortak 97 tam kaydı üzerinde yürütülmüş; A1, C4 ve C5 belgelenmiş anahtara göre ters puanlanmış ve maddeler örneklem standart sapması kullanılarak standartlaştırılmıştır. Eksik değer ataması veya FIML kullanılmamıştır.

## 3. Model ölçeklemesini açıkça belirtin

Gözlenen maddelerin z-puanlanması ile gizil faktörlerin ölçeklenmesi aynı işlem değildir.

Bu modellerde faktör varyansları 1'e sabitlenmiştir.

Raporunuzda model ölçeklemesini açıkça belirtin; gözlenen değişkenlerin varyansının 1 olmasından gizil faktör varyansının kendiliğinden 1 olduğu sonucunu çıkarmayın.

## 4. Model tanımını açıkça verin

Üç model karşılaştırılmıştır:

| Model | Kısıt | q | sd |
|---|---|---:|---:|
| M0 | İlişkisiz A ve C faktörleri | 20 | 35 |
| M1 | A ve C faktörleri ilişkili | 21 | 34 |
| M2 | M1 + A2→C çapraz yükü | 22 | 33 |

On değişken için 55 benzersiz kovaryans momenti vardır.

Örnek yöntem ifadesi:

> M0'da iki faktörün korelasyonu sıfıra sabitlenmiş, M1'de faktör korelasyonu serbest bırakılmış ve M2'de M1'e ek olarak A2'nin C faktöründeki çapraz yükü tahmin edilmiştir. Modeller sırasıyla 20, 21 ve 22 serbest parametre içermektedir.

## 5. Serbestlik derecesini tanımlanabilirlikle eşitlemeyin

Serbestlik dereceleri:

- M0: 35,
- M1: 34,
- M2: 33.

Pozitif sd gerekli bir bilgi olsa da yerel tanımlanabilirliğin tek başına kanıtı değildir. Bu pakette yerel Jacobian rankı ayrıca kontrol edilmektedir.

## 6. Tahmin yöntemini doğru adlandırın

Bu bölümde:

**normal-kuram kovaryans ML + Wishart `(n−1)` çarpanı**

kullanılmıştır.

Uygulanmayan yöntemler:

- MLR/sağlam ML,
- WLSMV,
- FIML,
- bootstrap.

Bu nedenle raporda yalnız gerçekten uygulanan tahminleyiciyi yazın.

## 7. M1 global uyumunu birlikte raporlayın

M1 için:

- `χ²(34)=45.138`,
- CFI `.935763`,
- RMSEA `.058114`,
- %90 RMSEA GA `[0,.099618]`,
- SRMR `.078238`.

Örnek raporlama:

> İlişkili iki faktörlü M1 modeli için `χ²(34)=45.14`, `CFI=.936`, `RMSEA=.058`, `%90 GA [0,.100]` ve `SRMR=.078` elde edilmiştir.

Ardından ölçülü yorum ekleyin:

> Uyum indeksleri birlikte değerlendirildiğinde model belirli ölçüde desteklenmekle birlikte, özellikle RMSEA güven aralığının üst sınırı ve madde düzeyindeki temsil farklılıkları nedeniyle sonuçlar modelin kesin doğruluğu olarak yorumlanmamıştır.

## 8. Ki-kareyi “doğru model” testi gibi yorumlamayın

Ki-kare testi model ile örneklem kovaryans yapısı arasındaki uyuşmazlığa ilişkin bilgi verir. Anlamlı veya anlamsız sonuç tek başına modelin bilimsel doğruluğunu belirlemez.

Örneklem büyüklüğü, varsayımlar, model karmaşıklığı, artıklar ve diğer uyum göstergeleri birlikte değerlendirilmelidir.

## 9. RMSEA güven aralığını raporlayın

M1 nokta RMSEA değeri `.058` olsa da %90 güven aralığı yaklaşık:

`[0,.100]`

şeklindedir.

Bu belirsizlik önemlidir.

Yalnız:

> RMSEA < .06, model iyi.

şeklinde kesin eşik yorumu yapmayın.

## 10. CFI başlangıç modelini M0 ile karıştırmayın

CFI için kullanılan bağımsız göstergeli başlangıç modelinde:

- `T=218.391072`,
- `sd=45`.

M0 ise iki faktörlü fakat faktör korelasyonu sıfıra sabitlenmiş bir ölçüm modelidir.

Bunlar farklı modellerdir.

## 11. SRMR ve RMSR_off ayrımını koruyun

M1 için:

- SRMR `.078238`,
- RMSR_off `.086495`.

SRMR, bu hesapta köşegen dahil 55 alt üçgen hücreyi; RMSR_off ise 45 benzersiz köşegen dışı çifti kullanır.

Raporunuzda hangisini verdiğinizi açıkça belirtin.

## 12. Yükü, R²'yi ve artık varyansını birlikte değerlendirin

A1 örneği:

- standartlaştırılmış yük `.304257`,
- `R²=.092572`,
- standartlaştırılmış artık varyansı `.907428`,
- %95 Wald GA `[.094327,.514187]`.

Örnek raporlama:

> A1'in standartlaştırılmış yükü `.304` olup model bu göstergenin varyansının yaklaşık `%9.3`'ünü açıklamıştır (`R²=.093`). Model-temelli %95 Wald aralığı `[.094,.514]` olmakla birlikte, düşük R² nedeniyle maddenin faktörü güçlü temsil ettiği sonucuna varılmamıştır.

Yük aralığının sıfırı dışlaması “madde iyidir” anlamına gelmez.

## 13. Yük güven aralıklarının kapsamını belirtin

Bu bölümdeki yük aralıkları:

- model-temelli,
- normal-kuramlı,
- delta yöntemli,
- tekil %95 Wald aralıklarıdır.

Sağlam değildir ve bütün yükleri aynı anda kapsayan eşzamanlı güven bandı değildir.

## 14. Faktör korelasyonunu raporlayın

M1 için:

`Phi=.339936`

ve %95 aralık:

`[.080523,.556219]`.

Ayrıca:

`Phi²≈.115556`.

Örnek ifade:

> A ve C gizil faktörleri arasında `.340` düzeyinde pozitif korelasyon tahmin edilmiştir; model-temelli %95 aralık `[.081,.556]`'dır.

Bu ilişki kültürel geçerlik veya nedensel etki olarak yorumlanmamalıdır.

## 15. AVE ve CR'yi birlikte ama ayrı yorumlayın

M1 sonuçları:

| Alt ölçek | AVE | CR |
|---|---:|---:|
| A | .334323 | .689265 |
| C | .361301 | .735159 |

AVE ve CR farklı formüller ve farklı sorular içerir.

Örnek raporlama:

> C faktörü için AVE `.361`, CR `.735`; A faktörü için AVE `.334`, CR `.689` bulunmuştur. CR değerleri AVE'nin yerini tutmadığından, görece yüksek CR düşük ortalama gösterge temsilini ortadan kaldıran bir geçerlik kanıtı olarak yorumlanmamıştır.

CR ham Cronbach alfa değildir.

## 16. AVE/CR için hesaplanmayan belirsizliği uydurmayın

Bu pakette AVE ve CR için güven aralıkları hesaplanmamıştır.

Dolayısıyla yalnız nokta tahminleri raporlanmalıdır.

## 17. M0–M1 karşılaştırmasını doğru yorumlayın

M0–M1 karşılaştırması:

- `Δχ²=6.114847`,
- `Δsd=1`,
- nominal `p=.013405`.

Örnek raporlama:

> Faktör korelasyonunun sıfıra sabitlendiği M0 ile korelasyonun serbest bırakıldığı M1 arasındaki fark `Δχ²(1)=6.11, p=.013` olmuştur. Bu sonuç, incelenen model ailesi içinde faktör korelasyonunun serbest bırakılmasını desteklemektedir.

## 18. M2'nin uyumunu raporlayın ama seçilme biçimini gizlemeyin

M2 sonuçları:

- `χ²(33)=37.527`,
- `p=.269328`,
- CFI `.973894`,
- TLI `.964401`,
- RMSEA `.037604`,
- %90 GA `[0,.086312]`,
- SRMR `.067726`.

M1–M2 farkı:

`Δχ²(1)=7.611594, p=.005799`.

A2'nin standartlaştırılmış C çapraz yükü:

`.302006`.

Örnek raporlama:

> A2'nin C faktöründeki çapraz yükünün serbest bırakıldığı M2, M1'e göre daha düşük uyumsuzluk göstermiştir, `Δχ²(1)=7.61, nominal p=.006`. Bununla birlikte, çapraz yük aynı verideki önceki AFA bulgusundan hareketle seçildiğinden bu karşılaştırma bağımsız doğrulayıcı test olarak değerlendirilmemiştir.

Bu son cümle kritik önemdedir.

## 19. M2'de A2 R²'sini yalnız birincil yükün karesi sanmayın

A2 iki faktöre yüklenirken faktörler de ilişkili olduğundan açıklanan varyans iki yükün ve `Phi` çapraz teriminin birleşimine bağlıdır.

Dolayısıyla M2'de:

`R² ≠ yalnız birincil yük²`.

## 20. Nominal p ile seçim-düzeltilmiş p'yi ayırın

M2 otomatik modifikasyon indeksi taramasıyla seçilmemiş olsa da aynı verideki AFA ipucundan sonra kurulmuştur.

Bu nedenle M1–M2 fark testindeki `.005799` p değeri **nominaldir**. Model seçimi sürecini hesaba katan düzeltilmiş bağımsız kanıt değildir.

## 21. AIC*/BIC* yıldızını koruyun

| Model | AIC* | BIC* |
|---|---:|---:|
| M0 | 91.253 | 142.747 |
| M1 | 87.138 | 141.207 |
| M2 | 81.527 | 138.170 |

Bu değerler ortak olabilirlik sabiti çıkarılmış öğretim karşılaştırmalarıdır.

Bunları AMOS veya lavaan'ın tam AIC/BIC değerleri gibi sunmayın.

## 22. Yazılım kaynağını doğru belirtin

Bu bölümdeki referans sayılar **Python hesaplarıdır**.

R/lavaan betiği hazırlanmıştır ancak bu dağıtım hazırlanırken çalıştırılmamıştır.

`amos-kontrol-listesi.md` ise AMOS'ta kurulacak model için kontrol listesidir; AMOS çıktısı değildir.

Uygun ifade:

> Sayısal sonuçlar bölümün Python uygulamasından elde edilmiştir. R/lavaan ve AMOS sonuçları bu paket hazırlanırken çalıştırılarak doğrulanmamıştır.

## 23. Yapılmamış yöntemleri sonuç gibi sunmayın

Bu bölümde yapılmamıştır:

- MLR,
- WLSMV,
- FIML,
- bootstrap,
- otomatik MI taraması,
- ölçüm değişmezliği,
- yeni örneklemde DFA.

Özellikle 1–6 aralığındaki maddelerin ordinal özellikleri için WLSMV/polikorik yaklaşım gelecekte değerlendirilebilir; ancak burada yapılmış gibi yazılamaz.

## 24. Bağımsız doğrulama protokolü oluşturun

Gelecek çalışmada şu kararlar sonuçlar görülmeden önce mümkün olduğunca açıklaştırılmalıdır:

1. hedef grup,
2. örneklem planı,
3. puanlama anahtarı,
4. eksik veri yaklaşımı,
5. temel faktör yapısı,
6. A2 çapraz yükünün kuramsal durumu,
7. tahminleyici seçimi,
8. uyum değerlendirme planı,
9. modifikasyon sınırları,
10. ölçüm değişmezliği planı.

Bu yaklaşım DFA'yı yalnız uyum indekslerini optimize eden bir işlem olmaktan çıkarıp gerçekten doğrulayıcı bir tasarıma yaklaştırır.

## 25. Örnek bütünleşik DFA raporu

> Yerel ilk 100 kayıt alıntısındaki A1–A5 ve C1–C5 maddelerinden ortak 97 tam kayıt seçilmiş, A1/C4/C5 belgelenmiş anahtara göre ters puanlanmış ve maddeler örneklem standart sapmasıyla standartlaştırılmıştır. Ortalama yapısı olmadan normal-kuram Wishart ML kullanılarak iki faktörlü ölçüm modelleri sınanmıştır. Faktör korelasyonunun serbest olduğu M1 modeli `χ²(34)=45.14`, `CFI=.936`, `RMSEA=.058`, `%90 GA [0,.100]` ve `SRMR=.078` vermiştir. Faktör korelasyonu `.340` olarak tahmin edilmiştir. A1'in standartlaştırılmış yükü `.304` ve `R²=.093` olduğundan madde düşük temsil açısından incelemeye ayrılmıştır. C faktörü için `AVE=.361` ve `CR=.735`, A faktörü için `AVE=.334` ve `CR=.689` bulunmuştur. AFA sonrası belirlenen A2 çapraz yükünü içeren M2 daha iyi nominal uyum göstermiştir (`Δχ²(1)=7.61, p=.006`); ancak alternatif aynı veri incelendikten sonra seçildiğinden bu fark bağımsız doğrulama kanıtı olarak yorumlanmamıştır. Sonuçlar aynı 97 kayıt üzerindeki öğretim uygulamasına aittir; yeni örneklem, Türkçe uyarlama, WLSMV/MLR/FIML, ölçüm değişmezliği veya bağımsız DFA kanıtı üretilmemiştir.

## 26. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Veri kaynağı ve `n=97` açıklanmış mı?
- Aynı veride önce AFA yapıldığı belirtilmiş mi?
- Bunun bağımsız doğrulama olmadığı açık mı?
- Ters puanlama ve eksik veri kararı belirtilmiş mi?
- Tam kayıt analizi FIML diye adlandırılmamış mı?
- Standartlaştırma ile faktör ölçekleme ayrılmış mı?
- M0/M1/M2 açıkça tanımlanmış mı?
- 55 kovaryans momenti ve parametre sayıları doğru mu?
- Pozitif sd tanımlanabilirliğin tek kanıtı sayılmamış mı?
- Tahminleyici normal-kuram Wishart ML olarak doğru adlandırılmış mı?
- MLR/WLSMV yapılmış gibi yazılmamış mı?
- Ki-kare, CFI, RMSEA ve SRMR birlikte raporlanmış mı?
- RMSEA güven aralığı verilmiş mi?
- M0 ile CFI başlangıç modeli ayrılmış mı?
- SRMR ve RMSR_off karıştırılmamış mı?
- Standart yükler R² ve artık varyansla birlikte değerlendirilmiş mi?
- Wald aralıklarının sağlam/eşzamanlı olmadığı belirtilmiş mi?
- Phi ve aralığı doğru yorumlanmış mı?
- AVE ve CR birbirinden ayrılmış mı?
- CR ham alfa diye adlandırılmamış mı?
- AVE/CR için olmayan güven aralıkları uydurulmamış mı?
- M0–M1 fark testi doğru model çiftine bağlanmış mı?
- M2'nin AFA sonrası seçildiği açıklanmış mı?
- M1–M2 p değeri nominal olarak tanımlanmış mı?
- M2 A2 R²'si yalnız birincil yük karesi sayılmamış mı?
- AIC*/BIC* tam yazılım AIC/BIC'si olarak sunulmamış mı?
- Python sonuçları lavaan veya AMOS çıktısı diye gösterilmemiş mi?
- Yapılmamış bootstrap, WLSMV, MLR, FIML veya değişmezlik sonuçları eklenmemiş mi?
- Yeni veriyle doğrulama için açık bir protokol yazılmış mı?

## Son mesaj

DFA'da temel bilimsel düşünce zinciri şöyledir:

**Kuram → Önceden tanımlanmış ölçüm modeli → Veri → Tahmin → Global uyum → Yerel parametreler → Belirsizlik → Alternatif model → Model seçiminin kaynağı → Sınırlılık → Yeni veride doğrulama → Akademik raporlama**

İyi DFA, en yüksek CFI veya en düşük RMSEA'yı arama işlemi değildir. Amaç, **önceden gerekçelendirilmiş bir ölçüm modelinin veride ne ölçüde desteklendiğini ve hangi belirsizliklerle karşı karşıya olduğunu şeffaf biçimde değerlendirmektir.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.