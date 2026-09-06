# Bölüm 12 — Kaynak ve analiz sözleşmesi

## Kaynak zinciri ve sınırlar
- `sleep.csv`: 20 satır, 10 ID, iki ilaç altında kontrole göre ek uyku (saat). Kaynak: R datasets `sleep`; Bölüm 10 kaynak kopyası ve lisans bildirimi bu pakette korunur.
- `ToothGrowth.csv`: 60 ayrı kobay, OJ/VC × 0.5/1/2 mg/gün, hücre başına 10 kayıt. Uzunluğun fiziksel birimi kısa kaynakta belirtilmiyor. Kaynak: R datasets, Bliss (1952); ilişkili çalışma Crampton (1947).
- `rounding-times.csv`: R stats `friedman.test` belgesindeki RoundingTimes kod matrisinin 22 satırı/66 değeri, sıra korunarak elle aktarılmıştır. Blok numarası tarafımızdan eklenmiştir. Yeni/sentetik ölçüm eklenmez.

Kaynaklar 5 Eylül 2026'da tarayıcıdan incelendi:
https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/sleep.html
https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/friedman.test.html

Son belgenin açıklama yorumunda 18 oyuncu, kodunda ise 22 satır vardır. Bu paket
22 satırlık kod örneğinin yeniden analizidir; özgün deney örneklemi ayrıca doğrulanmadı.
Belge Hollander ve Wolfe (1973), s.140 ve devamına atıf yapar. Her hücre iki koşunun
ortalama süresidir; iki ayrı tekrar olarak çoğaltılmaz. Süre birimi kısa açıklamadan
ayrıca doğrulanmadığı için grafiklerde kaynak birimi denir. Deney sırası, randomizasyon,
özgün kitap/ham kayıtlar ve uzak veri dosyaları otomatik doğrulanmadı.
R kod örneğinin kaynak/lisans bağlamı R projesidir; mevcut GPL-2 metni
`GPL-2.txt` içindedir.

Öğrenci sürümünün hash kontrolleri CRLF → LF ve son LF'leri tek LF'ye normalize eder; sayılar veya hücreler değiştirilmez.
RoundingTimes normalize SHA-256:
`b286d277d7784cdcb0e4916f1240d2ad03ffd7f6b18a9f456ea2183458f3d869`.
Ortak iki kaynağın normalize hash'leri önceki bölümdeki kopyalarla karşılaştırılır.
Ham hash'ler JSON'dadır. Yerel bütünlük, özgün araştırmaya karşı doğrulama değildir.

## Tanımlanmış analizler
1. ToothGrowth yalnız 1 mg/gün: OJ ilk grup, VC ikinci. Bağlı ortalama sıralarla U,
   süreklilik düzeltmeli normal yaklaşım ve bütün 184756 etiket atamasının iki yönlü
   sayımı. İki yönlü kesin p, küçük kuyruğun iki katıdır (en çok 1).
2. Sleep ID ile eşleme: ilaç2−ilaç1 farkı bir ondalığa yuvarlanır; `wilcox` kuralıyla
   bir sıfır dışlanır. Dokuz farkın 512 işaret örüntüsü sayılır. Bu sayım simetrik fark
   yokluk modeli altında geçerlidir. Sıra-biserial katsayının paydası sıfır olmayan sıralardır.
3. OJ üç doz: bağ-düzeltilmiş Kruskal–Wallis ve ortak 30 sıralı Dunn z testleri.
   Üç çift için tek Holm ailesi; bağımsız öğrenci etkinliğinde VC için ayrı aile.
4. RoundingTimes: 22×3 tam blok, bağ-düzeltilmiş Friedman ve Kendall W.
   Tohum 202612, 99999 blok içi rastgele koşul permütasyonu, `(b+1)/(B+1)` p değeri.
   Bu bir tam sayım değildir. Üç eşleştirilmiş Wilcoxon normal yaklaşımına ayrı Holm
   ailesi uygulanır; sıfır ve süreklilik kuralları açıktır. Farklar iki ondalıktır.
   Monte Carlo blok değiştirilebilirliğine; ikili Wilcoxon ayrıca fark simetrisine dayanır.
5. ToothGrowth tüm60: len≥20 öğretim eşiği; resmi/biyolojik/klinik başarı eşiği değil.
   2×2 Pearson düzeltmesiz ki-kare, Cramér V ve Fisher iki yönlü karşılaştırması.
   Dozlar birleştirilir; tablo doz etkisini/etkileşimi kontrol eden model değildir.

Etki büyüklükleri nokta tahminidir; güven aralığı üretilmedi. Bölüm10 ortalama farkı
ve Bölüm11 Tukey aralıkları bu sıra ölçülerinin aralıkları değildir. Bütün bölümün
birleşik test ailesi için .05 hata kontrolü iddia edilmez. Sonuçlar öğretim içindir.

## Bu öğrenci kopyası
Üç yerel CSV ve GPL-2.txt baytları değiştirilmeden kopyalanır. İlk iki CSV,
kitabın Bölüm 10 uygulamasından; üçüncüsü Bölüm 12 kaynak klasöründendir.
CSV başlıkları/sıra alanları aktarım düzenidir; dosyalar özgün R kaynak metninin
bayt kopyası değildir. Önceki kaynak inceleme tarihi korunur; bu paketleme
sırasında uzak belge veya özgün ham kayıt yeniden doğrulanmaz.

R kaynak dağıtımının mevcut GNU GPL v2 bildirimi GPL-2.txt içinde korunmuştur.
R COPYING kaydı: https://raw.githubusercontent.com/wch/r-source/trunk/COPYING .
Bu kaynaklara UCI/CC BY lisansı taşınmaz; bütün kitap veya öğrenci deposuna
burada yeni lisans atanmaz. Özgün makalelerin metin/şekilleri kopyalanmaz;
grafikler yerel yeniden analizin çıktılarıdır.

sleep için negatif ve sıfır ölçümler korunur. Bir sıfır yalnız işaretli sıra
hesabının wilcox kuralı gereği dışarıda kalır, ham kişiyi arşivden silmez.
Bir ondalık/iki ondalık fark hesabı, kaynak duyarlılığı ve sayısal bağlar için
belirlenmiştir; daha küçük p aramak için ayarlanmaz.

Doz 1 U karşılaştırması ortak dağılım yokluğunda etiket değiştirilebilirliğine;
Wilcoxon tam işaret sayımı simetrik fark yokluk modeline dayanır. Blok içi
Friedman permütasyonu bloklar arası bağımsızlık ve blok içi değiştirilebilirlik
varsayımlarını kaldırmaz. Her hücreyi bağımsız kişi saymak doğru değildir.
R/SPSS bu ortamda çalıştırılmamıştır. RoundingTimes kaynak notundaki 18/22
uyuşmazlığı giderilmiş gibi sunulmaz. Veri doldurma, yeni gözlem veya ana
analizden hata gerekçesiyle silme yapılmaz.