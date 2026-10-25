# Bölüm 3 — açıklamalı çözümler

22 bölümlük kitap sürümünün cevap anahtarından ilgili öğrenci çözümleridir.
Bulguların kapsamını ve yapılmamış analizleri koruyun.

## Kendinizi Sınayın

Belgelenmiş puanlama kuralına göre: kural “en az dört maddeye yanıt verenlerde yanıtlanan maddelerin ortalaması” ise payda 4’tür; toplam puan kullanılıyorsa eksik madde 0 sayılmaz. Kural önceden yazılır, eksik yanıt sayısı raporlanır ve beş maddelik ölçekte dört maddelik ortalamanın aynı ölçekte olduğu varsayımı açıkça belirtilir.

## Kolay Düzey

1.  Ad, açıklama, ölçüm düzeyi, geçerli değer/kodlar ve eksik değer tanımı temel alanlardır. Birim, ölçüm zamanı, kaynak, anahtar ve türetme kuralı da eklenmelidir. Sayısal saklama türü tek başına ölçüm düzeyi değildir.

2.  Eksik, beklenen yanıtın bulunmaması; geçersiz kod, sözlüğün izin vermediği değerdir. Geçersiz kodun gerçek değeri kaynaktan doğrulanmadan tahmin edilmez. Sonradan eksik olarak işaretlense bile neden ve eski değer günlüğe yazılır.

3.  Ters anahtarlı maddeleri aynı puan yönüne getirmek için yapılır. 1–5 için $6-x$, 1–6 için $7-x$ kullanılır; önce geçerli aralık ve kaynak anahtarı denetlenir. Ham madde korunur, dönüşüm yeni sütunda tutulur.

4.  Hayır. Uçluk doğal değişkenlik, özel bir alt grup veya hata olabilir. Kaynak ve içerik kontrol edilir; gerekçeli dışlama varsa ana sonuç ve duyarlılık ayrılır. Sırf sonucu değiştirmesi silme gerekçesi değildir.

5.  Genişte kişi tek satır, ölçümler ayrı sütunlardır; uzunda kişi–zaman veya kişi–madde ayrı satırdır. Tek bir kişinin çok satırda bulunması bağımsız kişi sayısını artırmaz. Uzun biçimin birleşik anahtarı tanımlanmalıdır.

## Orta Düzey

1.  Yüksek gelirdekiler daha fazla eksikse tam kayıtlar düşük gelirlileri fazla temsil edebilir; örneğin gelir ortalaması aşağı çekilebilir. Yanlılığın yönü ve büyüklüğü her hedef için aynı değildir. Gerçek gelir eksik olduğundan mekanizma iddiası ek bilgiyle gerekçelendirilir.

2.  Ölçeğin alt/üst sınırı ve iki ters maddenin anahtarı doğrulanır; yalnız bu maddeler yeni sütunlarda çevrilir. Eksik ve geçersiz kodlar önceden ayıklanır; ardından asgari madde eşiğiyle toplam/ortalama üretilir. Tersleme ikinci kez uygulanmaz.

3.  Önce 999’un anlamı sözlük veya veri kaynağından doğrulanır. Özel eksik kodsa analizde eksik tanımlanır; giriş hatasıysa doğrulanmış kaynağa göre düzeltilir. Bilinmeyen yaş uydurulmaz, 999 ortalamaya dâhil edilmez; işlem kaydedilir.

4.  Tek madde ordinaldir; kategori uzaklıkları garanti değildir. Çok maddeli toplam/ortalama daha çok değer alabilir fakat yaklaşık sürekli kullanımı içerik, yapı, puanlama ve analiz varsayımlarıyla gerekçelendirilir. Yüksek alfa veya çok madde tek başına aralık ölçeği kanıtı değildir.

5.  Kaynak/sürüm, başlangıç sayısı, eksik/geçersiz/tekrar kontrolleri, etkilenen kayıtlar, önceki/yeni değer, gerekçe, puanlama kuralı ve analize giren sayılar raporlanır. Ham dosya ile türetilmiş dosya ayrılır; gerçek eksik ve kurgusal sınama karıştırılmaz.

## İleri Düzey

