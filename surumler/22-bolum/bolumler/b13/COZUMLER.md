# Bölüm 13 — açıklamalı çözümler

Revizyon 16; yeni T1–T3 dahil.

## Kendinizi Sınayın

Katsayı artık “diğer yordayıcılar sabitken” kısmi bir etkidir. Yordayıcılar birbiriyle ilişkiliyse, ilk yordayıcının ortak varyansla açıkladığı kısım yeni yordayıcıyla paylaşılır; katsayı büyüklüğü ve yorumu değişir (hatta işaret değiştirebilir).

## Kolay Düzey

1.  Bağımlı değişken açıklanan sonuç; bağımsız değişkenler sonucu yordayan değişkenlerdir.

2.  Bağımlı değişkendeki varyansın modelce açıklanan oranını gösterir.

3.  Farklı ölçekteki yordayıcıların göreli katkısını karşılaştırmak için kullanılır.

4.  Diğer yordayıcılar sabitken, bir birim artış için odds çarpanıdır. 1’den büyük değer artış, küçük değer azalış yönündedir; olasılık çarpanı değildir.

5.  Katsayıların standart hatalarını büyütür ve tekil yordayıcı yorumunu belirsizleştirir.

## Orta Düzey

1.  Yordayıcılar birlikte anlamlı açıklama sağlıyor olabilir; tekil katkılar örtüşme veya düşük güç nedeniyle anlamsız çıkabilir.

2.  Kuramsal olarak gereksiz değişken çıkarma, bileşik puan kullanma veya modeli yeniden belirtme düşünülebilir.

3.  Dengesiz sınıflarda yüksek doğruluk yanıltıcı olabilir; duyarlılık, özgüllük ve ROC bilgisi de gerekir.

4.  Doğrusallık, sabit varyans, aykırı değer ve model biçimi hakkında tanısal bilgi verir.

5.  Katsayı diğer değişkenler sabitken koşullu ilişkiyi özetler; büyüklüğü ve anlamlılığı değişebilir. Bu tek başına nedensel etki değildir.

## İleri Düzey

1.  Zaman sırası, karıştırıcı kontrolü, uygun tasarım ve kuramsal gerekçe olmadan katsayı nedensel etki değildir.

2.  Eşik düşerse duyarlılık artıp özgüllük azalabilir; eşik yükselirse tersi beklenir.

3.  Etkili gözlem katsayıları ve uyumu değiştirebilir; dâhil/hariç duyarlılık analizi yapılmalıdır.

4.  Hiyerarşik regresyon bloklar hâlinde kuramsal ek katkıyı test eder; standart model tüm yordayıcıları birlikte değerlendirir.

5.  Bölümdeki gerçek veri örneği: “Yaş aynı tutulduğunda G1’in bir puanlık artışı için $G3\ge14$ olayının odds oranı 5.219’dur (yaklaşık %95 Wald GA $[2.049,13.296]$).” Pratik önem başlangıç olasılığına, karar bağlamına ve belirsizliğe bağlıdır; yalnız OR büyüklüğünden evrensel bir önem sınıfı çıkarılamaz.

## Bölüm 13: Gerçek Veri Etkinliklerinin Gerekçeli Yanıtları

Bu yanıtlar Bölüm 13’teki ilk 60 UCI kaydıyla model kurma ve sonraki 20 kayda sabit modeli uygulama etkinliklerine aittir. Lojistik olay $G3\ge14$ olarak tanımlanır; 14 resmî geçme sınırı değildir.

## D1–D3: Model Kurmadan Önce Düşünün

1.  Doğrusal model puanların koşullu ortalamasını, lojistik model belirlenmiş not hedefine ulaşma olasılığını modeller. G3=0 ve G3=13 ikili tanımda sıfır sınıfına girer; aralarındaki 13 puanlık fark kaybolur. Bu nedenle ikili analiz sürekli yanıt analizinin daha iyi bir sürümü olarak sunulamaz.

2.  Sabit terimli modelde bütün kayıtlar GP iken okul göstergesi yeni bilgi sağlamaz; sabitle tam doğrusal bağlantı oluşturur. Yaşı merkezlemek referansı 16 yaşa taşır, ancak sabit terimli doğrusal/logit modellerinde aynı model uzayını ve tahminleri korur. Bilgi eklemez, yaşı etkisizleştirmez.

