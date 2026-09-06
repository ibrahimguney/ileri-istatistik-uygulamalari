# Bölüm 10 — Çözüm rehberi

Bu değerler yerel arşivin yeniden analizidir; özgün makalenin sonuç tablosu değildir.
Tam hassasiyet beklenen.json içindedir. Yuvarlanmış değerlerle karar vermeyin.

## D1–D3
1. Her ID aynı kişinin iki ölçümünü bağlar; 20 ölçüm 10 tam çift oluşturur. extra
   kontrole göre artış olduğundan negatif ve sıfır mümkündür; eksik sayılmaz.
2. İlk soru 10 kişinin koşul 1 artışını 0 saate karşı, ikincisi 10 kişinin koşul
   2−1 farkını 0'a karşı sınar. Üçüncüsü doz 1'deki 10 OJ ve 10 VC hayvanın
   uzunluk farkıdır (kaynak birimi). Bağımsız grupları sıraya göre eşlemek yapaydır.
3. Testlerin büyük p'si varsayımı kanıtlamaz. Eşleşme ve bağımsızlık tasarımla
   belirlenir. Uyku uygulama sırası/taşıma etkisi ve hayvanların kafes/randomizasyon
   ayrıntıları kısa kaynak kopyasından doğrulanmaz.

## G1: Tek örneklem
n=10; ortalama=.75 saat, s=1.789010, SH=.565735. t=(.75−0)/SH=1.325710,
df=9, p=.217598; %95 fark GA=[−.529780,2.029780] saat; d=.419226.
H0 reddedilemez; sıfır etki kanıtı veya eşdeğerlik sonucu değildir.

## G2: Eşli
ID sırasıyla farklar: 1.2, 2.4, 1.3, 1.3, 0, 1, 1.8, .8, 4.6, 1.4 saat.
Ortalama=1.58, s=1.229995, SH=.388959, t=4.062128, df=9, p=.002833;
%95 GA=[.700114,2.459886] saat, dz=1.284558. Aynı 10 farkın tek örneklem testi
aynı t, p ve aralığı verir. s_D²=s_1²+s_2²−2cov=1.512889.
Bu, normal fark/bağımsız kişi modeli altındaki sonuçtur; normallik sorunu yokmuş
gibi raporlanmaz. Farkların Shapiro p≈.0333 sonucu ve Q–Q grafiğinin üst kuyruğu
model sınırlılığıdır; tanı sonucuna bakıp otomatik kişi silinmez.

## G3: Welch ve Student
Doz 1'de OJ−VC=5.93, t=4.032770, Welch df=15.357672, p=.001038;
%95 GA=[2.802148,9.057852], d_pooled=1.803509. Her grupta 10 kayıt olduğu için
Student ve Welch SH/t değerleri aynıdır; df seçimi farklı p ve aralık üretir.
Eşit n, eşit varyansın kanıtı değildir. Ortalama merkezli Levene p≈.14913;
medyan merkezli Brown–Forsythe p≈.21232. Welch ana yöntem olarak korunur.
d_pooled yalnız standartlaştırıcıdır; Welch'i Student'a dönüştürmez.

## G4: Dönüşümler
Saatten dakikaya geçiş fark, s, SH ve aralık uçlarını 60 ile çarpar;
t, p ve dz değişmez. Ortalama fark 94.8 dakika olur. Yön terslenirse ortalama,
t ve dz işaret değiştirir; iki yönlü p korunur; aralık [−üst,−alt] olur.

## B1: Doz 2
OJ−VC=−.08, p=.963852, %95 GA=[−3.798070,3.638070]. Aralık her iki yöndeki
farkları içerir. H0'ın reddedilememesi eşdeğerlik değildir; bağlamsal tolerans ve
uygun test gerekir. Bu başka dozda yeni grup karşılaştırmasıdır, dış doğrulama
veya doz etkisinin resmi etkileşim testi değildir. Ayrı doz p'leri çoklu test
ailesi için düzeltilmemiştir.

## B2: Yanlış bağımsızlık
Uyku koşulları bağımsızmış gibi hesaplanırsa p≈.079394 çıkar. Bu karşı örnek,
aynı kişiye ait iki ölçümün kovaryansını atar. Yöntem aranan p'ye göre değil
tasarıma göre belirlenir; yanlış yöntemin büyük p vermesi onu temkinli/doğru yapmaz.

## B3: Duyarlılık
Çift çıkarma sonuçlarında ortalama fark 1.24444–1.75556 saat aralığındadır.
ID=9 çıkarıldığında fark=1.24444, p≈.000477, %95 GA=[.73731,1.75158].
Hem fark hem belirsizlik değişir; daha küçük p daha büyük etki demek değildir.
Bu kayıt ana analizde korunur. Duyarlılık bütün 10 çıkarımı gösterir, en iyi
sonucu seçmez; veri hatası olduğu iddiasında bulunmaz.

## H1
1. n ölçüm sayısı değil bağımsız birim/tam çift sayısıyla belirlenir.
2. Levene reddedilemiyorsa varyans eşitliği kanıtlanmış olmaz.
3. Anlamsızlık eşdeğerlik değildir.
4. Eşli t küçük örneklemde normal fark modeline dayanır; tanı sorunu açıklanır.
5. Sonradan en küçük p'yi seçmek planı/hata oranını değiştirir; tüm dozlar raporlanır.
6. Bu aralık ortalama fark içindir; bireysel yarar, tahmin aralığı veya tedavi önerisi değildir.

## P1: Örnek rapor iskeleti
“R datasets kaynaklarından yerel CSV'ye aktarılmış tarihsel kayıtlar kullanıldı.
Uyku verisi ID ile eşlendi; 10 tam çiftte koşul 2−1 farkı 1.58 saatti.
Normal fark modeli altında t(9)=4.062, iki yönlü p=.0028, %95 GA [.700,2.460]
bulundu. Küçük örneklemde Shapiro ve Q–Q incelemesi normallik kaygısı verdi;
ana kayıtlardan silme yapılmadı ve tüm tek-çift duyarlılıkları raporlandı.
ToothGrowth doz 1'de 10 OJ ve 10 VC kayıt için Welch farkı 5.93 (kaynak birimi),
%95 GA [2.802,9.058] bulundu. Bu öğretim karşılaştırmaları çoklu doz için ortak
çıkarım, özgün tasarım doğrulaması veya tedavi önerisi olarak sunulmadı.”

Rapora G1 sonucu, yöntem gerekçeleri, kaynak/lisans notları, kod sürümleri ve
iki grafik eklenmelidir. Python'ın çalışması R/SPSS sonuçlarının doğrulandığı
anlamına gelmez. Rubrik GOREVLER.md içindedir.