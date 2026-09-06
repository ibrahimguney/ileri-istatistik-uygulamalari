# Bölüm 15 — Veri ve yöntem sözleşmesi

## Kaynak ve kapsam

Bölüm 13 arşivindeki `bfi-ilk100-AC.csv` baytları değiştirilmeden kopyalanır. Rdatasets psych/bfi aktarımının ilk 100 veri satırından A1–A5/C1–C5 kullanılır. Belgelenen tam kaynak 2800 kişi/25 IPIP maddesidir; bu alıntı o tam veri değildir. John ve arkadaşlarının Big Five Inventory testiyle veya geçerlenmiş Türkçe ölçekle karıştırılmaz.

- Veri tanımı/anahtar: https://www.personality-project.org/r/html/bfi.html
- CSV aktarımı: https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/psych/bfi.csv
- IPIP kullanım açıklaması: https://ipip.ori.org/newPermission.htm

Kaynak aktarım notu 5 Eylül 2026 tarihlidir: terminal erişimi engellendiğinden tarayıcıdan okunan sütun alıntısı yerel dosyaya aktarılmıştır. Bu hazırlıkta uzak CSV veya kurulu psych verisiyle otomatik hücre karşılaştırması yapılmaz. Hash yalnız yerel bütünlüktür. Yeni yanıt, katılımcı veya eksik doldurma yoktur. Kaynak sırası 1–100 aktarım konumudur; kaynak kayıt etiketi ilk 61617, son 61831'dir, gerçek kişi kimliği olarak kullanılmaz. Demografik sütunlar yoktur.

Sıralı ilk 100 seçim rastgele/temsili değildir. Bölüm 14'teki kişiler aynıdır: DFA burada yeniden hesaplama öğretimidir, bağımsız doğrulama değildir. Türkçe açıklamalar uygulanmaya hazır uyarlama formu değildir. Bu pakette yeni lisans atanmaz; IPIP maddelerinin kullanım açıklaması başka ölçeklerin veya tüm veri aktarımlarının lisansı olarak yorumlanmaz.

## Ön işlem

Yanıtlar 1–6, boş hücre eksiktir; 0/99 geçerli yanıt değildir. A1/C4/C5 bir kez `7-x` ile çevrilir. C1/satır63, A2/satır66, C3/satır90 nedeniyle ortak 97 tam kayıt kullanılır. A=99/C=98 matrisleri birleştirilmez, ikili silme veya atama yapılmaz. Eksiklik mekanizması belirlenmez.

Maddeler örneklem standart sapmasıyla (ddof=1) standartlaştırılır. S, bu z-puanların ddof=1 kovaryansı, dolayısıyla aynı kişilerin Pearson matrisidir. Faktör varyanslarının 1'e sabitlenmesi ayrı bir model ölçekleme kararıdır.

## Model ve indeks tanımları

On birincil yük ve on artık varyansı serbesttir. Faktör varyansları 1, artık kovaryansları sıfırdır. M0 ilişkiyi 0'a sabitler; M1 ilişkiyi serbest bırakır; M2 ayrıca A2'ye C yükü ekler. Serbest parametre/sd sırasıyla 20/35, 21/34, 22/33'tür. 55 kovaryans momentinden parametre çıkarmak tek başına tanımlanabilirlik kanıtı değildir; kod yerel Jacobian rankını ayrıca sınar.

F=logdet(Sigma)+tr(S @ inv(Sigma))−logdet(S)−10; T=(n−1)F normal-kuram Wishart hesabıdır. Ortalama yapısı, eşikler, faktör ortalamaları, çoklu grup veya ordinal model yoktur. CFI başlangıç modeli bağımsız on göstergelidir (sd=45), M0 değildir.