3.  G2 ikinci dönem notudur; birinci dönem sonunda kullanılabilir değildir. Eğitimdeki iyileşme, kullanılacak zamandaki bilgi koşulunu ihlal ederek elde edilmiş olabilir. İki grup da kaynak sırasıyla ayrılmış GP kayıtlarıdır; iki bağımsız okul örneklemi değildir. Gerçek kullanım öncesinde yordayıcıların erişim zamanı ve yeni veri performansı ayrıca doğrulanmalıdır.

## G1–G3: Rehberli Uygulama

1.  16 yaşta merkezlenmiş yaş sıfırdır. Yuvarlanmamış katsayılarla $$\widehat{G3}=5.295723+0.639696(12)=12.9721,$$ $$\hat\eta=-22.191778+1.652342(12)=-2.3637,
    \qquad \hat\pi=\frac{1}{1+e^{2.3637}}=0.0860.$$ İlk sayı puan ölçeğinde tahmin edilen ortalama, ikinci sayı 14 veya üzeri not olayının model olasılığıdır. 12.97’nin 14’ten küçük olması olay olasılığının sıfır olduğunu göstermez; ortalama ve eşik aşımı farklı özetlerdir.

2.  Düzeltilmiş $R^2=1-(1-0.581404)(59/57)=0.566716$ bulunur. Yaş için $t=0.505431/0.279742\approx1.8068$ ve $t^2=3.2644$ olup tek değişken eklenmesinin klasik $F(1,57)$ testiyle aynıdır. VIF=1.229 düşük doğrusal bağlantıya işaret eder; gözlem etkisini ölçmez. İlk kayıt çıkarıldığında yaş katsayısının 0.5054’ten 0.0683’e değişmesi ayrı bir kararlılık sorunudur.

3.  $OR=e^{1.652342}=5.2192$’dir. G1=12 ve 13 için $\hat\pi$ değerleri 0.0859847 ve 0.3293037 olduğundan fark 0.2433190, yani yaklaşık 24.33 yüzde puanıdır. Olasılık oranı ile odds oranı aynı değildir. Wald katsayı aralığının iki ucuna üstel dönüşüm uygulanır: $$[e^{0.717197},e^{2.587486}]=[2.0487,13.2963].$$ Bu aralık OR içindir; bireysel olasılığın güven aralığı değildir.

## B1–B3: Sabit Modelin Sonraki 20 Kayda Uygulanması

1.  Kaynak sırası 80: yaş=16, G1=12, G3=11. İlk 60 kaydın sabit doğrusal modeli $\widehat{G3}=12.9721$ verir; gözlenen eksi tahmin farkı $11-12.9721=-1.9721$ puandır. Lojistik olasılık 0.0860’tır. G3=11 olduğundan gerçek olay 0, $c=0.50$ ile tahmin de 0’dır; bu kayıt doğru negatiftir. Bu tek doğru sınıflandırma modelin genel başarısını kanıtlamaz.

2.  Gerçek olaylardan 3’ü doğru pozitif, 2’si yanlış negatiftir; olay olmayanlardan 14’ü doğru negatif, 1’i yanlış pozitiftir. Duyarlılık $3/5=0.60$, özgüllük $14/15=0.9333$, doğruluk $17/20=0.85$ olur. Herkese 0 diyen kural $15/20=0.75$ doğruluk ve sıfır duyarlılık üretir. Toplamda yalnız beş olay bulunduğu için bir kaydın sonucu duyarlılığı 0.20 değiştirir; kararlı bir kullanım başarısı iddia edilmemelidir.

3.  Eğitim AUC/Brier değerleri 0.9371/0.0897, aktarım değerleri 0.7600/0.1319’dur. Eğitim dışında daha düşük sıralama başarısı ve daha yüksek ortalama olasılık hatası görülür. Örnek sınırlılık paragrafı: “Modelin kaynak sırasıyla ayrılmış sonraki 20 kayıttaki performansı, eğitim performansından düşüktür. Her iki grup GP okulundandır ve aktarım grubunda yalnız beş olay vardır. Bu sonuçlar bağımsız dış doğrulama veya başka okullara genelleme kanıtı değildir. Hedef not ve olasılık eşikleri bu grubun sonuçlarına göre değiştirilirse grup model geliştirmede kullanılmış olur; artık dokunulmamış bir test kümesi sayılamaz. Eşik seçimi kullanım amacı ve hata maliyetleriyle, performans değerlendirmesi ayrı verilerle planlanmalıdır.”

## H1: Hatalı Raporun Düzeltilmesi

