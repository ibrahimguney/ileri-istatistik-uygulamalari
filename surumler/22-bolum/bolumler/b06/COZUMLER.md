# Bölüm 6 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

İki ölçüm aynı kişiden geldiği için birbirleriyle ilişkilidir; bağımsız gruplar testi bu ilişkiyi yok sayar, kişiler arası farkları hataya katar ve standart hatayı yanlış hesaplar. Doğru analiz her kişinin fark puanına dayanan eşli t-testidir.

## Kolay Düzey

1.  Parametreler hakkında varsayımlı çıkarım yapan testtir.

2.  Aynı/eşleştirilmiş bireyler iki kez ölçüldüğünde kullanılır.

3.  Birleştirilmiş varyans kullanan Student testinde standart hatanın varsayımıdır. Welch testi eş anakütle varyanslarını gerektirmez; bağımsızlık yine gereklidir.

4.  Belirtilen model altında ortalama veya ortalama farkının belirsizliğini gösterir; bireylerin yüzde 95’ini kapsayan bir aralık değildir.

5.  Farkın büyüklüğünü ve pratik önemini gösterir.

## Orta Düzey

1.  Tek örneklem t-testi uygundur.

2.  Bağımsız örneklemler t-testi uygundur.

3.  Eşleştirilmiş örneklemler t-testi uygundur.

4.  $p<.05$ olduğundan ortalamalar arasında anlamlı fark vardır; etki büyüklüğü de incelenmelidir.

5.  Eş varyans modeline karşı kanıt vardır; Welch uygun bir seçenektir. Ancak Welch seçmek için önce Levene’nin anlamlı çıkması gerekmez ve anlamsız Levene eş varyansı kanıtlamaz.

## İleri Düzey

1.  İstatistiksel olarak anlamlı fark pratikte çok küçük olabilir; sonuç abartılmamalıdır.

2.  Fark puanları yaklaşık normalse test savunulabilir.

3.  Rastgele atama yoksa başlangıç farkları nedensel yorumu sınırlar. Ayrıca iki sınıftaki öğrencilerin sınıf içi bağımlılığı değerlendirilmelidir; yalnız iki sınıfı çok sayıda bağımsız öğrenci gibi ele almak sözde tekrar oluşturabilir.

4.  Aralık sıfırı içerdiği için iki yönlü testte anlamlı değildir.

5.  Test türü, sd, istatistik, $p$, ortalama/SS, GA, etki büyüklüğü ve varsayımlar verilmelidir.

## Bölüm 6: Gerçek Veri Etkinliklerinin Açıklamalı Yanıtları

Bu çözümler Bölüm 6’daki `sleep` ve `ToothGrowth` uygulamalarına aittir. Bütün $p$ değerleri iki yönlüdür; güven aralıkları ham ortalama/fark içindir. Kaynak aktarımı ve otomatik doğrulama sınırları uygulama paketinde ayrıca belirtilmiştir.

## D1–D3: Tasarım ve Analiz Birimi

1.  20 satır, aynı 10 kişinin iki koşuldaki ölçümleridir; `group` bağımsız hasta grubunu değil ilaç koşulunu belirtir. ID bilgisini atmak kişi içi kovaryansı yok sayar. Negatif `extra`, kontrol koşuluna göre daha az uyku demektir; negatif mutlak uyku süresi değildir.

2.  `extra` zaten kontrole göre artış olarak tanımlandığı için sıfır artış doğal referanstır. Sıfır, ayrı bir kontrol örnekleminden bu analizde tahmin edilen ortalama değildir. Analiz 10 kişinin artış puanlarının ortalamasına ilişkindir; bu tanım, eski deneyin bütün uygulama koşullarını doğruladığımız anlamına gelmez.

3.  OJ ve VC farklı hayvanlardan oluşur; iki grubun ilk satırlarının eşleştiğine ilişkin çift kimliği yoktur. Aynı dozda bulunmaları eşli tasarım yapmaz. Ana test yalnız 1 mg/gün için karşılaştırmadır. Hayvanların kafes/ortak çevre yapısı ve atama düzeni ayrıca incelenmelidir; farklı satırlar bağımsızlığı tek başına kanıtlamaz.

## G1–G3: Rehberli Hesaplar

