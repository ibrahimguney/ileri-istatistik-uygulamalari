# Bölüm 16 — Yapısal Eşitlik Modelini Akademik Raporlama

Bu rehber, Bölüm 16'daki yapısal eşitlik modeli (YEM/SEM) uygulamasının bilimsel bir raporda doğru, şeffaf ve ölçülü biçimde sunulmasına yardımcı olur.

Temel raporlama zinciri:

**Kuram → Ölçüm modeli → Yapısal denklem → Ölçekleme → Veri → Tahmin → Global uyum → Yapısal yol → Varyans/R² → Belirsizlik → Eşdeğer modeller → Nedensellik sınırı → Bağımsız doğrulama**

## 1. SEM'in iki bileşenini ayırın

SEM aynı model içinde iki farklı soruyu birleştirir:

1. **Ölçüm modeli:** Gözlenen maddeler gizil yapıları nasıl temsil ediyor?
2. **Yapısal model:** Gizil yapılar birbirleriyle nasıl ilişkilendiriliyor?

Bu bölümde A ve C gizil faktörleri beşer maddeyle ölçülür ve ileri model:

`C = gamma A + zeta_C`

şeklinde kurulur.

Raporunuzda yalnız `A → C` yolunu vermek yeterli değildir; yolun hangi ölçüm modeli içinde tahmin edildiği de açıklanmalıdır.

## 2. Veri ve bağımsız doğrulama sınırını başta belirtin

Analiz Bölüm 14–15 ile aynı ortak 97 tam kayıt üzerinde yürütülmüştür.

Örnek ifade:

> SEM uygulaması, yerel ilk 100 kayıt alıntısındaki on A/C maddesinin ortak 97 tam kaydı üzerinde yürütülmüştür. Aynı kayıtlar önceki AFA ve DFA bölümlerinde de kullanıldığından bu analiz bağımsız doğrulama olarak değerlendirilmemiştir.

## 3. Ön işlemi açıkça raporlayın

- A1, C4 ve C5 bir kez `7−x` ile ters puanlanmıştır.
- Üç eksik satır yalnız tam-kayıt analizinden dışlanmıştır.
- Ham arşiv korunmuştur.
- Eksik değer ataması yapılmamıştır.
- Maddeler `ddof=1` örneklem standart sapmasıyla standartlaştırılmıştır.

Tam kayıt analizi FIML değildir.

## 4. Ölçekleme kararını belirtin

A1 ve C1'in ham marker yükleri `1` olarak sabitlenmiştir.

Bu kısıt gizil faktörlerin ölçeğini belirler.

**Marker yükü 1 = hatasız gösterge** değildir.

A1 örneğinde standartlaştırılmış yük yaklaşık `.304` ve gösterge `R²≈.093`'tür. Dolayısıyla marker kısıtı ölçüm hatasını sıfırlamaz.

## 5. Model parametrelerini ve serbestlik derecesini açıklayın

On gösterge için 55 benzersiz kovaryans momenti vardır.

İleri modelde:

- 8 serbest gösterge yükü,
- 10 gösterge hata varyansı,
- 1 dışsal faktör varyansı,
- 1 yapısal artık varyansı,
- 1 yapısal yol

olmak üzere 21 serbest parametre vardır ve `sd=34` olur.

Sıfır-yol modelinde yol sıfıra sabitlenir; `q=20`, `sd=35` olur.

Pozitif sd tek başına tanımlanabilirlik ispatı değildir; yerel rank ayrıca değerlendirilmiştir.

## 6. Tahmin yöntemini doğru adlandırın

Bu bölümde:

**normal-kuram kovaryans ML + Wishart `(n−1)` çarpanı**

kullanılmıştır.

Ortalama yapısı modellenmemiştir.

Uygulanmayan yöntemler arasında WLSMV, MLR, FIML, profil olabilirlik ve bootstrap vardır.

Altı kategorili maddelerin yaklaşık sürekli kabul edilmesi yöntemsel bir sınırlılık olarak belirtilmelidir.

## 7. Global uyumu raporlayın ama nedenselliğe dönüştürmeyin

İleri model:

- `χ²(34)=45.138`,
- CFI `.936`,
- RMSEA `.058`,
- %90 RMSEA GA `[0,.100]`,
- SRMR `.078`

vermektedir.

Örnek raporlama:

> İleri yapısal model için `χ²(34)=45.14`, `CFI=.936`, `RMSEA=.058`, `%90 GA [0,.100]` ve `SRMR=.078` elde edilmiştir.

Ardından:

> Bu uyum değerleri modelin gözlenen kovaryans yapısını belirli ölçüde yeniden üretebildiğini göstermekte, ancak A'dan C'ye nedensel yönü kanıtlamamaktadır.

