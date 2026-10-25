# Bölüm 9 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

\(1\) Bağımlı değişkenler arasındaki ilişki (kovaryans) bilgisini: gruplar ancak değişkenlerin bir bileşiminde ayrışıyorsa ayrı testler bunu göremez. (2) Aile boyu hata denetimini: ilişkili değişkenler üzerindeki çoklu testler Tip I hatayı biriktirir.

## Kolay Düzey

1.  Bütün grupların bağımlı değişken ortalama vektörlerinin eşit olmasıdır: $\boldsymbol\mu_1=\boldsymbol\mu_2=\dots=\boldsymbol\mu_g$. Bu, her değişkende tek tek eşitliği ve bütün doğrusal bileşimlerde eşitliği birlikte içerir.

2.  Köşegen öğeler her bağımlı değişkenin (arası veya içi) kareler toplamıdır; köşegen dışı öğeler iki değişkenin çapraz çarpımlarının toplamı, yani birlikte değişimidir.

3.  Pillai izi; özellikle dengesiz gruplar ve kovaryans eşitsizliğinde Tip I hata oranını en iyi korur.

4.  İki grubun birden çok bağımlı değişkendeki ortalama vektörlerini karşılaştırmak için; tek değişkenli bağımsız t-testinin çok değişkenli genellemesidir. Tekrarlı ölçümlerde tek örneklem biçimi karşıtlık puanlarına uygulanır.

5.  Grupların kovaryans matrislerinin eşitliğini; normalliğe çok duyarlı olduğundan genellikle .001 eşiğiyle ve betimsel incelemeyle birlikte okunur.

## Orta Düzey

1.  İki değişken neredeyse aynı şeyi ölçer; $\mathbf E$ tekile yakınlaşır ve MANOVA kararsızlaşır. Tek bir bileşik puan (ortalama veya faktör puanı) ya da yalnız kuramsal olarak birincil değişkenle tek değişkenli analiz önerilir.

2.  $1-\Lambda^{1/s}=1-.80^{1/2}=1-.894=.106$.

3.  Tek değişkenli sonuç önceden planlanmışsa ve düzeltilmişse ayrıca raporlanabilir. Önceden planlanmamışsa, anlamsız genel testten sonra bir değişkeni seçmek çoklu karşılaştırma sorunudur; keşif olarak etiketlenir. MANOVA’nın gücü, etkisiz değişkenler eklendiğinde düşebilir; bu da neden olabilir.

4.  Pillai izi. Küçük gruplar daha büyük varyanslıysa diğer istatistikler liberal, tersi durumda tutucu olur; Pillai bu koşullarda en dayanıklısıdır. Ayrıca grupları dengelemeyi veya duyarlılık analizini düşünün.

5.  Standartlaştırılmış ayırma katsayıları, diğer değişkenler sabitken her değişkenin fonksiyona özgün katkısıdır (kısmi, regresyon ağırlığı benzeri) ve çoklu doğrusal ilişkide kararsızdır. Yapı katsayıları değişken ile fonksiyon arasındaki basit korelasyondur; fonksiyonun anlamını yorumlamak için daha kararlıdır.

## İleri Düzey

1.  Grup içi korelasyon yüksek ve iki fark zıt yönlü veya birinin sıfır olduğu bir örüntü MANOVA’yı güçlendirir. Örneğin iki grup iki değişkende ayrı ayrı küçük ve anlamsız zıt yönlü farklar gösterir ($+2$, $-2$), ama değişkenler grup içinde $r=.9$ ile ilişkilidir; farkların farkı çok küçük grup içi varyanslı bir bileşimde büyük bir ayrılığa dönüşür. Bölümdeki cinsiyet örneği yumuşak bir biçimidir: SATV’de fark yokken $D=.43$, tek başına SATQ’nun $d=.35$ değerinden büyüktür.

