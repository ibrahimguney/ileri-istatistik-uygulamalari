# Bölüm 15 — Gerekçeli çözümler

Sonuçlar aynı yerel 97 kaydın öğretim hesabıdır; lavaan veya AMOS çıktısı değildir. Ayrıntılı sayılar beklenen.json'dadır.

## D1–D3

1. Aynı veride AFA'dan DFA'ya geçiş, serbest örüntü ile açık kısıtları karşılaştırır; yeni veriyle sınama olmadığı için bağımsız doğrulama değildir.
2. A1/C4/C5 bir kez 7−x; kaynak satırları 63/66/90 dışarıda. Örneklem ddof=1 z-puanlarından S elde edilir. Gözlenen varyansın 1 olması ile gizil faktör varyansını 1'e sabitlemek ayrı işlemdir.
3. Yalnız normal-kuram kovaryans ML, Wishart n−1 çarpanı uygulanır. Sağlam ML, WLSMV ve FIML burada yapılmamıştır; tam kayıt seçimi FIML değildir.

## G1–G4

1. 10×11/2=55 kovaryans momenti. On birincil yük+on artık varyansı M0'da q=20, sd=35; ilişki serbest M1'de q=21, sd=34; A2 C çapraz yükü eklenince q=22, sd=33. Faktör varyansları zaten 1, ortalama yapısı yoktur. Pozitif sd yeter koşul değildir; yerel Jacobian rankları 20/21/22 ayrıca kontrol edilir.
2. M1 F=.470188646; T=96F=45.138110. Başlangıç T=218.391072, sd=45. CFI=1−(45.138110−34)/(218.391072−45)=.935763. RMSEA=sqrt((45.138110−34)/(97×34))=.058114; %90 GA [0,.099618]. Nokta değer düşük olsa da üst sınır belirsizliği gösterir; doğru model kanıtı değildir. SRMR=.078238 (55 hücre), RMSR_off=.086495 (45 çift).
3. A1 standart yük=.304256697; R²=.092572137, theta_std=.907427863; %95 Wald GA [.094327,.514187]. Sıfır dışlansa da model bu maddenin varyansının yalnız yaklaşık %9.3'ünü temsil eder. Aralık sağlam değildir ve tüm yükler için eşzamanlı kapsama sağlamaz.
4. C için AVE=.361300918, CR=.735159133. AVE'nin payı yük kareleri toplamı, CR'nin payı yük toplamının karesidir; aynı sayı değildir. Basit M1, model-standartlaştırılmış maddeler ve ilişkisiz artıklar bağlamında hesaplanır. CR'nin görece büyük olması düşük AVE'yi veya içerik sorununu ortadan kaldırmaz.

## B1–B3

1. M0−M1: 51.252957−45.138110=6.114847; sd farkı=1, nominal p=.013405. M0 iki ilişkisiz faktördür; CFI başlangıcı bütün göstergeleri ilişkisiz sayar ve sd=45'tir.
2. M1−M2: 7.611594; sd farkı=1, nominal p=.005799. M2: T=37.526516, sd=33, p=.269328, CFI=.973894, TLI=.964401, RMSEA=.037604, %90 GA [0,.086312], SRMR=.067726. A2 standart C çapraz yükü .302006'dır. M2'de A2 R²'si iki yük ve Phi çapraz terimini içerir; yalnız birincil yük karesi değildir. Alternatif AFA ipucundan seçildi; otomatik MI taraması yapılmadı, nominal p model seçimine göre düzeltilmedi.
3. A: AVE=.334322744, CR=.689264711. M1 Phi=.339935607, Phi²≈.115556; Phi %95 GA [.080523,.556219]. Bu katsayılar Türkçe geçerlik veya kültürel eşdeğerlik onayı değildir. CR ham alfa değildir; AVE/CR aralıkları hesaplanmadı.

## H1

- Anlamsız ki-kare ve düşük nokta RMSEA modeli kanıtlamaz; belirsizlik, varsayımlar ve örneklem incelenir.
- Global CFI her maddenin güçlü temsil edildiğini göstermez; A1 örneği bunu açıkça ayırır.
- CR ve AVE farklı niceliklerdir; yüksek CR içerik/geçerlik belgesi değildir.
- Aynı veride AFA sonrası modeli değiştirmek bağımsız DFA doğrulaması değildir.
- Bu tablolar Python hesaplarıdır. AMOS ve R/lavaan çalıştırılmamıştır; hazır kontrol listesi çıktı sayılmaz.

AIC*/BIC* aynı veri/ortak sabit için karşılaştırılır: M0 91.252957/142.747177; M1 87.138110/141.207041; M2 81.526516/138.170158. Tam yazılım AIC/BIC değerleriyle doğrudan eşitlik iddiası kurulmaz.

## P1: Ölçülü rapor örneği

“Arşivin sıralı ilk 100 kaydından on A/C maddesinde 97 tam kayıt seçildi; anahtar uygulandı. Örneklem z-puan kovaryansına ortalama yapısı olmadan normal-kuram Wishart ML uygulandı. İlişkili iki faktör modeli T(34)=45.138, CFI=.936, RMSEA=.058 (%90 GA [0,.100]), SRMR=.078 verdi. A1 düşük temsil açısından incelemeye ayrıldı. AFA sonrası A2 çapraz yükü alternatifi keşifsel karşılaştırıldı; nominal p bağımsız doğrulama sayılmadı. R/lavaan ve AMOS çalıştırılmadı; ordinal/sağlam duyarlılık, yeni örneklem ve Türkçe uyarlama kanıtı üretilmedi.”

Gelecek çalışma tablosu bir protokoldür; yeni örneklem büyüklüğünü, uzman yanıtlarını veya DFA uyum indekslerini gerçekleşmiş gibi doldurmayın.