# Bölüm 16 — AMOS kurulumu ve çıktı kontrolü

Bu bir kurulum rehberidir, çalıştırılmış AMOS oturumunun raporu değildir.
R/lavaan ve AMOS bu ortamda çalıştırılmadı. Sayısal tablolar Python hesabıdır.

1. Python betiğinin ürettiği `sonuclar/standartlastirilmis.csv` dosyasını SPSS'te açın.
   Yalnız A1–A5, C1–C5 model göstergeleridir. Kaynak sıra/etiketlerini modele
   koymayın. 97 tam kayıt olmalı; ham arşivde 63/66/90 analiz dışıdır.
2. Dosyadaki yanıtlar zaten anahtarlanıp örneklem s'siyle standartlaştırılmıştır.
   A1, C4 ve C5'i tekrar terslemeyin. SPSS'ten ayrı bir SAV çalışma dosyası
   kaydedin; bu kitapta SAV dosyası hazırlanmış gibi gösterilmez.
3. A ve C için iki elips, maddeler için on dikdörtgen çizin. A yalnız A1–A5'e,
   C yalnız C1–C5'e yüklensin. Her madde için ayrı hata terimi ekleyin.
4. A→A1 ve C→C1 yüklerini 1'e sabitleyin. Diğer sekiz yük ve on hata varyansı
   serbest; hata kovaryansları ve çapraz yükler yoktur. Bu, gizil varyansları
   1'e sabitleyen Bölüm 15 parametreleştirmesi değildir.
5. A→C yolunu çizin. C için ayrıca zeta_C yapısal artığını ekleyin; artıktan
   C'ye yük 1, artık varyansı serbest olsun. A varyansı da serbesttir.
   A ile zeta_C arasındaki kovaryans sıfırdır. A~~C kovaryansını bunun üzerine
   serbest eklemeyin. İçsel C'nin toplam varyansını hata varyansı diye okumayın.
6. Normal-kuram ML, ortalama/intercept modeli olmadan çalışın. Python referansı
   ddof=1 S ve (n-1)F Wishart hesabıdır. AMOS'un matris böleni ve olabilirlik
   tanımı doğrulanmadan son basamak eşitliği iddia etmeyin.
7. Standardized estimates, squared multiple correlations ve residual
   covariance çıktısını isteyin. C için R² ile maddelerin R²'lerini ayırın.
   A1'in sabit yükü 1 için test istatistiği beklemeyin.
8. Serbest parametre 21, sd=34; gamma≈.739950, standart yol≈.339936,
   Var(A)≈.092572, Var(zeta_C)≈.387938, toplam Var(C)≈.438624 beklenir.
   Standartlaştırılmamış gamma Wald p≈.064892; bu küçük örneklemde aşağıdaki
   olabilirlik-oranı testinin p'siyle aynı değildir. İkisini saklamadan raporlayın.
9. Aynı dosyanın ayrı model kopyasında A→C yolunu 0'a sabitleyin: 20 parametre,
   sd=35; normal ML fark testi Δchi²≈6.114847 (1 sd), p≈.013405. Parametre
   sınama için klasik regresyon F testi kullanmayın. Sağlam/ordinal tahminciye
   geçilirse bu ham chi² farkını otomatik taşımayın.
10. Diğer kopyada C→A yönünü kurun; bu kez C dışsal, A içsel ve A'nın yapısal
    artığı vardır. Aynı marker yükleri korunur. Yol≈.156168, standart yol≈.339936
    ve aynı gözlenen kovaryans/uyum beklenir. Bu veri nedensel yönü seçmez.
11. Python'daki AIC_star/BIC_star ortak sabiti çıkarılmış karşılaştırma sayılarıdır;
    AMOS'un tam bilgi ölçütü sütunlarıyla doğrudan sayısal eşleştirmeyin.
12. Oturum gerçekten çalıştırıldıysa yazılım sürümü, SAV, AMW, çıktı raporu ve
    ayarları saklayın. Çalıştırılmadıysa ekran görüntüsü/AMOS sonucu üretmeyin.

Bu iki-faktörlü modelde aracı yapı yoktur. Dolaylı etki bootstrap menüsünün
varlığı aracı değişken yaratmaz. Üç-yapılı model, kuramsal ölçüm ve tasarım
kurulduktan sonra ayrıca tanımlanmalı; bootstrap türü ve başarısız çözümler
kaydedilmelidir. Bu paket bootstrap, çok grup, değişmezlik veya FIML uygulamaz.