şeklinde sınır eklenmelidir.

## 8. Gösterge hatası ve yapısal artığı ayırın

Gösterge hata varyansı, tek bir gözlenen maddenin gizil faktör tarafından açıklanmayan ölçüm kısmıdır.

`zeta_C` ise A tarafından açıklanmayan **gizil C yapısal artığıdır**.

Bunlar farklı model düzeylerindedir.

## 9. Yapısal artık ile toplam gizil varyansı karıştırmayın

İleri modelde:

- `gamma=.739950`,
- `u=Var(A)=.092572`,
- `psi=Var(zeta_C)=.387938`.

C'nin toplam varyansı:

`Var(C)=gamma²u+psi=.438624`.

Bu nedenle `.387938` C'nin toplam varyansı değil, yapısal artık varyansıdır.

## 10. Ham ve standartlaştırılmış yolu ayırın

Ham yol:

`gamma=.739950`.

Standartlaştırılmış yol:

`beta=.339936`.

Ham katsayı marker ölçeğine bağlıdır. Standartlaştırılmış yol farklı ölçeklerdeki yapıları daha karşılaştırılabilir bir biçimde ifade eder; ancak nedensellik kanıtı değildir.

Örnek ifade:

> A'dan C'ye ham yapısal yol `.740`, standartlaştırılmış yol `.340` olarak tahmin edilmiştir.

## 11. Yapısal R²'yi doğru yorumlayın

İçsel C faktörü için:

`R²=.115556`.

Örnek raporlama:

> Model içinde A, C'nin gizil varyansının yaklaşık `%11.6`'lık bölümünü açıklayan/ilişkili yapısal payla temsil edilmiştir (`R²=.116`).

Kesitsel gözlemsel veri nedeniyle “A'daki değişim C'nin %11.6'sına neden olur” gibi bir ifade kullanılmamalıdır.

Bu R², A1 veya başka bir göstergenin madde R²'si değildir.

## 12. Wald sonucunu eksiksiz raporlayın

Ham gamma için:

- `%95 Wald GA [-.045682,1.525582]`,
- `p=.064892`.

Örnek ifade:

> Ham yapısal yol `.740` olarak tahmin edilmiş, normal-kuram Wald %95 güven aralığı `[-.046,1.526]` ve `p=.0649` bulunmuştur.

Aralığın sıfırı kapsadığı açıkça görülmelidir.

## 13. LR sonucunu da raporlayın

Sıfır-yol modeli ile serbest-yol modeli arasındaki LR farkı:

- `Δχ²=6.114847`,
- `Δsd=1`,
- `p=.013405`.

Örnek ifade:

> Yolun sıfıra sabitlendiği modelle serbest bırakıldığı model arasındaki olabilirlik-oranı karşılaştırması `Δχ²(1)=6.11, p=.013` vermiştir.

## 14. Wald ve LR ayrışmasını gizlemeyin

Bu örnekte Wald `p=.0649`, LR `p=.0134` vermektedir.

İki yöntem farklı normal-kuram yaklaşık sınamalardır. Küçük örneklem, zayıf marker ölçeği ve parametrizasyon ayrışmaya katkıda bulunabilir.

Bilimsel raporlama yaklaşımı:

> Wald ve LR sonuçları farklılaştığından iki sınama da yöntemleriyle birlikte raporlanmış; yalnız daha küçük p değerine dayalı sonuç seçilmemiştir.

Bu pakette profil olabilirlik veya bootstrap ek denetimi yapılmamıştır.

## 15. Standart yol belirsizliğini raporlayın

Standart yolun dönüştürülmüş %95 aralığı:

`[.080523,.556219]`.

Bu aralık atanh/delta yaklaşımından geri dönüştürülmüştür; sağlam veya bootstrap aralığı değildir.

## 16. R² aralığının dönüşümünü anlayın

Beta aralığının iki ucu pozitif olduğundan kare görüntüsü:

`[.006484,.309380]`

olur.

Beta aralığı sıfırı kapsasaydı R² dönüşümlü aralığının alt sınırı `0` olurdu.

Simetrik Wald R² aralığı farklı bir yaklaşım olup negatif alt uç üretebilir. Bu negatif uç, negatif R² nokta tahmini değildir.

## 17. İleri ve ters model eşdeğerliğini açıkça raporlayın

Ters parametreleştirmede:

- `delta=.156168`,
- `psi_A=.081875`.

İleri ve ters modeller aynı gözlenen kovaryansı ve aynı global uyumu üretir:

`χ²(34)=45.138`.

Örnek ifade:

> İleri ve ters yapısal parametreleştirmeler aynı gözlenen kovaryans matrisi ve aynı global uyumu üretmiştir. Bu eşdeğerlik nedeniyle kesitsel kovaryans verisi yapısal yönü seçmek için kullanılmamıştır.

## 18. Ham gamma ve delta'yı doğrudan karşılaştırmayın

`.740` değerindeki ileri ham yol ile `.156` değerindeki ters ham yol farklı marker/gizil varyans ölçeklerinde tanımlanmıştır.

Daha küçük ham ters yol:

- daha kötü uyum,
- daha zayıf bilimsel model,
- ileri yönün doğru olması

anlamına gelmez.

## 19. İleri–ters yön için sahte fark testi üretmeyin

İleri ve ters modellerin:

- parametre sayısı aynı,
- serbestlik derecesi aynı,
- gözlenen kovaryansı aynı,
- uyumu aynı

olduğundan `Δsd=0` üzerinden yön seçen bir ki-kare fark testi p değeri üretilmez.

## 20. Eşdeğer model geri besleme kanıtı değildir

İleri ve ters modellerin aynı uyumu göstermesi:

> “A ve C birbirini karşılıklı olarak etkiliyor.”

sonucunu desteklemez.

Karşılıklı geri besleme ayrı bir model ve çoğu durumda ek tasarım/zamansal bilgi gerektirir.

## 21. Nedensellik dilini tasarımla sınırlandırın

Kesitsel kovaryans SEM'inde ok yönü kuramsal modelin parametreleştirmesidir.

Nedensel yorum için en azından:

- zaman sırası,
- alternatif nedenlerin değerlendirilmesi,
- araştırma tasarımı,
- ölçüm geçerliği,
- uygun müdahale/uzunlamasına kanıt

gibi ek dayanaklar gerekir.

## 22. Pozitiflik dönüşümünü aşırı yorumlamayın

Varyansların `exp` dönüşümüyle pozitif tutulması sayısal çözüm alanını düzenler.

Ancak:

- yanlış model,
- zayıf tanımlanabilirlik,
- sınır çözümleri,
- yakınsama sorunları,
- diğer uygunsuz çözümler

otomatik olarak ortadan kalkmaz.

## 23. Sayısal denetimleri model doğruluğu olarak sunmayın

Birden fazla başlangıç, L-BFGS-B/BFGS karşılaştırması, küçük gradyan, türev kontrolleri ve yerel rank çözümün sayısal güvenilirliğini değerlendirmeye yardımcı olur.

Bunlar kuramsal modelin doğru veya nedensel olduğu anlamına gelmez.

## 24. Kurgusal aracılık örneğini ayrı tutun

Kurgusal değerler:

- `a=.48`,
- `b=.41`,
- `c′=.19`.

Dolaylı etki:

`ab=.1968`.

Toplam:

`.3868`.

Bu yalnız cebir örneğidir.

Uygun ifade:

> Aracılık katsayıları gerçek A/C verisinden tahmin edilmemiş, yalnız dolaylı ve toplam etkinin cebirsel gösterimi için kullanılmıştır.

Veri olmadan bu sayılardan bootstrap aralığı veya p değeri üretilemez.

## 25. Yazılım kaynağını doğru belirtin

Referans sonuçlar Python uygulamasından gelmektedir.

R/lavaan betiği hazırlanmıştır fakat bu dağıtım hazırlanırken çalıştırılarak doğrulanmamıştır.

`amos-kontrol-listesi.md` AMOS çıktısı değildir.

Örnek ifade:

> Sayısal sonuçlar bölümün Python uygulamasından elde edilmiştir; R/lavaan ve AMOS bu paket hazırlanırken çalıştırılarak doğrulanmamıştır.

## 26. Yapılmamış analizleri rapora eklemeyin

Bu pakette yapılmamıştır:

- WLSMV,
- MLR,
- FIML,
- profil olabilirlik,
- bootstrap,
- ölçüm değişmezliği,
- yeni örneklemde SEM doğrulaması,
- gerçek aracılık modeli.

## 27. Yeni bir SEM çalışması için protokol yazın

Yeni araştırmada önceden tanımlanması gereken temel kararlar:

1. gizil yapılar ve göstergeler,
2. ölçüm zamanları,
3. ölçekleme yöntemi,
4. yapısal yollar ve sıfır kısıtları,
5. alternatif/eşdeğer modeller,
6. veri türü ve tahminleyici,
7. eksik veri yaklaşımı,
8. örneklem planı,
9. uyum ve belirsizlik raporlama planı,
10. modifikasyon sınırları,
11. bağımsız doğrulama,
12. gerekiyorsa ölçüm değişmezliği.

