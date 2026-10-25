# Bölüm 14 — açıklamalı çözümler

Revizyon 17; yeni T1–T3 dahil.

## Kendinizi Sınayın

Hayır. Rastgele atanmış gruplarda kovaryat hata varyansını azaltarak kesinliği artırır. Rastgele atanmamış gruplarda kovaryat yalnız ölçülmüş başlangıç farkını istatistiksel olarak düzeltir; ölçülmemiş farkları, ölçme hatasını (düzeltme eksik kalır) ve grup ile kovaryat ilişkisini ortadan kaldırmaz; sonuç nedensel “eşitleme” değildir.

## Kolay Düzey

1.  ANCOVA, sayısal kovaryatı içeren doğrusal modelde grupları aynı kovaryat düzeyinde karşılaştırır. Bütün başlangıç farklarını veya karıştırıcılığı kendiliğinden gidermez.

2.  Belirtilmiş kovaryat değerinde modelin tahmin ettiği grup ortalamasıdır. Ham ortalama veya tek bir bireyin düzeltilmiş puanı değildir.

3.  Kovaryat–yanıt doğrusal eğiminin gruplarda aynı olmasıdır; grup$\times$kovaryat terimi bu kısıtı sınamak için kullanılabilir. Anlamsız test eşitlik ispatı değildir.

4.  Kuramsal rol, ölçüm zamanı, güvenirlik, yanıtla ilişki ve ortak destek önemlidir. Yalnız anlamlılıkla seçim yapılmaz; işlemden etkilenmiş bir değişken hedeflenen etkiyi değiştirebilir.

5.  Ölçülen kovaryat eklendikten sonra grup farkı için kanıt zayıflamış olabilir. Farkın kesin sıfır olduğu veya kovaryatın nedensel olarak bütün farkı açıkladığı söylenmez; aralıklar, hedef karşılaştırma ve model kontrol edilir.

## Orta Düzey

1.  Grup$\times$kovaryat etkileşimi ortak eğim kısıtına karşı kanıt verir. Tek bir bütün-aralık grup farkı yerine destek içindeki koşullu farklar ve bunların aralıkları değerlendirilir.

2.  Kovaryat dağılımları ve modeldeki düzeltme, ham karşılaştırmadan farklı bir karşılaştırma üretmiştir. Yönün değişmesi tek başına düzeltilmiş karşılaştırmanın nedensel veya daha doğru olduğunu kanıtlamaz.

3.  İşlem öncesindeki düzeyi temsil eden, güvenirliği yeterli ve ilgili bir ön-test hata varyansını azaltabilir ve başlangıç düzeyini hesaba katar. Ölçüm hatası, eksikler ve örtüşme ayrıca değerlendirilir.

4.  İşlem sonrası değişken bir aracı veya çarpıştırıcı olabilir; kontrol etmek hedefi değiştirebilir veya yanlılık doğurabilir. Her işlem sonrası değişken aynı şekilde ele alınmaz; nedensel rol gerekçelendirilir.

5.  ANCOVA’nın hedefi aynı kovaryat düzeyindeki model karşılaştırmasıdır. Ham ortalamalar da veri tanıtımında korunur; düzeltilmiş ortalamanın referansı ve belirsizliği açık yazılır.

## İleri Düzey

1.  Kovaryatın hata varyansını azaltma yararı sınırlı olabilir; fakat kuramsal/karıştırıcı rolü sırf p büyük diye yok sayılmaz. Örneklem ve ölçüm kalitesi dikkate alınır.

2.  Etkileşimli model, ayrı eğimler ve önceden belirlenmiş kovaryat düzeylerinde kontrastlar incelenir. Doğrusal ilişki de ayrıca denetlenir; esnek veya kategorik alternatifler gerekebilir.

3.  Ölçüm hatası düzeltmeyi zayıflatabilir ve katsayıları yanıltabilir. ANCOVA kovaryatı hatasız hâle getirmez; güvenirlik ve uygun ölçüm modeli gerekebilir.

