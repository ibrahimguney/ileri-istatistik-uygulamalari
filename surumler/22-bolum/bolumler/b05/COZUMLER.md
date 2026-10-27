# Bölüm 5 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

Anlamlı çıkmama, verinin sıfır hipoteziyle uyumlu olduğunu gösterir; farkın sıfır olduğunu kanıtlamaz. Düşük güç, küçük örneklem veya büyük değişkenlik gerçek bir farkı gizleyebilir. “Fark yok” demek için güven aralığının önemsiz sayılan bir aralıkta kaldığı eşdeğerlik testi (ör. TOST) veya yeterli güçle planlanmış bir çalışma gerekir.

## Kolay Düzey

1.  Seçilen alternatif gerçekten geçerliyken, belirli model ve test planında $H_0$’ı reddetme olasılığıdır: $1-\beta$. Hipotezin doğru olma olasılığı veya tek çalışmanın başarı garantisi değildir.

2.  Tip I hata doğru $H_0$’ı reddetmek, Tip II hata belirli bir alternatif doğruyken $H_0$’ı reddedememektir. Alfa ile denetlenen hata ve etkiye bağlı beta farklı koşullu olasılıklardır.

3.  Etki büyüklüğü farkın/ilişkinin büyüklüğünü verir; p tek başına bu büyüklüğü göstermez. Etki de güven aralığı ve bağlam olmadan yeterli değildir. Standartlaştırılmış katsayı pratik önemi otomatik belirlemez.

4.  Aynı tasarım, varyans ve bağımsızlık koşulları altında genellikle azalır; ortalama için $\sigma/\sqrt n$ örnektir. Kümelenmiş veya tekrarlı satırları bağımsız n saymak bu kazancı abartır.

5.  Alfa testin hata düzeyini, güç seçilen gerçek etkiyi yakalama hedefini, etki ise alternatifin büyüklüğünü belirtir. Bunlara test, yön, yayılım ve tasarım eklenerek n hesaplanır. n’nin grup başına mı toplam mı olduğu yazılır.

## Orta Düzey

1.  Diğer girdiler sabitken daha büyük örneklem gerekir. Ana örnekte 64’ten 86 kişi/gruba, toplam 128’den 172’ye çıkılır; tam sayıda ulaşılan güç .903230’dur.

2.  Sinyal/gürültü oranı küçüktür; aynı ret eşiğinde daha fazla bilgi gerekir. Ana modelde $d=.20$ için 394, $d=.50$ için 64 kişi/grup bulunur. Küçük etkinin pratik değeri yalnız bu sayılardan belirlenmez.

3.  $H_0$ reddedilememiştir; etki yokluğu veya eşdeğerlik kanıtlanmaz. Tahmin, güven aralığı, planın duyarlılığı ve sınırlılıklar verilir. Gözlenen etkiyi gerçek sayan sonradan güç hesabı yeni bağımsız kanıt değildir.

4.  Pilot ölçüm, yayılım ve uygulanabilirlik bilgisi sağlayabilir; küçük örneklem tahminleri belirsizdir. Tek büyük pilot etkisine dayanmak yerine bağımsız bilgi ve duyarlılıklar kullanılır. Sleep arşivi yeni pilot değildir; onun s’sini yerine koymak yalnız bir öğretim senaryosudur.

5.  Anlamlılık test modeli altında sıfırla uyumsuzluğa, pratik önem araştırmanın önemli gördüğü büyüklüğe ilişkindir. Küçük bir etki büyük n ile anlamlı olabilir. Önem eşiği, yarar/zarar ve ölçüm bağlamıyla önceden gerekçelendirilir; evrensel d eşiği değildir.

## İleri Düzey

1.  Örneğin katılımcı yükü yüksek bir çalışmada bilimsel soruya az bilgi sağlayan tasarım emeği boşa harcayabilir. Daha çok kişi de sınırsız hedef değildir; bilgi getirisi, kaynaklar ve yük dengelenir. Sabit bir .80 eşiği bütün çalışmalar için tek etik ölçüt sayılmaz; kaynak kısıtı ve duyarlılık açık yazılır.

2.  Düzeltilmeden çok test yapmak aile hatasını artırabilir. Bonferroni tekil alfayı küçültür; sabit n’de tekil güç düşebilir. Hedef bütün testlerin mi, en az birinin mi, belirli bir birincil testin mi reddi olduğu belirtilmelidir. Her testin .80 gücü, bütün testlerin ortak .80 gücü değildir.

3.  Korelasyonda hedef $\rho$ ve referansı; regresyonda toplam veya ek $R^2$, sınanan yordayıcı sayısı ve tam model tanımlanır. $f^2=(R^2_{\text{tam}}-R^2_{\text{kısıtlı}})/(1-R^2_{\text{tam}})$ ek katkı hedefidir. .30’u tek örneklem t farkı olarak girmek korelasyon planı üretmez.

4.  Abartılı gerçek etki varsayımı n’yi küçültür; gerçek etki daha küçükse güç hedefin altında kalır. Ana modelde .80 etki varsayımıyla bulunan 26 kişi/grup, .50 etki için .80 güçlü değildir. Kuram, bağımsız önceki bulgu ve daha küçük etki senaryoları gereklidir.

