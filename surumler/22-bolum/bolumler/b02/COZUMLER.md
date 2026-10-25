# Bölüm 2 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

Okul kodları kategorileri adlandıran nominal etiketlerdir; sayıların büyüklüğü ve aralarındaki fark anlam taşımaz. Kodların ortalaması, kodlama değiştirildiğinde değişen keyfî bir sayıdır. Nominal değişken için frekans, yüzde ve mod raporlanır.

## Kolay Düzey

1.  Toplam 40, n=5 olduğundan ortalama 8; sıralı dizinin ortadaki değeri de 8’dir.

2.  $IQR=Q_3-Q_1$, dağılımın orta bölgesindeki yayılımı özetler. Çeyrek yöntemi belirtilir; ayrık veride aralık içinde tam yüzde 50 kayıt bulunması zorunlu değildir.

3.  Pozitif ve sıfırdan yeterince uzak ortalamalı, anlamlı sıfıra sahip oran ölçeklerinde göreli yayılım karşılaştırılabilir. Farklı birim tek başına gerekçe değildir; keyfî sıfırlı not/Celsius ölçekleri ve sıfıra yakın ortalamalar için mekanik oran yanıltıcıdır.

4.  Sağa çarpıklık veya yüksek değerlerin ortalamayı çekmesi düşünülebilir; kesin tanı değildir. Çok modluluk, bağlar ve dağılımın bütünü grafikle incelenmelidir.

5.  Güçlü pozitif doğrusal ilişkiyi özetler; nedensellik kanıtı değildir. Doğrusal olmayan yapı, uç kayıtlar ve kullanılan n ayrıca değerlendirilir.

## Orta Düzey

1.  Toplam 70 ve ortalama 14’tür. Kareli sapmalar $16+4+0+0+36=56$; örneklem varyansı $56/4=14$, standart sapma $\sqrt{14}=3.741657$ olur. Bölen 5 alınırsa başka tanımla varyans 11.2 elde edilir.

2.  Ortalama $69/5=13.8$, medyan 8’dir. 40 büyük değer olarak ortalamayı yukarı çeker; kaynağı incelenmeden hatalı sayılmaz veya otomatik silinmez.

3.  Uygun oran ölçekleri varsayılırsa $CV_A=100(8/80)=\%10$, $CV_B=100(5/20)=\%25$; B göreli olarak daha değişkendir. Bu varsayım olmadan oranları anlamlı karşılaştırma diye sunmayın.

4.  $IQR=34-18=16$. Alt sınır $18-1.5(16)=-6$, üst sınır $34+1.5(16)=58$ olur. Bunlar tarama sınırlarıdır; ham gözlemler olmadan kutu grafiğinin bıyık uçları söylenemez.

5.  Pozitif kovaryans aynı yönlü doğrusal birlikte değişimi; $r=.20$ zayıf pozitif doğrusal ilişkiyi gösterir. Kovaryans büyüklüğü birimlere bağlıdır; bu iki sayı nedensellik veya anlamlılık sınaması değildir.

## İleri Düzey

1.  Ortalama $25/5=5$, medyan 4; kareli sapmalar $9+1+1+1+16=28$’dir. Örneklem varyansı 7, s=$\sqrt7=2.645751$ ve mekanik CV $100\sqrt7/5=\%52.9150$ olur. Göreli yayılım yorumu için değişkenin uygun oran ölçeğinde olduğu ayrıca varsayılır.

2.  Medyan ve IQR tipik konumu/yayılımı uç yüksek gelirlerden daha az etkilenerek özetler; özellikle vurgulanır. Ortalama ve s de amaca göre birlikte verilebilir. Uç gelirler gerçek olabilir; yalnız istatistiksel uzaklık silme gerekçesi değildir.

3.  $\bar x=2.5$, $\bar y=5$. Kareli sapmalar toplamları 5 ve 26, çarpım sapmaları toplamı 11’dir. Örneklem kovaryansı $11/3=3.666667$; $s_x=\sqrt{5/3}$, $s_y=\sqrt{26/3}$ olur. Sonuç $$r=\frac{11/3}{\sqrt{5/3}\sqrt{26/3}}=\frac{11}{\sqrt{130}}=.964764$$ olarak bulunur; yaklaşık .965’tir.

4.  Aynı s, ortalamaya göre farklı oran oluşturabilir; ancak küçük ortalama sıfıra yakınsa oran kararsızlaşır. Değişken oran ölçeğinde değilse CV karşılaştırması anlamlı değildir. Ortalamaya sabit ekleyerek CV’yi değiştirebilmek bu sorunu gösterir.

