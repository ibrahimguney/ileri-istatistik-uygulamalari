# Bölüm 11 — Kaynak ve analiz sözleşmesi

## Kaynak ve kapsam
Yeni veya sentetik gözlem eklenmez. Kitabın Bölüm 10 uygulamasındaki
`kaynak/ToothGrowth.csv` bu öğrenci bölümüne baytları değiştirilmeden kopyalanır.
Böylece dağıtım paketi tek başına çalışır. Kitabın analiz kaynağı değiştirilmez.
R kaynak metninden tarayıcıyla CSV aktarımı 5 Eylül 2026 tarihinde yapılmıştır;
bu aktarım geçmişi yerel kaynaktan korunur, burada yeni uzak doğrulama yapılmaz.
CSV düzeni, başlıklar ve kaynak_satir yerel aktarımın parçasıdır; CSV özgün R
kaynak dosyasının bayt kopyası değildir. Sayısal gözlemler üretilmemiştir.

R kaynak dağıtımının mevcut GNU GPL v2 bildirimi `GPL-2.txt` içinde korunur.
R COPYING kaydı: https://raw.githubusercontent.com/wch/r-source/trunk/COPYING .
Bu kaynaklara UCI/CC BY lisansı taşınmaz; bütün kitap veya öğrenci deposuna
burada yeni lisans atanmaz. Özgün makalenin şekilleri/metni kopyalanmaz;
analiz ve grafikler kitap için yeniden hesaplanmıştır.

R sözlüğü: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/ToothGrowth.html
R kaynak metni: https://raw.githubusercontent.com/wch/r-source/trunk/src/library/datasets/data/ToothGrowth.R
R belgesinde kaynak: Bliss (1952), The Statistics of Bioassay; ilişkili çalışma:
Crampton (1947), The Journal of Nutrition 33(5), 491–504,
DOI 10.1093/jn/33.5.491. Kaynak sözlüğü 5 Eylül 2026'da tekrar incelendi.
Özgün makalenin ham kayıtları ve uzak CSV/R metni otomatik karşılaştırılmadı.
Yerel hash eşleşmesi bu doğrulamaların yerine geçmez.

60 ayrı hayvan, OJ/VC × 0.5/1/2 mg/gün, her hücrede 10 kayıt vardır.
len odontoblast uzunluğudur; kısa kaynakta birim belirtilmediğinden mikrometre
varsayılmaz. supp: OJ portakal suyu, VC askorbik asit; dose mg/gündür.
Doz burada üç düzeyli faktördür, tek doğrusal eğim değildir. Tekrarlı ölçüm yoktur.
Kafes, randomizasyon ve ortak çevre yapısı kısa dosyada doğrulanmadığından
bağımsızlık varsayımı ayrıca tartışılır. İnsanlara veya tedaviye genellenmez.

CSV sonundaki satır sonu uygulama tarafından kaldırılmış olabilir. Bu öğrenci betiği CRLF satır sonlarını LF yapıp
son LF karakterlerini tek LF olarak normalize ederek eski veri kopyasının hash'iyle
karşılaştırır; kaynak baytlarını değiştirmez. Hücre veya sayı değişikliği kabul edilmez.
Normalize SHA-256: 654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3.
Gerçekte okunan baytların hash'i JSON'da ayrıca kaydedilir.

## Önceden tanımlanmış öğretim analizleri
- OJ, 30 kayıt: üç doz için klasik ANOVA + üç çiftin Tukey ailesi.
- Aynı OJ kayıtları: Welch + Games–Howell alternatif varyans modeli; yöntemler
  Levene sonucuna göre otomatik değiştirilmez. İkisi aynı verinin alternatifidir.
- VC, 30 kayıt: öğrencinin bağımsız çözeceği aynı analizler.
- Bütün 60 kayıt: iki sabit faktör, uygulama × doz etkileşimli OLS modeli.
- Üç dozun OJ−VC basit etkileri: tüm modelin ortak MSE'si ve 54 sd ile,
  tek üç-karşılaştırmalı ailede Bonferroni p ve en az %95 eşzamanlı aralıklar.
  Bunlar Bölüm 10'daki ayrı Welch testlerinin aralıkları değildir.
- Etkileşim için HC3 kovaryanslı iki kısıtlı Wald F duyarlılığı, yaklaşık F(2,54).
  Bu, klasik SS oranı değildir; yeni bir robust kareler toplamı gibi sunulmaz.

Tukey ve Games–Howell için aynı üç çift ailesi tanımlıdır; Games–Howell'in aile
kontrolü yaklaşık ve varsayımlara bağlıdır. OJ, VC ve üç basit etki ailesi ayrı
öğretim sorularıdır. Bütün bölümde yapılan testlerin toplam hata oranını .05'te
kontrol ettiğimiz iddia edilmez. Bu bir yeni deneyin önkaydı değildir.

## Hesaplar ve doğrulamalar
SSG+SSW=SST; klasik F elle/SciPy; Welch elle/SciPy/Statsmodels ile doğrulanır.
Tukey ve Games–Howell için öğrencilendirilmiş açıklık q, farklar, aralıklar ve
p değerleri elle/SciPy ile karşılaştırılır; Tukey ayrıca Statsmodels ile denetlenir.
Faktöriyel kareler toplamları hücre ortalamalarından ayrıca hesaplanır. Dengeli ve
tam 2×3 tasarımda Sum kodlamalı Tip II/III sonuçları karşılaştırılır; bu eşitlik
boş hücrelere veya dengesiz tasarımlara genellenmez. HC3 matris hesabı ve ortak
etkileşim karşıtlığı iki ayrı yoldan doğrulanır. Satır sırasının sonuçları
etkilemediği ve kaynak baytlarının değişmediği denetlenir.

Eta-kare OJ tek yönlü modelinin SSG/SST oranıdır. Omega-kare aynı klasik modele
ait düzeltmeli tahmindir. Faktöriyel tabloda kısmi eta-kare SS_etki/(SS_etki+SSE)
kullanılır; üç kısmi eta-kare toplanmaz. Etki büyüklükleri için GA üretilmez.

## Çalıştırma sınırı
Python hesapları için DOGRULAMA.json kaydına bakın. R kurulu veri tablolarıyla
karşılaştırma yalnız hazırlanmış kodtur; R/SPSS bu ortamda çalıştırılmamıştır.
Bootstrap, permütasyon, tekrarlı ölçüm ve etki büyüklüğü güven aralığı bu pakette
üretilmez. Yeni veri toplama, kayıp doldurma veya ana analizden silme yoktur.