1.  İlaç 1 toplamı 7.5, ortalaması 0.75 saattir. Örneklem varyansı 3.20056, SS=1.78901, SH=0.56573 bulunur. $t(9)=1.32571$, $p=.21760$, %95 GA $[-0.52978,2.02978]$ saattir. Uygun yorum: “Sıfır ortalama artış hipotezi reddedilemedi; aralık hem azalma hem artışla uyumlu olduğundan sıfır etki kanıtlanmış değildir.” $d_{\rm tek}=0.41923$ tek başına pratik önem kararı verdirmez.

2.  Farklar sırasıyla $1.2,2.4,1.3,1.3,0,1.0,1.8,0.8,4.6,1.4$; toplam 15.8 ve ortalama 1.58’dir. Kovaryans 2.84833 olduğundan: $$3.20056+4.00900-2(2.84833)=1.51289=s_D^2.$$ $s_D=1.23000$, $d_z=1.28456$ ve $d_z\sqrt{10}=4.06213=t$ elde edilir. Dakikaya geçince fark 94.8, aralık $[42.00685,147.59315]$ olur; SS ve SH de 60 ile çarpılır. $t$, $p$ ve $d_z$ değişmez. Fark yönü ters çevrilirse $t$ ve $d_z$ işaret değiştirir, aralık uçları yer değiştirerek negatiflenir; iki yönlü $p$ aynı kalır.

3.  Doz 1’de OJ/VC örneklem standart sapmaları 3.91095/2.51531; ortak SH=1.47045’tir. Welch formülüne yerleştirme $sd=15.35767$, Student modeli $sd=18$ verir. Eşit grup büyüklüğü $n$ için iki varyans formülü de $(s_1^2+s_2^2)/n$’ye indirgenir; bu yüzden t=4.03277 aynıdır. Ancak referans t dağılımının serbestlik derecesi farklı olduğundan $p_W=0.001038$, $p_P=0.000781$ ve güven aralıkları farklıdır. Bu örnek, anakütle varyanslarının eşitliğini göstermez.

## B1–B3: 2 mg/gün Dozunda Yeni Karşılaştırma

1.  Doz 2’de OJ: $n=10$, ort.=26.06, SS=2.65506; VC: $n=10$, ort.=26.14, SS=4.79773. OJ$-$VC farkı $-0.08$, SH=1.73400, $t=-0.04614$, $sd=14.03982$, $p=.96385$ ve %95 GA $[-3.79807,3.63807]$ bulunur. Negatif yön korunmalıdır; fark mutlak değere çevrilmez.

2.  Birleştirilmiş SS=3.87734, $d_{\rm pooled}=-0.02063$’tür. Nokta tahmini sıfıra yakın olsa da aralık yaklaşık 3.80 birim VC lehine ve 3.64 birim OJ lehine farklarla uyumludur. Önceden belirlenmiş anlamlı fark sınırı ve uygun eşdeğerlik analizi olmadan “kesin eşdeğer” denmez. $p=.96385$, sıfır hipotezinin doğru olma olasılığı değildir.

3.  Örnek rapor: “ToothGrowth verisinin 2 mg/gün dozunda ayrı OJ ve VC grupları Welch testiyle karşılaştırılmıştır. OJ$-$VC farkı $-0.08$ kaynak ölçüm birimidir (%95 GA $[-3.80,3.64]$), $t(14.04)=-0.046$, $p=.964$; birleştirilmiş SS ile $d=-0.021$ bulunmuştur. Sıfır fark hipotezi reddedilememiştir; geniş aralık eşdeğerliği kanıtlamaz. Sonuçlar bu doz ve tarihsel hayvan örneklemiyle sınırlıdır.” Dozlar arasında farkın değişimini sınamak, iki ayrı $p$’yi kıyaslamak yerine uygulama–doz etkileşimini ortak modelde incelemeyi gerektirir.

## H1: Altı İddianın Düzeltilmesi

1.  Uyku örneğinde 20 bağımsız kişi değil, 10 kişi ve 20 ölçüm vardır.

2.  Eşli test kişi kimliğiyle belirlenen tasarım nedeniyle seçilir; en küçük $p$’yi verdiği için değil. Yanlış bağımsız analiz aynı 1.58 farkına rağmen SH=0.84909 ve $p=.07939$ verir.