5.  Hedef/ana sonuç, desen ve birim, test/model, yön/alfa, etki ve yayılım gerekçesi, hedef güç veya hassasiyet, oran, tam sayı ve n–1 denetimi, analiz/kayıt sayıları, kayıp/çoklu aile/durdurma planı, yazılım/sürüm ve duyarlılıklar yazılır. Yapılmamış ön kayıt veya yazılım çalıştırması iddia edilmez.

## D1–D3: Sayıdan Önce

1.  Beş puan gerçek ortalama farkı için öğretim girdisi, on puan grup içi gerçek standart sapma varsayımıdır. $d=5/10=.5$ oranı her ikisinin alan/ölçüm gerekçesini gizlememelidir. Beklenen fark ile en küçük önemli fark farklı olabilir.

2.  Bağımsız iki-grup ana planında 64 grup başına, toplam 128 kişidir. Eşli analizde n tamamlanmış kişi farkı/tam çift sayısıdır. Davet/kayıt sayısı ise kayıplar nedeniyle ayrıca planlanır.

3.  Hayır. Burada sabit n ve tek belirlenmiş test vardır. Sonuca bakarak kişi eklemek durdurma kuralını değiştirir; nominal alfa ve güç aynı kalmaz. Sıralı analiz seçilecekse ayrı sınır ve güç planı gerekir.

## G1–G4: Rehberli Çözüm

1.  $d=5/10=.5$, $\nu=64+64-2=126$ ve $\lambda=.5\sqrt{64/2}=2.828427$ bulunur. Merkezi $t_{.975,126}$ sınırının dışındaki merkezsiz t olasılığı .801460’tır. 63’te .795168 olduğundan minimum tam sayı 64’tür; sürekli kökü aşağı yuvarlamak hedefi kaçırır.

2.  Güç .90 için minimum 86 kişi/grup, toplam 172; bir önceki güç .899894, ulaşılan .903230’dur. Alfa .01 ve güç .80 için 96 kişi/grup, toplam 192; bir önceki .799469, ulaşılan .804547’dir. Diğer girdiler sabit tutulur.

3.  $\lceil64/.85\rceil=76$ kişi/grup ve beklenen $76(.85)=64.6$ tam kayıt bulunur. .422777, bağımsız binom tutulma varsayımı altında *iki grupta da* en az 64 kişinin kalma olasılığıdır; test gücü değildir. En az .90 olasılık hedefi için 81’in .896208 değeri yetmez; 82’nin .935473 değeri yeter. Böylece iki farklı kayıt planı 152 veya 164 toplam kişi verir.

4.  $d_z=.5/1.229995=.406506$ olur. 49 çiftte güç .796229, 50’de .804475 olduğundan minimum 50 tam çifttir. Arşivde yalnız 10 kişi vardır; 50 yeni gözlem yaratılmamıştır. .5 saat önemli klinik fark diye doğrulanmış değildir; tarihsel s de bilinen gerçek $\sigma_D$ değildir.

## B1–B3: Bağımsız Çözüm

1.  40 kişi/grup için $d=.50$ gücü .598147; .80 güce karşılık gelen d=.634299’dur. $\sigma=10$ varsayımında yaklaşık 6.343 puandır. Daha küçük etkiler hiç anlamlı çıkamaz denmez; yalnız hedef .80 güce ulaşılmaz. Önemli fark kaynak sınırına uydurularak yeniden tanımlanmaz.

2.  2:1 kısıtında 48/96, toplam 144 kişi ve .802140 güç bulunur; önceki izinli 47/94 çifti .793739 verir. Üç karşılaştırma için Bonferroni alfa $.05/3$ ve her birinde .50 etki varsayımında 86 kişi/grup gerekir. .804291 tekil güçtür. Hepsinin veya en az birinin reddi ortak dağılıma bağlıdır; bağımsız ve tam .80 güçlü üç testin hepsini reddetme olasılığı .512’dir.

3.  Fisher-z yaklaşımındaki 85, x ve y’si birlikte gözlenen 85 bağımsız kişi/kayıttır; 84’te yaklaşık güç .795517, 85’te .800346’dır. Eşli $d_z=.5$ için 34 kişinin tam ölçüm çifti, toplam 68 ölçüm satırı vardır. Korelasyon ve standartlaştırılmış ortalama farkı farklı parametrelerdir; tek örneklem t planı korelasyon dağılımını kullanmaz. 85 tam yöntem değil, belirtilmiş yaklaşım sonucudur.

## H1: Hatalı Planı Onarma

1.  d=.5 evrensel önem ölçütü değildir; beş puanlık fark ve on puanlık yayılımın ayrı gerekçeleri gerekir.

2.  64 grup başına analiz edilebilir kişidir; toplam 128’dir. Kayıt hedefi kayıp planıyla ayrıca belirlenir.

3.  Pilotun gözlenen etkisi belirsizdir; büyük tahmini gerçek saymak iyimser küçük n verir. Bağımsız bilgi, önemli fark ve yayılım duyarlılıkları kullanılır.

