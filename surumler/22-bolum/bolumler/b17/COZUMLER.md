# Bölüm 17 — açıklamalı çözümler

Revizyon 20; yeni T1–T3 dahil.

## Kendinizi Sınayın

Hayır. Alfa, madde sayısı ve maddeler arası ortalama korelasyonla artar; birden çok ilişkili boyut veya çok sayıda madde de yüksek alfa verebilir. Tek boyutluluk faktör analizi ve artık korelasyonlarla sınanır; alfa ayrıca tau-eşdeğerlik varsayar.

## Kolay Düzey

1.  Güvenirlik tutarlılık, geçerlik doğru yapıyı ölçmeyle ilgilidir.

2.  Yüksek alfa geçerliği kanıtlamaz ve madde tekrarına işaret edebilir.

3.  Maddenin ölçekle zayıf uyumlu olduğunu düşündürür.

4.  Alfa yapay olarak düşebilir.

5.  Alt boyutları tek yapı gibi gösterebilir.

## Orta Düzey

1.  Bu örneklemde görece yüksek iç tutarlılık katsayısıdır; güven aralığı, madde içeriği, yapı ve kullanım amacı olmadan yeterlilik veya geçerlik kararı verilemez.

2.  Madde, kodlama veya içerik açısından incelenmelidir.

3.  $\alpha=\frac{4}{3}(1-5.4/15)=.853333$. Bu hesap öğretim için verilen özetlere aittir; IPIP örneğinin katsayısı değildir. Yüksek değer tek başına tek boyutluluk veya geçerlik kanıtlamaz.

4.  Çok yüksek alfa madde benzerliği/tekrarını düşündürebilir.

5.  Çeviri, uzman görüşü, pilot veri ve kuramsal kapsam incelenir.

## İleri Düzey

1.  Alt boyut güvenirlikleri ayrı verilmelidir.

2.  Belgelenmiş anahtara göre yanlış puanlama düzeltilince tutarlılığın arttığını gösterir. Anahtar yalnız katsayıyı yükseltmek için sonradan seçilmemelidir.

3.  Kültürel uygunluk ve geçerlik ayrıca gerekir.

4.  Yalnız alfaya göre silme içerik geçerliğini zayıflatabilir.

5.  Madde sayısı, n, alfa, madde-toplam, madde silinirse alfa, ters kodlama ve kuramsal gerekçeler verilmelidir.

## Gerçek Veri ve Uyarlama Etkinliklerinin Açıklamalı Yanıtları

Yanıtlar `psych::bfi` verisinin ilk 100 satırındaki A ve C maddeleri içindir; veri kaynağı Bölüm 17’de açıklanmıştır. Bu bölüm Türkçe ölçek geçerleme çalışması değil, gerçek yanıtlarla güvenirlik ve uyarlama kararları öğretimidir.

## D: Kaynak, Yön ve Eksikler

1.  `kaynak_satir` 1–100 konumunu, `kaynak_kayit` yayımlanan CSV’nin özgün satır etiketini korur. İlk etiket 61617, son etiket 61831’dir; bunlar yeni öğrenci numarası veya gerçek kimlik olarak yorumlanmaz. İlk 100 kayıt rastgele seçilmiş değildir ve Türkiye’yi temsil etmez. A ve C farklı madde kümeleridir; on madde tek yapı diye toplanmaz.

2.  Altı seçenekli ölçekte ters değer $7-x$’tir: A1=6 için 1; C5=1 için 6. A2/satır66 eksiktir; 0 geçerli yanıt değildir. Bu kişinin anahtarlanmış A yanıtları $(5,\mathrm{NA},4,6,4)$’tür. Eksik atlanarak hesaplanan 19, beş maddelik tam toplamla karşılaştırılamaz.

3.  A2/satır66 nedeniyle A’da 99; C1/satır63 ve C3/satır90 nedeniyle C’de 98 tam kayıt kalır. On maddenin ortak tam kayıt sayısı 97’dir. A2 silinirken 100 kayda çıkmak, madde etkisiyle örneklem değişimini karıştırır; beş madde için seçilmiş aynı 99 kişiyle karşılaştırılır. C için de aynı 98 kişi korunur.

## G: Rehberli Hesaplar ve Kararlar

1.  A için $k=5$, $\sum s_j^2=9.130076$ ve $s_T^2=18.395176$ olduğundan $$\alpha=\frac{5}{4}\left(1-\frac{9.130076}{18.395176}\right)=.629588.$$ Ortalama $r=.272051$ ile $\alpha_{std}=5(.272051)/(1+4(.272051))=.651399$. Ham ve standart alfa farklı puan ölçeklemesine aittir. A1 çevrilmediğinde ham alfa .437554’tür. Artış, belgelenmiş ters yönün düzeltilmesinin sonucudur; kültürel eşdeğerlik veya tek boyutluluk kanıtı değildir.

