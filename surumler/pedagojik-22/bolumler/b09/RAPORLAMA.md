# Bölüm 9 — raporlama

## Bölümdeki örnek ve açıklama

> **Rapor kontrolü:** veri kaynağı ve birimi; analiz birimi/eşleme; hipotez; örneklem ve sıfır sayısı; bağ kuralı; istatistiğin yönü; kesin/yaklaşık yöntem ve süreklilik düzeltmesi; karşılaştırma ailesi; yön/etki özeti; varsa uygun güven aralığı; sınırlılıklar. P değeri yöntemini veya etki büyüklüğü aralığının yokluğunu gizlemeyin.

Örnek: “1 mg/gün dozunda OJ ve VC için 10’ar ayrı hayvanın uzunlukları karşılaştırıldı. OJ için $U=88.5$, tüm 184756 etiket atamasına dayanan iki yönlü $p=.002230$ ve örneklem üstünlük tahmini $\widehat A=.885$ bulundu. OJ daha yüksek değer eğilimi gösterdi; sonuç doğrudan medyan farkı veya nedensel başarı olasılığı olarak yorumlanmadı.”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 13: belirsizlik ve hedef

Doz1'de A=.885, BM t=4.302937, sd11.835244, yaklaşık p=.001059; klasik tam
U p=.002230 ile farklı kalibrasyonlar. En küçük p seçilmez. Grup-içi hayvan
bootstrap (20000, seed20261025) yaklaşık percentile aralığı [.690,1.000];
2415 tekrar1. Üst sınır kusursuz evren ayrımı veya kesin %95 kapsama değildir.
100 ikili kazanım bağımsız sayılmaz.

Sleep10 çift: sıfır dışlanan işaret testinde9/9 pozitif, koşullu p=.00390625.
Medyan1.3 saat; sıfır dahil10 farkla sıra aralığı[.8,2.4]. Sürekli medyan
modelinde kapsama .978515625; kesikli kayıtlar için eşitlik değil tutuculuk
söz konusu olabilir. Bu aralık eşli fark medyanınındır, marjinal medyan farkının değil.
W/V aralıkları, BCa ve öğrencilendirilmiş permütasyon yapılmadı.
