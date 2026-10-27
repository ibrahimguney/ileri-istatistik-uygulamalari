# Bölüm 7 — açıklamalı çözümler

Revizyon 25 bütünlük düzeltmeleri.

## Kendinizi Sınayın

Her test $\alpha=.05$ ile yapılırsa en az bir yanlış ret olasılığı testler bağımsız sayıldığında $1-(.95)^3\approx.14$’tür; testler aynı gruplar üzerinden ilişkili olsa da hata birikir. ANOVA tek genel test yapar; ardından planlı karşıtlıklar veya Tukey gibi aile boyu hatayı denetleyen yöntemler kullanılır.

## Kolay Düzey

1.  Tüm grup ortalamalarının eşit olmasıdır.

2.  $SSW$ grup içi/hata değişkenliğini gösterir.

3.  Araştırma sorusuna göre planlı karşıtlıklar veya çoklu karşılaştırma düzeltmeli çiftler incelenir; genel F testi düzeltmesiz bütün çiftleri tarama izni değildir.

4.  Eşit olmayan varyanslarda ortalama karşılaştırması için Welch düşünülebilir. Sıra temelli Kruskal–Wallis farklı bir hipotezi sınar; otomatik olarak ortalama testi yerine konmaz.

5.  $\eta^2=SSG/SST$, örneklemdeki toplam kareler toplamının gruplar arasına düşen oranıdır; nedensel açıklama değildir.

## Orta Düzey

1.  Çoklu t-testleri Tip I hatayı artırır; ANOVA tek genel test sağlar.

2.  En az bir ortalama farklıdır; hangi grubun farklı olduğunu söylemez.

3.  Bir faktörün etkisi diğer faktör düzeyine bağlıdır.

4.  Dört grup vardır; genel ANOVA anlamlıdır.

5.  İhlalin şiddeti ve Welch gibi sağlam seçenekler incelenir.

## İleri Düzey

1.  Genel F ve tanımlanmış ailenin bütün çiftleri, fark yönleri, düzeltilmiş p değerleri ve eşzamanlı aralıklarıyla raporlanır. Yalnız bir çiftin anlamlı olması genel testle çelişmez; diğer sonuçlar saklanmaz.

2.  Etkileşim koşullu örüntüyü değiştirdiği için ana etkiler tek başına yanıltabilir.

3.  İstatistiksel sonuç güçlü, pratik etki küçük olabilir.

4.  Doğal gruplarda nedensellik için rastgele atama yoktur.

5.  Kareler toplamı türü, karşıtlık kodlaması, hücre büyüklükleri, boş hücreler, hata terimi ve marjinal ortalamaların ağırlıkları incelenir. Dengeli örnekteki Tip II/III eşitliği bu tasarıma otomatik taşınmaz.

## Gerçek Veri Etkinliklerinin Açıklamalı Yanıtları

Aşağıdaki sonuçlar Bölüm 6 ile paylaşılan 60 kayıtlık ToothGrowth veri kopyasından yeniden hesaplanmıştır. Raporlanan uzunlukların birimi kısa kaynak belgesinde belirtilmediği için fiziksel birim eklenmez. Yuvarlamalar gösterim içindir; hesaplarda tam duyarlık kullanılır.

## D: Tasarımı Okuma

1.  Uygulama iki düzeylidir (OJ, VC); doz üç düzeylidir (0.5, 1, 2 mg/gün). Altı hücrenin her birinde 10 ayrı hayvan, toplamda 60 analiz birimi bulunur. Aynı hayvanın üç dozda tekrar ölçülmesi söz konusu değildir; dozları eşleştirilmiş ölçüm gibi analiz etmek yanlıştır.

2.  OJ tek yönlü hipotezi $\mu_{OJ,0.5}=\mu_{OJ,1}=\mu_{OJ,2}$’dir. Etkileşim hipotezi ise üç dozda $\delta_j=\mu_{OJ,j}-\mu_{VC,j}$ farklarının eşit olmasıdır. Birincisi OJ içindeki doz farkını, ikincisi doz örüntüsünün uygulamaya göre değişip değişmediğini sınar.

3.  Üç düzeyli faktör doz ortalamaları için iki serbestlik derecesi kullanır. Sayısal doz tek eğimle doğrusal bir örüntü dayatır; 0.5–1 aralığı ile 1–2 aralığı da eşit değildir. Bu iki model aynı hipotez değildir.

## G: Rehberli Hesaplar