2.  A1’in kendisini içeren toplamla korelasyonu .513648, diğer dört madde toplamıyla korelasyonu .198701’dir. İlki maddeyi iki tarafta da kullandığı için örtüşme içerir; düzeltilmiş korelasyon okunmalıdır. A4 silinirse alfa .675706 ve artış $.675706-.629588=.046118$ olur. Bu fark için anlamlılık testi yapılmamıştır. İçerik daralması, çeviri ve örneklem kararlılığı incelenmeden silme kararı verilmez. A1 silinirse .670624 elde edilmesi de aynı gerekçeyle otomatik silme kuralı değildir.

3.  Aynı kişinin maddeleri arasındaki ortak değişim korunmalıdır; bu yüzden tüm yanıt satırı iadeli seçilir. Hücreleri bağımsız çekmek ölçeğin kovaryansını bozar. 20000 tekrarlı percentile aralık \[.464423,.736637\], bu veri ve yeniden örnekleme varsayımları altındaki belirsizliği gösterir. Türkçe sürümün güvenirliğini, rastgele örneklemeyi veya eksiklerin zararsızlığını kanıtlamaz. İki ayrı ölçeğin aralıklarının örtüşmesi/örtüşmemesi tek başına güvenirlik farkı testi değildir.

## B: C Maddelerinde Bağımsız Çözüm

1.  C4 ve C5 $7-x$ ile çevrilir. $n=98$, ham alfa .722610, standart alfa .731783 ve ortalama $r=.353029$’dur. Ham toplam varyansı 21.934357, madde varyansları toplamı 9.254366’dır. Ters yönler düzeltilmeden alfa $-.082651$ çıkar: ortak yön varsayımıyla puanlanmamış maddeler negatif ortalama kovaryans verebilir. Negatif değer sıfıra kırpılmaz ve “negatif gerçek güvenirlik” diye yorumlanmaz; anahtar, içerik ve veri kontrol edilir.

2.  Aynı 98 kişide sonuçlar şöyledir:

    <div class="center">

    | Madde | Madde–kalan $r$ | Silinirse ham alfa |
    |:------|----------------:|-------------------:|
    | C1    |         .545418 |            .653951 |
    | C2    |         .502439 |            .667962 |
    | C3    |         .512805 |            .664335 |
    | C4    |         .493804 |            .670744 |
    | C5    |         .387612 |            .723448 |

    </div>

    C5 silinince artış $.723448-.722610=.000838$’dir (yuvarlanmamış fark .000837). Bu çok küçük örneklem içi kazanç, içerik kaybını ve tekrar örneklemede kararsızlığı değerlendirmeden madde silmeye gerekçe değildir. Katsayılar için otomatik kabul/silme eşiği kullanılmaz.

3.  Örnek rapor: “Rdatasets psych/bfi aktarımının ilk 100 kaydından C1–C5’i tam olan 98 kişi incelendi. Belgelenmiş anahtarla C4 ve C5, $7-x$ biçiminde çevrildi; eksik yanıt doldurulmadı. Ham alfa .723, standart alfa .732 bulundu. Katılımcı satırlarının 20000 iadeli örneklemesiyle percentile %95 aralık \[.580,.811\] elde edildi (Python tohumu 202614). Bu sıralı alt küme temsili örneklem değildir. Sonuç, Türkçe uyarlama, tek boyutluluk veya bireysel kullanım uygunluğunun kanıtı değildir.”

## H1: Altı İddiayı Düzeltme

1.  Alfa .70’i geçmek bir dil uyarlama işlemi değildir. Dilsel anlam, hedef grupta anlaşılabilirlik, yapı ve eşdeğerlik kanıtları gerekir.

2.  Negatif korelasyon otomatik çevirme emri değildir. Anahtar özgün madde anlamına dayanır; kodlama hatası, farklı yapı ve örneklem oynaklığı da araştırılır.

3.  A1’in düzeltilmemiş .514 korelasyonu kendi toplamına katılmasından etkilenir; düzeltilmiş değer .199’dur. Tek katsayıyla madde kalitesi onaylanmaz.

4.  A’nın beş sütunu aynen iki kez yazılınca alfa .835372 olur; bağımsız yeni bilgi eklenmez. Bu, tekrarın katsayıyı yanıltabileceğini gösterir. Ayrıca yalnız ilk maddeyi 10 ile çarpmak ham alfayı .145256’ya indirirken korelasyonları ve standart alfayı değiştirmez. Puan ağırlıkları açıklanmalıdır.

5.  Bootstrap mevcut örneklemi yeniden kullanır; seçilmeyen kişilerin bilgilerini veya kültürel temsili üretmez.

