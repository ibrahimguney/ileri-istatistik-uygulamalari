# Bölüm 9 — açıklamalı çözümler

Revizyon 12; kuramsal sınırlar ve yeni T1–T3 dahil.

## Kendinizi Sınayın

\(1\) Bağımlı değişkenler arasındaki ilişki (kovaryans) bilgisini: gruplar ancak değişkenlerin bir bileşiminde ayrışıyorsa ayrı testler bunu göremez. (2) Aile boyu hata denetimini: ilişkili değişkenler üzerindeki çoklu testler Tip I hatayı biriktirir.

## Kolay Düzey

1.  Bütün grupların bağımlı değişken ortalama vektörlerinin eşit olmasıdır: $\boldsymbol\mu_1=\boldsymbol\mu_2=\dots=\boldsymbol\mu_g$. Bu, her değişkende tek tek eşitliği ve bütün doğrusal bileşimlerde eşitliği birlikte içerir.

2.  Köşegen öğeler her bağımlı değişkenin (arası veya içi) kareler toplamıdır; köşegen dışı öğeler iki değişkenin çapraz çarpımlarının toplamı, yani birlikte değişimidir.

3.  Pillai izi birçok koşulda görece dayanıklıdır; dengesizlik ve heterojen kovaryansta nominal hata kontrolünü garanti etmez.

4.  İki grubun birden çok bağımlı değişkendeki ortalama vektörlerini karşılaştırmak için; tek değişkenli bağımsız t-testinin çok değişkenli genellemesidir. Tekrarlı ölçümlerde tek örneklem biçimi karşıtlık puanlarına uygulanır.

5.  Grupların kovaryans matrislerinin eşitliğini; normalliğe duyarlı olduğundan betimsel kovaryans incelemesiyle birlikte okunur. .001 bir evrensel seçim eşiği değildir; anlamsızlık eşitlik kanıtı olmaz.

## Orta Düzey

1.  Yüksek korelasyon ortaklık gösterir, aynı yapıyı ölçtüklerini kanıtlamaz. Grup-içi kovaryansın koşulluluğu ve ölçme kuramı incelenir. Kuramsal olarak geçerli bileşik puan veya birincil sonuç düşünülebilir; sırf korelasyon yüksek diye birleştirme yapılmaz.

2.  $1-\Lambda^{1/s}=1-.80^{1/2}=1-.894=.106$.

3.  Tek değişkenli sonuç önceden planlanmışsa ve düzeltilmişse ayrıca raporlanabilir. Önceden planlanmamışsa, anlamsız genel testten sonra bir değişkeni seçmek çoklu karşılaştırma sorunudur; keşif olarak etiketlenir. MANOVA’nın gücü, etkisiz değişkenler eklendiğinde düşebilir; bu da neden olabilir.

4.  Pillai görece dayanıklı bir seçenek olabilir. Küçük grupta yüksek varyans liberal sonuç riskini düşündürür; gerçek hata oranı tasarıma/dağılıma bağlıdır. Önceden seçilmiş hedefe uygun heterojen kovaryans duyarlılığı gerekir; veri azaltarak grupları dengelemek veya etiketleri körlemesine permüte etmek otomatik çözüm değildir.

5.  Standartlaştırılmış ayırma katsayıları, diğer değişkenler sabitken her değişkenin fonksiyona özgün katkısıdır (kısmi, regresyon ağırlığı benzeri) ve çoklu doğrusal ilişkide kararsızdır. Yapı katsayıları değişken ile fonksiyon arasındaki basit korelasyondur; fonksiyonun anlamını yorumlamak için daha kararlıdır.

## İleri Düzey

1.  Grup içi korelasyon yüksek ve iki fark zıt yönlü veya birinin sıfır olduğu bir örüntü MANOVA’yı güçlendirir. Örneğin iki grup iki değişkende ayrı ayrı küçük ve anlamsız zıt yönlü farklar gösterir ($+2$, $-2$), ama değişkenler grup içinde $r=.9$ ile ilişkilidir; farkların farkı çok küçük grup içi varyanslı bir bileşimde büyük bir ayrılığa dönüşür. Bölümdeki cinsiyet örneği yumuşak bir biçimidir: SATV’de fark yokken $D=.43$, tek başına SATQ’nun $d=.35$ değerinden büyüktür.

2.  Tekrarlı ölçümlerde $k-1$ karşıtlık puanı çok değişkenli bağımlı değişkenler gibi ele alınır; içerideki etki, bu puanların ortalama vektörünün sıfır olup olmadığının Hotelling $T^2$ testidir, arası $\times$ içi etkileşim de karşıtlık puanları üzerinde bir MANOVA’dır. İki yaklaşım aynı matris cebirine dayanır.