5.  Ortalama ve s çarpık veride de tanımlı ve yararlı olabilir; fakat biçimi, çok modluluğu, uç kayıtları ve çeyrekleri tek başına göstermez. Grafik ve dayanıklı özetler eklenmelidir. Normal dağılıma özgü kapsama yorumları yalnız bu iki sayıdan çıkarılmaz.

## D1–D3: Özetten Önce

1.  Kaynak G1=0’ı not olarak kaydetmiştir; eksik kod tanımı yoktur. Ana 80 kayıt korunur. İlk satırın dışlanması yalnız ayrı duyarlılık dosyasıdır; sonucun değişmesi hatalı kayıt kanıtı değildir.

2.  Hayır. $n-1$ hesap tanımını belirler; ilk 80 kaydın kaynak sırasıyla seçilmiş olmasını, GP kapsamını veya bağımlılık sorunlarını ortadan kaldırmaz.

3.  Aynı kayıtlar, filtre/ağırlık, eksik tanımı, sıralama, çeyrek algoritması ve kutu/bıyık tanımı karşılaştırılır. NumPy linear/R tip 7, yarı-medyan ve SPSS HAVERAGE otomatik eşit kabul edilmez. Yazılımın çalıştırılıp çalıştırılmadığı belirtilir.

## G1–G4: Rehberli Çözüm

1.  G3 toplamı 1011, n=80; ortalama 12.6375’tir. $SS=324.4875$ olduğundan $s^2=324.4875/79=4.107437$, s=2.026681 bulunur. Kapalı 80 kayıt için n bölenli varyans $324.4875/80=4.056094$’tür. İlk ölçünün birimi puan kare, standart sapmanın birimi puandır.

2.  $h=1+79(.75)=60.25$. G1’in sıralı 60/61 değerleri 13/14 olduğundan $Q_3=13+.25(14-13)=13.25$ olur. $Q_1=11$, IQR=2.25, sınırlar 7.625 ve 16.625’tir. Sınır içinde gözlenen en küçük/en büyük notlar 8 ve 16 olduğundan bıyıklar bunlara uzanır. Kaynak satırları 1, 16, 48, 61 işaretlenir; silinmez.

3.  İlk 60 ortalaması 12.783333, son 20 ortalaması 12.2’dir. Kişi sayılı ağırlıklarla birleşim $(60\bar x_1+20\bar x_2)/80=12.6375$ olur. Eşit iki ağırlık 12.491667 verir; iki blokta kişi sayısı farklıdır. Bunlar okul/müdahale grupları veya temsil düzeltici ağırlıklar değildir.

4.  Çarpım sapmaları toplamı 273.075; kovaryans $273.075/79=3.456646$ olur. $s_{G1}=2.427558$ ve $s_{G3}=2.026681$ ile $r=.702586$ elde edilir. Fark varyansı $$s_D^2=5.893038+4.107437-2(3.456646)\approx3.087184$$ ve s=1.757038’dir. Yuvarlama öncesi değerlerle özdeşlik tam sağlanır. Ortalama fark .4625, medyan fark 0; 32 artış, 31 eşitlik, 17 azalış vardır. Hesap aynı eşleşmiş 80 kayda dayanır; anlamlılık testi yapılmaz.

## B1–B3: Bağımsız Çözüm

1.  İki 40’lık yarının medyanları 11 ve 13.5’tir. IQR=2.5, alt/üst sınırlar 7.25/17.25 olur; yalnız ilk sıfır not işaretlenir. 17 notları değişmediği hâlde yöntem değişince etiket değişmiştir. Ana rapor tip 7’yi korur; yöntem sonucu beğenmek için seçilmez.

2.  G3’e 10 eklenince ortalama 22.6375, s yine 2.026681, mekanik CV yüzde 8.9528 olur. G3’ü 5 ile çarpınca ortalama 63.1875, s=10.133406, mekanik CV yine yüzde 16.0370’dır. Pozitif çarpma birimi değiştirir; sabit ekleme başlangıcı değiştirir. Bu oranlar göreli yetenek ölçüsü değildir; dönüştürülmüş değerler özgün notlar olarak sunulmaz.

