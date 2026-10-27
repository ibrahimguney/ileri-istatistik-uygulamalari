# AMOS DFA kontrol listesi — Bölüm 19

Bu liste modeli AMOS'ta kurarken izlenecek adımları verir. Kitaptaki sayısal
tablolar Python ile hesaplanmış ve R/lavaan ile aynı bulunmuştur; AMOS ekran
görüntüsü değildir.
Temel belge: IBM SPSS Amos 31 User's Guide,
https://www.ibm.com/docs/SSLVMB_31.0.0/pdf/IBM_SPSS_Amos_User_Guide.pdf
(erişim: 6 Eylül 2026).

1. Önce Bölüm 18 ve Bölüm 19 Python betiklerini çalıştırın. `puanlanmis.csv`
   yarım B'nin 1316 kaydını içerir; A1/C4/C5 zaten çevrilmiştir, tekrar ters
   kodlama yapmayın. SPSS'te CSV'yi okuyup `.sav` olarak kaydedin. `kaynak_satir`
   ve `kaynak_kayit` gösterge olarak seçilmemelidir.
2. A ve C adlı iki gizil faktör; A1–A5 ve C1–C5 adlı on gösterge; her göstergeye
   ayrı artık terimi ekleyin. A maddelerini yalnız A'ya, C maddelerini yalnız C'ye
   bağlayın. Artıkların göstergelerine giden yollar 1; artık varyansları serbesttir.
3. Faktör varyanslarının her birini 1'e sabitleyin; işaretleyici yükleri ayrıca
   1'e sabitlemeyin. M1'de A–C ilişkisi serbest: 21 parametre/34 sd.
4. M0'da A–C ilişkisini 0 yapın: 20 parametre/35 sd.
5. M2'de M1'e ek olarak e_A1↔e_A2, e_C1↔e_C2 ve e_C4↔e_C5 çift yönlü oklarını
   ekleyin: 24 parametre/31 sd. Bu çiftler yarım B açılmadan önce yazılmıştır;
   AMOS'un Modification Indices listesinden yeni ok eklemeyin.
6. ML seçimini ve ortalama yapısının kapalı olduğunu kontrol edin. AMOS ki-kare
   için n−1 çarpanını kullanır; kitap da Wishart n−1 yaklaşımını kullanır.
   RMSEA/SRMR, bilgi matrisi ve aralık tanımları ayrıca karşılaştırılmalıdır.
7. Yakınsama, uyarılar, negatif varyans, sınır korelasyonu, standart hatalar ve
   tanımlanabilirlik incelenmeden uyum indekslerini onaylamayın. Standart ve
   standart olmayan yükleri ayrı okuyun.
8. Beklenen değerler: M1 T≈306.99, sd=34; M2 T≈180.54, sd=31; M1'de phi≈.340.
   Tam AIC/BIC ile kitaptaki AIC*/BIC* aynı sayılar değildir. AMOS sürümü ve
   ayarları kaydedilmeden son basamak eşitliği iddia etmeyin.
9. Modification Indices seçeneği açılırsa M1 için C4↔C5, C1↔C2 ve A1↔A2 en
   üstte görünmelidir (AMOS eşik ve ölçek farkları nedeniyle sayılar lavaan'dan
   biraz ayrılabilir). Liste betimseldir. WLSMV/sağlam düzeltme uygulanmış
   sayılmaz; ölçme değişmezliği ayrı bölümde ele alınır.
