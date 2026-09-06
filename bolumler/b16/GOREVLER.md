# Bölüm 16 — Öğrenci görevleri

VERI.md ile başlayın. Hesap için calisma.ipynb, gerekçeler için COZUMLER.md kullanın. Gerçek iki faktörlü analiz ile kurgu üç-yapılı aracılığı ayırın.

## D1–D3

1. Neden n=97? Bu kişiler Bölüm 15'ten bağımsız mı? Ham arşivden kayıt silindi mi?
2. Gösterge hatası, C'nin yapısal artığı ve C'nin toplam varyansını ayrı tanımlayın.
3. A→C oku neyi modeller, hangi nedensel iddiayı kanıtlamaz? Gerçek analizde aracı değişken var mı?

## G1–G4

1. 55 momenti ve 21 parametreyi sayın. Sıfır yol kısıtında hangi parametre/sd değişir?
2. Gamma, u, psi'den Var(C), standart yol ve R²'yi hesaplayın.
3. Sıfır-yol LR istatistiğini ve nominal p'yi bulun. Bunun ileri–ters yön testi olmadığını açıklayın.
4. A1 ham yükü 1 iken standart yükü nasıl .304 olabilir? Ham yol Wald aralığı/p ile LR sonucunu, birini gizlemeden yorumlayın.

## B1–B3

1. İleri modelin gizil kovaryansından ters delta ve psi_A'yı bulun. Daha küçük ham ters yol daha zayıf uyum mu?
2. Beta dönüşümlü aralığından R² dönüşümlü aralığını hesaplayın. Beta aralığı sıfırı kapsasaydı alt uç ne olurdu? Simetrik Wald aralığı ile aynı mı?
3. Kurgu a=.48, b=.41, c′=.19 için ab ve toplamı bulun. Bu sayılardan p veya bootstrap aralığı üretilebilir mi?

## H1 — Altı iddiayı düzeltin

“A1 yükü 1, hatasız. C'nin yapısal artığı .388, toplam varyansı da budur. CFI iyi, A C'ye neden olur. Ters modelin uyumu aynı, geri besleme kanıtlandı. Exp dönüşümü bütün Heywood sorunlarını çözer. Kurgu katsayılarına bakarak 5000 bootstrap yaptığımızı yazdık.”

Ölçekleme, varyans, eşdeğerlik ve çalıştırılmış işlem ayrımını kullanın.

## P1 — Denetlenebilir SEM protokolü

Yeni araştırmada yapı/gösterge, ölçüm zamanı, veri türü, ölçekleme, sıfır/eşitlik kısıtları, tanımlanabilirlik, tahminci, eksikler, örneklem planı, uyum/yol aralıkları ve alternatifleri yazın. Aracılık gerçekten planlanıyorsa tam modeli, bootstrap birimini ve başarısız çözüm kuralını belirtin; burada uygulanmış gibi göstermeyin.

| Karar/kanıt | Buradaki durum | Yeni çalışma planı | Gerekli dayanak |
|---|---|---|---|
| Kaynak/ön işlem | Yerel 97 tam kayıt | … | Uzak hücre teyidi yok |
| Ölçüm/marker | A1 ve C1 sabit 1 | … | İçerik ve ölçüm sınırı |
| Yol yönü | İleri/ters eşdeğer | … | Zamansal/tasarımsal kanıt |
| Tahmin ve eksikler | Normal-kuram ML; tam kayıt | … | Ordinal/sağlam duyarlılık yapılmadı |
| Yeni örneklem doğrulaması | Yapılmadı | … | Veri toplama uydurulmaz |
| Aracılık / bootstrap | Gerçek modelde yok | … | Yalnız kurgu cebir var |

Teslim: kaynak ve model sözlüğü, çalışan kod, uyum/yapısal nicelik/artık tabloları, grafik ve bir sayfalık protokol. Rubrik: kuram/ölçüm 25, model/tanımlama 25, tahmin/belirsizlik 25, yorum/sınırlılıklar 15, yeniden üretim 10.