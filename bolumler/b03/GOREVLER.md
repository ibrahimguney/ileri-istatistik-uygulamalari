# Bölüm 3 — Öğrenci görevleri

Ham CSV'yi değiştirmeyin; bütün denemeleri kopyalarda yapın.

## D — Hesaptan önce

1. Bir satır, bir madde hücresi ve kaynak etiketi neyi gösterir?
2. Boş hücre, sıfır ve 99 neden aynı kod değildir?
3. A1/C4/C5'i terslemeden önce hangi kaynak ve ölçek uçlarını kontrol edersiniz?

## G — Rehberli uygulama

1. Şemayı, anahtar benzersizliğini ve madde tür/aralıklarını denetleyin.
   Eksik hücre yüzdesi ile en az bir eksiği olan kayıt yüzdesini ayrı hesaplayın.
2. Ana veriyi koruyarak üç ters sütun üretin. A ve C için 5/5 ana puanı ile
   4/5 duyarlılık puanını hesaplayın. Her ortalamanın geçerli n'sini yazın.
3. Veriyi uzun biçime çevirin; boş yanıtları saklayın. Kişi–madde anahtarını
   kontrol ederek geniş biçime dönün ve özgün değerlerle eşitliğini sınayın.
4. A'nın ana puanını kullanılabilir kayıtların örneklem standart sapmasıyla
   standartlaştırın. Ortalama ve s denetimini yapın; normallik sonucu çıkar mı?

## B — Bağımsız denemeler

1. Ayrı kopyalarda 99, 2.5, metin, boş anahtar ve yinelenen anahtar ekleyin.
   `validate` hangi hatalarda durur? Bunları gerçek verinin hatası diye raporlamayın.
2. Tam boş, yalnız bir yanıtlı ve `[6,4,5,3,NA]` kurgusal satırları deneyin.
   Varsayılan toplam/ortalama ile minimum madde eşiği arasındaki farkı açıklayın.
3. C1'in tek eksiğini yalnız geçici kopyada gözlenen ortalamayla doldurun.
   Önce/sonra örneklem varyansını karşılaştırın. Ortalamanın değişmemesi yeterli mi?
4. Yinelenen anahtarlı birleşimi ve yinelenen kişi–madde pivotunu deneyin.
   `validate="one_to_one"` ve `pivot` neden hata vermelidir?

## H — Hatalı raporu onarın

“Yalnız yüzde 0.3 eksik olduğundan mekanizma MCAR'dır. Boşları sıfır yaptık.
Dört maddelik ortalamayı beş maddelik toplam diye raporladık. z puanları
normal dağılımı kanıtladı. Puanlanmış dosyayı yeniden terslemek güvenlidir.”
Beş iddiayı kayıt, hesap tanımı ve yorum sınırıyla düzeltin.

## Teslim

Kısa veri hazırlama raporu, notebook/kod, eksik özeti ve karar günlüğü teslim edin.
Ana 5/5 analiz ile 4/5 duyarlılığı ayırın; atama ve kayıt silme yapılmadığını,
kaynak sınırını ve yazılım sürümünü belirtin. MCAR testi veya güvenirlik analizi
bu uygulamada yapılmış gibi yazılmamalıdır.
Rubrik: kaynak/şema 20, denetimler 25, puan/reshape 30, yorum 15, yeniden üretim 10.