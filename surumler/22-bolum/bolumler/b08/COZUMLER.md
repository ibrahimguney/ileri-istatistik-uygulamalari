# Bölüm 8 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

Gözlemlerin bağımsızlığı varsayımını çiğner: aynı kişinin ölçümleri birbirine benzer. Model 144 bağımsız bilgi varmış gibi davranır, kişiler arası kalıcı farkları hataya katar ve serbestlik derecesini yanlış (136) hesaplar; doğru yaklaşım kişiyi birim alan tekrarlı ölçümler ANOVA’sı veya karma etkiler modelidir.

## Kolay Düzey

1.  Her kişi kendi kontrolüdür; kalıcı kişi farkları hatadan çıkarıldığı için aynı etki daha az katılımcıyla daha kesin kestirilir. Bedeli, ölçümler arası bağımlılığın modellenmesi ve sıra/taşıma etkileridir.

2.  Bütün ölçüm çiftleri arasındaki farkların varyanslarının eşit olmasıdır (eşdeğer biçimde ortonormal karşıtlıkların kovaryans matrisinin birim matrisin katı olması). İki ölçümde tek bir fark vardır; eşitlenecek başka fark olmadığından varsayım kendiliğinden sağlanır.

3.  F değerini değil, karşılaştırıldığı dağılımın iki serbestlik derecesini $\hat\varepsilon_{GG}$ ile çarparak küçültür; p değeri büyür, test tutucu olur.

4.  Uzun biçimde her satır bir kişi–ölçüm gözlemidir (kişi kimliği, zaman/koşul, yanıt); geniş biçimde her satır bir kişidir ve ölçümler ayrı sütunlardadır. Karma modeller uzun, SPSS GLM tekrarlı ölçümler ve Mauchly/Hotelling hesapları geniş biçimi kullanır.

5.  İki: aradaki etkiler için kişiler/grup hatası, içerideki etkiler ve etkileşim için içerideki faktör $\times$ kişiler/grup hatası.

## Orta Düzey

1.  Düzeltilmiş sd’ler $4(.62)=2.48$ ve $76(.62)=47.12$’dir. F aynı kalır (3.10); küresellik varsayılan $p\approx.020$ iken GG ile $p\approx.044$ olur. Sınırda kararlar düzeltmeyle değişebilir; hangi düzeltmenin önceden seçildiği raporlanır.

2.  Kısmi eta-kare kişi varyansını paydadan çıkardığı için denek içi desende şişkin görünür; bağımsız gruplar $\eta^2$’siyle karşılaştırılamaz. Karşılaştırma için genelleştirilmiş eta-kare ($\eta^2_G$) kullanılmalı ve türü yazılmalıdır.

3.  Koşul etkisi sıra (öğrenme, yorgunluk, taşıma) etkisiyle karışır. Karşı dengeleme (tam veya Latin kare), yeterli ara süre ve sıra etkisinin modelde ayrı faktör olarak sınanması önerilir.

4.  ANOVA 9 kişiyi tümden atar (%22 kayıp) ve bu kişiler sistematik farklıysa yanlılık doğar. Karma model eksik ölçümü olan kişilerin mevcut ölçümlerini kullanır ve rastgele eksiklik (MAR) altında geçerli çıkarım verir. Eksiklik nedenleri incelenmeli, seçim ve varsayım raporlanmalıdır.

5.  Ana etkiler etkileşimin varlığında ortalama bir özet olarak kalır ve yanıltıcı olabilir. Öncelik basit etkilere veya odaklı etkileşim karşıtlıklarına verilir; ana etkiler, etkileşimin örüntüsüyle birlikte yorumlanır.

## İleri Düzey

1.  Küresellik ciddi bozulduğunda ve $n$ düzey sayısına göre büyük olduğunda çok değişkenli yaklaşım genellikle daha güçlüdür; küresellik yaklaşık sağlanıyorsa ya da $n$ küçükse ($n-k$ küçük hata sd’si) düzeltilmiş tek değişkenli test daha güçlüdür. Seçim önceden yapılır; iki yaklaşım da raporlanıp elverişlisi seçilmez. Uyku verisinde hata sd’si yalnız 11 olan Hotelling testi ($p=.0018$), GG düzeltmeli teste ($p=2\times10^{-7}$) göre daha zayıf kalmıştır.

2.  Kişilerin eğimleri modelin öngördüğünden farklı değil demektir; rastgele eğim modelden çıkarılabilir. Ancak varyans sınırda (sıfırda) kestirildiğinde olabilirlik oranı testinin dağılımı standart ki-kare değildir (karışım dağılımı); yakınsama uyarıları ve tasarımın rastgele eğimi destekleyecek kadar ölçüm içerip içermediği de incelenir.

