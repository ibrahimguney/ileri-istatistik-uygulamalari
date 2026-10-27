# Bölüm 21 — AMOS kurulumu ve çıktı kontrolü

Bu bir kurulum rehberidir, çalıştırılmış bir AMOS oturumunun raporu değildir.
Kitaptaki sayısal tablolar Python ile hesaplanmış ve R/lavaan ile aynı bulunmuştur.

1. Python betiğinin ürettiği `standartlastirilmis.csv` dosyasını SPSS'te açıp
   `.sav` olarak kaydedin. Model göstergeleri A1–A5, C1–C5; aracılık modelinde
   ayrıca K (1 kadın, 0 erkek). `kaynak_satir`/`kaynak_kayit` modele konmaz.
   1316 kayıt olmalıdır. A1, C4, C5 zaten terslenmiştir.
2. A ve C için iki elips, on gösterge, her göstergeye ayrı hata terimi çizin.
   A yalnız A1–A5'e, C yalnız C1–C5'e yüklensin. e_A1↔e_A2, e_C1↔e_C2 ve
   e_C4↔e_C5 çift yönlü okları ekleyin (Bölüm 19 M2).
3. A→A1 ve C→C1 yüklerini 1'e sabitleyin; diğer sekiz yük ve on hata varyansı
   serbest. Bu, gizil varyansları 1'e sabitleyen Bölüm 19 parametreleştirmesi değildir.
4. İleri model: A→C yolunu çizin; C'ye ayrıca zeta_C yapısal artığını ekleyin
   (yük 1, varyans serbest). A ile zeta_C arasında kovaryans yoktur; A↔C
   çift yönlü okunu ayrıca eklemeyin. 24 parametre, sd=31.
   Beklenen: gamma≈.629, Var(A)≈.0852, Var(zeta_C)≈.2269, standart yol≈.360, R²_C≈.129.
5. Ayrı kopyada C→A (ters) kurun: aynı ki-kare (≈180.54, sd=31), delta≈.206.
   Bu veri nedensel yönü seçmez; ikisini sd=0 fark testiyle karşılaştırmayın.
6. Ayrı kopyada A→C yolunu 0'a sabitleyin: 23 parametre, sd=32, ki-kare≈269.15;
   fark Δchi²(1)≈88.61.
7. Aracılık kopyası: K dikdörtgeni ekleyin; K→A (a), A→C (b), K→C (c') yollarını
   çizin; A ve C'ye yapısal artık ekleyin; K'nın varyansı serbest. 27 parametre,
   sd=39, ki-kare≈215.02. Analysis Properties → Output: Indirect, direct & total
   effects; Bootstrap: 2000 örneklem, percentile CI. AMOS bootstrap'i maddeleri
   çekiliş içinde yeniden standartlaştırmaz ve farklı rastgele sayı üreticisi
   kullanır; aralıklar kitaptakine yakın ama birebir aynı olmaz.
   Beklenen ham dolaylı etki ≈.097, doğrudan ≈.012.
8. Normal-kuram ML, ortalama/intercept modeli olmadan çalışın. AMOS ki-kare için
   n−1 kullanır; RMSEA/SRMR ve standart hata tanımlarını ayrıca karşılaştırın.
9. Standardized estimates ve squared multiple correlations çıktısında AMOS
   K'yı da standartlaştırır (std.all); kitap K'yı ham bırakan std.nox ölçeğini
   raporlar. İki sayıyı karıştırmayın.
10. Oturum gerçekten çalıştırıldıysa yazılım sürümü, SAV, AMW, çıktı raporu ve
    ayarları saklayın. Çalıştırılmadıysa ekran görüntüsü/AMOS sonucu üretmeyin.
