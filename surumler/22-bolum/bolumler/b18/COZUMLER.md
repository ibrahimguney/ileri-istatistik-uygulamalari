# Bölüm 18 — açıklamalı çözümler

Revizyon 21; yeni T1–T3 dahil.

## Kendinizi Sınayın

Hayır. PCA toplam varyansı (özgül ve hata varyansı dâhil) en az bileşenle özetler; ortak faktör modeli yalnız maddeler arasındaki ortak varyansı açıklar, maddeye özgü varyansı ayrı bir terimde tutar. Bu yüzden PCA yükleri genellikle daha büyük çıkar ve gizil yapı sorusu için AFA uygundur.

## Kolay Düzey

1.  Sıfır sıralı ve kısmi korelasyon karelerini karşılaştıran uygunluk ölçüsüdür; tek başına örneklem büyüklüğü yeterliği veya temsil gücü testi değildir.

2.  Korelasyon matrisinin birim matristen farklı olduğuna ilişkin kanıttır; faktör sayısını, iyi model uyumunu veya geçerliği kanıtlamaz.

3.  Birden fazla faktöre benzer yük veren maddedir.

4.  Madde içeriği ve kurama göre yapılır.

5.  Hayır; diğer ölçütlerle birlikte değerlendirilir.

## Orta Düzey

1.  Veri faktör analizi için zayıf görünür.

2.  İki boyutlu aday çözümü incelemeyi destekler; özdeğerlerin bileşen mi azaltılmış matris özdeğeri mi olduğu belirtilmeli, paralel analiz ve içerik birlikte değerlendirilmelidir.

3.  Çapraz yüklenen madde olarak içerikçe incelenir.

4.  İstatistiksel çözüm kuramsal olarak anlamlı değilse kabul edilmemelidir.

5.  Aynı çıkarımın yüklerini yorumlanabilir biçimde yeniden gösterir. Uygun matris dönüşümüyle ortak varyans ve artık uyumu değişmez; eğik çözümde faktör korelasyonu hesaba katılır.

## İleri Düzey

1.  Özdeğer kuralı tek başına fazla/eksik faktör verebilir.

2.  Küçük örneklem kararsız yükler ve tekrarlanamayan çözüm doğurabilir.

3.  Paralel analiz, içerik, çapraz yük ve artıklar incelenir; üçüncü boyut yönteme veya madde içeriğine bağlı olabilir. Yeni/ayrılmış veride gerekçeli DFA planlanır; aynı veriyi tekrar kullanmak bağımsız doğrulama değildir.

4.  Ayırt edici geçerlik zayıf olabilir.

5.  KMO, Bartlett, yöntem, rotasyon, özdeğer, varyans, yükler, çapraz yükler ve faktör adları verilmelidir.

## Gerçek Veri Etkinliklerinin Açıklamalı Yanıtları

Aşağıdaki sonuçlar `psych::bfi` verisinin keşif yarısı (yarım A, $n=1316$), on A/C maddesi, Pearson matrisi ve belgelenmiş ters anahtar içindir.

## D: Ön İşlem ve Uygunluk

1.  AFA’dan sonra bölmek, keşfin sonuçlarını (hangi maddelerin iyi çalıştığını) görerek bölme veya madde seçimi yapma olanağı bırakır; doğrulama yarısı artık keşiften bağımsız olmaz. Analizden önce sabit tohumla bölmek ve `bolme.csv` dosyasını saklamak, bölmenin sonuçlara göre değiştirilmediğini denetlenebilir kılar ve başkasının aynı yarıları yeniden üretmesini sağlar.

2.  Büyük örneklem tahminlerin örnekleme belirsizliğini azaltır, ama model yanlışlığını, madde içeriğini, ölçüm türünü (altı kategorili yanıt) veya örneklemin kime genellenebileceğini düzeltmez. Bu veride üç faktörlü çözüm 1316 kişiye rağmen Heywood durumuna düşmüştür; büyük n uygunsuz modeli uygun yapmaz.

3.  Ters çevrilen standart madde, korelasyon matrisinin ilgili satır/sütun işaretini değiştirir. $R^*=DRD$ ve $D^2=I$ olduğundan özdeğerler ve determinant korunur; korelasyon ve kısmi korelasyon kareleri de korunur. Bu yüzden KMO/Bartlett yanlış yönü yakalamayabilir. Puanlama anahtarı içerikten doğrulanır; aynı KMO yanlış toplam puanı meşrulaştırmaz.

## G: Rehberli Hesaplar

