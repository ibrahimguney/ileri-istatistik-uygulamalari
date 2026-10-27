# Bölüm 10 — raporlama

## Bölümdeki örnek ve açıklama

Korelasyon bulguları raporlanırken yalnızca katsayı verilmemelidir. Sağlıklı bir raporda aşağıdaki unsurlar yer almalıdır:

- korelasyon katsayısı ($r$ ya da $r_s$),

- örneklem büyüklüğü ($n$),

- anlamlılık düzeyi ya da $p$-değeri,

- ilişkinin yönü ve gücü,

- gerekiyorsa belirlilik katsayısı ($r^2$),

- nedensellik iddiasından kaçınan bağlamsal yorum.

Örneğin raporlama şu biçimde yapılabilir: “Çalışma süresi ile sınav puanı arasında pozitif yönlü ve güçlü bir ilişki bulunmuştur ($r=.96$, $n=6$, $p<.01$).”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 14: aynı satır bootstrap

60 GP kaydı, ilk satır/sıfır not korunur. 20000 ortak satır çekilişi, seed20261025;
Spearman sıraları her tekrarda yenilenir. Yaklaşık percentile aralıkları Pearson
[.6216,.9091], Spearman[.7064,.9092], rs−r[-.0865,.2018]. Ayrı marjinal
aralıklar; ortak %95 kapsama yok. Aynı kişilerde farklı iki hedef bağımsız
Pearson fark testine sokulmaz; sıfırı içeren fark eşdeğerlik kanıtı değildir.

İlk satırın çekilip çekilmemesine göre koşullu bootstrap dağılımları betimseldir;
yeni öğrenci grupları veya kayıt silme gerekçesi değildir. iid satırlar varsayımı
sıralı tek okul alt kümesinde doğrulanmış sayılmaz. Küme-bootstrap/BCa/kapsama
simülasyonu yapılmadı. Korelasyon uyum, sıfır korelasyon bağımsızlık değildir.
Yeni ek yalnız Python; R/SPSS ve Bland–Altman/ICC analizi yok.