3.  Tek sd’li karşıtlık belirli bir hipoteze odaklanır, gücü yüksektir ve yorumu açıktır. Risk, sonuçlar görüldükten sonra seçilmesidir; o zaman aileyi gizleyen bir veri taramasına dönüşür. Karşıtlık önceden yazılır; sonradan seçilmişse keşif olarak etiketlenir ve çoklu karşılaştırma düzeltmesi yapılır.

4.  Karma etkiler modelinde gruplara göre farklı rastgele etki ve artık varyansları tanımlanabilir; çok değişkenli yaklaşımda grup başına ayrı kovaryans kabul eden yöntemler (ör. Welch–James türü) veya kişi başına karşıtlık puanlarıyla Welch testleri kullanılabilir. Bölümdeki büyüme hızı karşıtlığında Welch testi bu nedenle seçilmiştir.

5.  Tasarım ve ölçüm zamanları; kişi/ölçüm sayıları ve eksikler; betimsel istatistikler (hücre ortalamaları, SS); küresellik incelemesi ve kullanılan düzeltme ($\varepsilon$ dâhil); F, düzeltilmiş sd, p; etki büyüklüğü türü ($\eta^2_G$/$\eta^2_p$); önceden belirlenmiş karşıtlıklar ve çoklu karşılaştırma düzeltmesi; varsayım ihlalleri ve duyarlılık (karma model); yazılım ve sürüm.

## D1–D3: Analizden Önce

1.  `lme4` belgesi ve Belenky vd. (2003) 0–1. günleri uyum/alıştırma, 2. günü temel olarak tanımlar; kısıtlama sonrası değişim sorusu için bu günler analiz edilecek koşullar değildir. Karar sonuçlara bakmadan, belgeye dayanarak verilir ve raporlanır.

2.  Bağımsız sayılırsa $144-8=136$; tekrarlı ölçümlerde $(8-1)(18-1)=119$ (düzeltmesiz). 136 sd, bağımsız olmayan 144 satırı 144 bilgi gibi sayar; ayrıca kişi farkları hataya karışır. Doğru birim kişidir.

3.  Öğrenme veya alışma (tersine yorgunluk), günlük koşullar, laboratuvar ortamında kalmanın kendisi, ölçüm tekrarının etkileri ve zamanla değişen diğer etkenler. Karşılaştırma grubu olmadan yoksunluk etkisi zaman etkisinden ayrılamaz.

## G1–G4: Rehberli Çözüm

1.  $MS_{\text{gün}}=100926.5/7=14418.07$, $MS_{\text{hata}}=112068.9/119=941.76$, $F=15.31$. Kişi payı $253102.1/466097.6=.543$, yani toplam değişkenliğin yaklaşık %54’ü kalıcı kişi farklarıdır.

2.  $7(.4448)=3.11$ ve $119(.4448)=52.94$. F kareler toplamlarının oranıdır ve $\varepsilon$ yalnız referans dağılımın biçimini değiştirir; pay ve payda aynı oranda çarpıldığı için F sabit kalır.

3.  $\eta^2_p=100926.5/(100926.5+112068.9)=.474$; $\eta^2_G=100926.5/466097.6=.217$. Fark, kişi değişkenliğinin (253102.1) $\eta^2_G$’nin paydasında kalması, $\eta^2_p$’de çıkarılmasıdır.

4.  $t=74.11/(50.74/\sqrt{18})=74.11/11.96=6.20$, sd 17. Her kişinin tek bir karşıtlık puanı vardır; test yalnız bu puanların varyansını kullanır, farklı karşıtlıkların varyanslarının eşitliğini gerektirmez.

## B1–B3: Bağımsız Çözüm

1.  Cinsiyet: $F=140.46/(377.91/25)=140.46/15.12=9.29$, sd (1, 25), $p=.005$. Yaş: $F=(209.44/3)/(148.13/75)=69.81/1.98=35.35$, sd (3, 75). Cinsiyet kişi ortalamalarının grup içi değişkenliğiyle; yaş ve etkileşim kişi içi değişimlerin grup içi tutarsızlığıyla karşılaştırılır. Kişi içi hata çok daha küçüktür (MS 1.98 ve 15.12); yaş etkisi bu yüzden daha kesin sınanır.

2.  $3(.8672)=2.60$, $75(.8672)=65.04$; $F(2.60,\,65.04)=2.36$, $p=.088$. Özgün HF formülü $\hat\varepsilon_{GG}$ yüksek ve örneklem küçükken 1’i aşabilir; $\varepsilon$ 1’den büyük olamayacağı için 1’e kırpılır. Lecoutre düzeltmesi (R) .977 verir.

3.  Genel testin $.05$’te reddetmediği, önceden belirtilmemiş odaklı karşıtlığın ise erkeklerde daha hızlı doğrusal büyüme gösterdiği (.78’e karşı .48 mm/yıl, $t(24.0)=2.51$, $p=.019$) birlikte yazılır; karşıtlığın sonradan seçildiği belirtilir ve bağımsız veride sınanması önerilir. Eğim varyanslarının farklılığı ve Welch kullanımı da raporlanır.