1.  **VIF bütün varsayımları sınamaz.** VIF doğrusal yordayıcı bağlantısını inceler. Koşullu ortalama biçimi, bağımsızlık, gözlem etkisi ve çıkarım koşulları ayrıca değerlendirilmelidir.

2.  **$R^2$ artışı nedensellik değildir.** Aynı gözlemler üzerindeki iç içe OLS modellerinde yordayıcı eklenince eğitim $R^2$’si zaten azalmaz. Yaşın klasik ek katkı testi $p=.0761$’dir; gözlemsel tasarım ve ilk kaydın etkisi varken nedensel etki iddiası yapılamaz.

3.  **OR olasılık oranı değildir.** 5.219, diğer yordayıcı aynı tutulduğunda odds çarpanıdır. Olasılık farkı başlangıç profiline göre değişir; G1=12’den 13’e geçişte yaklaşık 24.33 yüzde puanıdır.

4.  **Eğitim doğruluğu kullanım onayı değildir.** 0.8833 aynı verideki eğitim doğruluğudur; sınıf dengesi ve eşik seçimine bağlıdır. Sonraki 20 kayıt da yeni okul örneklemi değildir. Yeni kullanım bağlamı için bağımsız değerlendirme ve kalibrasyon incelemesi gerekir.

5.  **İki farklı eşik vardır.** 14, öğretim amacıyla tanımlanan hedef not; 0.50, tahmin edilen olasılığı sınıfa çeviren karar eşiğidir. Hiçbiri burada resmî geçme kuralı veya bütün uygulamalar için zorunlu karar olarak sunulamaz.

## T1–T3: Olasılık ve Kalibrasyon Denetimi

1.  $p_0=.085985$, $p_1=.329304$, fark .243319 (24.33 yüzde puan), koşullu OR 5.219’dur; olasılık çarpanı değildir. Tam katsayı kovaryansıyla delta SH .114630, yaklaşık aralık \[.01865,.46799\] çıkar. Tahminler bağımsız değildir; ayrı varyans toplamı ortak kovaryansı atlar. Bu, model profil farkıdır; nedensel etki veya gelecekteki 0/1 yanıt aralığı değildir. Profil olasılığı GA’ları logit ölçeğinden ters dönüşür.

2.  Pozitif c sıralamayı ve logit işaretini korur; AUC .760, .50 doğruluğu .850 kalır. Olasılık uzaklıkları değiştiğinden Brier/log-kayıp değişir. Örneğin c=2’de ortalama .26486 olay oranı .25’e yakınken log-kayıp .82157 olur; yalnız toplu ortalama tam kalibrasyon değildir. Tablo yeni model uyumu veya kullanım önerisi değildir.

3.  Kontrol etiketleriyle c/olay/olasılık eşiği seçilirse aynı veri seçime de kullanılır; artık el değmemiş kontrol sayılmaz. Beş olayla esnek eğri/alt grup çıkarımı güçlü değildir. Profil güven aralığı model parametrelerinin belirsizliğidir; AUC/Brier kalibrasyon belirsizliği veya dış okul geçerliği değildir. Yeni ekte performans aralıkları ve dış doğrulama yoktur.

## P1: Analiz Denetiminin Kontrol Noktaları

Doğrusal G1 katsayısı 0.6396963, klasik standart hatası 0.0740429, HC3 standart hatası 0.2270434’tür. HC3 $t_{57}$ aralığı $[0.1850,1.0943]$’tür. Yaş için karşılık gelen HC3 aralığı $[-0.5375,1.5484]$ olur. Kaynak sırası 1’in kaldıracı 0.4534916 ve Cook uzaklığı 6.4827020’tır. Bu kayıt çıkarıldığında doğrusal G1/yaş katsayıları 0.8594205/0.0683148 olur. Lojistik G1/yaş katsayıları ise gösterilen basamaklarda 1.6523417/$-0.3199655$ olarak kalır. Duyarlılık model ve yanıt tanımına bağlıdır; otomatik silme gerekçesi değildir.

G3 doğrusal modelde yanıt, `hedef14` lojistik modelde yanıttır. `hedef14`’ü G3 yordayıcısı yapmak gelecekteki yanıtı modele taşır; ayrıca lojistik yanıttan yine kendisini yordamak ayrışmaya yol açabilir. Tam puan için kaynak ve bilgi zamanı (20), katsayı/OR/aralıklar (25), gözlem etkisi–VIF–HC3 ayrımı (20), sabit-model aktarımı (20), kod ve ölçülü rapor (15) birlikte değerlendirilir.
