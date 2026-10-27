# Bölüm 11 — raporlama

## Bölümdeki örnek ve açıklama

Regresyon raporlarında katsayılar, güven aralıkları, model uyumu ve varsayım kontrolleri birlikte verilmelidir (Kitap kaynakçası: montgomery2021,kutner2005).

| **Yordayıcı**  | **B** | **SH** | **t** | **$p$** |
|:---------------|------:|-------:|------:|--------:|
| Sabit          | 42.10 |   5.80 |  7.26 | $<.001$ |
| Çalışma süresi |  3.25 |   0.72 |  4.51 | $<.001$ |
| Ön bilgi puanı |  0.41 |   0.12 |  3.42 |    .001 |

Örnek regresyon katsayıları tablosu

Regresyon analizi sonuçları raporlanırken yalnızca denklem yazmak yeterli değildir. Sağlıklı bir raporda şu unsurlar birlikte verilmelidir:

- regresyon denklemi,

- eğim ve sabit terimin yorumu,

- $R^2$ değeri,

- katsayıların anlamlılık düzeyi,

- gerekliyse güven aralıkları,

- varsayım kontrollerine ilişkin kısa değerlendirme.

Örneğin şu ifade kullanılabilir: “Reklam harcaması satış miktarını anlamlı ve pozitif yönde yordamaktadır ($b_1=3.31$, $p<.05$, $R^2=0.99$).”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 15: ayrı kalibrasyon

Ana60 kayıtlık model korunur. Ayrı deney: eğitim1–40, kalibrasyon41–60,
kontrol61–80. Model yalnız40 kayıtta kurulur; sonrasında yeniden kurulmaz.
Sabit7.167985/eğim.470810; m20 ve alpha.05 için k20, q2.876083.
G1=12 nokta12.817702, split aralık[9.9416,15.6938]. Aynı40 kayıtta klasik
bireysel aralık[9.9660,15.6694]. Kontrol20 kişide ikisi de18/20 kapsar;
bu oran dış doğrulama veya gelecekte garantili kapsama değildir.

Değiştirilebilirlik altında split conformal garanti marjinaldir; her x/alt grup
ve bütün20 yeni kişiye eşzamanlı değildir. Kaynak sırası/tek okul varsayımı
kanıtlamaz. HC3 katsayı aralığı bireysel tahmin aralığı değildir. Yeni ek
yalnız Python; küme/zaman/çapraz conformal veya normalize skor yok.
