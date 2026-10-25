# Bölüm 19 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

Keşif aşamasında model örneklemin rastlantısal özelliklerine uydurulmuştur; aynı veride sınandığında bu özellikler yeniden “doğrulanır” ve uyum iyimser çıkar. Bağımsız kanıt için model, keşifte kullanılmayan veride (ayrılmış yarım veya yeni örneklem) önceden yazılmış biçimde sınanmalıdır.

## Kolay Düzey

1.  DFA önceden belirtilen yük ve kovaryans kısıtlarını sınar; AFA daha serbest bir yük yapısını keşfeder. Aynı veride AFA sonrası DFA bağımsız doğrulama değildir.

2.  CFI ve TLI hedef modeli bağımsızlık başlangıç modeliyle karşılaştırır; TLI serbestlik derecelerini de kullanır. Tek başlarına madde kalitesini göstermezler.

3.  Diğer koşullar benzerken yaklaşık uyumsuzluk artar. Nokta tahminiyle birlikte güven aralığı, örneklem ve serbestlik derecesi değerlendirilir.

4.  Faktörün göstergelerinde temsil ettiği ortalama varyansı özetler; yakınsak geçerlik incelemesine katkı sağlar, tek başına geçerlik veya güvenirlik kanıtı değildir.

5.  MI beklenen yerel ki-kare azalmasına ilişkin bir yaklaşımdır. İçerik, beklenen parametre değişimi ve bağımsız sınama planıyla birlikte kullanılmalı; otomatik model aramasına dönüştürülmemelidir.

## Orta Düzey

1.  CFI=.88, TLI=.86 ve RMSEA=.091 kayda değer uyumsuzluk düşündürür; ancak sabit eşiklerle tek karar verilmez. RMSEA aralığı, artıklar, kestirici ve model kısıtları incelenir.

2.  Hayır. Yükün belirsizliği, artık varyansı, kodlama, içerik kapsamı ve başka örneklemdeki kararlılık incelenir; .39 otomatik silme eşiği değildir.

3.  Ortak ifade, içerik veya yöntem etkisi önceden gerekçelendirilebiliyorsa düşünülebilir. Yalnız MI yüksekliği yeterli değildir; ekleme ve veri sonrası niteliği raporlanıp yeni veride sınanır.

4.  İlgili faktör göstergelerinin ortak varyansı sınırlı olabilir. Global uyum ve CR yüksekliği bu sorunu ortadan kaldırmaz; içerik ve yükler birlikte incelenir.

5.  DFA belirli bir ölçüm modelinin verilere uyumunu inceler. Dilsel/kültürel uygunluk, dış ölçüt ilişkileri, değişmezlik ve kullanım amacına ilişkin kanıtların yerine geçmez.

## İleri Düzey

1.  Örnekleme aşırı uyum ve tekrarlanamama riski doğar. Veri sonrası kararlar açıkça ayrılmalı, sabitlenen model yeni veride sınanmalıdır.

2.  İki faktörün yeterince ayrışmadığı düşünülebilir. Korelasyonun belirsizliği, içerik, çapraz yükler ve alternatif modeller incelenir; tek değer kesin hüküm değildir.

3.  Kategori sayısı, dağılım ve kestirici uyumu incelenir. Ordinal modelde eşikler/polikorik ilişkiler ve uygun WLSMV gibi bir yöntem düşünülebilir; sürekli veri için sağlam ML kullanmak ordinal model kurmakla aynı değildir.

4.  İçerik kapsamı korunarak kodlama, anlaşılabilirlik, yük aralığı ve artıklar incelenir. Revizyon veya çıkarma kararı yeni veri planıyla gerekçelendirilir; salt sayısal artış yeterli değildir.

5.  Kaynak ve örneklem, eksikler/puanlama, model ve ölçeklendirme, kestirici, parametre sayısı/sd, yükler ve belirsizlikleri, artık varyansları, faktör korelasyonları, uyum/artıklar, AVE/CR tanımları, modifikasyonlar ve bağımsız doğrulama durumu verilmelidir.

## D1–D3: Veri ve Kanıt Sınırı

1.  Yarım B’deki 1316 kişi AFA’da hiç kullanılmadı ve modeller (M1 ile M2’nin hata çiftleri) yarım B açılmadan önce yazıldı. Böylece keşifte yakalanan örnekleme özgü dalgalanmalar DFA’yı iyimser göstermez; sınama örneklem içi çapraz geçerlemedir. Kalan sınır: iki yarı aynı çevrimiçi, çoğunluğu ABD’li gönüllü örneklemden gelir. Başka anakütle, dil (Türkçe form) veya toplama koşulunda kopyalama yerine geçmez; ayrıca bölme öncesi 168 eksik kaydın dışlanması her iki yarıyı da aynı biçimde etkiler.

2.  A1, C4 ve C5 bir kez $7-x$ ile ters puanlanır. Bölme tam kayıtlarda yapıldığı için yarım B’de eksik yoktur; n = 1316’dır. Gözlenen maddelerin örneklem standart sapmasıyla standartlaştırılması $S$’nin köşegenini 1 yapar. Bu, ayrı bir model kararı olan gizil faktör varyanslarını 1’e sabitlemek değildir.