1.  KMO $6.275687/(6.275687+1.724063)=.784485$’tir. Bartlett çarpanı $1316-1-25/6=1310.833333$; $-1310.833333\times(-2.151426)=2820.16$ ve $sd=10(9)/2=45$ olur; $p<.001$. Faktör sayısı, bağımsızlık, kültürel eşdeğerlik ve tüm maddelerin iyi temsil edildiği bu iki istatistikten çıkmaz; büyük örneklemde birim matristen küçük sapmalar bile saptanabilir; gerçek küresellik altında anlamlılık zorunlu değildir.

2.  PCA sürümünde 3.064 \> 1.174 ve 1.864 \> 1.125, fakat 0.876 \< 1.087; karar iki boyuttur. SMC sürümünde ilk dört değer (2.375, 1.165, .131, .093) referansları (.186, .135, .095, .064) aşar; beşinci değer (.012) aşmaz, karar dörttür. Bu örnekte permüte matrislerin SMC’leri sıfıra yakın olduğundan referanslar küçüktür; .131 ve .093 değerlerinin bunları aşması tek başına içerik önemini veya kararlı ortak faktörleri kanıtlamaz. Üç faktörlü PAF denemesi uygunsuzdur; Revizyon 21 ekindeki dört faktörlü PAF da aynı SMC başlangıcıyla 2000 yinelemede yakınsamaz (en büyük ortak varyans 1.669407). İki faktör içerik, PCA paralel analizi ve yük/artık incelemesiyle aday olarak izlenir; dört faktörün uygunluğu ayrıca sınanmadan reddedilemez.

3.  A4 için yapı C katsayısı $.130377+.460568(.317112)=.276429$’dur. Ortak varyans $.460568^2+.130377^2+2(.460568)(.130377)(.317112)=.267205$; özgüllük .732795 olur. Yalnız örüntü kareleri toplamı .229121’dir; faktör ilişkisine ait çapraz terim (.038084) eksik kalır. .276 yapı korelasyonudur, .130 örüntü katsayısıyla karıştırılmaz.

4.  İki faktörde $\sum h_j^2=3.718418$ ve $\sum h_j^2/10=.371842$’dir. PCA oranı $(3.064124+1.863922)/10=.492805$ olup farklı bir toplam-varyans hedefini özetler. On maddenin benzersiz köşegen dışı çift sayısı $10(9)/2=45$’tir. İki faktörlü RMSR .037685; 45 çiftten 11’inde $|e|>.05$ vardır. Bu tarama işareti anlamlılık testi değildir.

## B: Bağımsız Model İncelemeleri

1.  A1 için $$h^2=.438069^2+(-.108918)^2+2(.438069)(-.108918)(.317112)=.173507.$$ Özgüllük .826493’tür. Çapraz terim negatiftir; yalnız kareleri toplamak (.203767) ortak varyansı olduğundan büyük gösterir. C yapı katsayısı .030 iken C örüntü katsayısı $-.109$’dur. Belgelenmiş puan yönü doğrudur; bu küçük negatif koşullu katsayı yeniden ters kodlama gerekçesi değildir.

2.  Bir faktörde RMSR .129158, en büyük mutlak artık .250450 ve .05’i aşan 41/45 çift vardır; tek genel faktör A ve C içeriklerini ayırt etmediği için ilişkilerin önemli bölümü açıklanmadan kalır. Üç faktörlü deneme 2000 yinelemede yakınsamaz ve bir ortak varyans 1.94’e çıkar. Bu bulgu dört faktörlü PAF hakkında sonuç vermez. Raporda “üç faktörlü PAF uygunsuz çözüm (Heywood durumu) verdiği için yorumlanmadı” yazılır; yakınsamayan çözümün yükleri tabloya konmaz.

3.  A1/A4 çıkarılıp *aynı 1316 kişi* korununca sekiz maddelik iki faktörlü PAF 84 yinelemede yakınsar: RMSR .031820, en büyük $|e|=.086022$, .05’i aşan çift sayısı 4/28, ortak varyans oranı .411491’dir. Önceki oran .371842’ydi. Madde evreni ve payda 10’dan 8’e, artık çiftleri 45’ten 28’e değiştiği için bu artış doğrudan aynı yapının daha iyi ölçüldüğünü göstermez; zayıf maddeleri çıkarmak ortalama temsili mekanik olarak yükseltir. Seçim aynı veriden yapıldığı için iyimserlik de doğabilir. Bu bir duyarlılık incelemesidir; ana analizden madde silinmemiştir.

## H1: Raporu Onarma