1.  MCAR’da eksiklik yanıt değerlerinden bağımsızdır; rastgele teknik kayıp bir senaryodur. MAR’da kaydedilmiş yaş gibi gözlenen değişkenlere koşullandıktan sonra eksik yanıta ek bağımlılık kalmaz. MNAR’da aynı gözlenen özelliklerde daha yüksek gerçek gelirin yanıtsızlığı artırması gibi ek bağımlılık sürer. Örnekler varsayımsaldır; az eksik veya ısı haritası mekanizmayı kanıtlamaz. MAR ile MNAR yalnız gözlenen veriden genel olarak ayırt edilemez.

2.  Kaynak hatası doğrulanırsa düzeltme yapılabilir; gerçek uç gözlem sırf kutu dışında diye silinmez. Araştırmanın dâhil etme ölçütü, model ve ölçüm bağlamı değerlendirilir. Dışlama gerekçesi önceden tanımlanmalı; sonuca göre karar verme ve seçici raporlama önlenmelidir.

3.  Aynı tam k maddede toplam $k\bar x$’tir; yalnız ölçek birimi değişir. Eksik sayısı değişiyorsa gözlenen toplam daha az yanıtı da yansıtır, ortalama ise farklı içerik kümelerine dayanabilir. Asgari madde sayısı belirlenir; ortalamayı k ile çarpmak gözlenmiş tam toplam üretmez. Farklı alt boyutlar aynı yanıt aralığında diye otomatik karşılaştırılabilir değildir.

4.  Ham arşiv ve dosya özeti (SHA-256), sözlük ve anahtar, tür/aralık, eksik desenleri/payda, tekrar/mantıksal tutarlılık, tersleme/puan eşiği, dönüşüm geri-kontrolü, birleşme çokluğu, analiz kaydı ve karar günlüğü denetlenir. Kurgusal hatalı girdilerin yakalandığı sınanır; yazılım sürümü/komutu saklanır.

5.  Örneğin internet erişimi kısıtlı grubun daha fazla eksik yanıtı varsa tam kayıt seçimi bu grubu azaltabilir. Daha temiz görünen dosya hedefi daha iyi temsil ediyor demek değildir. Başlangıç ve analiz kapsamları karşılaştırılır; nedensellik ve genelleme sınırları yazılır.

## D1–D3: Temizlemeden Önce

1.  Not sözlüğü 0–20’ye izin verir; buradaki maddeler 1–6 kategorilidir. Sıfır için tek bir evrensel silme/eksik kuralı yoktur. Kural değişkenin kaynağı ve ölçüm tanımından gelir.

2.  Geniş arşivde bir satır bir katılımcı kaydıdır. Kaynak sırası izleme alanıdır; puan, özellik veya rastgele seçilme olasılığı değildir. Kaynak etiketi gerçek yaşam kimliği olarak yorumlanmaz.

3.  Ham arşiv kanıtı korur; puan dosyası türetme kuralını gösterir; analiz dosyası belirli model için kullanılabilen kayıtları seçer. Bir modelde eksik puan bulunması kaydı bütün arşivden silme gerekçesi değildir.

## G1–G4: Rehberli Çözüm

1.  $100\times10=1000$ madde hücresinde 3 eksik: $100(3/1000)=\%0.3$. Eksikler üç farklı kayıtta: $100(3/100)=\%3$. A için yalnız 66 eksik olduğundan 99; C için 63 ve 90 eksik olduğundan 98; ortak tam küme $100-3=97$ kayıttır. Yüzde 0.3 kayıt dışlama oranı değildir.

2.  A1 ham 2 iken ters değeri 5 olur. Anahtarlanmış dizi $5,\mathrm{NA},4,6,4$, gözlenen toplam 19’dur. 5/5 puanı eksik; 4/5 puanı $19/4=4.75$ olur. $19/5=3.8$ eksik yanıtı sıfır sayar. $5(4.75)=23.75$ gözlenmiş beşli toplam değil, ek varsayımla orantılanmış puandır.

3.  Uzun dosyada 1000 satır, 997 gözlenen yanıt ve 100 kaynak kaydı vardır. Kaynak sırası–madde anahtarı benzersiz olmalı; geri dönüşte sütun/satır eşleştirmesi, 997 değer ve 3 eksik konumu aynı kalmalıdır. Boşları düşürmek madde hücresi paydasını görünmez kılabilir.