3.  Hesaplanan yöntem, altı kategorili yanıtları yaklaşık sürekli kabul eden normal kuramlı kovaryans ML’dir; Wishart çarpanı $n-1=1315$’tir. Sağlam ML düzeltmesi, WLSMV, FIML veya ordinal eşik modeli çalıştırılmamıştır. Liste boyu dışlama da eksiklik mekanizmasının zararsız olduğunu kanıtlamaz.

## G1–G4: Rehberli Çözüm

1.  On değişkende $10(11)/2=55$ benzersiz kovaryans momenti vardır. M1’de 10 birincil yük, 10 artık varyansı ve 1 faktör korelasyonu olmak üzere $q=21$ serbest parametre bulunur; $sd=55-21=34$’tür. M2 üç hata kovaryansı ekler: $q=24$, $sd=31$. Faktör varyansları 1’e sabittir. İşaretleyici yaklaşımında bunun yerine bir yük sabitlenip faktör varyansı tahmin edilir; iki ölçeklendirme aynı anda dayatılmaz. Pozitif sd tek başına tanımlanabilirliği garanti etmez; bu uygulamada sayısal Jacobian tam sütun ranklıdır.

2.  $T=1315(.2334523886)=306.990$, $sd=34$, $p<.001$ bulunur. Bağımsızlık modelinde $T_b=2703.402$, $sd_b=45$ olduğundan $$\mathrm{CFI}=1-\frac{306.990-34}{2703.402-45}=1-\frac{272.990}{2658.402}=.897.$$ TLI $=(2703.402/45-306.990/34)/(2703.402/45-1)=(60.076-9.029)/59.076=.864$. RMSEA için $$\sqrt{\frac{306.990-34}{1316(34)}}=\sqrt{.006101}=.078.$$ Wishart testinde 1315, bu RMSEA tanımının paydasında 1316 kullanılmıştır. Merkezi olmayan ki-kare terslemesiyle %90 GA $[.070,.086]$ bulunur. Alt sınırın .05’in açıkça üstünde olması, büyük örneklemde yaklaşık uyumsuzluğun rastlantıyla açıklanamayacağını gösterir; model yararsız değildir ama yerel sorunlar incelenmelidir.

3.  A1’in standart yükü .345’tir: $R^2=.345^2=.119$ ve standart artık varyansı $1-R^2=.881$ olur. Yük için %95 Wald GA $[.290,.401]$ sıfırı rahatça dışlar; buna rağmen maddenin varyansının yalnız %12’si faktörle açıklanır. Büyük örneklem küçük yükleri de “anlamlı” yapar; istatistiksel ayrışma güçlü ölçümle aynı değildir. Bu aralık normal kuramlıdır; sağlam veya bootstrap aralığı değildir.

4.  A için $\sum\lambda=2.866728$, $\sum\lambda^2=1.741045$ ve $\sum\theta=3.258955$ olur: $$\begin{aligned}
    \mathrm{AVE}_A&=\frac{1.741045}{5}=.348,\\
    \mathrm{CR}_A&=\frac{(2.866728)^2}{(2.866728)^2+3.258955}=\frac{8.218129}{11.477084}=.716.
    \end{aligned}$$ AVE karelerin toplamını, CR toplamın karesini kullanır. Bu CR, M1’in model-standartlaştırılmış beş göstergesinin eşit ağırlıklı toplamı için omega türü bileşik güvenirliktir. Tek ilgili faktör, sıfır çapraz yük ve ilişkisiz artıklar varsayılmıştır; ham alfa veya bütün on maddenin güvenirliği değildir.

## B1–B3: Bağımsız Çözüm

1.  M0’da $\chi^2(35)=393.467$, M1’de $\chi^2(34)=306.990$; fark $\Delta\chi^2(1)=86.477$, $p<.001$’dir. Faktör ilişkisini serbest bırakmak uyumu belirgin biçimde iyileştirir ($\hat\phi=.340$). M0 yalnız faktörler arası ilişkiyi sıfırlar; her beşli içindeki ilişkileri modellemeye devam eder. CFI başlangıç modeli ise bütün gözlenen kovaryansları sıfırlar ve $sd=45$’tir.

2.  M2’de $\chi^2(31)=180.541$, CFI $=.944$, TLI $=.918$, RMSEA $=.061$ (%90 GA $[.052,.069]$), SRMR $=.041$ bulunur. M1–M2 farkı $\Delta\chi^2(3)=126.449$, $p<.001$’dir; $\mathrm{AIC}^*$ 348.99’dan 228.54’e, $\mathrm{BIC}^*$ 457.82’den 352.92’ye düşer. Fark, seçim sürecindedir: bu üç çift yarım A’nın artıklarından ve madde içeriğinden, yarım B’ye bakılmadan yazıldı. Yarım B’nin MI listesinde ilk üç sırada çıkmaları bu nedenle bağımsız bir yineleme bulgusudur. MI listesine bakıp en büyük değerleri eklemek ise aynı veride arama olurdu; nominal p değerleri seçimi hesaba katmaz ve A1–C4 veya C$\to$A4 gibi içerik gerekçesi zayıf parametreleri de modele sokardı.