1.  KMO/Bartlett ölçek geçerliği göstermez; yalnız korelasyon matrisinin faktör analizine uygunluğuna ilişkin ön bilgidir.

2.  SMC sürümü bu veride dört, PCA sürümü iki aday boyut önermiştir. Bu ayrım doğrudan bir faktör sayısı kararı yerine ek inceleme gerektirir. Revizyon 21 ekinde dört faktör doğrudan denenir ve bu yordam/başlangıçta Heywood ile yakınsamaz; yükler yorumlanmaz. Bu sonuç tüm dört faktörlü modelleri reddetmez; alternatif kestirim, içerik ve örnekleme kararlılığı ayrıca incelenir.

3.  Varimax, aynı çıkarımın ortak matrisini ve artıklarını değiştirmez; yalnız gösterimi değiştirir. Quartimin için aynı matris $\Lambda\Phi\Lambda'$ ile üretilir.

4.  A4’ün C örüntü katsayısı .130, yapı katsayısı .276’dır. Yapı katsayısı faktörler arası korelasyonu da içerir; ikisi ayrı raporlanır.

5.  Aynı 2632 kişinin yarısında model keşfedildiyse, DFA yalnız dokunulmamış yarım B’de yapılmalıdır. Keşif yarısını da içeren veriyle yapılan DFA bağımsız sınama değildir.

## P1: Kanıt Dosyası ve DFA’ya Geçiş

Dosyada kaynak, 168 eksik kaydın dışlanması, bölme tohumu (20261001) ve yarım büyüklükleri, A1/C4/C5 anahtarı, Pearson tercihi, paralel analizin iki sürümü/tohumu/2000 tekrarı ve farklı kararları, üç faktörlü denemenin Heywood sonucu, PAF toleransı ve quartimin normalizasyon kararı bulunmalıdır. Tam örüntü, yapı, $\Phi$, ortak varyans ve artık tabloları eklenir; küçük yükler gizlenmez.

Yarım B için önceden yazılacak DFA modeli: iki ilişkili faktör, her madde yalnız kendi içerik faktörüne yüklenir (basit yapı; AFA’da çapraz katsayılar $|.13|$’ü aşmadı). Artık taramasında öne çıkan C4–C5, C1–C2 ve A1–A2 çiftleri için ilişkili hata terimleri *alternatif* model olarak, içerik gerekçesiyle önceden listelenir. Karar ölçütleri (uyum indeksleri birlikte, yerel artıklar, yük büyüklükleri) yarım B açılmadan yazılır. Rubrik: kaynak/ön işlem 20, yöntem/hesap 30, matris yorumu 25, sınırlılıklar/doğrulama planı 15, yeniden üretim 10 puan.

## T1–T3: Faktör Sayısı ve Puan Denetimi

1.  Aynı SMC başlangıcıyla dört faktörlü PAF, 2000 yinelemede yakınsamaz; son norm .000128141, en büyük ortak varyans 1.669407’dir. Negatif özgüllük/Heywood uygunsuzluğu nedeniyle kabul edilmiş yük veya puan tablosu verilmez. Bu sayısal deneme tüm başlangıçları, MINRES/ML/ordinal modelleri reddetmez; iki faktörü tek doğru sayı yapmaz.

2.  Regresyon puanları $V_{\rm reg}=\Phi-C$ kovaryansına sahiptir; normalize edilmiş korelasyonu .391331, gözlenen yarım A’daki korelasyonu .391078’dir. $\Phi$’deki .317112 başka bir niceliktir. Bartlett için model/gözlenen puan korelasyonları .238858/.238580’dir. Puanlama yöntemi değişmiştir; madde modeli, ortak matris ve madde uyumu değişmez. Puanlar gözlenmiş hatasız faktörler değildir.

3.  Koşullu standart sapmalar .472962/.494400, normal %95 yarı genişlikler .926989/.969007’dir. Sabit kabul edilen model parametrelerine koşulludur; yük, faktör sayısı/rotasyon belirsizliği, ordinal yapı ve uyumsuzluk dışarıdadır. Yeni örneklemde kapsama veya bireysel tanı doğrulanmamıştır. Madde sırası, anahtar, eğitim ortalama/standart sapmaları ve katsayılar saklanır; yeni yarıyla yeniden ölçekleme farklı kuraldır. Bu ekte B yanıtları okunmaz/puanlanmaz. Sonuç görülerek değişiklik yapılırsa keşifsel diye belgelenir; dosyalama dış zaman damgalı ön kayıt sayılmaz.
