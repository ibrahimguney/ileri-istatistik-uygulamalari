# Bölüm 5 — Güç ve örneklem planlama

Kitap kökünden `python uygulamalar/b05-guc-analizi/analiz.py` çalıştırılır.
R karşılığı: `Rscript uygulamalar/b05-guc-analizi/analiz.R` (kitap kökünden).
`analiz.sps` IBM SPSS Statistics 27 ve üstündeki POWER MEANS INDEPENDENT komutunu kullanır.
R betiği (`power.t.test`, `pwr`) Python ile aynı örneklem büyüklüklerini ve güçleri verir.

## Hesap sözleşmesi
- Bağımsız, normal, eşit varyanslı iki grup; sabit n, iki yönlü pooled Student testi.
- Ana plan: varsayımsal eğitim puanında Δ=5, σ=10, d=.5, alfa .05, güç .80.
- İki yönlü güç merkezsiz F kuyruğuyla hesaplanır: T² ~ F(1,sd,ncp²).
  Bu özdeşlik büyük ncp'de merkezsiz t kuyruğunun olası sayısal sorununu önler.
  Raporlanan senaryolar ayrıca iki merkezsiz t kuyruğu ve statsmodels ile karşılaştırılır.
- Tamsayı minimumu ve bir önceki n denetlenir; n grup başınadır. Eşli analizde n tam çift/kişidir.
- R'de `strict=TRUE` iki yönlü testin iki ret kuyruğunu da içerir.
- Fisher-z korelasyon planı **normal yaklaşımıdır**, tam korelasyon gücü veya G*Power doğrulaması değildir.
- %15 kayıp için beklenen sayı payı ile iki grupta yeterli kişi kalma olasılığı ayrı hesaplanır.
  Bağımsız Bernoulli tutulma varsayımı gerçek kayıp mekanizmasını doğrulamaz.
- Hassasiyet hesabı σ'yı yerine koyan t-aralık yarı genişliği planıdır; genişlik garantisi değildir.
- Çıktı CSV/JSON'ları ve `assets_figures/b05-guc-planlama.pdf` deterministiktir; simülasyon yoktur.

## Gerçek arşivin sınırlı rolü
Bölüm 6 `kaynak/sleep.csv`: 20 satır, ID ile eşlenmiş 10 kişi, saat birimi.
Yalnız tarihsel fark yayılımı s_D=1.229995 örnek alınır. Yeni pilot/deney değildir.
Δ=.5 saat öğretim girdisidir; klinik önem standardı veya tedavi önerisi değildir.
Kaynak: R datasets sleep belgesi; aktarım ve GPL bildirimi Bölüm 6 klasöründedir.
Normalize LF SHA256: adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e.
Veri, R `datasets::sleep` ile birebir aynıdır; özet dosyanın değişmediğini denetler.
Ham arşiv değiştirilmez, gözlenen büyük etki gerçek plan etkisi diye kullanılmaz.

## Denetimler
Kaynak/eşleme/sıra değişmezliği, t/F/statsmodels uyumu, n−1 minimalite,
merkezi sıfırda güç=alfa, işaret simetrisi ve yanlış tek yön,
güç eğrisi monotonluğu, Fisher-z minimumu, binom eşiği ve geçersiz girdi reddi.
Yüksek n/normal model hesabı temsil, nedensellik, küme tasarımı veya eksik veri çözümü sağlamaz.
Yöntem belgeleri ve erişim tarihi: kitap Bölüm 5 kaynakçası, 6 Eylül 2026.