Aracılık planlanıyorsa zaman sırası, tam aracılık modeli, dolaylı etki, bootstrap örnekleme birimi ve başarısız çözümlerin nasıl ele alınacağı ayrıca önceden belirtilmelidir.

## 28. Örnek bütünleşik SEM raporu

> On A/C maddesinin ortak 97 tam kaydı üzerinde marker yükleri A1 ve C1 için 1'e sabitlenerek, ortalama yapısı olmadan normal-kuram Wishart ML ile iki gizil yapılı SEM kurulmuştur. İleri modelde C, A üzerine yapısal olarak regres edilmiştir. Model `χ²(34)=45.14`, `CFI=.936`, `RMSEA=.058`, `%90 GA [0,.100]` ve `SRMR=.078` vermiştir. Ham yapısal yol `gamma=.740` olup Wald %95 aralığı `[-.046,1.526]` ve `p=.0649` bulunmuştur; buna karşılık yolun sıfıra sabitlendiği modelle LR karşılaştırması `Δχ²(1)=6.11, p=.0134` vermiştir. İki yaklaşık sınama arasındaki ayrışma gizlenmemiştir. Standartlaştırılmış yol `.340`, C'nin yapısal `R²` değeri `.116` olarak hesaplanmıştır. Ters model aynı gözlenen kovaryans ve uyumu ürettiğinden kesitsel veri nedensel yönü seçmek için kullanılmamıştır. Sonuçlar aynı 97 kayıt üzerindeki öğretim uygulamasıdır; R/lavaan/AMOS, WLSMV/MLR/FIML, bootstrap, ölçüm değişmezliği veya bağımsız SEM doğrulaması yapılmamıştır.

## 29. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Aynı 97 kaydın B14–B15'te de kullanıldığı belirtilmiş mi?
- Bağımsız doğrulama iddiasından kaçınılmış mı?
- Ölçüm modeli ve yapısal model ayrı tanımlanmış mı?
- Marker yükleri ve ölçekleme kararı açıklanmış mı?
- Marker=1 hatasız gösterge diye yorumlanmamış mı?
- Gösterge hatası ile yapısal artık ayrılmış mı?
- 55 moment ve 21 parametre doğru sayılmış mı?
- Tahmin yöntemi normal-kuram Wishart ML olarak belirtilmiş mi?
- Tam kayıt FIML diye adlandırılmamış mı?
- Altı kategorili verinin yaklaşık sürekli kabulü sınırlılık olarak belirtilmiş mi?
- Global uyum nedensellik kanıtına dönüştürülmemiş mi?
- `gamma`, `u`, `psi` ve `Var(C)` ayrılmış mı?
- Yapısal artık toplam varyans diye sunulmamış mı?
- Ham ve standart yol ayrılmış mı?
- Yapısal R² madde R²'siyle karıştırılmamış mı?
- Wald aralığı/p raporlanmış mı?
- LR testi ayrıca raporlanmış mı?
- Küçük p seçilmemiş mi?
- Beta ve R² aralıklarının dönüşüm mantığı doğru mu?
- İleri ve ters modellerin eşdeğerliği belirtilmiş mi?
- Ham gamma/delta büyüklüklerinden yön seçilmemiş mi?
- İleri–ters için sahte sd=0 p değeri üretilmemiş mi?
- Eşdeğerlik geri besleme kanıtı sayılmamış mı?
- Nedensel dil araştırma tasarımıyla sınırlandırılmış mı?
- Pozitiflik dönüşümü bütün Heywood sorunlarını çözer denmemiş mi?
- Kurgusal aracılık gerçek veri sonucu olarak sunulmamış mı?
- Kurgusal katsayılara bootstrap/p uydurulmamış mı?
- Python sonuçları lavaan/AMOS sonucu diye gösterilmemiş mi?
- Yapılmamış WLSMV/MLR/FIML/değişmezlik sonuçları eklenmemiş mi?

## Son mesaj

SEM'de temel bilimsel düşünce zinciri şöyledir:

**Kuram → Ölçüm modeli → Yapısal model → Ölçekleme → Tanımlanabilirlik → Tahmin → Global uyum → Yol → Varyans/R² → Belirsizlik → Eşdeğer modeller → Nedensellik sınırı → Yeni veride doğrulama → Akademik raporlama**

İyi SEM, diyagramdaki okun yönünü veri tarafından kanıtlanmış nedensellik gibi okumak değildir. Güçlü uygulama, **ölçüm ve yapısal varsayımları açıklaştırır, eşdeğer modelleri dikkate alır, belirsizliği eksiksiz raporlar ve nedensel iddiayı araştırma tasarımının izin verdiği düzeyle sınırlar.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.