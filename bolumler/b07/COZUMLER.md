# Bölüm 7 — Çözüm rehberi

Önce GOREVLER.md görevlerini tamamlayın; yuvarlanmamış hedefler beklenen.json içindedir.

## OLS ve klasik belirsizlik

Sxx=385.4, Sxy=224.3; eğim=Sxy/Sxx=.581992735,
sabit=12.783333333−.581992735×12.1=5.741221242.
SSE=103.642362913, SST=234.183333333; R²=.557430662.
Bu R² aynı 60 kaydın Pearson r²'sidir; başarı olasılığı değildir.

Artık standart sapması sqrt(SSE/58)=1.336763738;
eğitim RMSE=sqrt(SSE/60)=1.314295521. Klasik eğim SH=.068092425,
t(58)=8.547100, p≈7.46694e−12, %95 GA=[.445690937,.718294532].
Eğim, notlar arasındaki model-temelli ilişkiyi gösterir; bir kişiye
müdahale edildiğinde kesin .582 puan artış olacağını kanıtlamaz.

## G1=12: İki farklı aralık

Nokta tahmini=12.725134060. Klasik ortalama %95 güven aralığı
[12.379417955,13.070850164], yeni birey %95 tahmin aralığı
[10.027069900,15.423198219]. Bireysel aralık ek hata değişkenliği nedeniyle
daha geniştir; koşullu ortalama aralığını tek öğrenci için kullanmayın.
Grafikteki bant klasik ortalama güven bandıdır. Bu aralıkların model
koşulları veri seçimi ve artık incelemesinden bağımsız varsayılamaz.

## Etki, HC3 ve çapraz doğrulama

İlk kaydın kaldıracı=.396557689, Cook uzaklığı=8.426851703.
Kaynak 1 çıkarılınca eğim=.855596961 olur. Yüksek etki kaydın hatalı
olduğunu kanıtlamaz. 60 birini-dışarıda-bırakma eğimi
[.543534284,.855596961] aralığındadır; bu bir güven aralığı değildir.
En küçük eğim kaynak 19, en büyük kaynak 1 çıkarılınca oluşur.

HC3 eğim SH=.280588385; t(58) referanslı %95 aralık
[.020334059,1.143651411], p=.042510676. Klasik SH ile fark saklanmaz.
OLS nokta tahmini aynıdır; yalnız kovaryans hesabı değişir. HC3 seçilim,
kümelenme, yanlış model veya nedensellik sorunlarını çözmez ve klasik
bireysel tahmin aralığını kendiliğinden sağlamlaştırmaz.

LOOCV RMSE=1.620229877; her döngüde kalan 59 kayıtla model yeniden kurulur.
Dışarıda bırakılan kayıt hatası e_i/(1-h_ii) özdeşliğiyle eşleşir.
Eğitim RMSE'sinden yüksek olması bu örnekte eğitimdeki uyumun ayrılmış
kayıt tahminiyle aynı olmadığını gösterir; yeni okul/yıl başarısını garanti etmez.

## Son 20 kayıt ve kullanım sınırı

Son 20 kayıtta yeniden kurulan modelde sabit=4.111675127,
eğim=.652284264, R²=.393514216. Bu, ana modelin dondurulup test edildiği
bir dış doğrulama sonucu değildir. Her iki alt küme aynı okulun sıralı alıntısıdır.
Ana G1 aralığı 0–17 olduğundan G1=20 ekstrapolasyondur.
G1 henüz bilinmiyorsa yıl başında kullanılamaz. Küçük p varsayım kanıtı,
R² başarı oranı, kaynak atfı temsili örnekleme veya nedensellik kanıtı değildir.