3.  M2’de C yükleri $\sum\lambda=2.861928$, $\sum\lambda^2=1.650621$, $\sum\theta=3.349379$; üstelik C1–C2 (.137) ve C4–C5 (.150) hata kovaryansları pozitiftir. Toplam puanın faktöre ait olmayan ortak varyansı paydaya $2(.137232+.149723)=.573910$ olarak eklenir: $\mathrm{CR}=8.190632/(8.190632+3.349379+.573910)=.676$. M1 bu ortak hata varyansını faktöre yazdığı için CR’yi (.736) olduğundan yüksek gösterir. M1’de $\phi=.340$, $\phi^2=.115$; her iki AVE (.348, .359) bu kareden büyüktür. Bu sınırlı bir ayırt edicilik taramasıdır; düşük AVE’leri, içerik sorunlarını veya belirsizliği ortadan kaldırmaz. Türkçe katılımcı yanıtları, yerel uyarlama ve değişmezlik kanıtı bulunmadığından Türkçe ölçek geçerliği sonucuna varılmaz.

## H1: Raporu Onarma

1.  1316 kişide ki-kare, anakütlede küçük ama sistematik sapmaları bile reddeder. Ret “yapı yok” demek değildir: M1’de bütün yükler .345–.752 aralığında, $\hat\phi=.340$’tır; yaklaşık uyum ve yerel artıklar birlikte okunur.

2.  MI listesinden sonuç görüldükten sonra altı parametre eklemek aynı veride model aramasıdır; CFI’nin .95’i geçmesi doğrulama değil, örnekleme uyarlanmadır. Bu bölümde yalnız önceden yazılmış üç çift sınanmıştır; A1–C4, C2–C5 ve C$\to$A4 eklenmemiş, raporlanmıştır.

3.  C’de CR=.736 iken AVE=.359’dur. Güvenirlik ve ortalama temsil edilen varyans farklı soruları yanıtlar; biri diğerinin yerine geçmez.

4.  Tersine: hata kovaryansları pozitif olduğunda doğru CR paydası büyür ve C’nin CR’si .736’dan .676’ya düşer. Uyum iyileşir ama güvenirlik “artmaz”; ortak hata varyansının faktöre yazılması düzeltilmiş olur.

5.  Rastgele bölme örneklem içi çapraz geçerlemedir. Aynı örneklemin iki yarısı kullanılmıştır; başka anakütlede, başka dilde veya farklı koşullarda kopyalama yapılmamıştır.

## P1: Bağımsız Doğrulama Protokolü

Örnek protokol, yeni hedef grupta (örneğin Türkçe formun uygulandığı bir örneklemde) iki ilişkili faktörlü M1’i ana model, üç hata çiftli M2’yi önceden gerekçelendirilmiş alternatif olarak tanımlar; çiftlerin `bfi` yarım A’da bulunup yarım B’de yinelendiği yazılır. Yarım B’de önceden öngörülmeden görülen A4–C artıkları ve C$\to$A4 çapraz yükü *yeni hipotez* olarak, yönleriyle birlikte, üçüncü model biçiminde önceden kaydedilir; yeni veride sonuç ne olursa olsun raporlanır. A1 ve A4 için içerik ve anlaşılabilirlik incelemesi planlanır; yapılmamış uzman görüşmesi veya bilişsel görüşme “planlandı; henüz veri yok” olarak belirtilir. Kaynak, kullanım hakları, dilsel uyarlama adımları ve puanlama anahtarı ayrı belgelenir.

Örneklem planı sabit kişi/madde kuralıyla değil, beklenen yükler (.30–.75), model karmaşıklığı, kategori dağılımları ve hedef belirsizlik üzerinden gerekçelendirilir; benzetim yapılmadıysa yapılmış gibi yazılmaz. Eksik yanıtların tanımı, dışlama kuralı ve gerekçesi; ordinal veya yaklaşık sürekli model tercihi, kestirici ve raporlanacak standart hata/test düzeltmeleri önceden belirlenir. Karşılaştırılacak gruplar varsa ölçme değişmezliği planı gerekir. Modifikasyonlar içerik gerekçesiyle sınırlanır; veri sonrası değişiklikler ayrı raporlanır ve yeni doğrulama gerektirir.

Teslim dosyasında kaynak/ön işlem günlüğü, model kısıtları ve ölçeklendirme, uyum ve artık tabloları, yük belirsizlikleri, AVE/CR tanımları (hata kovaryanslı CR dâhil), yazılım/sürüm ve yeniden üretim komutları bulunur. Rubrik: kaynak/ön işlem 20, model/hesap 30, belirsizlik/yorum 25, bağımsız doğrulama planı 15, yeniden üretim 10 puan.
