# SPSS uygulama planı — çalıştırılmadı

1. Ayrı çalışma oturumunda önce filtre, ağırlık ve split-file ayarlarını kontrol edin.
2. Python'un ürettiği `sonuclar/doz_uzunluk.csv` dosyasını sütun adlarıyla açın:
   kaynak_satir, len, supp, dose, oj, dose_c. oj=1 OJ, oj=0 VC'dir.
3. General Linear Model / Univariate altında len yanıt, oj faktör,
   dose_c kovaryat olarak ortak eğim ve oj×dose_c etkileşimli modelleri ayrı kurun.
   Kaynak satırını kovaryat yapmayın. Referans dose_c=0, yani 1 mg/gündür.
4. Altı hücre modeli için doz kategorik faktördür. Grup×doz etkileşim testi,
   ayrı doğrulara karşı iki sd'li biçim testiyle aynı değildir. İlgili iki modelin
   SSE ve hata sd'sini kaydedip F farkını ayrıca hesaplayın.
5. OJ−VC yönünü kontrol edin: I=1,J=0. Ters satırın işareti ters olur.
   Ortak modelin farkı tek ailedir. Diğer iki modelin üç doz karşılaştırmasında
   p_düzeltilmiş=min(3p,1); tekil %98.3333 aralıklar en az %95 aile kapsaması içindir.
   Her doz için ayrı düzeltme seçmek üç dozu ortak ailede birleştirmez.
6. Düzeltilmiş ortalamaların tekil %95 aralıklarını grup farkı aralıkları veya
   bireysel tahmin aralıklarıyla karıştırmayın. Aynı SPSS çağrısında alfa
   değiştirilirse ortalama aralıklarının düzeyi de değişebilir.
7. Levene'nin merkezleme yöntemini belirtin; burada altı hücre medyan merkezlidir.
   HC3, gözlem etkisi ve 60 dışlama için Python paketi referanstır.

Menü/çıktı adları sürümle değişebilir; kullanılan sürümü, model terimlerini,
referans dozunu, aileyi ve çıktı dosyasını kaydedin. Bu rehber bir `.sps`,
`.sav` veya çalıştırılmış SPSS analizi değildir. Sayılar eşleştirilmeden
“SPSS ile doğrulandı” yazmayın.