3.  Anlamsız Levene eşitliği kanıtlamaz. Ana Welch seçimi ön testin anlamlılığına bağlanmaz; küçük örneklemde varyans testinin gücü de sınırlıdır.

4.  Büyük $p$, eşdeğerlik kanıtı değildir. Doz 2 aralığı sıfırın iki yanında geniş bir değer kümesini içerir.

5.  Ortalama farkının güven aralığı bireysel farkların yüzde 95’ini içerme iddiası değildir. Ortalama parametresinin belirsizliği ile bireysel değişkenlik ayrılmalıdır.

6.  Daha küçük $p$ kayıt silme gerekçesi değildir. ID 9’u çıkarınca ortalama fark küçülürken SS daha fazla küçülebilir; ana 10 çiftlik analiz korunmalı, bütün tek-çift duyarlılıkları birlikte raporlanmalıdır.

## P1: Yeniden Üretim Kontrol Noktaları

Kaynaklar uyku için 20 satır/10 ID; diş için 60 satır/6 hücre içerir. Her uyku ID’si iki kez, her doz–uygulama hücresi 10 kez bulunur. ID ile eşleme satır sırasından bağımsızdır. Doz filtreleri 20 ayrı hayvan seçer; eksik kayıt silinmemiştir.

Tek çifti dışarıda bırakmada ortalama farkın en küçüğü ID 9 dışarıdayken 1.24444; en büyüğü ID 5 dışarıdayken 1.75556 saattir. ID 9 için aralık $[0.73731,1.75158]$, ID 5 için $[0.86070,2.65041]$ olur. Bütün 10 duyarlılık aralığı sıfırın üzerindedir; ancak bu, farkların normal dağıldığını veya nedensel etkinin tanımlandığını kanıtlamaz. Ana fark dağılımında Shapiro $p=.03334$ ve üst Q–Q noktasındaki sapma özellikle belirtilmelidir.

Tam puan için kaynak/ID denetimi (20), üç test ve yön (25), aralık/etki büyüklüğü paydası (20), tanılar/bütün çiftler için duyarlılık (20), çalıştırma/ölçülü rapor (15) beklenir. Raporda hangi sonucun hangi yazılımla üretildiği belirtilmelidir.


## Revizyon 10: kalibrasyon ve hedef duyarlılığı

## T1–T3: Varsayım, Kalibrasyon ve Hedef Denetimi

1.  Gerçek varyans $9/10+1/30=.933333$; pooled standart hata karesinin beklentisi $[(9\cdot9+29\cdot1)/38](1/10+1/30)=.385965$’tir. Oran .413534 ve belirsizlik küçümsenir. Sıfır ortalama fark doğru olduğundan .210145 güç değil, yanlış red olasılığının simülasyon tahminidir. Büyük varyans büyük gruba geçince gerçek varyans .400000, beklenti .947368 ve oran 2.368421 olur; Student red oranı .004045 ile tutucudur. Senaryolar normal ve bağımsız model kurgusudur; gerçek ToothGrowth sonuçları veya evrensel hata oranları değildir.

2.  Her grupta n=10 korunur; her kuyruktan iki değer konum hesabı dışında kalır, altı değer katkı verir. Ana dosyadan hayvan silinmez. Welch sıradan ortalama farkını, Yuen yüzde 20 kırpılmış anakütle ortalamaları farkını hedefler. Yuen varyans için winsorize dizi kullanır; bu dizi ham veri diye saklanmaz. p=.001038/.003369 sonuçlarından küçük olanı seçmek analiz planı değildir; ana hedef ve duyarlılık gerekçesi ayrı yazılır. Yuen yaklaşımı bağımsızlık ve küçük örneklem sorunlarını otomatik çözmez.

3.  p\>.05 normalliği kanıtlamaz; küçük örneklemde tanının duyarlılığı düşük olabilir. p\<.05 ise sapmanın belirli hedef ve kestirici üzerindeki önemini tek başına ölçmez. Student’ın eş varyans varsayımı, Welch’in yayılım uyarlaması ve sıra testinin farklı hedefi tasarımla birlikte değerlendirilir. Eşli t’de kişi içi farklar ve çiftler arası bağımsızlık önemlidir; iki koşul sütununu ayrı ayrı test ederek eşleşme modeli doğrulanmaz. Q–Q, uç kayıt, seçilme/bağımlılık ve uygun duyarlılık birlikte raporlanır.
