# Bölüm 11 — açıklamalı çözümler

Revizyon 14; yeni T1–T3 dahil.

## Kendinizi Sınayın

Ortak bir nedenin (karıştırıcı) iki değişkeni birlikte etkilediği durumlarda, ters nedensellikte, seçilim (örneklemin bir değişkene göre seçilmesi) ve rastlantıda; ayrıca zaman sırası belirsizse. Korelasyon yalnız birlikte değişimi gösterir; nedensel çıkarım uygun tasarım, zaman sırası ve karıştırma/seçilim hakkında savunulabilir tanımlama varsayımları ister; yalnız güçlü kuram veya korelasyon yeterli değildir.

## Kolay Düzey

1.  Tam ters yönlü doğrusal ilişkiyi gösterir.

2.  Aynı kayıtlarda sabit terimli tek açıklayıcılı OLS modelinin açıkladığı yanıt değişkenliği oranıdır; nedensel açıklama değildir.

3.  Pozitif ve görece güçlü ilişki olarak yorumlanır.

4.  $0\le r^2\le1$ aralığındadır.

5.  Pearson doğrusal ve sürekli değişken ilişkisine duyarlıdır.

## Orta Düzey

1.  Pozitif, orta-güçlü ilişki vardır; çalışma süresi arttıkça puan artma eğilimindedir.

2.  Negatif ve düşük-orta ilişki vardır; $p<.05$ ilişki için istatistiksel kanıt sağlar.

3.  Pearson doğrusal olmayan örüntüyü yakalamayabilir; grafikle birlikte yorumlanır.

4.  $r^2=0.25$; aynı kayıtlar üzerindeki sabit terimli basit OLS modelinde yanıtın merkezlenmiş kareler toplamının yaklaşık %25’i açıklanır.

5.  Sıralı veri için genellikle Spearman daha uygundur.

## İleri Düzey

1.  Aykırı gözlem denetlenmeli ve duyarlılık analizi yapılmalıdır.

2.  Korelasyon nedensellik kanıtı değildir; üçüncü değişkenler olabilir.

3.  Stres arttıkça uyku kalitesi düşme eğilimindedir; ilişki anlamlı ve güçlüdür.

4.  Monoton fakat doğrusal olmayan yapı veya aykırı değerler fark yaratabilir.

5.  Doğrusal olmayan veya kümeli bağımlılıkta sıfır korelasyon bağımsızlık anlamına gelmeyebilir.

## Bölüm 11: Gerçek Veri Etkinliklerinin Gerekçeli Yanıtları

Bu yanıtlar Bölüm 11’deki UCI Portekizce dersi etkinliklerine aittir. İlk 60 kayıt ana analiz, 61–80. kayıtlar bağımsız çözüm içindir; hesaplar seçili yerel kayıtlara dayanır.

## D1–D3: Hesaplamadan Önce Düşünün

1.  Pozitif ilişki vardır; kaynak sırası 1 olan $(G1,G3)=(0,11)$ kaydı yatay eksende diğerlerinden ayrılır. Tek katsayı, notların kümelenmesini, aynı çiftin tekrarını, ilişki biçimini ve tekil kayıt etkisini göstermez. Büyük veya küçük katsayı tek başına veri kalitesi göstergesi değildir.

2.  Puanların doğrusal birlikte değişimi için Pearson, göreli sıralamanın monoton birlikte değişimi için Spearman seçilir. İkisini yan yana vermek puan uzaklıkları ile sıralamanın farklı yönlerini görünür kılar. Yüksek olanı seçip diğerini gizlemek uygun değildir.

3.  Sıfır notu ölçeğin içindedir; tek başına eksiklik veya hata kanıtı değildir. Kaynak veri sözlüğü, eksik kod tanımı ve mümkünse özgün kayıt incelenmelidir. Belgelenmiş hata olmadan ana analiz kaydı korur; dışarıda bırakma sonucu duyarlılık karşılaştırması olarak raporlanır.

## G1–G3: Rehberli Uygulama

1.  $G1=12$ için $(23+34)/2=28.5$, $G3=12$ için $(15+28)/2=21.5$ bulunur. Kaynak sırası 3 olan kaydın sıra çifti $(28.5,21.5)$’tir. Sıralar seçilen bütün veri kümesine göre tanımlandığından yalnızca ilk altı kaydı sıralamak farklı konumlar üretir; bu, 60 kaydın sıra hesabı değildir.

2.  Pozitif doğrusal ölçek dönüşümü Pearson’ı değiştirmez: kovaryans ve ilgili standart sapma aynı pozitif çarpanla değişir. Sıralama ve bağlar korunacağından Spearman da değişmez. Her iki durumda $r=.7466128$, $r_s=.8310857$ elde edilir. Bu özellik Pearson için genel olarak doğrusal olmayan dönüşümlere genişletilemez.

3.  Yuvarlanmamış değerlerle $b_1=r(s_y/s_x)=0.5819927$ ve $R^2=r^2=0.5574307$ bulunur. Bunlar Bölüm 12’nin aynı 60 kayıt üzerindeki sabit terimli basit OLS sonuçlarıdır. $r_s^2=0.6907034$, ham G3 notlarındaki açıklanan varyans değildir; sıraların doğrusal ilişkisine aittir. Korelasyon iki değişkenin yerleri değiştirildiğinde aynı kalır, regresyon eğimi ise hangi değişkenin yanıt seçildiğine ve ölçü birimine bağlıdır.

## B1–B3: Sonraki 20 Kayıt

1.  $r=51.4/\sqrt{78.8(85.2)}=0.6273071$ ve yeniden hesaplanan ortalama sıralarla $r_s=.5705355$ bulunur. İlk 60 kayıttakinin aksine burada Pearson sayısal olarak daha büyüktür; yöntemlerin değişmez bir üstünlük sırası yoktur.