1.  OJ genel ortalaması 20.66333’tür. Grup ortalamaları 13.23, 22.70 ve 26.06; grup SS değerleri 4.45971, 3.91095 ve 2.65506’dır. $SSG=885.26467$, $SSW=380.10500$, $SST=1265.36967$ bulunur. Üç ayrı grup ortalaması tahmin edildiğinden hata sd’si $30-3=27$; toplam sd $30-1=29$ olur. $MSG=442.63233$, $MSE=14.07796$, $F(2,27)=31.44150$, $p<.001$. $\eta^2=.69961$ ve $$\omega^2=\frac{885.26467-2(14.07796)}{1265.36967+14.07796}=.66991.$$ Bu oranlar örneklem ve modele bağlıdır; genel bir nedensel etki oranı değildir.

2.  OJ grubunda 2–1 mg ortalama farkı 3.36’dır. Tukey düzeltilmiş $p=.13093$ ve eşzamanlı %95 güven aralığı $[-0.80040,7.52040]$ bulunur. Genel test tüm ortalamaların eşitliğini reddeder; bu çiftin farklı olduğunu tek başına söylemez. Diğer iki Tukey aralığı sıfırın üzerindedir. Games–Howell aynı çift için $p=.09352$ ve $[-0.50094,7.22094]$ verir. İki yöntem de bu çift için sıfır farkı dışlamaz; bu, dozların eşdeğerliğini kanıtlamaz.

3.  Tam modelde $205.35000+2426.43433+108.31900+712.10600=3452.20933$. Hata serbestlik derecesi $60-6=54$ ve ortak hata kareler ortalaması $MSE=13.18715$’tir. Etkileşim için $$\begin{aligned}
    F&=(108.319/2)/13.18715=4.10699,\\
    \eta_p^2&=108.319/(108.319+712.106)=.13203
    \end{aligned}$$ bulunur. Doz 1 için OJ–VC farkı 5.93’tür. Ortak standart hata $$SH=\sqrt{13.18715(1/10+1/10)}=1.62402$$ ve üçlü Bonferroni aralığı $5.93\pm t_{1-.05/(2\cdot3),54}(1.62402)=[1.91730,9.94270]$’tir. Düzeltilmiş $p=.00177$. Bölüm 6’daki ayrı Welch aralığı $[2.80215,9.05785]$ ile aynı değildir: hata varyansı, sd ve karşılaştırma ailesi farklıdır.

## B: VC Grubunda Bağımsız Uygulama

1.  VC ortalamaları sırasıyla 7.98, 16.77, 26.14; SS değerleri 2.74663, 2.51531, 4.79773’tür. Her grupta $n=10$ ve genel ortalama 16.96333’tür. $SSG=1649.48867$, $SSW=332.00100$, $SST=1981.48967$, $MSE=12.29633$. Böylece $F(2,27)=67.07238$, $p<.001$, $\eta^2=.83245$ ve $\omega^2=.81498$ bulunur.

2.  Aşağıda her fark yüksek doz eksi düşük dozdur. İki yöntemde de üç aralık sıfırın üzerindedir; her yöntemin kendi üç çiftlik ailesi vardır.

    <div class="center">

    | Doz çifti |  Fark |          Tukey %95 GA |             GH %95 GA |
    |:----------|------:|----------------------:|----------------------:|
    | 1–0.5     |  8.79 |  $[4.90176,12.67824]$ |  $[5.78218,11.79782]$ |
    | 2–0.5     | 18.16 | $[14.27176,22.04824]$ | $[13.59636,22.72364]$ |
    | 2–1       |  9.37 |  $[5.48176,13.25824]$ |  $[4.87139,13.86861]$ |

    </div>

    Tukey düzeltilmiş p değerleri sırasıyla .00001755, $1.6593\times10^{-11}$ ve .00000661’dir. Games–Howell p değerleri .00000196, .00000013 ve .00025258’dir. Welch genel testi $F(2,17.16451)=59.37220$, $p<.001$ verir; klasik testin $MSE$’si veya sd’si bu teste taşınmaz.

3.  Örnek rapor: “VC grubundaki 30 ayrı hayvanda ortalama uzunluklar 0.5, 1 ve 2 mg/gün için 7.98, 16.77 ve 26.14’tür. Eşit hata varyanslı tek yönlü ANOVA doz ortalamalarının eşitliğini reddetmiştir, $F(2,27)=67.07$, $p<.001$, $\eta^2=.832$. Üç çiftlik Tukey ailesinde tüm yüksek doz–düşük doz aralıkları pozitiftir. Welch ve Games–Howell duyarlılık incelemesi de bu örüntüyü desteklemiştir. Sonuçlar bu hayvan verisiyle sınırlıdır; insanlara genellenmez.” VC ve OJ içi p değerlerinin karşılaştırılması etkileşim testi yerine geçmez.

## H1: Hatalı İddiaları Düzeltme

1.  Genel F, bütün ortalamaların eşitliği hipotezini sınar; bütün çiftlerin farklılığını göstermez. OJ 2–1 mg çifti bunun somut karşı örneğidir.