4.  Yalnız ölçülen kovaryatlar, seçilen ilişki biçimi ve varsayımlar altında kontrol edilmiştir. Ölçülmeyen farklar, ortak destek eksikliği ve model hatası kalabilir.

5.  Kaynak/örneklem, bağımlı değişken ve grup, kovaryatın rolü/zamanı, kodlama/merkez, model ve varsayımlar, referans ortalamalar, kontrast aralıkları/aile düzeltmesi, F/sd/p, tanımlı etki büyüklüğü, duyarlılıklar ve sınırlılıklar verilmelidir.

## D1–D3: Modelden Önce

1.  Yanıt `len`, grup `supp` (OJ/VC), sayısal kovaryat `dose`’dur. Doz uygulanan miktardır; hayvanın işlem öncesi ölçülen özelliği değildir. Bu matematiksel ANCOVA örneğini öğrenci ön-test/son-test çalışması diye sunmak yanlıştır. Uzunluk birimi kısa kaynakta açık olmadığından kaynak ölçeği korunur.

2.  Her grupta .5, 1 ve 2 mg/günde 10 kayıt vardır; gözlenen doz noktalarında destek örtüşür. 3 mg/gün dışarıdadır; burada tahmin dışa kestirim olur. Ortak min–maks aralığı içinde bulunmak bile çok seyrek bölgelerde yeterli veri garantisi değildir.

3.  P değeri değişkenin ölçüm zamanını, karıştırıcı/aracı rolünü veya güvenirliğini belirlemez. Sırf anlamlı diye işlem sonrası değişken eklemek hedefi değiştirebilir; sırf anlamsız diye kuramsal kontrolü silmek de uygun olmayabilir.

## G1–G4: Rehberli Çözüm

1.  $d=1$ için $x=0$’dır. Ortak modelde VC=15.336071 ve OJ=$15.336071+3.7=19.036071$ bulunur. İki grupta $\bar d_g=7/6$ olduğundan ham ortalamalardan aynı düzeltme çıkarılır: $$9.763571(7/6-1)=1.627262.$$ VC için $16.963333-1.627262=15.336071$, OJ için $20.663333-1.627262=19.036071$’dir. Ham ve düzeltilmiş fark bu dengeli tasarımda 3.7 kalır; bu her veri setinde beklenmez. Ortak eğim modelinin burada nihai yorum modeli olmadığı da belirtilir.

2.  Ek KT $1022.555036-933.634929=88.920107$, pay sd 1, payda MSE $933.634929/56=16.672052$’dir. Sonuç $F(1,56)=5.333483$, $p=.024631$ olur. Bu testte hücre modelinin $712.106/54$ MSE’sini kullanmak farklı test üretir. Tek parametreli etkileşim için $F=t^2$ kontrolü de yapılabilir.