4.  76/grup beklenen sayı artırmasıdır; tam kayıt garantisi değildir. Buradaki bağımsız .85 modelinde iki grupta 64 kişinin kalma olasılığı .422777’dir. Kayıp sonuçla ilişkiliyse daha çok kayıt yanlılığı gidermez.

5.  Tekil test gücü ailede bütün testlerin gücü değildir. Çoklu düzeltme ve ailede hedeflenen olay belirtilir; .80 tekil güçten .80 ortak güç çıkarılmaz.

6.  Sonuçlara bakarak kişi eklemek sabit n planını değiştirir. Önceden belirlenmiş durdurma kuralı veya ayrı hesaplanmış sıralı tasarım gerekir; yalnız anlamlı sonucu sunmak uygun değildir.

## P1: Denetlenebilir Örneklem Gerekçesi

Örnek protokolde iki eğitim yönteminin belirli zamandaki puan farkı birincil hedef olarak tanımlanır. Öğrencinin mi sınıfın mı atanacağı, bağımsızlık ve kümelenme, ölçüm ölçeği ve hedef grup belirtilir. Önemli farkın alan dayanağı, beklenen farkın kanıtı ve yayılım belirsizliği ayrı kaydedilir. Gerçek kanıt yoksa beş/on puan örneği yalnız varsayımsal plan olarak yazılır.

Ana senaryo sabit örneklemli iki yönlü, alfa .05, d=.50, güç .80 ise 64/grup analiz hedefi raporlanır. Kayıt hedefinin 76/grup beklenti artırması mı, varsayımsal bağımsız tutulmada 82/grup olasılık hedefi mi olduğu seçilip gerekçelendirilir. Bu alternatiflerin hepsi aynı anda gerçek araştırma kararıymış gibi yazılmaz. Tutulma varsayımı, seçici kayıp, eksik veri analizi ve kişi yükü ayrıca değerlendirilir.

Kaynak yalnız 40/grup ise .598147 güç ve .80 güce karşılık gelen .634299 etki açıklanır. Hassasiyet amacı varsa ayrıca tanımlanır; .2$\sigma$ yarı genişlik için 194/grup yerine koymalı hesabı bir genişlik garantisi değildir. Çoklu aile, yön, dışlama, izleme ve durdurma kararları sonuçlara bakmadan yazılır. Komut, sürüm, tam sayı denetimi ve duyarlılık tabloları saklanır. Python hesapları R/SPSS/G\*Power’ın çalıştırıldığı anlamına gelmez. Rubrik: hedef/tasarım 25, etki gerekçesi 25, hesap/birim 25, kayıp/çokluk 15, yeniden üretim 10 puan.


## Revizyon 9: eşdeğerlik gücü ve hassasiyet

## T1–T3: Güç ve Hassasiyet Hedeflerini Eşleştirme

1.  Eşdeğerlik sınırı her iki planda $(-5,5)$; gerçek fark varsayımı değişir. 0 için önceki 69’da .798512, 70’te .805931; 2.5 için 198’de .799080, 199’da .800840 güç bulunur. Toplamlar 140 ve 398’dir. Ana 64 kişi/grup planı, sıfırdan farklılık testi ve gerçek fark 5 varsayımıyla .801460 gücü hedefler; aynı hipotez değildir. Gerçek fark 5 eşdeğerlik sıfır hipotezinin sınırındadır; eşdeğerlik red olasılığı .05’i aşmamalıdır ve .80 güce erişmesi istenmez. Öğretim sınırları alan kanıtı yerine geçmez.

2.  n=194, s yerine $\sigma$ konan planlama yarı genişliğini 2’nin altına indirir; gerçekleşen rastgele yarı genişliğin bu hedefi sağlama olasılığı .530073’tür. n=210’da .893633, n=211’de .906617 ile en az .90 olasılık ilk sağlanır. Bu, sabit $\sigma=10$ ve normal/eşit varyanslı iki grup altında genişlik olayının olasılığıdır. %95 aralık kapsaması veya sıfır hipotezinin red gücü değildir; gözlenmiş aralık için posterior olasılık da değildir.

3.  Tekrarlar normal ortalama farkı ve ki-kare varyansın kuramsal dağılımlarından alınır. Yeni katılımcı veya klinik pilot üretmez; mevcut/gelecek verinin varsayımlarını doğrulamaz. Daha fazla tekrar yalnız Monte Carlo hatasını küçültür. Pilotun bilinmeyen gerçek $\sigma$’sı için önsel üzerinden bütünleştirme yapılmamıştır. Güç, genişlik ve tutulma aynı değişkenlere bağlı olabilir; ortak olayın olasılığı bağımsızlık gerekçesi veya ortak model olmadan marjinal olasılıkların çarpımı değildir. Bu uygulamada kayıp modeli birleştirilmemiştir.

## Ç1 çıkış sorusunun yanıtı

Hayır. Güç, belirli gerçek etki ve model altında tekrarlı çalışmaların red olasılığıdır; tek çalışmaya garanti vermez.
