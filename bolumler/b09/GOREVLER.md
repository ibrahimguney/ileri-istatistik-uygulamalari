# Bölüm 9 — Öğrenci görevleri

## D — Önce tasarım

1. Hangi sütun aracı, hangisi düzenleyici? İki yanıt neden ayrı üretildi?
2. Üretici a=.6 ile örneklem a tahmini neden aynı olmak zorunda değil?
3. Gerçek bir araştırmada zaman sırası ve karıştırıcılar için hangi ek kanıt gerekir?

## G — Aracılık

1. Üç OLS modeli kurup a, b, c', c ve ab hesaplayın. c=c'+ab eşitliğini denetleyin.
2. 5000 satır-bootstrap uygulayın. X, M ve Y'yi ayrı ayrı örneklemek neden yanlış?
3. Persentil %95 aralığını ve bootstrap SH'yi bulun; BCa ve p değeriyle karıştırmayın.
4. Gözlenen ab'yi üretici .42 ile kıyaslayın. Tek aralığın .42'yi içermesi
   veya içermemesi yöntemin kapsama oranını doğrular mı?

## B — Düzenleyicilik

1. Merkezli ve ham etkileşim modellerinin tahminlerini karşılaştırın.
   Merkezlemek etkileşim katsayısını ve model uyumunu değiştirir mi?
2. W ortalama ve ortalama±1SS için basit eğim, SH ve noktasal t aralıklarını bulun.
   SH hesabında kovaryans terimi çıkarılırsa ne olur?
3. İki basit eğimin p değerlerinin farklı olması doğrudan etkileşim testi midir?
4. Sabit W'de X artınca tahmin farkını modelden bulun; bu farkı basit eğimle denetleyin.

## H — Hatalı raporu düzeltin

“160 gerçek öğrencide nedensel mekanizma kanıtlandı. Bootstrap BCa kullandık.
M ve Y sütunlarını ayrı ayrı örnekledik. c' anlamsızsa tam aracılık kesindir.
Merkezleme etkileşimi ortadan kaldırdı. Bir eğim anlamlı diğeri değil,
etkileşim kesin var. Aynı dosyada M ve W bulunduğu için koşullu dolaylı etkiyi de hesapladık.”
Yedi iddiayı yöntem ve veri kapsamıyla düzeltin.

## P — Teslim

Simülasyon etiketi taşıyan kısa rapor, kod/notebook, bootstrap dağılımı ve
basit eğim grafiği. Model/yanıt eşleştirmesi, yollar, bootstrap birimi,
B/seed/yöntem, kovaryanslı eğim belirsizliği ve nedensellik sınırlarını yazın.
Rubrik: tasarım/kapsam 20, aracılık/yeniden örnekleme 30,
etkileşim/eğim 30, yorum 10, yeniden üretim 10 puan.