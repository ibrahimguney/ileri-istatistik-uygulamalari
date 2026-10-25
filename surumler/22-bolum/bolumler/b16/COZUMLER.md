# Bölüm 16 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

Hayır. Okul türü okul içinde sabittir; düzey 2 ilişkisinin tahmini için 160 okulun sayısı ve özellikleri önemlidir. Öğrenciler arasındaki kümelenme de belirsizlik hesabına katılmalıdır. Yaklaşık 806 etkili gözlem hesabı bir ortalama için kaba tasarım etkisinden gelir; okul türü veya bütün öğrenci düzeyi katsayıları için ortak bir örneklem büyüklüğü değildir.

## Kolay Düzey

1.  Toplam varyansın gruplar arasındaki payını; eşdeğer olarak aynı gruptan rastgele seçilen iki gözlem arasındaki korelasyonu.

2.  Rastgele kesişim grupların ortalama düzeyinin (sabit terimin) gruptan gruba değişmesine izin verir; rastgele eğim bir yordayıcının etkisinin gruptan gruba değişmesine izin verir.

3.  Düzey 1 yordayıcısından kendi grubunun ortalamasını çıkarmaktır; böylece değişken grup içi farklılığı taşır; uygun modelde katsayı okul içi ilişkiyi temsil eder. Bu dönüşüm tek başına nedensel etki sağlamaz.

4.  $\mathrm{DE}=1+(\bar n-1)\mathrm{ICC}$; her ek grup üyesi yeni bağımsız bilginin yalnız bir kısmını getirir. Aynı ICC’de büyük kümeler çok daha az etkili gözlem demektir.

5.  REML, varyans bileşenlerini raporlamak ve aynı sabit yapıdaki rastgele etki yapılarını karşılaştırmak için; ML, sabit etki yapıları farklı modelleri olabilirlik oranı veya bilgi ölçütleriyle karşılaştırmak için kullanılır.

## Orta Düzey

1.  $\mathrm{DE}=1+29(.05)=2.45$: standart hatalar yaklaşık $\sqrt{2.45}=1.57$ kat küçük görünür. ICC küçük olsa da bu fark önemlidir; çok düzeyli model veya küme-sağlam SH kullanılmalıdır.

2.  Bağlamsal etki $1.5-1.5=0$’dır: grup ortalamasının, bireyin kendi değerinin ötesinde ek bir ilişkisi yoktur; tek bir eğim iki düzeyi yeterince temsil eder.

3.  Grup ortalamasına merkezlenmiş bir yordayıcı grup içi varyansı açıklar; model gruplar arası farkların bir kısmını daha önce $\sigma^2$’ye yazdığı için $\tau_{00}$ artabilir. Ayrıca tamamen düzey 1’de değişen bir yordayıcı, gruplar içinde kompozisyon farklılıklarını ortaya çıkararak grup ortalamalarının düzeltilmiş farklarını büyütebilir. Bu nedenle düzey başına $R^2$ negatif çıkabilir.

4.  Düzey 2 için yalnız 12 bağımsız birim vardır: sabit etkinin standart hatası belirsiz, varyans bileşeni yanlı ve dengesizdir. Kenward–Roger veya Satterthwaite sd düzeltmesi, basit modeller ve sonuçların temkinli raporlanması gerekir; mümkünse daha çok okul toplanır.

5.  Rastgele eğim modelden çıkarılıp rastgele kesişimli modelle karşılaştırılır (sınırda LR); sonuç raporlanır. Kuramsal olarak eğimin değişmesi bekleniyorsa, farklı başlangıç ve çözücülerle yeniden kestirim, yordayıcının ölçeklenmesi veya kesişim–eğim korelasyonunu sıfıra sabitlemek denenebilir. Uyarı gizlenmez.

## İleri Düzey

1.  Okullar arası eğim (5.87) öğrenci düzeyinde yorumlanırsa, SES’in öğrenci başarısıyla ilişkisi abartılır (ekolojik yanılgı); gerçek okul içi eğim 2.19’dur. Tersine okul içi eğimden okulların ortalamaları hakkında sonuç çıkarmak (atomistik yanılgı) okul düzeyindeki ek ilişkiyi (bağlamsal etki 3.68) kaçırır.

