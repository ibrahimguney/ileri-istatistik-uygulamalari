# Bölüm 16 — raporlama

## Bölümdeki örnek ve açıklama

“7185 öğrencinin (160 okul) matematik başarısı iki düzeyli modellerle incelendi (REML, `lme4` ile doğrulandı). Boş modelde ICC .18 idi (tasarım etkisi 8.9). Grup ortalamasına merkezlenmiş SES’in okul içi eğimi 2.19 (SH .11), okul ortalama SES’inin eğimi 5.87 (SH .36) idi; bağlamsal etki 3.68 puandı. Okul içi SES eğimi okullar arasında değişti ($\tau_{11}=.70$, sınırda LR $=10.50$, $p=.003$). Eğim Katolik okullarda devlet okullarına göre 1.64 puan daha düzdü (SH .24) ve okul ortalama SES’iyle arttı (1.04, SH .30); iki okul değişkeni eğim varyansının %86’sını açıkladı. Okul türü rastgele atanmadığından sonuçlar nedensel yorumlanmamalıdır.”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 19: hedef ve tahmin

Öğrenci ortalaması12.747853, eşit okul ortalaması12.620755, boş model sabiti12.636974.
DE gerçek büyüklüklerle9.479471; n_eff757.953649 yalnız öğrenci ortalaması içindir.
Okul8367 için büzülmüş merkez6.533962; okul ortalaması koşullu varyansı2.111023,
yeni öğrenci varyansı41.259345. Yeni okulda tek öğrenci47.762347,
aynı yeni okulun30 öğrenci ortalaması9.918969 varyansına sahiptir.
Normal tak-yerine-koy aralıkları parametre kestirim belirsizliğini içermez.
Yeni okul hedefi bütün okulları ayıran doğrulama gerektirir; burada uygulanmadı.
Okul örneklem büyüklüğü toplam mevcut değildir; tarama ağırlığı uygulanmadı.
Ek yalnız Python ile sınandı.
