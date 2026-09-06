# Bölüm 16 — Kaynak ve yöntem sözleşmesi

## Yerel arşiv ve sınır

Kaynak, Bölüm 13'te korunan Rdatasets psych/bfi ilk 100 veri satırının A1–A5/C1–C5 alıntısıdır. Tam belge 2800 kişi/25 IPIP maddesi tanımlar; burada tam kaynak, John ve arkadaşlarının Big Five Inventory testi veya onaylanmış Türkçe ölçek kullanılmıyor.

- Veri tanımı/anahtar: https://www.personality-project.org/r/html/bfi.html
- CSV aktarımı: https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/psych/bfi.csv
- IPIP kullanım açıklaması: https://ipip.ori.org/newPermission.htm

5 Eylül 2026 tarihli aktarım geçmişi korunur: terminal erişimi engellendiği için tarayıcıdan okunan sütun alıntısı aktarılmıştır. Bu öğrenci hazırlığında uzak CSV veya kurulu psych verisiyle yeni otomatik hücre karşılaştırması yapılmaz. Yerel hash kaynak doğrulaması değildir. Hiçbir yanıt üretilmez/doldurulmaz. Yeni lisans atanmaz; IPIP madde kullanım açıklaması tüm veri aktarımlarının veya başka ölçeklerin lisansı sayılmaz.

Kaynak satırı 1–100 aktarım konumudur; kaynak kayıt etiketi ilk 61617, son 61831'dir, gerçek kişi kimliği olarak kullanılmaz. Demografik sütunlar yoktur. İlk 100 kayıt rastgele/temsili değildir; Bölüm 14–15 ile aynı kişiler tekrar kullanılır, bağımsız SEM doğrulaması yapılmaz. Türkçe madde açıklamaları uygulanmaya hazır uyarlama formu değildir.

Kitap uygulamasının README'sinde önceki HolzingerSwineford1939/AMOS anlatımının kaynak raporu doğrulanamadığından yerel BFI örneğine geçildiği açıklanır. Bu paket o eski AMOS sayılarını yeniden üretmiş gibi sunmaz; eski sayıların mutlaka yanlış olduğu iddiasını da kurmaz.

## Ön işlem

1–6 tamsayı yanıt, boş hücre eksiktir. A1/C4/C5 anahtarla bir kez 7−x; eksik kaynak satırları 63/66/90 yalnız tam-kayıt analizinden çıkarılır, ham arşivde kalır. Ortak n=97; atama, ikili silme veya eksiklik mekanizması testi yoktur. Maddeler ddof=1 s ile standartlaştırılır; S ddof=1 kovaryansı Pearson matrisine eşittir.

CRLF → LF ve tek son LF ile normalize SHA-256:
`8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557`.
Gerçek bayt hash'i ayrıca JSON'a yazılır. Kaynak çalışma sonunda başlangıç baytlarıyla karşılaştırılır; bu kontrol hücrelerin uzak kaynağa uygunluğunu kanıtlamaz.

## Ölçüm ve yapı

A1 ve C1 marker yükleri 1; diğer sekiz yük ve on gösterge hata varyansı serbest, çapraz yükler/hata kovaryansları sıfırdır. İleri modelde C=gamma A+zeta_C, Var(A)=u, Var(zeta_C)=psi, Cov(A,zeta_C)=0. Phi=[[u,gamma u],[gamma u,gamma²u+psi]], Sigma=Lambda Phi Lambda.T+Theta. İleri/ters modeller 21 parametre, 34 sd; sıfır yol 20 parametre, 35 sd'dir. Sıfır yol bağımsız on göstergeli CFI başlangıç modeli değildir.

Var(C)=gamma²u+psi; standart yol=gamma sqrt(u/Var(C)), R²=gamma²u/Var(C). Ters regresyon aynı pozitif gizil kovaryansı yeniden parametreleştirir. Daha küçük ham ters yol daha kötü uyum değildir. Eşdeğer gözlenen kovaryans nedensel yön veya geri besleme kanıtı değildir; ileri–ters fark testi için sd=0 üzerinden p üretilmez.

## Tahmin ve denetim