3.  Gruplar arası fark taşıyan bir değişken eklemek gücü artırabilir; farkı olmayan değişkenler eklemek, sd kaybı nedeniyle gücü düşürür. Değişken sayısı grup başına gözlem sayısına yaklaştığında $\mathbf E$ kararsızlaşır. Bağımlı değişkenler kuramla seçilmelidir.

4.  Hangi türün önceden belirlendiği ve nedenini raporlarsınız; farkın dengesiz hücrelerden kaynaklandığını açıklarsınız. Etkileşim anlamlıysa ana etkiler zaten tek başına yorumlanmamalıdır; Tip II ve Tip III farklı hipotezleri sınayabilir; kodlama ve karşıtlık ağırlıkları açıklanır, küçük p seçilmez. İki sonucu da ek olarak vermek şeffaflığı artırır.

5.  Bağımlı değişkenlerin seçim gerekçesi ve korelasyonları; grup büyüklükleri ve eksikler; betimsel istatistikler; uç değer ve Box M incelemesi; seçilen istatistik ve gerekçesi (değer, F, sd, p); çok değişkenli etki büyüklüğü; izleme analizleri (ayırma fonksiyonu yapı katsayıları, düzeltilmiş tek değişkenli testler); kareler toplamı türü; duyarlılık analizleri; yazılım ve F yaklaşımı.

## D1–D3: Analizden Önce

1.  SATQ 13 kişide eksiktir; MANOVA her kişinin üç puanını birlikte istediği için liste boyu dışlama yapılır. MCAR tam kayıt yaklaşımı için yeterli, her modelde zorunlu olmayan bir koşuldur. Hedeflenen grup ortalamalarının tam kayıtlarda temsil edildiği gerekçelendirilmelidir; küçük eksiklik oranı bunu kanıtlamaz.

2.  Kodların eşit aralıklı bir ölçek olduğu belgelenmemiştir (0 ve ara kodlar tanımsızdır); sürekli değişken gibi kullanmak doğrusal bir ilişki dayatır ve bilinmeyen anlamları sayıymış gibi yorumlar. Kategorik faktör olarak kullanmak bu varsayımı gerektirmez.

3.  Üç puan ortak bir “akademik yetenek” alanını farklı yönlerden ölçer; eğitimle genel bir farklılaşma sorusu birlikte analiz için gerekçe olabilir. Araştırma sorusu yalnız sayısal yetenek ise veya puanlar farklı kuramsal yapılar olarak ele alınıyorsa, önceden planlanmış ayrı analizler daha uygundur.

## G1–G4: Rehberli Çözüm

1.  $T^2=\frac{245\cdot442}{687}(.4264)^2=157.63\times.1818=28.65$; $F=\frac{687-2-1}{2(685)}T^2=\frac{684}{1370}(28.65)=14.31$, sd (2, 684).

2.  $\Lambda=1/(1.0356\cdot1.0078\cdot1.0014)=.957$; $V=.0356/1.0356+.0078/1.0078+.0014/1.0014=.0344+.0078+.0014=.0435$; $U=.0356+.0078+.0014=.0448$; Roy $=.0356$.

3.  $1-.9568^{1/3}=.0146$ ve $V/s=.0435/3=.0145$. ACT’nin tek değişkenli $\eta^2$’si .031’dir; $V/s$ kanonik kare korelasyonların ortalamasıdır; $1-\Lambda^{1/s}$ farklı bir özettir. Özgün puanların toplam açıklanan varyansı değildirler; tekil ACT $\eta^2$’siyle aynı hedefi ölçmezler.

4.  Katsayı, SATQ sabitken SATV’nin özgün katkısıdır. İki puan grup içinde güçlü ilişkili olduğundan SATQ’daki farkın bir kısmı “SATV’nin beklenen payı”dır; SATV’ye negatif ağırlık vermek bu ortak kısmı çıkarır ve $SATQ-SATV$ benzeri, grupları daha iyi ayıran bir bileşim üretir. Tek değişkenli fark ise SATV’nin kendi başına küçük pozitif farkıdır.

## B1–B3: Bağımsız Çözüm

1.  Box M .001 eşiğini de aşar ve standart sapmalar eğitim koduyla sistematik azalır. Grup büyüklükleri de çok dengesizdir (43–269). Bu nedenle Pillai izi raporlanır; büyük grupların varyansı küçük olduğundan testin liberal olabileceği belirtilir ve p değeri sınırda sayılır. Bu örüntüden nominal hata oranı hesaplanamaz. Hedefe uygun heterojen kovaryans yöntemi ayrıca gerekçelendirilir; yeni iki grup eki altı eğitim grubunu kapsamaz.

2.  Dışlama eğitim etkisini biraz güçlendirmiş ($p$ .012’den .005’e), cinsiyet etkisini değiştirmemiştir; ana sonuç uç değerlere bağlı değildir. Silmek için kayıtların gerçekten hatalı olduğunu gösteren dış bilgi (resmî puan, veri toplama kaydı, tutarlılık denetimi) gerekir; yalnız istatistiksel uzaklık yeterli değildir.

