# AMOS DFA kontrol listesi — Bölüm 15

Bu liste **yapılacak uygulama** içindir; AMOS bu ortamda çalıştırılmamıştır.
Sayısal tablolar Python hesabıdır, AMOS ekran görüntüsü veya çıktısı değildir.
Temel belge: IBM SPSS Amos 31 User's Guide,
https://www.ibm.com/docs/SSLVMB_31.0.0/pdf/IBM_SPSS_Amos_User_Guide.pdf
(erişim: 6 Eylül 2026).

1. Önce Python analizini çalıştırın. `sonuclar/standartlastirilmis.csv` on madde/97 satır
   içerir; örneklem standart sapmasıyla standartlaştırılmıştır. SPSS'te bu CSV'yi
   okuyup desteklenen bir `.sav` dosyasına kaydetmek gerekebilir. Kaynak etiketleri
   gösterge olarak seçilmemelidir. Tekrar ters kodlama yapmayın.
2. A ve C adlı iki gizil faktör; A1–A5 ve C1–C5 adlı on gösterge; her göstergeye
   ayrı artık terimi ekleyin. A maddelerini yalnız A'ya, C maddelerini yalnız C'ye
   bağlayın. Artıkların göstergelerine giden yollar 1; artık varyansları serbesttir.
3. Faktör varyanslarının her birini 1'e sabitleyin. İşaretleyici yükleri ayrıca
   1'e sabitlemeyin; bu seçenekte on birincil yük serbesttir. Artık kovaryansları
   ve çapraz yükler sıfırdır. M1'de A–C ilişkisi serbest: 21 parametre/34 sd.
4. M0'da A–C ilişkisini 0 yapın: 20 parametre/35 sd. M0 bağımsız göstergeli
   başlangıç modeli değil, ilişkisiz iki faktör modelidir.
5. M2'de M1'e ek olarak C'den A2'ye bir yol ekleyin: 22 parametre/33 sd.
   Bu alternatif aynı verideki AFA ipucundan seçilmiştir; bağımsız doğrulama değil.
6. ML seçimini ve ortalama yapısının kapalı olduğunu kontrol edin. Kovaryans
   matrisi böleni ve ki-kare çarpanını yazın; Python Wishart n−1 yaklaşımını kullanır.
   Yazılımın RMSEA/SRMR, bilgi matrisi ve aralık tanımları da karşılaştırılmalıdır.
7. Yakınsama, uyarılar, negatif varyans, sınır korelasyonu, standart hatalar ve
   tanımlanabilirlik incelenmeden uyum indekslerini onaylamayın. Standart ve
   standart olmayan yükleri ayrı okuyun; modelin ürettiği kovaryansları denetleyin.
8. Model uyumu, standart tahminler, artıklar ve faktör korelasyonunu kaydedin.
   M1 yaklaşık T=45.138, sd=34 verir; tam AIC/BIC ile kitaptaki ortak sabiti
   çıkarılmış AIC*/BIC* aynı sayılar değildir. AMOS sürümü ve ayarları kaydedilmeden
   son basamak eşitliği iddia etmeyin.
9. Bu liste MI taraması veya otomatik artık kovaryansı ekleme talimatı değildir.
   WLSMV/sağlam düzeltme uygulanmış sayılmaz. Türkçe uyarlama, bağımsız veriyle
   doğrulama ve ölçüm değişmezliği ayrıca planlanmalıdır.