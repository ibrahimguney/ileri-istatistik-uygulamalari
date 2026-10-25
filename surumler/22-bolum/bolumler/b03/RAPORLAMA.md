# Bölüm 3 — raporlama

## Bölümdeki örnek ve açıklama

Örnek rapor: “İlk 100 kaydın on maddesinde 3/1000 hücre eksikti (%0.3); üç kayıtta en az bir eksik vardı (%3). Ham kayıtlar korundu. A1, C4, C5 ayrı sütunlarda $7-x$ ile anahtarlandı. Beş tam madde kuralıyla A için 99, C için 98 puan üretildi; ortak tam küme 97 kayıttı. En az dört yanıt kuralı yalnız duyarlılık olarak incelendi. Eksiklik mekanizması belirlenmedi; madde ataması yapılmadı. Bulgular bu 100 kaydı betimler.”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Birleştirme ve bilgi sınırı

A=99, C=98, ortak=97 geçerli puan. Inner 97; A solda left 99; outer 100 satırdır.
Outer'da A/C geçerli 99/98; ortak analiz 97'dir. Ortak A ortalaması 4.554639,
bütün A puanlarında 4.563636; değişim kayıt kümesindendir.
Eksik nedenleri bu arşivde bilinmiyor; reddetme/uygulanamazlık nedeni uydurmayın.
Atama modeli analiz sorusu ve değişken türleriyle uyumlu planlanmalıdır.
Eğitim/test merkezleme örneği ayrı kurgudur; gerçek BFI tahmin modeli veya
başarım ölçüsü yoktur. Yeni R/SPSS/MICE/FIML yürütmesi yapılmadı.
