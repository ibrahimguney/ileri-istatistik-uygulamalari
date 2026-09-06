# Bölüm 16 — Gerekçeli çözümler

Bu sayılar aynı 97 kaydın Python öğretim hesabıdır; AMOS/lavaan veya bağımsız doğrulama sonucu değildir. Son basamaklar için beklenen.json kullanın.

## D1–D3

1. C1/satır63, A2/satır66, C3/satır90 eksik olduğundan ortak 97 tam kayıt kullanılır; arşivde 100 kayıt korunur. Aynı kişiler Bölüm 14–15'te kullanılmıştır.
2. Gösterge hatası bir maddenin ölçüm modelindeki özgül kısmıdır. Yapısal artık zeta_C, A ile açıklanmayan gizil C kısmıdır; toplam Var(C), gamma² Var(A)+Var(zeta_C)'dir.
3. Ok koşullu ilişki parametreleştirmesidir; nedensel yönü kanıtlamaz. Bu iki-faktörlü gerçek örnekte aracı yapı yoktur.

## G1–G4

1. 10×11/2=55 moment; sekiz serbest yük+on gösterge hata varyansı+dışsal varyans+yapısal artık varyansı+yol=21, sd=34. Sıfır yol q=20/sd=35. CFI başlangıcı bağımsız göstergeler modelidir; sıfır yol modeliyle aynı değildir. Yerel rank ayrıca kontrol edilir.
2. Gamma=.739950416, u=.092572138, psi=.387938109. Var(C)=gamma²u+psi=.438623819; beta=gamma sqrt(u/Var(C))=.339935608; R²=.115556217. Yapısal artık toplam varyans değildir; R² göstergenin değil içsel gizil C'nin model içi payıdır.
3. LR=51.252956953−45.138110038=6.114846915, sd farkı=1, nominal p=.013405102. İleri ve ters modeller aynı kovaryansı verir; aralarında yön seçen sd=0 fark testi p'si üretilmez.
4. A1'in marker yükü 1 yalnız gizil ölçeği tanımlar; standart yük=1×sqrt(Var(A)/Var(A1))≈.304257, madde R²≈.092572. Ham gamma Wald %95 GA [−.045682,1.525582], p=.064892; LR p=.013405'tir. Farklı normal-kuram yaklaşık sınamalar, küçük örneklem ve zayıf marker ölçek belirsizliğinde ayrışabilir. Küçük p seçilmez; profil veya bootstrap ek denetimi yapılmamıştır.

## B1–B3

1. Cov(A,C)=gamma u. Ters delta=Cov(A,C)/Var(C)=.156167518; psi_A=u−Cov(A,C)²/Var(C)=.081874852. İleri/ters/CFA aynı gözlenen kovaryansı ve T=45.138110, sd=34 uyumunu verir. Ham yolların büyüklükleri ölçeğe bağlıdır; küçük ters yol daha zayıf uyum veya geri besleme kanıtı değildir.
2. Beta dönüşümlü %95 aralığı [.080523,.556219]; iki uç pozitif olduğundan R² aralığı [.006484,.309380]. Aralık sıfırı kapsasaydı kare görüntüsünün alt sınırı 0 olurdu. R²'nin simetrik Wald aralığı [−.048794,.279907] başka yaklaşımdır; negatif alt uç negatif R² nokta tahmini değildir. Nokta R²=.115556. Sabit sıfır modelindeki [0,0] ise kısıtın sonucu olup veriyle kesin sıfır etkisi kanıtı değildir.
3. Kurgu ab=.48×.41=.1968, toplam=.19+.1968=.3868. Bir veri seti/örnekleme modeli olmadan bunlardan p veya bootstrap aralığı türetilmez; gerçek iki-yapılı BFI modeline bu aracılık eklenmez.

## H1

- Marker yükü 1 hata varyansını sıfırlamaz; standart yük ve gösterge R² ayrıca okunur.
- .387938 yapısal artık; .438624 toplam Var(C)'dir.
- İyi CFI nedensellik kanıtı değildir; ölçüm ve tasarım kanıtı gerekir.
- Aynı uyum eşdeğer parametreleştirmeyi gösterir, geri beslemeyi kanıtlamaz.
- Pozitiflik dönüşümü sınır/yakınsama/uygunsuz çözüm denetimini ortadan kaldırmaz.
- Kurgu çarpımı bootstrap değildir; 5000 tekrar veya aralık yapılmış gibi yazılmaz.

## P1 — Ölçülü rapor örneği

“On A/C maddesinde aynı 97 tam kayıt anahtarlanıp ddof=1 ile standartlaştırıldı. Marker yükleri A1/C1=1 altında normal-kuram Wishart ML yapısal model kuruldu. İleri model T(34)=45.138, CFI=.936, RMSEA=.058 (%90 GA [0,.100]), SRMR=.078 verdi. Ham gamma=.740 için Wald p=.0649; sıfır yol LR testi p=.0134 bulundu ve yaklaşımlar ayrı raporlandı. Standart yol .340, içsel R²=.116 idi. Ters model aynı kovaryansı verdi; nedensel yön seçilmedi. R/lavaan/AMOS, bootstrap, ordinal duyarlılık ve bağımsız doğrulama yapılmadı.”

Yeni protokolde ölçüm zamanı ve kısıtlar sonuçlardan önce gerekçelendirilir. Yapılmamış veri toplama, uzman görüşmesi, bootstrap veya doğrulama tabloya sonuç olarak yazılmaz.