2.  Tekrarlı ölçümlerde $k-1$ karşıtlık puanı çok değişkenli bağımlı değişkenler gibi ele alınır; içerideki etki, bu puanların ortalama vektörünün sıfır olup olmadığının Hotelling $T^2$ testidir, arası $\times$ içi etkileşim de karşıtlık puanları üzerinde bir MANOVA’dır. İki yaklaşım aynı matris cebirine dayanır.

3.  Gruplar arası fark taşıyan bir değişken eklemek gücü artırabilir; farkı olmayan değişkenler eklemek, sd kaybı nedeniyle gücü düşürür. Değişken sayısı grup başına gözlem sayısına yaklaştığında $\mathbf E$ kararsızlaşır. Bağımlı değişkenler kuramla seçilmelidir.

4.  Hangi türün önceden belirlendiği ve nedenini raporlarsınız; farkın dengesiz hücrelerden kaynaklandığını açıklarsınız. Etkileşim anlamlıysa ana etkiler zaten tek başına yorumlanmamalıdır; etkileşim yoksa Tip II ana etkiler için daha güçlüdür. İki sonucu da ek olarak vermek şeffaflığı artırır.

5.  Bağımlı değişkenlerin seçim gerekçesi ve korelasyonları; grup büyüklükleri ve eksikler; betimsel istatistikler; uç değer ve Box M incelemesi; seçilen istatistik ve gerekçesi (değer, F, sd, p); çok değişkenli etki büyüklüğü; izleme analizleri (ayırma fonksiyonu yapı katsayıları, düzeltilmiş tek değişkenli testler); kareler toplamı türü; duyarlılık analizleri; yazılım ve F yaklaşımı.

## D1–D3: Analizden Önce

1.  SATQ 13 kişide eksiktir; MANOVA her kişinin üç puanını birlikte istediği için liste boyu dışlama yapılır. Bu, eksikliğin tamamen rastgele (MCAR) olduğunu veya en azından sonuçları yanlılaştırmadığını varsayar; 13/700 oranı küçüktür ama varsayım raporlanır.

2.  Kodların eşit aralıklı bir ölçek olduğu belgelenmemiştir (0 ve ara kodlar tanımsızdır); sürekli değişken gibi kullanmak doğrusal bir ilişki dayatır ve bilinmeyen anlamları sayıymış gibi yorumlar. Kategorik faktör olarak kullanmak bu varsayımı gerektirmez.

3.  Üç puan ortak bir “akademik yetenek” alanını farklı yönlerden ölçer; eğitimle genel bir farklılaşma sorusu birlikte analiz için gerekçe olabilir. Araştırma sorusu yalnız sayısal yetenek ise veya puanlar farklı kuramsal yapılar olarak ele alınıyorsa, önceden planlanmış ayrı analizler daha uygundur.

## G1–G4: Rehberli Çözüm

1.  $T^2=\frac{245\cdot442}{687}(.4264)^2=157.63\times.1818=28.65$; $F=\frac{687-2-1}{2(685)}T^2=\frac{684}{1370}(28.65)=14.31$, sd (2, 684).

2.  $\Lambda=1/(1.0356\cdot1.0078\cdot1.0014)=.957$; $V=.0356/1.0356+.0078/1.0078+.0014/1.0014=.0344+.0078+.0014=.0435$; $U=.0356+.0078+.0014=.0448$; Roy $=.0356$.

3.  $1-.9568^{1/3}=.0146$ ve $V/s=.0435/3=.0145$. ACT’nin tek değişkenli $\eta^2$’si .031’dir; çok değişkenli ölçü üç boyutun ortalaması olduğundan, etkinin tek değişkende yoğunlaştığı durumda daha küçük çıkar.