2.  Ham yordayıcının katsayısı grup içi ve gruplar arası ilişkilerin karışımı olur; rastgele kesişim yordayıcıyla ilişkiliyse bu karışım yanlıdır (ihmal edilmiş değişken yanlılığı). Grup ortalamasına merkezleme ve grup ortalamasını modele eklemek okul içi/gruplar arası bileşenleri ayırır. Doğrusal ortak eğimli uygun modelde okul içinde sabit eklenebilir özellikler okul içi sapmayla birlikte değişmez. Ancak bu, öğrenci düzeyindeki karıştırıcıları, ölçüm hatasını veya eğim heterojenliğini kendiliğinden gidermez; her karma modelin okul sabit etkileri kestirimine eşdeğer olduğu da söylenemez.

3.  Genel ortalamaya merkezlemede düzey 1 katsayısı grup içi ve gruplar arası etkilerin karışımıdır; etkileşim de bu karışımın grup özelliğine göre değişimini gösterir ve yorumu belirsizleşir. Grup ortalamasına merkezleme, düzeyler arası etkileşimi saf grup içi eğimin düzenlenmesi olarak yorumlanabilir kılar.

4.  Soru yalnız sabit etkilerle ilgiliyse ve gruplar arası değişkenlik ilgi konusu değilse, küme sayısı yeterince büyükken küme-sağlam OLS basit ve varsayımı azdır. Gruplar arası varyans, rastgele eğimler, düzeyler arası etkileşimler, grup tahminleri veya dengesiz/küçük kümelerde verimlilik önemliyse çok düzeyli model tercih edilir.

5.  Düzeyler ve örneklem büyüklükleri (küme sayısı, küme büyüklüğü dağılımı); boş model ve ICC; merkezleme kararları; model denklemleri ve rastgele etki yapısı; kestirim yöntemi (ML/REML) ve yazılım; sabit etkiler (kestirim, SH, sd yöntemi); varyans bileşenleri ve kesişim–eğim korelasyonu; model karşılaştırma testleri (sınır düzeltmesi dâhil); açıklanan varyans ölçüsünün tanımı; yakınsama ve varsayım denetimleri.

## D1–D3: Analizden Önce

1.  Düzey 1 öğrenci, düzey 2 okuldur. SES öğrenci düzeyinde ölçülür (okul ortalaması türetilmiş bir düzey 2 değişkenidir); okul türü (Sector) düzey 2 değişkenidir.

2.  Okul türü bütün öğrencilerde okul içinde sabittir; gerçekte yalnız 160 bağımsız okul gözlemi vardır. Öğrencileri bağımsız saymak okul düzeyindeki bağımlılığı yok sayar ve standart hatayı küçültebilir. Yaklaşık 8.9 tasarım etkisi bir ortalamaya ilişkindir; okul türü katsayısının standart hatasının tam üç kat değişeceği buradan çıkarılamaz. Katsayıya uygun küme-sağlam veya çok düzeyli belirsizlik hesabı gerekir.

3.  Hesaplamanın analiz edilen kayıtlarla tutarlı olması ve yeniden üretilebilmesi; hazır sütunun nasıl hesaplandığı (yuvarlama, farklı örneklem) belgelenmemiş olabilir. Buradaki fark küçüktür (.006) ama iş akışı şeffaftır.

## G1–G4: Rehberli Çözüm

1.  $\mathrm{ICC}=8.614/(8.614+39.148)=.180$; $\mathrm{DE}=1+(44.9-1)(.180)=8.92$; ortalama için yaklaşık etkili $n=7185/8.92=806$. Bu yaklaşım eşit küme büyüklüğü ve ortak ICC varsayımlarına dayanır; burada küme büyüklükleri değiştiği için kaba bir özettir ve her katsayıya uygulanmaz.

2.  $\lambda=8.614/(8.614+39.148/14)=8.614/(8.614+2.796)=.755$. Güvenirlik görece düşük olduğundan (okulların ortalaması .90) okulun gözlenen ortalaması daha gürültülüdür; BLUP okulun ortalamasını $\lambda$ ağırlığıyla, genel ortalamayı $1-\lambda$ ağırlığıyla birleştirir; küçük okul daha çok büzülür.