3.  79-kayıt duyarlılığında G1 ortalaması 12.329114, s=2.011005 ve G1–G3 korelasyonu .793762’dir. Ana 80-kayıt değerleri 12.1750, 2.427558 ve .702586 idi. Değişim ilk kaydın etkisini gösterir, veri hatası kanıtlamaz. Kaynak kaydı ana analizde kalır; dışlama yalnız açıkça belirtilmiş duyarlılıktır.

## H1: Hatalı Raporu Onarma

1.  Ortalama–medyan sıralaması çarpıklık için ipucudur, kesin tanı değildir. Histogram, bağlar ve olası çok modluluk incelenir.

2.  Kutu işaretleri kaynak incelemesi başlatır; hata ya da otomatik silme kuralı değildir. G1=0 dâhil ana 80 kayıt korunur.

3.  Bıyıklar sınırların içindeki en uç gözlemlerdir. G1 tip 7 sınırları 7.625/16.625 iken bıyıklar 8/16’dır.

4.  Varyans böleni örnekleme tasarımını değiştirmez; ilk 80 GP kaydının daha geniş hedefi temsil ettiği gösterilmemiştir.

5.  Not CV’si göreli yetenek ölçüsü değildir. Sabit 10 eklenmesi s’yi değiştirmeden oranı değiştirir; anlamlı sıfır koşulu eksiktir.

6.  Ortalama fark .4625 olsa da 17 öğrencinin notu düşmüş, 31’inin aynı kalmıştır. Yalnız 32 kayıtta artış vardır; betimsel değişim nedensel etki değildir.

## P1: Denetlenebilir Betimsel Rapor

Rapor 80 GP kaydının kaynağını, ilk-sıra seçimini, not ölçeğini ve eksik bulunmadığını belirtir. G1/G3 ortalama, örneklem s, medyan ve tip 7 çeyrekleri birlikte verilir. Histogramlar ortak puan ekseni ve bir puanlık sınıflarla; kutular açık çeyrek/bıyık tanımıyla sunulur. Aynı değerdeki noktalar üst üste gelebileceği için taranan kayıt listesi ayrıca tutulur.

İlk satırın dışlanması ana sonuç değil duyarlılıktır. Dönem farkı ve 32/31/17 yön sayıları raporlanabilir; bunlar test veya nedensellik iddiasına çevrilmez. Ortak kayıt kümesi, varyans böleni, yazılım/sürüm ve komut saklanır. Hangi sonucun hangi yazılımla üretildiği belirtilir. Rubrik: kapsam/ölçüm 20, hesap/tanımlar 30, grafik/uç kayıt 20, yorum 20, yeniden üretim 10 puan.


## Revizyon 6: özet seçimi

## T1–T3: Özet Seçimi ve Dağılım Denetimi

1.  Üç sayı farklı tanımlı konum hedefleridir. Aritmetik toplam veya kayıt başına aritmetik düzey için ortalama; ortadaki konum için medyan; önceden tanımlı uç duyarlılığını azaltan hedef için kırpılmış ortalama kullanılır. Her kuyrukta $\lfloor .20(80)\rfloor=16$, toplam 32 değer hesap dışında kalır; 48 değerle ortalama hesaplanır. Ana dosya 80 kaydı korur. Kaydın hatalı olduğuna veya bilimsel olarak dışlanması gerektiğine hükmedilmez. Farklı hedefler raporlanırken oran ve amaç açık yazılır.

2.  $1-\widehat F(15)=9/80=.1125$ yalnız 15’ten büyükleri verir. En az 15 için $1-\widehat F(15^-)=15/80=.1875$ gerekir. Eşiğe eşit 6 kaydın payı $6/80=.075$, yani 7.50 yüzde puanıdır. G1 ters ampirik çeyreği sıralı 60. değer 13’ü, tip 7 ise $h=60.25$ ile 60/61. değerler arasında $13+.25(14-13)=13.25$’i kullanır. Algoritmalar farklıdır; ana tip 7 tanımı değiştirilmez.

3.  Ayrı medyanlar 2 ve 100, farkları 98’dir. Eşleşmiş farklar 1, 98, 1 ve medyanları 1’dir. Gerçek notlarda her iki sonucun 0 olması genel bir eşitlik kanıtlamaz. Ortalamalar farkında doğrusallık vardır; medyanda böyle bir kural yoktur. Ortak ölçekli dağılım/ampirik dağılım ile eşleşmiş fark sayımları birlikte sunulabilir; az sayıda birimde eşleşmiş nokta/çizgi de kullanılabilir. Ortalama çubukları tek başına bireysel değişimleri göstermez. Kurgu gerçek not ölçeğiyle karıştırılmaz.