3.  İki grup analizinde (yalnız SATV, SATQ) cinsiyet $F(2,684)=14.31$; iki faktörlü modelde üç puanla ve eğitim dengelenerek Pillai $F(3,673)=9.84$, $p<.001$’dir. Cinsiyetin eğitim ana etkisine göre düzeltilmiş hipotezi reddedilir; bu istatistiksel/ nedensel bağımsızlık anlamına gelmez. Tip II ve Tip III, hücreler dengesiz ve etkileşim sıfırdan farklıyken farklılaşır; dengeli tasarımlarda aynıdır.

## H1: Raporu Onarma

1.  Anlamlı MANOVA en az bir bileşimde fark olduğunu gösterir; izleme analizleri bu ailede ACT için daha belirgin kanıt bulmuştur; diğer puanlarda eşdeğerlik kanıtlanmaz.

2.  Roy’un p’si bir alt sınırdır ve iyimserdir; genel karar için Pillai (veya Wilks) raporlanır.

3.  Box M’nin anlamlılığı analizi yasaklamaz; Pillai izi seçilir, grup varyansları incelenir ve duyarlılık yapılır.

4.  Düzeltmesiz üç ANOVA aile boyu hatayı korumaz; Bonferroni (veya aile denetimi yapılan planlı karşıtlıklar) kullanılır. Önceden planlama tek başına çokluk denetimi değildir.

5.  SATV tek başına farksız olsa da ayırma fonksiyonunda belirgin (negatif) bir ağırlık taşır; çünkü SATQ ile ilişkisi nedeniyle bileşimin ayırıcılığını artırır. Tek değişkenli önem ile çok değişkenli katkı farklı sorulardır.

## T1–T3: Hedef, Birim ve Aile Denetimi

1.  Ortak tersinir dönüşümde fark ve kovaryans birlikte dönüşür; genelleştirilmiş özdeğerler/Hotelling karesel biçimi değişmez. Tek bileşik puan boyut ve hipotez azaltır. Gruplara ayrı standartlaştırma ortak dönüşüm değildir; incelenen ortalama farkını silebilir.

2.  Marjinal aralık her sonuç için ayrı %95’tir; ortak kapsama garantisi yoktur. Bonferroni tanımlı iki koordinatı en az %95 birlikte kapsar; Hotelling aynı elipsoidden bütün doğrultuları kapsar. İki yöntem farklı aileler içindir. SATV Bonferroni aralığı $[-15.58,24.98]$, SATQ $[19.46,60.30]$ puandır. Sıfırı içeren aralık, önceden belirlenmiş eşdeğerlik sınırları içine bütünüyle girdiği gösterilmeden eşdeğerlik değildir.

3.  Hayır; yalnız aynı 687 tam kişide iki cinsiyet ve iki puan incelenmiştir. Wald sonucu büyük örneklem yaklaşımıdır; küçük örneklem Welch–James düzeltmesi yoktur. Box M ön test seçim anahtarı, Pillai heterojen kovaryans düzeltmesi değildir. Sıradan tam etiket permütasyonu değiştirilebilirlik ister; yalnız ortalamaların eşitliği yeterli değildir. Altı grup için uygun sağlam yöntem ayrı bir analiz gerektirir; burada yapıldığı iddia edilmez.

## P1: MANOVA Planı

Üç alanın ortak soru için gerekçesi, hedeflenen ortalama vektörü ve analiz birimi yazılır. Korelasyonlar tek başına yöntem veya bileşik puan seçtirmez. Birincil istatistik ve izleme ailesi sonuç görülmeden tanımlanır; örneğin Pillai ve üç sonuç için Holm/Bonferroni. Box M otomatik seçim anahtarı değildir. Bağımsızlık, grup-içi artıklar, kovaryans koşulluluğu ve kayıt doğrulama incelenir; uç değerler otomatik silinmez. Heterojen kovaryans ve eksik kayıt yaklaşımı için tasarıma uygun duyarlılık ayrıca planlanır; sıradan etiket permütasyonu gerekçesiz uygulanmaz. Ham farklar ve aileyle uyumlu aralıklar, tam tanımlanmış çok değişkenli özetler raporlanır; $V/s$ toplam varyans yüzdesi değildir. Ayırma yönünün keşif niteliği ve dış doğrulama sınırı yazılır. Örneklem gerekçesi en küçük önemli vektör farkı, kovaryans, grup oranları ve planlı testin kalibrasyon/gücünü kullanır; eksik izlem ayrıca hesaba katılır. Rubrik: kuram 20, analiz planı 30, varsayımlar 20, izleme 20, raporlama 10 puan.

## Ç1 çıkış sorusunun yanıtı

Hayır. Ortak vektör veya bir bileşim farklı olabilir; tekil hipotezler ve izleme ailesi ayrıca incelenir.
