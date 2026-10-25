# Bölüm 10 — gerçek verilerle parametrik olmayan testler

## Kaynak zinciri ve sınırlar
- `../b06-parametrik-testler/kaynak/sleep.csv`: 20 satır, 10 ID, iki ilaç altında kontrole göre ek uyku (saat). Kaynak: R datasets `sleep`; aktarım bilgileri ve lisans metni Bölüm 6 paketinde.
- `../b06-parametrik-testler/kaynak/ToothGrowth.csv`: 60 ayrı kobay, OJ/VC × 0.5/1/2 mg/gün, hücre başına 10 kayıt. Uzunluğun fiziksel birimi kısa kaynakta belirtilmiyor. Kaynak: R datasets, Bliss (1952); ilişkili çalışma Crampton (1947).
- `kaynak/rounding-times.csv`: R stats `friedman.test` belgesindeki RoundingTimes kod matrisinin 22 satırı/66 değeri, sıra korunarak elle aktarılmıştır. Blok numarası tarafımızdan eklenmiştir. Yeni/sentetik ölçüm eklenmez.

Kaynak belgeler (erişim: 5 Eylül 2026):
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
`../b06-parametrik-testler/kaynak/GPL-2.txt` içindedir.

Hash kontrolleri son LF'leri tek LF'ye normalize eder; sayılar veya hücreler değiştirilmez.
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

Etki büyüklükleri nokta tahminidir; güven aralığı üretilmedi. Bölüm 6 ortalama farkı
ve Bölüm 7 Tukey aralıkları bu sıra ölçülerinin aralıkları değildir. Bütün bölümün
birleşik test ailesi için .05 hata kontrolü iddia edilmez. Sonuçlar öğretim içindir.

## Çalıştırma ve doğrulama
Kitap kökünden:
```sh
python uygulamalar/b10-parametrik-olmayan/analiz.py
Rscript uygulamalar/b10-parametrik-olmayan/analiz.R
```
Python: numpy, pandas, scipy (doğrulanan 1.17.0), matplotlib ve statsmodels gerekir.
U/sıra toplamı/çift kazanımı, tüm etiket ve işaret sayımları SciPy ile karşılaştırılır.
Kruskal/Friedman elle bağ düzeltmesiyle denetlenir. Dunn paydasının ortak sıra
örneklem varyansına eşitliği, Holm'un statsmodels ile eşitliği kontrol edilir.
Beklenen frekanslar marjinallerden hesaplanır. ID eşlemesi satır sırasından bağımsızdır.
Kaynak dosyalarının değişmediği doğrulanır.

R betiği yaklaşık testleri, Dunn–Holm'u ve sleep
kesin işaret sayımını verir; U tam permütasyonu ve Friedman Monte Carlo için Python
kullanılır. SPSS betiği temel testleri verir; kesin p, Dunn–Holm veya izleme Holm
sonuçlarını otomatik üretmez. SPSS/R varsayılan U/W/T yönlerini ve süreklilik
seçeneklerini denetlemeden aynı sayıyı beklemeyin.

## Dosyalar
- `sonuclar/ozet.json`: kaynak, tüm sayısal sonuçlar ve sürümler.
- `sonuclar/uyku_farklar.csv`, `dunn_OJ.csv`, `dunn_VC.csv`, `friedman_ikili.csv`.
  Dunn karşılaştırma indeksleri 0/1/2 → 0.5/1/2 mg; Friedman 0/1/2 → Round/Narrow/Wide.
- `uyku_genis.csv`: ID, ilac1, ilac2; `dis_analiz.csv`: orijinal sütunlar + supp_kod
  (OJ1/VC2), dose_kod (0.5→1,1→2,2→3), esik20 (len≥20 için1).
- Kitap kökündeki `assets_figures/b12-sira-ve-fark.pdf`, `b12-friedman.pdf`.

Kontroller: U_OJ88.5, A.885, kesin p.002229968; sleep T0, p.00390625;
OJ H18.505593, p.000095843; Friedman Q11.142857, W.253247, MCp.003120;
Pearson chi2 5.406007, p.02006757, V.300167. Sayısal p yöntemi rapordan çıkarılmamalı.