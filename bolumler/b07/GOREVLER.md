# Bölüm 7 — Öğrenci görevleri

## D — Analizden önce

1. G1/G3 rollerini, birimlerini ve tahmin zamanını yazın. Neden çalışma saati
   veya nedensel müdahale örneği değil?
2. Ana 60, son 20 ve ham 80 kaydın amaçlarını ayırın. Son 20 dış doğrulama mı?
3. G1=0 olan ilk kaydı inceleyin. Kaynak kontrolü olmadan silinebilir mi?

## G — Rehberli hesap

1. Sxx ve Sxy üzerinden eğim/sabiti hesaplayın. SciPy ve statsmodels ile
   karşılaştırın. Aynı kayıtlarda R² ile Bölüm 6'nın Pearson r²'sini eşleştirin.
2. Artık, SSE, SST, R², artık standart sapması ve eğitim RMSE'sini bulun.
   Son iki değerin paydaları neden farklı?
3. Klasik eğim SH, t, p ve %95 aralığını hesaplayın. Küçük p varsayımları kanıtlar mı?
4. G1=12 için nokta tahmini, ortalama güven aralığı ve yeni birey tahmin
   aralığını bulun. Grafikteki bant hangi aralığı gösteriyor?

## B — Bağımsız uygulama

1. İlk kaydın kaldıraç/Cook değerlerini ve kaynak 1 çıkarılınca eğimi bulun.
   Kaldıraç, büyük artık ve etki aynı kavram mı?
2. Her seferinde bir kayıt dışlayan 60 modelde eğim aralığını bulun.
   Gerçek LOOCV hatalarını e_i/(1-h_ii) özdeşliğiyle karşılaştırın.
3. HC3 standart hatasını matris formülüyle hesaplayın, klasik SH ile kıyaslayın.
   HC3 nokta tahminini veya klasik bireysel tahmin aralığını değiştiriyor mu?
4. Son 20 kayıtta yeniden model kurun. Ana modelden farkı genellenebilirlik testi mi?
5. G1=20 için kullanım sınırını, eğitim/LOOCV RMSE farkını ve yeni okul
   performansına ilişkin hangi iddiaların kurulamayacağını açıklayın.

## H — Hatalı raporu onarın

“G1'i bir puan artırınca herkesin G3'ü .582 artar. R²=.557, öğrencilerin
%55.7'si başarılı demektir. Küçük p bütün varsayımları kanıtlar. G1=12 olan
tek öğrenci için 12.38–13.07 aralığını kullandık. HC3 bütün sorunları çözdü.
İlk kaydı çıkarıp daha iyi sonucu seçtik. Son 20 kaydı yeniden modelleyince
dış doğrulama yapmış olduk.” Her iddiayı ayrı düzeltin.

## P — Teslim

2–3 sayfalık rapor: kaynak/seçim, değişkenler, model ve katsayılar, iki aralık,
ham/artık grafikleri, HC3/klasik ayrımı, kayıt etkisi, eğitim/LOOCV farkı,
sınırlılıklar ve çalıştırma yönergeleri. Kod ve çıktı tablolarını ekleyin.
Rubrik: kaynak/tasarım 20, hesap/aralık 30, tanı/duyarlılık 25,
yorum/sınırlar 15, yeniden üretim 10 puan. Yapılmamış analizleri sonuç diye yazmayın.