6.  Omega yükler, hata varyansları ve belirlenmiş ölçüm modeline bağlıdır. Uygun modelin incelenmesi atlanamaz; bu veriye uygunluğu sınanmış bir omega modeli kurulmamıştır. Revizyon 20 yalnız bilinen parametreli modellerde sayısal karşı örnek ekler; bunlar IPIP omega kestirimi değildir. A+C’nin 97 kişideki .727369 alfası da tek boyutlu toplamın geçerli olduğunu göstermez.

## P1: Uyarlama Dosyası İçin Örnek İskelet

A4 için “Çocukları severim” taslağı özgün çocuklara yönelik içeriği korur. “İnsanlara karşı hoşgörülüyüm” ise hedefi ve tutumu değiştirir; aynı madde diye benimsenmemelidir. İkisi de bu etkinlikte yalnız taslaktır, onaylanmış Türkçe madde değildir.

- Bilişsel soru 1: Bu ifadeyi kendi sözlerinizle nasıl anlatırsınız; “çocuklar” sözcüğü kimleri çağrıştırıyor?

- Bilişsel soru 2: Yanıt verirken hangi deneyiminizi düşündünüz; çocuklarla temasınızın az olması yanıtınızı nasıl etkiledi?

- Bilişsel soru 3: Altı yanıt kategorisi arasından seçiminizi nasıl yaptınız; size uygun bir seçenek eksik miydi?

Revizyon günlüğünde madde kodu, sürüm/tarih, taslak, gözlenen anlaşılma sorunu, kanıt kaydı, önerilen değişiklik, gerekçe, karar verenler ve yeniden sınama durumu için alanlar açılır. Görüşme yapılmadıysa kanıt alanı “planlandı; henüz veri yok” olarak bırakılır.

<div class="center">

| Kanıt alanı        | Bu etkinlikte durum ve sonraki iş                                                         |
|:-------------------|:------------------------------------------------------------------------------------------|
| Kaynak ve haklar   | Kaynak/anahtar ve IPIP açıklaması incelendi; başka testlere otomatik izin çıkarılmaz.     |
| Dilsel taslak      | Öğretim taslakları hazır; uzman uzlaşması ve bilişsel görüşme yapılmadı.                  |
| Hedef grupta pilot | Yapılmadı; örneklem ve uygulama protokolü planlanır.                                      |
| Yapı ve güvenirlik | Yabancı kaynak alt kümesinde alfa hesaplandı; Türkçe veriyle yapı/güvenirlik çalışılmadı. |
| Değişmezlik        | Yapılmadı; karşılaştırılacak gruplar ve yeterli veri gerekir.                             |
| Kullanım           | Bireysel tanı ve karar için kullanıma uygunluk gösterilmedi.                              |

</div>

Değerlendirme: kaynak/puanlama 20, hesap ve eksikler 25, belirsizlik ve madde kararı 20, uyarlama planı 25, yeniden üretim 10 puan. Yapılmamış araştırmayı yapılmış gibi yazmak kanıt üretmez; açık sınırlandırma beklenir. Hangi sonucun hangi yazılımla üretildiği belirtilir.

## T1–T3: Model ve Belirsizlik Denetimi

1.  Ortak 97 tam kayıt örneklem kuralını sabitler. $\alpha_A=.627614$, $\alpha_C=.722686$, fark .095072’dir. Ortak satır çekimi A–C bağımlılığını korur; 20000 tekrarın persentil aralığı $[-.062180,.268615]$’tir. Sıfırı içermesi eşitlik/eşdeğerlik veya eşit geçerlik kanıtı değildir. Farklı yapılar ve seçilmiş tam kayıtlar için alfa fonksiyonelleri karşılaştırılır; seçilim/eksiklik yanlılığı giderilmez.

2.  Alfa .733471’den .750000’a yükselir; hedef faktör payı .743802’den .720000’a düşer. Artık kovaryansı .2 iki simetrik hücrede olduğundan toplam hata varyansı $3.1+2(.2)=3.5$ olur. Hedef faktör varyansı $(.8+.7+.6+.5+.4)^2=9$ değişmez. Yeni pay $9/(9+3.5)=.72$’dir. Bu bir bilinen-model karşı örneğidir; veriye uydurulmuş omega değildir.

3.  SEM $\sqrt{3.1}=1.760682$, bağımsız ve eşit normal hata senaryosunda yaklaşık fark sınırı $1.96\sqrt{6.2}=4.880$ puandır. İlişkili zaman hatalarında kovaryans terimi gerekir. Tek uygulamalı iç tutarlılık verisi bu varsayımları veya klinik anlamlı değişimi doğrulamaz. Puan ölçeği, koşullu hata, değişmezlik ve amaç ayrıca incelenir; grup ortalaması veya alfa katsayısı standart hatasıyla SEM karıştırılmaz.