2.  $n=20$ için Fisher dönüşümü ve $1/\sqrt{17}$ standart hatasıyla yaklaşık %95 GA $[0.2558,0.8374]$ elde edilir. İlk 60 kaydın $[0.6079,0.8411]$ aralığından daha geniştir. İki ayrı güven aralığının örtüşmesi, korelasyonların farkı için hesaplanmış bir güven aralığı veya test değildir. Gruplar kaynak sırasıyla ayrılmış ve aynı okuldan gelmiştir; uygun fark çıkarımı için örnekleme ve bağımsızlık koşulları ayrıca gerekçelendirilmelidir.

3.  Örnek rapor: “UCI Portekizce dersi verisinin 61–80. GP kayıtlarında birinci dönem ve yıl sonu notları pozitif ilişkilidir ($n=20$, Pearson $r=.627$, Spearman $r_s=.571$). Pearson için model-temelli yaklaşık %95 Fisher GA $[0.256,0.837]$’dir. Alt küme rastgele seçilmemiştir ve dış doğrulama grubu değildir. Gözlenen ilişki nedensellik göstermez; küçük, tek okul alt kümesinden daha geniş öğrenci kitlesine doğrudan genellenemez.”

## H1: Hatalı Raporun Düzeltilmesi

1.  **Normallik kapısı:** Betimsel Pearson katsayısı normallik testi anlamlı olsa da hesaplanabilir. Sorgulanması gereken, araştırma sorusuna uygunluğu ve klasik çıkarımın koşullarıdır.

2.  **Spearman’ın karesi:** $r_s^2$ ham notların açıklanan varyansı değildir. Aynı kayıtlar üzerindeki sabit terimli tek yordayıcılı OLS için Pearson $r^2=0.5574$ kullanılır.

3.  **Birim ve nedensellik:** $r=.747$ bir eğim değildir. İlgili OLS eğimi yaklaşık 0.582’dir; bu da notu idari olarak yükseltmenin nedensel etkisini göstermez.

4.  **Sıfır $p$:** Ekranda yuvarlanan değer $p=0$ diye yazılmamalıdır. Ana Pearson testi $p\approx7.47\times10^{-12}$ verir. İleri permütasyon etkinliğinde ise 19999 tekrarda sıfır uç sonuç, artı-bir düzeltmesiyle $p_{\mathrm{MC}}=0.00005$ üretir; kesinlik veya sıfır olasılık anlamına gelmez.

5.  **Silme ve genelleme:** İlk kaydı silince Pearson’ın artması hata kanıtı değildir. Ana analiz kaydı korur, duyarlılık sonucu ayrıca sunulur. Rastgele seçilmemiş GP kayıtları bütün öğrencilere doğrudan genellenmez.

## T1–T3: Birlikte Belirsizlik ve Uyum Denetimi

1.  Yeniden örnekleme birimi bütün $(G1,G3)$ öğrenci satırıdır. Ayrı sütun çekimi ilişkiyi bozar; aynı çekilişin iki katsayıda kullanılması tahminler arası bağımlılığı korur. Spearman sıraları her örneklemde ham notlardan, bağlara ortalama sıra verilerek yeniden oluşturulur. Bağımsız Pearson katsayıları için Fisher fark formülü, aynı 60 kişinin Pearson/Spearman karşılaştırması değildir. iid satırlar modeli okul/sınıf bağımsızlığı kanıtı olmaz.

2.  Fark .0845’tir; yaklaşık aralık sıfırı içerir. İki katsayı farklı ilişki özelliklerini hedefler; bu, Spearman’ın daha doğru olduğu veya aynı Pearson parametresinin karşılaştırıldığı anlamına gelmez. Sıfırı içerme eşdeğerlik değildir. İlk satırın olmadığı 7164 tekrar koşullu ampirik bootstrap örnekleridir; yeni gözlem veya dış doğrulama değildir. Kayıt silmeye gerekçe üretmez.

3.  $Y^\dagger=X+5$ aynı sıralı doğrusal örüntüyü korur, ama her fark 5 birimdir; uyum kabul sınırları olmadan değiştirilebilirlik söylenemez. $Y=X^2$ modelinde $E(X)=E(X^3)=0$ nedeniyle kovaryans sıfır, bağımlılık kesindir. İlk örnekte fark/kalibrasyon, ikincide eğrisel saçılım ve bağımsızlık sorusu gerekir. İkisi de yeni not kaydı değildir; bu kitapta uyum analizi veya genel bağımsızlık testi eklenmiş sayılmaz.

## P1: Duyarlılık Projesinin Kontrol Noktaları

60 ayrı dışarıda bırakma hesabında Pearson en küçük 0.7278461 (kaynak sırası 16 veya 48 çıkarıldığında), en büyük 0.8658335 (sıra 1 çıkarıldığında) olur. Spearman en küçük 0.8222556 (sıra 16 veya 48 çıkarıldığında), en büyük 0.8498310 (sıra 40 çıkarıldığında) olur. Her hesap kalan 59 gözlemle ve yeniden oluşturulan sıralarla yapılır. Katsayı aralıkları güven aralığı değildir; gözlem duyarlılığını betimler.

Tam puanlık rapor, bölümdeki rubriğe göre veri kaynağını ve seçimi (20), doğru grafik ve katsayıları (25), yeniden sıralanan 60 karşılaştırmayı (25), silme/genelleme ve çıkarım sınırlılıklarını (20), çalıştırılabilir kod ve sürümleri (10) içerir. Yalnızca beklenen katsayıları yazmak yeterli değildir.
