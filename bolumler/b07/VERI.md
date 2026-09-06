# Bölüm 7 — Kaynak ve analiz sözleşmesi

Cortez, P. (2008). Student Performance [Veri seti]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T. Veri lisansı: CC BY 4.0.
Özgün araştırma: Cortez, P., & Silva, A. (2008). Using data mining to predict
secondary school student performance. FUBUTEC 2008, 5–12. EUROSIS.

- Kaynak: https://archive.ics.uci.edu/dataset/320/student+performance
- CSV: https://archive.ics.uci.edu/static/public/320/data.csv
- Lisans: https://creativecommons.org/licenses/by/4.0/

Kitap kaynak notlarına göre Portekizce dersi tam dosyası 649 kayıt içerir.
Yerel alıntı, ilk 80 satırın school/G1/G3 alanlarının tarayıcıdan aktarılmasıyla
oluşturulmuştur; kaynak_satir eklenmiştir. Burada bu yerel arşiv aynı baytlarla
`veri.csv` olarak sunulur. Tam kaynakla otomatik çevrimiçi karşılaştırma
bu hazırlıkta yapılmamıştır. Sonuçlar özgün makalenin bulguları değil,
kitap için yerel alıntıda yeniden yapılan hesaplardır.

Kod ve açıklamalara yeni lisans atanmadı; verinin lisansı bütün depoya
genişletilmez. Kitabın tam metni bu öğrenci paketinde dağıtılmaz.

## Seçim ve birimler

İlk 60 kayıt ana OLS, 61–80 ayrı model kurma etkinliğidir. Aynı ana 60 kayıt
Bölüm 6 korelasyon örneğinde de kullanılır; yeniden kullanmak bağımsız
kanıt oluşturmaz. Bütün 80 kayıt GP okulundandır. Bu, rastgele/temsili örneklem
veya yeni okul doğrulaması değildir. Kaynak sırası öğrenci kimliği değildir.
G1 birinci dönem, G3 üçüncü dönemdeki yıl sonu notudur; ikisi de 0–20 ölçeğinde.
[Sözlük](veri_sozlugu.csv) ve ham CSV birlikte tutulmalıdır.

Eksik değer yoktur; sıfır notlar korunur. İlk kayıt G1=0, G3=11'dir.
Yüksek etki, kaydı hatalı saymaya veya otomatik silmeye yetmez. Ham 80 kayıt
silinmez, yuvarlanmaz veya doldurulmaz. Ana G1 aralığı 0–17'dir; G1=20
kaynak ölçeğinde geçerli olsa da bu model için gözlenen aralığın dışındadır.

Normalize LF SHA-256:
`51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9`.
CRLF→LF ve sondaki tek satır sonu yalnız hash hesabında kullanılır; ham
CSV'ye yazılmaz. Hash doğrulaması uzak kaynak veya temsiliyet kanıtı değildir.

## Hesap sözleşmesi

Sabit terimli G3 ~ G1 OLS kurulur. Katsayı, klasik standart hata ve aralıklar
aynı 60 kayda dayanır. G1=12 için ortalama güven aralığı ve yeni birey tahmin
aralığı ayrı hesaplanır. HC3 sandviç kovaryansı ve t(58) referanslı eğim
aralığı klasik sonuçlardan ayrı verilir. LOOCV'de her kayıt için model kalan
59 kayıtla yeniden kurulur. Son 20 kayıtta yeni OLS kurmak ana modelin dış
validasyonunu yapmak değildir.

Yordama zamanı birinci dönem sonudur; yıl başında henüz bilinmeyen G1
kullanılamaz. Bu gözlemsel ilişki müdahale etkisi değildir. Klasik aralıkların
model koşulları kanıtlanmış değildir; HC3, seçilim/kümelenme/model biçimi
sorunlarını düzeltmez ve sağlam bireysel aralık üretmez. Yeni okul ve yıllara
aktarılabilirlik veya Türkiye için norm sonucu bu paketle gösterilmez.