2.  Levene testinin anlamlı olmaması eşit varyansı kanıtlamaz. Hücre başına 10 kayıtta tanı gücü sınırlıdır; grafikler, tasarım ve duyarlılık birlikte değerlendirilir.

3.  Sayısal doz doğrusal eğim; faktör doz iki bağımsız ortalama karşıtlığı getirir. Üç düzey bulunması onları aynı model yapmaz.

4.  59 toplam sd’dir; altı hücre ortalaması tahmin edilen tam modelin hata sd’si 54’tür.

5.  Kısmi eta-karelerin paydaları farklıdır. .22383, .77311 ve .13203 toplanıp açıklanan toplam oran olarak yorumlanamaz.

6.  “Bir dozda anlamlı, diğerinde değil” farkların birbirinden farklı olduğunu kanıtlamaz. Ortak modelde etkileşim karşıtlıkları sınanmalıdır; burada klasik $F(2,54)=4.10699$, $p=.02186$ bulunur.

## P1: Yeniden Üretim ve Değerlendirme

Başarılı teslimde kaynakta 60 ayrı kayıt, altı hücre ve hücre başına 10 gözlem doğrulanır; doz faktör olarak kodlanır. OJ ve VC alt kümeleri birbirinden ayrı hayvanlardır; VC etkinliği dış doğrulama veri seti değildir.

Tam modelde uygulama, doz ve etkileşim F değerleri sırasıyla 15.57198, 91.99996 ve 4.10699’dur. Üç dozun OJ–VC farkları 5.25, 5.93, $-0.08$; üçlü Bonferroni düzeltilmiş p değerleri .00628, .00177, 1.00000’dır. Eşzamanlı aralıklar $[1.23730,9.26270]$, $[1.91730,9.94270]$ ve $[-4.09270,3.93270]$ olur. Son dozda farkın dışlanmaması uygulamaların eşdeğer olduğunu kanıtlamaz.

Artık Shapiro $p=.66942$ ve altı hücre için medyan merkezli Levene $p=.14836$ varsayımların kanıtı değildir. Q–Q ve artık grafikleriyle birlikte raporlanır. HC3 ortak etkileşim testi yaklaşık $F(2,54)=3.52285$, $p=.03647$ verir. Klasik testle karar yönü benzer olmakla birlikte bu test ortak klasik MSE’nin oranı değildir; HC3 bağımlı gözlemleri bağımsız hâle getirmez.

Değerlendirme: kaynak ve hücre kodlaması 20; kareler toplamları ve etki büyüklükleri 25; karşılaştırma aileleri ve aralıklar 25; etkileşim, tanılar ve HC3 20; yeniden üretilebilirlik ve sınırlılıklar 10 puan. Kod, veri sözlüğü, üç grafik ve bir sayfalık rapor beklenir. OJ, VC ve basit etkilerin ayrı öğretim aileleri olduğu belirtilmeli; tüm bölüm için tek bir .05 aile hatası kontrolü iddia edilmemelidir. R/SPSS çıktıları ancak bu yazılımlarda gerçekten çalıştırılmışsa doğrulanmış sayılır.

## T1–T3: Hedef ve Etkileşim Denetimi

1.  Eşit doz ağırlıkları $1/3$ ile fark 4.376111; ortak örneklem doz ağırlıkları ile 4.220660’dır. 5.654783 her grubun kendi doz bileşimiyle ham farktır; aynı doz dağılımına standartlaştırılmış fark değildir. Farklı hedefler hata veya daha doğru p seçimi diye sıralanmaz.

2.  Etkileşim doğrudan farkların farkıdır. 1–.5 ve 2–.5 kestirimleri $-2.570$ ve $-7.461667$; yalnız bu iki kontrastın HC3/t–Bonferroni aralıkları $[-9.354,4.214]$ ve $[-14.603,-.320]$’dir. Aile bütün hedefleri kapsamaz. Bir koşulun anlamlı, diğerinin anlamsız olması farklarının anlamlı olduğunu göstermez. Küçük hücrelerde HC3 t yaklaşımı kesin test değildir.

3.  Alt küme, altı hücreden kaynak sırasıyla 5/10/8 ve 10/6/9 kayıt seçilen öğretim örneğidir; ana veri değişmez, yeni gözlem veya rastgele kayıp üretilmez. Tip III etiketi tek başına hipotezi açıklamaz; kontrast, kodlama ve hedef ağırlıklar yazılır.

## Ç1 çıkış sorusunun yanıtı

Hayır. Omnibus test tüm ortalamaların eşitliğiyle ilgilidir; hangi karşıtlığın neyi sınadığı ve aile düzeltmesi ayrıca belirlenir.
