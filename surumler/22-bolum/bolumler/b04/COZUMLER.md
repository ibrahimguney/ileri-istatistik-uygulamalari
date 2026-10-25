# Bölüm 4 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

Standart sapma bireysel gözlemlerin ortalama çevresinde ne kadar yayıldığını betimler; örneklem büyüdükçe küçülmez. Standart hata, örneklem ortalamasının örneklemden örnekleme ne kadar değişeceğini (kestirimin belirsizliğini) ölçer ve $s/\sqrt n$ ile küçülür. Biri veriyi, diğeri kestirimi betimler.

## Kolay Düzey

1.  Doğru $H_0$ reddedilirse Tip I hata oluşur. Nominal alfa, geçerli test modeli ve plan altında bu olasılığı denetler; belirli bir reddin yanlış olma olasılığı değildir.

2.  $H_1:\mu\ne\mu_0$ yazılır. Hipotez örneklemdeki $\bar x$ değil hedef anakütle ortalaması üzerinedir; referansın neden seçildiği belirtilmelidir.

3.  Güç $1-\beta$, belirli bir gerçek alternatif altında $H_0$’ı reddetme olasılığıdır. Etki, n, varyans, alfa, yön ve tasarıma bağlıdır; tek bir p değerinin başka adı değildir.

4.  Levene testi kullanılabilir; medyan merkezli sürümü ayrıca belirtilir. Reddedilememe eşit varyansların kanıtı değildir. Welch t testi eşit varyans gerektirmez; yöntem yalnız Levene p’sine göre otomatik seçilmemelidir.

5.  İki kategorik değişkenin çapraz tablo sayıları için uygundur. Birimlerin bağımsızlığı ve beklenen hücre sayıları değerlendirilir. Eşli kategorik ölçümlerde sıradan bağımsızlık testi eşleşmeyi göz ardı eder.

## Orta Düzey

1.  $H_0:\mu=500$, $H_1:\mu\ne500$; $SH=10/\sqrt{25}=2$, $t=(496-500)/2=-2$, $sd=24$. Ek hesap: iki yönlü p=.056940, yüzde 95 ortalama aralığı $[491.872203,500.127797]$ ml’dir. .05 düzeyinde reddedilemez; bu tam 500 veya eşdeğerlik kanıtı değildir.

2.  Artış için $H_0:\mu\leq70$, $H_1:\mu>70$; hesap sınırdaki $\mu=70$ altında yapılır. Yön önceden seçilmelidir. 70 geçmiş bir örneklem ortalamasıysa belirsizliğini yok saymak ayrıca gerekçe ister; tek referans karşılaştırması yeni yöntemin nedensel etkisini kanıtlamaz.

3.  Gerçekten bağımsız gruplarda iki örneklem t testi, örneğin Welch kullanılır. Kişilerin farklı olması sınıf/okul içi bağımlılığı ortadan kaldırmaz. Tasarım, dağılım/uç kayıtlar ve ölçüm incelenir; birleştirilmiş varyanslı Student sürümü ayrıca eşit varyans varsayar.

4.  Aynı veri/model/standart hata ile kurulmuş iki yönlü yüzde 95 aralık referansı dışlıyorsa .05 testinde $H_0$ reddedilir. Tek yönlü p, farklı güven düzeyi veya çoklu düzeltmesi farklı aralık aynı eşleşmeyi sağlamaz. Yuvarlanmış sınır değerlerden karar verilmez.

5.  $p=.032<.05$ olduğundan seçilen testte $H_0$ reddedilir. “Belirtilen model altında ilgili sıfır hipotezine karşı istatistiksel kanıt bulundu ($p=.032$).” İlgili tahmin, yön, güven aralığı ve etki büyüklüğü eklenmelidir; p hipotezin doğru olma olasılığı değildir.

## İleri Düzey

1.  $SH=12/\sqrt{36}=2$, $t=(52-50)/2=1$, $sd=35$. Yön, alfa ve test varsayımları belirlenmelidir. İki yönlü model seçilirse p=.324174 ve yüzde 95 ortalama aralığı $[47.939784,56.060216]$ olur. Sağ yönlü p=.162087’dir; iki yönlü .05 testinde reddedilemez.