3.  Etkileşim modelinde 1 mg/gün için $L=[0,1,0,0]$; fark 4.350714, SH=$\sqrt{LVL'}=1.091266$’dır. Üç dozluk aile için $$4.350714\pm t_{1-.05/6,56}(1.091266)
    =[1.657445,7.043983]$$ ve düzeltilmiş $p=.000588$ bulunur. Bu fark aralığı, tekil ortalama güven aralığı veya bireysel hayvan tahmin aralığı değildir. Etkileşim modelinin doğrusal şekil sorunu nedeniyle hücre modeliyle karşılaştırılır.

4.  $\eta_p^2=205.35/(205.35+1022.555036)=.167236$ bulunur. Pay, doz modeline grup eklemenin açıkladığı ek KT’dir; payda bu KT ile ortak modelin hata KT’sidir. Bu toplam yanıt varyansının veya nedensel etkinin oranı değildir; başka modelde aynı sayıyı beklemek gerekmez. Etki büyüklüğü GA’sı hesaplanmamıştır.

## B1–B3: Bağımsız Çözüm

1.  Yeni merkezde OJ–VC grup katsayısı $4.350714-3.904286=.446429$ olur. VC sabit terimi $15.010714+11.715714=26.726429$’a taşınır. İma edilen yanıtlar, SSE, eğimler ve etkileşim testi değişmez; yalnız katsayıların referans yorumu değişir.

2.  İki grubun ayrı doğruları dört parametre, altı serbest hücre ortalaması altı parametre kullanır; fark iki sd’dir. Ek KT 221.528929, hücre MSE’si $712.106/54=13.187148$; $F(2,54)=8.399425$, $p=.000667$ bulunur. Ortak eğimi reddedip ayrı doğrulara geçmek bütün ortalama-biçim sorunlarını çözmemiştir. Doz bazındaki esas yorum hücre modeline dayandırılır; yeni dozlara genellenmiş eğri iddia edilmez.

3.  Son dozda OJ–VC farkı $26.06-26.14=-.08$ olur. Üçlü Bonferroni aralığı $[-4.092698,3.932698]$’dir; düzeltilmiş p 1’e sınırlandırılır. Sıfırdan ayrışma gösterilmez; eşdeğerlik için ayrı bir tolerans ve sınama gerekir. HC3 aynı katsayıların kovaryans tahminini değiştirir; tek-kayıt koşuları veriyi birer satır eksilterek yeniden tahmin eder. İkincisinin sonuç aralığı güven aralığı değildir. Ana analizde kayıt silinmez.

## H1: Hatalı Raporu Onarma

1.  Doz ön-test değil, uygulanan koşuldur. Model bütün başlangıç farklarını veya karıştırıcıları temizlemiş değildir; rastgeleleştirme/körleme kısa sözlükten varsayılamaz.

2.  Altı hücrede medyan merkezli Levene $p=.148361$ eşit varyansı reddetmez; bağımsızlık, doğrusal şekil ve ortak eğim için onay vermez.

3.  Ortak modelin 3.7 farkı modelin dayattığı sabit farktır. Eğim etkileşimi $p=.024631$ olduğundan bütün dozlarda aynı fark yorumu uygun değildir. Ayrı modelde fark $4.350714-3.904286(d-1)$ olarak değişir.

4.  Ayrı eğimler için hücre modeline karşı $p=.000667$ bulunmuştur. Doğrusal biçim sorunu devam eder; HC3 eklemek bunu da onarmaz.

5.  2 mg/gündeki farkın aralığı sıfırı içerir ve kayda değer farkları da dışlamaz. Anlamsızlık eşdeğerlik değildir; .5 ve 1 mg/gündeki anlamlılıkla doğrudan “farklar arası fark” testi yapılmış da olmaz.

6.  Üç doz kontrastı tek aile olarak tanımlanmalıdır. Her dozdaki ayrı iki-grup düzeltmesi dozlar arasını otomatik kapsamaz. Burada Bonferroni aralıkları her modeldeki üç farkı kapsar; modeller arasındaki arama/karar sürecini düzelttiği iddia edilmez. Değerler Python ile hesaplanmış, R/`emmeans` ile aynı bulunmuştur.

## T1–T3: Hedef Dağılım ve Ön-Test Denetimi

1.  $\Delta=(5.25,5.93,-.08)$ ile eşit hedef 3.700, düşük doz hedefi $.6(5.25)+.3(5.93)+.1(-.08)=4.921$, yüksek doz hedefi $.1(5.25)+.1(5.93)+.8(-.08)=1.054$ olur. Hedef dağılım değişince genel olarak parametre değişir; küçük p seçilmez. Her grupta ayrı doz ağırlıkları kullanmak aynı dağılıma standardizasyon değil, bileşim farkını da içeren karşılaştırmadır.

2.  Hücre katsayı sırasıyla $L_w=(-w_1,-w_2,-w_3,w_1,w_2,w_3)$ ve $SH=\sqrt{L_wVL_w'}$ kullanılır. Hücre OLS üçlü aralıkları \[1.3833,6.0167\],\[2.1995,7.6425\],\[-2.2059,4.3139\]’dur. Ortak eğim modelinde fark bütün dozlarda aynı $\tau$ olduğundan tek kontrast vardır. Hücreleri ağırlıklandırmak ara dozda tahmin yapmak değildir; hedefin ortalama dozunda hücre olmaması bu toplamı engellemez. Yeni aile önceki doz ailesini veya model aramasını topluca düzeltmez.

3.  Y’den X çıkarılınca yalnız X katsayısı $\beta$’dan $\beta-1$’e değişir; aynı tasarımda grup katsayısı ve artıklar korunur. X’i çıkarmak Y ölçeğinde ön-test eğimini 1’e kısıtlar; yalnız son-test modeli ise 0’a kısıtlar. Uygunluk ve nedensel yorum ayrı sorulardır. ToothGrowth dose uygulanan koşuldur, ön-test değildir ve yanıtla aynı ölçekte puan değildir; sayısal çıkarma yapabilmek anlamlı değişim puanı üretmez.

## P1: Ön-Test Kontrollü Yeni Bir Çalışma

Örnek protokolde öğretim grupları, son-test yanıtı ve işlemden önce uygulanacak, güvenirliği yeterli bir ön-test tanımlanır. Rastgele atama yapılacaksa yöntemi planlanır; yapılmış gibi yazılmaz. Ön-test, işlem sonrası katılım veya motivasyonla karıştırılmaz. Eksik veri kuralları, ölçüm hatası, grup bazında kovaryat desteği ve olası bağımlı sınıf/okul birimleri önceden değerlendirilir. Sınıf kümeleri varsa bağımsız birey ANCOVA’sının standart hataları otomatik uygun kabul edilmez.

Birincil karşılaştırma için ortak destek içinde kuramsal anlamı olan ön-test referansı belirlenir. Ortak ve ayrı eğim ile doğrusal biçim kontrolleri planlanır; yalnız p değerine göre sürekli model değiştirmekten kaçınılır. Koşullu farkların hangi düzeylerde raporlanacağı ve karşılaştırma ailesinin büyüklüğü belirtilir. Düzeltilmiş ortalamalar, fark aralıkları, uygun etki büyüklüğü, ham özetler ve sağlamlık/duyarlılık sonuçları birlikte sunulur. Doğrusal biçim veya destek sorunları varsa başka model ve veri toplama gereksinimi açıkça yazılır.

Kaynak, kodlama, merkezleme, yazılım/sürüm ve yeniden üretim komutları saklanır. Yeni öğrenci verisi toplanmadıysa “planlandı; henüz veri yok” denir. ToothGrowth kayıtları öğrenci başarı puanı diye yeniden etiketlenmez. SPSS/R dosyalarının varlığı bu yazılımların çalıştırıldığı anlamına gelmez. Rubrik: kaynak/tasarım 20, model/hesap 30, kontrast/belirsizlik 25, yorum/sınırlılıklar 15, yeniden üretim 10 puan.

## Uygulama Teslim Kontrolü

Beklenen denetim zinciri: 60 kayıt ve altı hücrede 10’ar gözlem; ortak/ayrı/hücre hata sd’leri 57/56/54; OJ–VC yönü ve 1 mg/gün merkezi; tekil ortalama aralıklarının fark aralıklarından ayrılmasıdır. Ayrı doğruların biçim testi $F(2,54)=8.399425$, hücre modelindeki genel grup–doz etkileşim testiyle aynı hipotez değildir.

SPSS’te `oj=1` eksi `oj=0` satırı okunur. Ayrı/hücre çağrılarının genişletilmiş aralıkları üçlü aile içindir; ham p ayrıca $\min(3p,1)$ ile raporlanır. Aralığı bir kez daha genişletmek çift düzeltme olur. `duzeltilmis_ortalamalar.csv` ortalamaları, `karsilastirmalar.csv` kontrastları içerir. R sonuçları paketteki betikle doğrulanmıştır; SPSS sözdizimi aynı tanımlarla hazırlanmıştır.