RMSEA=sqrt(max((T−sd)/(n×sd),0)); %90 aralık merkezi olmayan ki-kare CDF'sinin .95/.05 terslenmesiyle bulunur. SRMR, örneklem varyanslarıyla standartlaştırılmış kovaryans artıklarının köşegen dahil 55 alt üçgen hücresinden; RMSR_off ise 45 köşegen dışı çiftten hesaplanır. Birbirinin veya Bölüm 14'teki farklı model RMSR'sinin yerine konmaz.

AIC*=T+2q, BIC*=T+q log(n) aynı veri için ortak olabilirlik sabiti çıkarılmış karşılaştırmalardır; AMOS/lavaan tam AIC/BIC sayılarıyla eşit değildir. Sağlam düzeltme, WLSMV veya FIML uygulanmaz.

## Belirsizlik ve sayısal denetimler

Artık varyansları exp, ilişki tanh parametresiyle temsil edilir. Yük sınırları [-3,3], log varyans [-12,3], ilişki dönüşümü [-4,4]; sonuç sınıra yaklaşırsa kod durur. Pozitiflik dönüşümü uygunsuz çözümleri kendiliğinden çözüyor sayılmaz. Bu veri için sınır sorunu görülmemiştir.

Dört L-BFGS-B başlangıcı ve ek BFGS karşılaştırması; küçük gradyan, aynı amaç/model kovaryansı ve sınırdan uzaklık denetlenir. Analitik türevler merkezi sonlu farklarla; F genelleştirilmiş özdeğerlerle; beklenen bilgi model kovaryansındaki sayısal Hessian'la kontrol edilir. Bunlar global tek çözüm veya doğru model kanıtı değildir. İkinci algoritmanın success alanı tek başına değil gradyan ve kovaryansla okunur.

Beklenen bilgi (n−1)/2 × tr(Sigma^-1 D_a Sigma^-1 D_b) hesabıdır. Standart yük SE'leri delta yöntemi; %95 Wald aralıkları tekil, normal-kuramlı ve sağlam değildir. Phi aralığı tanh-parametre aralığından geri dönüştürülür. CR/AVE yalnız basit M1 için hesaplanır; M2 çapraz yükünde birincil yükün karesi tek başına açıklanan varyans değildir. CR model-standartlaştırılmış alt ölçek toplamına ilişkin omega türü ölçüdür, ham alfa veya on maddelik toplam değildir. CR/AVE aralıkları üretilmez.

M1–M2 fark testi otomatik MI taraması değildir; AFA sonrası seçimin nominal p'si seçim yanlılığını düzeltmez. Bootstrap, ordinal/sağlam duyarlılık, ölçüm değişmezliği ve yeni veriyle DFA yapılmamıştır.

## İzlenebilirlik ve belgeler

CRLF → LF ve tek son LF ile normalize SHA-256:
`8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557`.
Gerçek bayt hash'i ayrıca JSON'dadır. Çalışma sonunda kaynak baytları değişmeden kalır. Beklenen dosya ham-bayt hash'i/sürüm yerine normalize kaynak hash'i ve kitap sonuçlarını içerir; ham kopyanın bayt eşitliği ayrıca sınanır.

6 Eylül 2026 tarihinde lavaan'ın ML/Wishart, CFA ve kategorik veri belgeleri yeniden incelendi; bu, R/lavaan çalıştırılması veya kaynak hücrelerinin doğrulanması değildir. Diğer bağlantılar kitabın yöntem kaynaklarıdır:

- https://lavaan.ugent.be/tutorial/est.html
- https://lavaan.ugent.be/tutorial/cfa.html
- https://lavaan.ugent.be/tutorial/cat.html
- https://lavaan.ugent.be/tutorial/cov.html
- https://lavaan.ugent.be/tutorial/modindices.html
- Rosseel (2012): https://doi.org/10.18637/jss.v048.i02
- https://search.r-project.org/CRAN/refmans/semTools/html/AVE.html
- https://search.r-project.org/CRAN/refmans/semTools/html/compRelSEM.html