## H1: Raporu Onarma

1.  144 ölçüm bağımsız değildir; 18 kişinin tekrarlı ölçümleri tekrarlı ölçümler ANOVA’sı veya karma modelle analiz edilir.

2.  Mauchly anlamlılığı ANOVA’yı yasaklamaz; GG/HF düzeltmesi, çok değişkenli yaklaşım veya karma model kullanılır. Düzeltme baştan planlanmalıdır.

3.  $\eta^2_p$ kişi varyansını dışarıda bıraktığı için bağımsız gruplar $\eta^2$’siyle karşılaştırılamaz; $\eta^2_G=.217$ daha uygundur.

4.  Anlamsız etkileşim eşit büyümeyi kanıtlamaz; odaklı büyüme hızı karşıtlığı farklılık gösterir ve güven aralıkları raporlanmalıdır.

5.  Veriye bakarak en büyük farkı veren günleri seçmek çoklu karşılaştırmayı gizler ve Tip I hatayı şişirir; karşılaştırma önceden tanımlanmalı (ör. temel ile son gün) veya bütün çiftler düzeltmeyle sınanmalıdır.

## P1: Tekrarlı Ölçüm Çalışması Planı

İyi bir plan, rastgele atanmış müdahale ve kontrol gruplarını, temel ölçüm dâhil eşit aralıklı dört ölçümü ve ölçüm koşullarının standartlaştırılmasını tanımlar. Birincil hipotez tek sd’li bir karşıtlık olarak yazılır: grup $\times$ doğrusal zaman (büyüme hızı farkı). İkincil karşıtlıklar ve çoklu karşılaştırma ailesi belirtilir. Küresellik için GG düzeltmesi önceden seçilir; birincil analiz olarak, eksik ölçümlere dayanıklı olduğu için rastgele kesişim ve eğimli karma model tercih edilir, ANOVA duyarlılık analizi olur. Eksiklik nedenleri kaydedilir; MAR varsayımı ve duyarlılık analizi (ör. tam kayıt karşılaştırması) planlanır. Etki büyüklüğü olarak ham eğim farkı ve güven aralığı, ek olarak $\eta^2_G$ verilir. Raporlanacak tablolar: hücre betimselleri, model tahminleri, varyans bileşenleri, karşıtlık sonuçları. Kod, sürüm ve veri sözlüğü paylaşılır. Rubrik: tasarım 25, analiz planı 30, varsayımlar 20, raporlama 15, yeniden üretim 10 puan.


## Revizyon 11: eksik izlem ve aynı hedef

## T1–T3: Eksik İzlem ve Hedef Denetimi

1.  Özgün arşivde eksik yoktur. Maske 40 ölçümü gizler; bütün 18 kişide en az iki ölçüm kalır, yalnız yedi kişinin sekiz ölçümü tamdır. Bu nedenle mevcut veri 104, tam-kişi veri 56 satırdır. Üçünde de aynı doğrusal rastgele kesişim/eğim REML modeli kullanılır; gün kategorilerinin genel ANOVA testiyle karşılaştırma hem hedefi hem modeli değiştirirdi. Eğimler 11.435, 12.753, 10.411 ms/gündür. İlki bilinen anakütle gerçeği değil, tam arşivin model kestirimidir; bir maske yanlılık/üstünlük kanıtı vermez. SH’nin maskede azalması bilgi kazancı diye yorumlanmaz.

2.  Çıkış olasılığı yalnız gözlenen temel tepki ve bağımsız rastgele çekilişle belirlenmiştir; bu öğretim mekanizmasında MAR yapısı bilinir. Gerçek veri için mekanizma testi yapılmamıştır. Yakınsama ve pozitif kovaryans özdeğerleri yalnız sayısal kontrollerdir; doğru ortalama/kovaryans ve MAR’ı kanıtlamaz. Normal Wald aralığı ortalama eğim kestiriminin model-temelli belirsizliğidir; normal rastgele eğim dağılımından $\hat\beta_1\pm1.96\hat\tau_1$ ise parametreler sabitken kişiler arası merkez aralığıdır. İkincisi belli kişinin aralığı veya nedensel duyarlılık değildir. Küçük örneklem sd düzeltmesi ve MNAR duyarlılığı yapılmamıştır.

3.  Holm p’leri yaş sırasıyla .109487, .109487, .038228, .005306; Bonferroni p’leri .273898, .218973, .050970, .005306’dır. Holm 12/14, Bonferroni yalnız 14 yaş sorusunu reddeder. Bunlar belirli yaşlardaki grup farklarıdır; genel kategorik etkileşim ve kişi başına doğrusal eğimlerin Welch karşılaştırması farklı hedef/hata yapısı kullanır. Düzeltme veya aile sonuçları gördükten sonra avantaj için değiştirilmez. Bu alıntıda aile öğretim içindir, gerçek önkayıt değildir; düzeltilmiş aralık verilmemiştir.
