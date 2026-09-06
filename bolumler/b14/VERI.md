# Veri, kaynak ve yöntem sınırı

## Değişmeyen yerel kaynak

Bölüm 13 arşivindeki `bfi-ilk100-AC.csv` dosyasının aynısı kullanılır. Rdatasets psych/bfi CSV aktarımının ilk 100 veri satırından yalnız A1–A5 ve C1–C5 seçilmiştir. Paket belgesinde tam kaynak 2800 kişi ve 25 IPIP maddesi olarak tanımlanır; bu dosya o tam veri değildir. John ve arkadaşlarının Big Five Inventory testiyle veya onaylanmış Türkçe testle karıştırılmaz.

- Veri tanımı/anahtar: https://www.personality-project.org/r/html/bfi.html
- CSV aktarımı: https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/psych/bfi.csv
- IPIP kullanım açıklaması: https://ipip.ori.org/newPermission.htm

Önceki aktarım notu 5 Eylül 2026 tarihlidir: terminal indirmesi engellendiği için tarayıcıda görülen sütun alıntısı yerel dosyaya aktarılmıştır. Bu paket uzak CSV veya kurulu psych verisiyle yeni otomatik hücre karşılaştırması yapmaz. Yerel hash bütünlüğü kaynak doğrulaması değildir. Yeni yanıt, doldurma veya yeni örneklem yoktur.

Kaynak satırı 1–100 aktarım konumudur; kaynak kayıt etiketi ilk 61617, son 61831'dir, gerçek kişi kimliği olarak kullanılmaz. İlk 100 kayıt rastgele veya temsili değildir. Demografik sütunlar yoktur. IPIP maddelerine ilişkin kullanım açıklaması bütün veri aktarımlarına veya başka ölçeklere lisans atamak için kullanılmaz; bu pakette yeni lisans atanmadı. Türkçe içerik açıklamaları uygulanmaya hazır uyarlama formu değildir.

## Analiz sözleşmesi

Yanıtlar 1–6, boş hücre eksiktir; 0 ve 99 geçerli yanıt değildir. A1, C4 ve C5 anahtara göre `7-x` ile bir kez çevrilir. On madde için ortak tam kayıt seçilir: C1/satır63, A2/satır66, C3/satır90 dışarıda; n=97. Bölüm 13'ün ayrı A=99 ve C=98 matrisleri birleştirilmez. İkili eksik silme veya atama yapılmaz; eksiklik mekanizması belirlenmez.

Pearson matrisi kullanılır, polikorik/ordinal model üretilmez. PAF, SMC başlangıç köşegeniyle ortak varyans değişiminin Öklid normu 1e-10 altına inene kadar, en çok 2000 yineleme çalışır. Yetersiz pozitif çıkarım özdeğeri veya yakınsamama hatadır. Heywood ayrıca raporlanır; mevcut 1/2/3 adaylarda görülmemiştir.

Quartimin: Kaiser satır normalizasyonu yok, tolerans 1e-8, üst sınır 10000. Sütunlar ve işaretler A/C içeriğini okunabilir kılacak şekilde düzenlenir; çapraz yükler sıfıra zorlanmaz. Örüntü L, faktör korelasyonu Phi, yapı L @ Phi; ortak matris L @ Phi @ L.T'dir. İki algoritmada aynı amaç değerine ulaşmak küresel optimum veya örneklem kararlılığı kanıtı değildir.

RMSR yalnız 45 benzersiz köşegen dışı çift üzerinden hesaplanır; .05 artık işaretleme eşiği bir test değildir. Bu değer CFA-SRMR veya RMSEA değildir. A1/A4 çıkarma duyarlılığında 8 madde, aynı 97 kişi ve 28 çift vardır; payda/ içerik değişir.

Paralel analiz 2000 kez her sütunu ayrı permüte eder; tohum 20261401. Sütun dağılımları korunur, satır içi ilişkiler kırılır. Her sıralı özdeğer için doğrusal %95 referans niceliği ve ilk sıradan ardışık aşma kuralı kullanılır. PCA köşegeni 1'dir; SMC sürümünde her permütasyonun kendi SMC köşegeni hesaplanır. SMC spektrumu yakınsamış PAF özdeğeri değildir. Referans eğrileri gözlenen özdeğerlerin güven aralığı değildir. R ve Python aynı tohumla aynı diziyi üretmek zorunda değildir.

## İzlenebilirlik

CRLF → LF, ardından tek son LF ile normalize SHA-256:
`8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557`.
Gerçek bayt hash'i ayrıca JSON'a yazılır. Normalizasyon hücre değişimini gizlemez. Python kaynak dosyasının çalışma sonunda değişmediğini denetler. Beklenen kitap JSON'unda eski ham-bayt hash'i sürüme/son satır sonuna bağlı olabileceği için karşılaştırma kaynağı normalize hash'tir; öğrenci kopyasının kitap CSV'siyle bayt eşitliği ayrıca sınanır.

## Yöntem belgeleri

Kitaptaki yöntem notları 6 Eylül 2026 tarihlidir. Bu öğrenci hazırlığında statsmodels Factor ve rotate_factors resmi belgeleri tekrar incelendi; bu erişim veri doğrulaması değildir. Çalıştırılan sürümler requirements.txt/DOGRULAMA.json'dadır; webdeki stable belge sürümüyle aynı olduğu varsayılmaz.

- https://www.statsmodels.org/stable/generated/statsmodels.multivariate.factor.Factor.html
- https://www.statsmodels.org/stable/generated/statsmodels.multivariate.factor_rotation.rotate_factors.html
- https://personality-project.org/r/psych/help/fa.html
- https://personality-project.org/r/psych/help/fa.parallel.html
- https://personality-project.org/r/psych/help/KMO.html
- https://personality-project.org/r/psych/help/cortest.bartlett.html
- Horn (1965): https://doi.org/10.1007/BF02289447
- MacCallum ve arkadaşları (1999): https://doi.org/10.1037/1082-989X.4.1.84