4.  Gözlenen 99 değerin varyans paydası 98’dir. Gözlenen ortalama eklendiğinde ortalama ve kareli sapmalar toplamı değişmez, yeni n=100 olduğundan payda 99 olur: $$s^2_{\text{doldurulmuş}}=s^2_{\text{gözlenen}}\frac{98}{99}
    =1.515769944\frac{98}{99}=1.500459137.$$ Bu karşı örnek ana dosyaya yazılmaz. Ortalama değişmediği için yöntem zararsız sayılmaz; bilinmeyen yanıt ve atama belirsizliği ortadan kalkmış değildir.

## B1–B3: Bağımsız Çözüm

1.  Kaynak 63’te C anahtarlı yanıtları $\mathrm{NA},6,6,5,4$; 4/5 ortalaması $21/4=5.25$’tir. Kaynak 90’da $3,3,\mathrm{NA},4,4$; ortalama $14/4=3.5$’tir. Her ikisinde 5/5 puanı eksik kalır. 4/5 kuralı bilinmeyen C1/C3 değerlerini bulmuş olmaz.

2.  Tam boş satır ile yalnız bir yanıtı 6 olan satırda 4/5 puanı eksiktir. $6,4,5,3,\mathrm{NA}$ satırında $18/4=4.5$ bulunur; 5/5 puanı yine eksiktir. Varsayılan toplam tam boş satıra 0, eksikleri atlayan ortalama tek yanıta 6 verebilir. Geçerli madde sayısı ayrıca denetlenmelidir; bu satırlar gerçek kayıtlardan değildir.

3.  Kontrolsüz birleşme 1 anahtarını iki sağ kayıtla eşleştirip toplam üç satır üretir. Bire bir beklentisinde doğrulama hata vermelidir; çoğalan satırı yeni kişi saymak yanlıştır. Bu kurgusal kontrolün gerçek arşivde tekrar bulunduğuna dair kanıt değeri yoktur.

## H1: Hatalı Raporu Onarma

1.  Yüzde 0.3 hücre, yüzde 3 eksikli kayıt oranıdır; ikisi de MCAR kanıtı değildir. Gerçek eksiklerin nedenleri bilinmiyor.

2.  Boş yanıt bilinmeyendir; sıfır bu ölçeğin geçerli yanıtı bile değildir. Ana dosyada üç eksik korunur, madde ataması yapılmaz.

3.  İki tersleme $7-(7-x)=x$ ile ham yönü geri getirir. Doğru anahtar bir kez, yeni sütuna ve ham kaynaktan uygulanır.

4.  Tek yanıt beş maddelik içerik kapsamını taşımaz. Ana eşik 5/5, duyarlılık 4/5’tir; bu ikinci kural test kılavuzu önerisi diye sunulmaz.

5.  1000 kişi–madde satırı 100 kaynak kaydına aittir. Uzun biçim bağımsız n’yi artırmaz; boş satırlar korunur.

6.  z dönüşümü aynı 99 geçerli A puanında ortalamayı 0, s’yi 1 yapar; dağılımın biçimini normalleştirmez, geçerlik ve eksiklik mekanizması sağlamaz.

## P1: Denetlenebilir Hazırlama Protokolü

Protokol hedef birimi, kişi/zaman anahtarını, veri kaynağını ve sözlüğü tanımlar. Özel eksik kodlar yanıtsızlık nedenlerinden ayrılır; geçerli aralık, mantıksal kurallar ve tekrarlı anahtar çözümü önceden yazılır. Doğrulanamayan değerler için bekleme/inceleme kararı verilir; bilinmeyen yanıt uydurulmaz. Ham dosya değiştirilmez, sürümlenir; kişisel tanımlayıcılara erişim sınırlandırılır.

Puanlama anahtarı, tam ve asgari-madde kuralları, toplam/ortalama ayrımı ve kullanılacak ortak kayıt kümesi belirtilir. Geniş–uzun geri dönüşü, birleştirme çokluğu ve eşleşmeyen anahtarlar denetlenir. Kayıt/hücre/puan paydaları, önceki-yeni değer, gerekçe ve etkilenen kayıtlar günlüğe alınır. Aykırı görünen kaydın neden incelendiği ve duyarlılık planı yazılır; temizleme sonucun anlamlılığına göre değiştirilmez.