2.  Alfa .05 ise reddedilemez; etkisizlik kanıtlanmış olmaz. Aralık hem sıfırı hem anlamlı olabilecek etkileri içerebilir. Gerekçeli eşdeğerlik sınırlarıyla ayrı test gerekir. Gözlenen etkiyi gerçek sayan sonradan güç hesabı yeni bağımsız kanıt üretmez.

3.  Büyük n standart hatayı küçültebilir; çok küçük fark da küçük p verebilir. Ham fark/aralık ve açık tanımlı etki büyüklüğü raporlanır; pratik önem alanın karar ölçütleriyle gerekçelendirilir. İstatistiksel anlamlılık yarar veya nedensellik değildir.

4.  Ki-kare referans yaklaşımı zayıflayabilir. Beklenen sayılar ve tablo boyutu değerlendirilir; uygun durumda kesin yöntemler veya tasarımdan gerekçeli kategori düzenlemesi düşünülebilir. 5 eşiği tek başına evrensel kural değildir; kategoriler yalnız küçük p üretmek için birleştirilmez.

5.  Diğer koşullar sabitken n veya gerçek etki büyürse güç genellikle artar, Tip II hata azalır. Gürültü artarsa standartlaştırılmış etki küçülür ve güç azalabilir. Hedef etki, ölçüm kalitesi, kümelenme, kayıp ve çoklu aile planlamada birlikte ele alınır; sadece n artırmak tasarım yanlılığını gidermez.

## D1–D3: Testten Önce

1.  20 satır aynı 10 kişinin iki ölçümüdür. ID üzerinden eşlenen 10 fark için n=10, sd=9 kullanılır. Ana yön koşul 2 eksi koşul 1’dir; satır sırası eşleştirme anahtarı değildir.

2.  Saat birimi ham farkı yorumlatır, koşul kodları hangi ölçümlerin karşılaştırıldığını belirtir. Rastgeleleştirme, uygulama sırası, taşıma etkisi ve hedef anakütle temsili kısa arşivden doğrulanmaz. Negatif extra değerleri hata diye silinmez.

3.  Yön, alfa ve dışlama sonuçlara göre seçilirse nominal hata planı değişebilir. Bu tarihsel örnekte iki yönlü seçim öğretim sözleşmesidir; yeni bir araştırmada gerçekten ön kayıt yapılmış gibi sunulmaz.

## G1–G4: Rehberli Çözüm

1.  On farkın toplamı 15.8, ortalaması 1.58, kareli sapmalar toplamı 13.616’dır: $$\begin{aligned}
    s_D&=\sqrt{13.616/9}=1.229995,\\
    SH&=s_D/\sqrt{10}=.388959,\\
    t&=1.58/.388959=4.062128.
    \end{aligned}$$ Serbestlik derecesi 9’dur. Eşli t ile farklara tek örneklem t aynı hesabı verir. $d_z=1.284558$ ve $d_z\sqrt{10}=t$; standartlaştırıcı kişi farklarının s’sidir.

2.  Kritik değer $t_{.975,9}=2.262157$; ortalama fark aralığı $$1.58\pm2.262157(.388959)=[.700114,2.459886]$$ saattir. Sıfır dışarıda, iki yönlü p=.002832890 olduğundan .05’te red vardır. Aralık ortalama fark içindir; kişilerin yüzde 95’ini kapsayan aralık veya nedensellik kanıtı değildir.

3.  Dolumda $t=-2$, $sd=24$, iki yönlü p=.056940; aralık $[491.872203,500.127797]$ referansı içerir. Reddedilemez; fark aralığı $[-8.127797,.127797]$ ml olduğundan önemli azalmalar da dışlanmamıştır. Sonradan azalış yönünü seçip .028470 raporlamak iki yönlü planı değiştirmektir; artış yönünün doğru p’si .971530’dur.

4.  Sıfır senaryosunda $1004/20000=.0502$ yanlış red; kapsama $1-.0502=.9498$’dir. .5 senaryosunda güç $13334/20000=.6667$, kuramsal değer .669708’dir. Gerçek .5’i kapsama .9474, sıfırı dışlama ise .6667’dir; farklı olaylardır. MC SH .001544 ve .003333 tekrar sayısının belirsizliğidir, gerçek uyku verisinin SH’si değildir.