3.  $5.866-2.191=3.675$. Aynı SES’e sahip iki öğrenciden, ortalama SES’i bir birim yüksek okulda olanın başarısı ortalama 3.7 puan daha yüksektir (betimsel; nedensel değil).

4.  $\tfrac12P(\chi^2_1>10.50)+\tfrac12P(\chi^2_2>10.50)=\tfrac12(.0012)+\tfrac12(.0053)=.0032$. Sıfır hipotezi varyansı sıfırda, parametre uzayının sınırında tanımlar; bu durumda LR’nin asimptotik dağılımı karışımdır ve düz $\chi^2_2$ tutucudur.

## B1–B3: Bağımsız Çözüm

1.  $2.945+1.039(0.5)-1.643=1.822$ puan/SES birimi.

2.  Okul ortalama SES’i ve okul türü eklendiğinde eğim varyansı .701’den .101’e iner; $1-.101/.701=.86$. Bu oran bir örneklem tahminidir, varyans bileşenlerinin belirsizliği büyüktür ve modele göre değişir; varyansın “açıklanması” nedensellik göstermez ve negatif değerler alabilir.

3.  Naif OLS .076, küme-sağlam OLS .169, rastgele kesişimli model .188. Naif SH bağımsızlık varsayımıyla yanlıştır. Küme-sağlam SH, OLS kestiriminin (öğrenci ağırlıklı ortalama) belirsizliğini doğru ölçer; çok düzeyli modelin SH’si, okul ortalamalarını güvenirliklerine göre ağırlıklandıran farklı bir kestiricinin belirsizliğidir.

## H1: Raporu Onarma

1.  ICC .18 okul farklılığının azımsanmayacak olduğunu gösterir; tasarım etkisi 8.9’dur ve bağımsızlık varsayımı standart hataları ciddi biçimde küçültür.

2.  3.18 okul içi ve okullar arası ilişkilerin karışımıdır ve SH .097 naif hesaptır; okul içi eğim 2.19 (SH .11), okullar arası eğim 5.87’dir.

3.  5.87 okul ortalamaları arasındaki ilişkidir; bireysel SES sabitken ek fark (bağlamsal etki) 3.68’dir ve rastgele atama olmadığı için nedensel değildir.

4.  Varyans sıfır hipotezi sınırdadır; karışım dağılımıyla $p=.0032$ bulunur.

5.  Katolik okullarda SES eğimi daha düzdür; ancak okul türü rastgele atanmamıştır, seçilim ve ölçülmemiş farklar olasıdır. “Kanıtlanmıştır” yerine betimsel bir ilişki raporlanır.

## P1: Çok Düzeyli Çalışma Planı

İyi bir plan, müdahale sınıf düzeyinde uygulanıyorsa atama birimini sınıf olarak alır (küme randomize tasarım); öğrenci düzeyinde randomizasyon bulaşma riski taşır. Öğrenci düzeyi (düzey 1), sınıf (düzey 2) ve gerekirse okul (düzey 3) tanımlanır. Benzer çalışmalardan beklenen ICC (ör. .10–.20), hedef etki, sınıf sayısı ve büyüklük dağılımı, atama düzeni ve kayıp senaryoları birlikte kullanılarak güç planlanır. Tasarım etkisi başlangıç yaklaşımı olabilir; özellikle etkileşim ve rastgele eğimler için modele uygun güç hesabı veya simülasyon tercih edilir. 40–50 sınıf gibi bir sayı evrensel alt sınır sayılmaz. Ön test puanı hem grup ortalamasına merkezlenmiş (düzey 1) hem sınıf ortalaması (düzey 2) olarak eklenir. Birincil model rastgele kesişimlidir; ön test eğiminin sınıflar arası değişimi ikincil sorudur. Varyans bileşenleri REML ile, sabit etki karşılaştırmaları ML ile yapılır; sınıf sayısı küçükse Kenward–Roger sd düzeltmesi planlanır. Raporlanacaklar: boş model ICC, model tablosu, varyans bileşenleri, etki büyüklüğü (standartlaştırılmış ortalama fark), yakınsama denetimleri. Kod ve veri sözlüğü paylaşılır. Rubrik: tasarım 25, örneklem 20, model 30, raporlama 15, yeniden üretim 10 puan.