F=logdet(Sigma)+tr(S Sigma^-1)−logdet(S)−10; Wishart T=(n−1)F. Normal-kuram kovaryans ML, ortalama yapısı olmadan; ordinal/sağlam tahmin, polikorik matris veya FIML değildir. Altı kategoriyi yaklaşık sürekli saymak bu öğretim örneğinin sınırıdır.

Yükler [-10,10], log varyanslar [-12,4], ham yol [-10,10] sayısal sınırları içinde aranır. Varyanslar exp dönüşümlüdür. Üç başlangıç (sayısal başlangıç tohumu 20260906), L-BFGS-B ve ek BFGS ile gradyan/amaç/model kovaryansı kontrol edilir. Bu tohum yeni katılımcı veya bootstrap üretmez. Sınır, yakınsamama, büyük gradyan veya rank sorunu kabul edilmez. Pozitiflik dönüşümü bütün Heywood sorunlarını çözmez; yerel rank küresel tanımlanabilirlik ispatı değildir.

Beklenen bilgi (n−1)/2 tr(Sigma^-1 D_a Sigma^-1 D_b); tersi parametre kovaryansıdır. Türevler merkezi sonlu farkla, bilgi model-kovaryansındaki sayısal Hessian ile, F genelleştirilmiş özdeğerlerle kontrol edilir. Paketteki `dfa_referans.py` kitabın B15 fonksiyonlarını taşır; CFA→marker ölçek dönüşümü ve ileri/ters/CFA kovaryans eşitliği ayrıca sınanır. Yardımcı veri okumaz/üretmez, B15 ana programı çalıştırılmaz.

## Aralık ve p türleri

Ham yol için normal-kuram Wald %95 aralığı ve p; standart yol/R² için delta SE verilir. Standart yol ayrıca atanh ölçeğinde delta aralığından geri tanh dönüşümüyle raporlanır. İki faktörlü bu modelde standart yol korelasyona eşittir. R²'nin dönüşümlü aralığı beta aralığının kare görüntüsüdür; beta aralığı sıfırı içeriyorsa R² alt sınırı 0 olur. Tekil/ yaklaşık/sağlam olmayan aralıklardır, bootstrap veya profil olabilirlik değildir.

CSV/JSON'daki simetrik Wald varyans/R² aralıklarının negatif uçları negatif nokta varyans tahmini değildir; uçlar sessizce kesilmez. Sabit sıfır-yol modelindeki sıfır SE ve [0,0] değerleri tahmin belirsizliği kanıtı değil kısıtın sonucudur. Ham gamma Wald p=.064892 ile sıfır-yol LR p=.013405 aynı kısıtın farklı yaklaşık sınamalarıdır; Wald dönüşüme değişmez değildir, küçük örneklem ve zayıf marker belirsizliği önemlidir. Küçük p seçilmez.

RMSEA=sqrt(max((T−sd)/(n×sd),0)); %90 aralık merkezi olmayan ki-kareden. SRMR köşegen dahil 55 benzersiz standartlaştırılmış artık hücresidir. CFI/TLI başlangıç sd=45. AIC*=T+2q, BIC*=T+q log(n) ortak sabiti çıkarılmış karşılaştırma ölçüleridir; yazılımların tam AIC/BIC sütunları değildir.

## Yapılmayanlar ve belgeler

Gerçek örnekte aracı yapı yoktur. Kurgu a=.48, b=.41, c′=.19 yalnız çarpım/toplam öğretimidir; gerçek veri sonucu veya bootstrap değildir. Yeni örneklem, uzman görüşmesi, WLSMV/sağlam duyarlılık, profil olabilirlik, değişmezlik ve R/lavaan/AMOS çalıştırması yapılmamıştır.

6 Eylül 2026: lavaan SEM ve tahminci belgeleri incelendi; bu erişim sayısal lavaan doğrulaması veya uzak veri teyidi değildir. Kitabın yöntem kaynakları:

- https://lavaan.ugent.be/tutorial/sem.html
- https://lavaan.ugent.be/tutorial/est.html
- https://lavaan.ugent.be/tutorial/mediation.html
- https://lavaan.ugent.be/tutorial/cat.html