## B1–B3: Bağımsız Çözüm

1.  Yeni fark ortalaması $-1.58$, $t=-4.062128$ olur; s ve SH değişmez. İki yönlü p=.002832890; sağ p=.998583555’tir. Aralık $[-2.459886,-.700114]$ olur. Eski üst ucun negatifi yeni alt uçtur. Yönü tersleyip eski sağ p’yi kullanmak yanlış alternatif sınar.

2.  Her beklenen hücre $50(50)/100=25$. Dört hücre katkısı $25/25=1$ olduğundan $\chi^2=4$, sd=1, p=.045500, $V=\sqrt{4/100}=.20$ bulunur. Bu düzeltmesiz Pearson hesabıdır; Yates/Fisher aynı sonuç varsayılmaz. Kurgusal tablo gerçek 10 kişiden türetilmez.

3.  En az bir yanlış red $1-.95^{20}=.641514$; Bonferroni tekil eşik $.05/20=.0025$’tir. Çarpım formülü bağımsız testler ve her birinde tam .05 hata varsayar. Bonferroni üst sınırı uygun tekil testlerle bağımlılık altında da kullanılabilir; test ailesi ve seçim süreci açık tanımlanmalıdır.

## H1: Hatalı Raporu Onarma

1.  p, model/$H_0$ altında en az gözlenen kadar uç test istatistiğinin olasılığıdır; $H_0$’ın doğru olma olasılığı değildir.

2.  20 ölçüm satırından 10 kişi farkı vardır. Ana t hesabında n=10 ve sd=9 kullanılır; eşleşme yok sayılamaz.

3.  p=.056940 tam 500’ü kanıtlamaz; aralık azalmaları da içerir. Eşdeğerlik için önceden gerekçeli sınırlar ve ayrı yöntem gerekir.

4.  Sonuca bakarak yön seçmek nominal alfa .05’i korumaz. İdeal sıfır simülasyonunda yanlış yön seçme kuralının red oranı .1016, kuramsal değeri .10 olmuştur.

5.  Verilen aralık ortalama farkın model-temelli güven aralığıdır; kişisel farkların yüzde 95’inin aralığı değildir. Kapsama yorumu tekrarlanan örnekleme yöntemine aittir.

6.  Simülasyon n=25, normal ve sigma=1 ideal modeli içindir. Gerçek uyku verisinin n=10 ve bilinmeyen dağılımına doğrudan aktarılmaz; varsayım doğrulaması veya gözlenen güç raporu değildir.

## P1: Önceden Yazılmış Test Planı

Hedef parametre ve referansın kaynağı tanımlanır; sabit referansla tahmin edilmiş geçmiş ortalama ayrılır. Birim/örnekleme/atama düzeni, eşleşme veya sınıf kümelenmesi açıklanır. Birincil sonuç, ölçüm zamanı, yön ve alfa; planlanan n ve durdurma/ara analiz kararı veri görülmeden yazılır. Gerçekte yapılmamış ön kayıt, rastgele atama veya güç hesabı yalnız plan olarak belirtilir.

Eksik ve geçersiz değer kuralları, dışlama gerekçeleri, model varsayımları ve gerekirse alternatif/duyarlılık yöntemleri belirtilir. Çoklu aile ve düzeltme, ham tahmin ve güven aralığı, etki büyüklüğünün standartlaştırıcısı ile pratik önem ölçütü birlikte planlanır. Eşdeğerlik hedefleniyorsa sınırlar ayrıca gerekçelendirilir. Küçük p için yöntem/yön/durdurma değiştirilmez; bütün planlı sonuçlar raporlanır.

Kaynak/sürüm, kod, yazılım, simülasyon tohumu ve karar günlüğü saklanır. Ana sonuç ile kurgusal öğretim veya simülasyon sonuçları ayrılır. Python hesabı R/SPSS’in çalıştırıldığını göstermez; d için aralık, normallik veya permütasyon yapılmadıysa yapılmış denmez. Rubrik: soru/tasarım 25, hipotez/yön 20, hesap/varsayım 25, belirsizlik/çokluk 20, yeniden üretim 10 puan.