4.  Katsayı, SATQ sabitken SATV’nin özgün katkısıdır. İki puan grup içinde güçlü ilişkili olduğundan SATQ’daki farkın bir kısmı “SATV’nin beklenen payı”dır; SATV’ye negatif ağırlık vermek bu ortak kısmı çıkarır ve $SATQ-SATV$ benzeri, grupları daha iyi ayıran bir bileşim üretir. Tek değişkenli fark ise SATV’nin kendi başına küçük pozitif farkıdır.

## B1–B3: Bağımsız Çözüm

1.  Box M .001 eşiğini de aşar ve standart sapmalar eğitim koduyla sistematik azalır. Grup büyüklükleri de çok dengesizdir (43–269). Bu nedenle Pillai izi raporlanır; büyük grupların varyansı küçük olduğundan testin liberal olabileceği belirtilir ve p değeri sınırda sayılır. Duyarlılık için grupları dengeleyen bir yeniden örnekleme veya sağlam yöntem düşünülebilir.

2.  Dışlama eğitim etkisini biraz güçlendirmiş ($p$ .012’den .005’e), cinsiyet etkisini değiştirmemiştir; ana sonuç uç değerlere bağlı değildir. Silmek için kayıtların gerçekten hatalı olduğunu gösteren dış bilgi (resmî puan, veri toplama kaydı, tutarlılık denetimi) gerekir; yalnız istatistiksel uzaklık yeterli değildir.

3.  İki grup analizinde (yalnız SATV, SATQ) cinsiyet $F(2,684)=14.31$; iki faktörlü modelde üç puanla ve eğitim dengelenerek Pillai $F(3,673)=9.84$, $p<.001$’dir. Cinsiyet etkisi eğitimden bağımsız olarak sürer. Tip II ve Tip III, hücreler dengesiz ve etkileşim sıfırdan farklıyken farklılaşır; dengeli tasarımlarda aynıdır.

## H1: Raporu Onarma

1.  Anlamlı MANOVA en az bir bileşimde fark olduğunu gösterir; izleme analizleri farkın yalnız ACT’de olduğunu göstermiştir.

2.  Roy’un p’si bir alt sınırdır ve iyimserdir; genel karar için Pillai (veya Wilks) raporlanır.

3.  Box M’nin anlamlılığı analizi yasaklamaz; Pillai izi seçilir, grup varyansları incelenir ve duyarlılık yapılır.

4.  Düzeltmesiz üç ANOVA aile boyu hatayı korumaz; Bonferroni (veya önceden planlanmış karşıtlıklar) kullanılır.

5.  SATV tek başına farksız olsa da ayırma fonksiyonunda belirgin (negatif) bir ağırlık taşır; çünkü SATQ ile ilişkisi nedeniyle bileşimin ayırıcılığını artırır. Tek değişkenli önem ile çok değişkenli katkı farklı sorulardır.

## P1: MANOVA Planı

İyi bir plan, üç başarı alanını ortak bir “akademik başarı” kuramı altında seçtiğini ve beklenen orta düzey korelasyonları (.4–.7) belirtir; çok yüksek korelasyon beklenirse bileşik puanı alternatif olarak yazar. Birincil test Pillai izidir; dengesiz grup ve kovaryans eşitsizliği olasılığı gerekçe olarak verilir. Varsayımlar için Mahalanobis uzaklığı (.999 eşiği) ve Box M (.001 eşiği) ile grup kovaryanslarının betimsel incelemesi planlanır; uç değerler silinmez, duyarlılık analizi yapılır. İzleme için önceden: ayırma fonksiyonu yapı katsayıları ve Bonferroni düzeltmeli üç ANOVA; grup karşılaştırmaları için Tukey veya planlı karşıtlıklar. Etki büyüklüğü olarak çok değişkenli $\eta^2$ ve her değişken için ham fark ile güven aralığı verilir. Örneklem gerekçesi beklenen en küçük anlamlı etkiye göre yapılır (ör. G\*Power’da MANOVA global etkisi). Rubrik: kuram 20, analiz planı 30, varsayımlar 20, izleme 20, raporlama 10 puan.
