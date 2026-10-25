# Bölüm 12 — raporlama

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