Bu arşiv için 100 kayıt korunur; A 5/5 n=99, C 5/5 n=98 ve ortak n=97 raporlanır. 4/5 puanlarının ortalamaları A=4.5655 ve C=4.1915’tir; küçük farklar mekanizma kanıtı değildir. Yapılmamış çoklu atama, FIML, mekanizma testi ve Türkçe uyarlama açıkça belirtilir. Python denetimleri R/SPSS’in çalıştığı anlamına gelmez. Rubrik: kaynak/sözlük 20, doğrulama 25, eksik/puanlama 30, dönüşüm/günlük 15, sınırlılıklar 10 puan.

## M1–M3: Çoklu Atama Uygulaması

1.  $T=.447825+(1+1/200)(.162112)=.610748$ ve $SH=\sqrt T=.781504$. Yalnız $\bar U$ kullanmak atamalar arası B bileşenini dışlar; bilinmeyen yanıtların ve atama parametrelerinin belirsizliği hesaba katılmaz.

2.  Her tamamlanmış dosyada yalnız 104 eksik yanıt 6 azalır; toplam değişim $-624$, ortalama değişimi $-624/240=-2.6$ olur. $49.467-2.6=46.867$. Delta gözlenen veriden belirlenmiş değildir; aralık bu sabit varsayıma koşulludur ve MAR/MNAR testi sayılmaz.

3.  50, veri üreten anakütlenin bilinen ortalamasıdır; 49.629 ise 240 kişilik tam simülasyon örnekleminin ortalamasıdır. MI yalnız gözlenen veriyi kullanır; gizlenmiş Y değerlerini bilmez. Kapsama oranı, aynı tasarım altında çok sayıda bağımsız veri/maske üretiminde aralıkların hedefi kapsama sıklığıyla değerlendirilir; tek başarılı koşu bunu göstermez.


## Revizyon 7: veri akışı ve bilgi sınırı

## T1–T3: Veri Akışı ve Bilgi Sınırı

1.  `inner`: 97 satır, A/C geçerli 97/97. A solda `left`: 99 satır, geçerli 99/97. `outer`: 100 satır, geçerli 99/98; iki yalnız A, bir yalnız C kaydı vardır. Ortak A ortalaması 4.554639, bütün 99 A puanının ortalaması 4.563636’dır. C’de eksiği olan iki A kaydı ortak kümeden çıkar; kayıt kümesi değiştiği için özet değişebilir. Bu, aktarım hatası veya eksiklik mekanizmasının kanıtı değildir. A’yı tek başına betimlemek için C tamlığı dayatılmaz; ortak analizin kendi kullanılabilirlik kuralı yazılır.

2.  Boş anahtar gözlem kimliğini belirlemez; bazı yazılımlarda boşların birbirine eşleşmesi hatalı bağlantı yaratabilir. Tekrar bire bir çokluğu bozar ve satırları çoğaltabilir. “01” kodundaki baştaki sıfır anlamlı olabilir; sayısal 1’e dönüşüm ancak kaynağa dayalı açık kuralla yapılır. Burada sorunlu anahtarlar ayrı kontrol kopyalarında denenir; gerçek BFI kaynağında hata bulunduğu iddia edilmez. Tür eşitliği ve benzersizlik de yanlış ama aynı biçimde kodlanmış kimlikleri tek başına doğrulayamaz.

3.  Eğitim ortalaması 1, doğru merkezlenmiş eğitim $(-1,1)$’dir. Eğitim+test ortalaması 51, bu ortalamayla eğitim $(-51,-49)$ olur. İkinci işlem test dağılımını eğitim temsilini kurmakta kullanmıştır. Sabit $7-x$ kuralı veri sözlüğünden bilinir; ortalama/s/atama parametreleri öğrenilir ve tahmin değerlendirmesinde eğitim katında kalır. Gelecekte bilinmeyen test sonucu kullanılamaz; buna karşılık çıkarım amaçlı MI’da gözlenen sonuç yardımcı olabilir. Kurgu BFI kişilik yanıtları değildir; tahmin başarımı hesaplanmamıştır.
