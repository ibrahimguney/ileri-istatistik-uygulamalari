# B18 — Görevler

Önce `VERI.md` dosyasını okuyun. Ana analiz ile öğretim amaçlı karşı örnekleri birbirine karıştırmayın.

## D1–D3 — Çalıştırmadan önce

**D1.** Uyku kaynağında neden 20 satır varken analiz birimi 10 kişidir? `group` değişkenini neden bağımsız grup değişkeni olarak kullanmıyoruz?

**D2.** `FILTER OFF` ile ham kaynağı yeniden okumak arasındaki farkı açıklayın. Gerçek bir araştırmada gerekli tasarım ağırlığının neden gelişigüzel kapatılamayacağını yazın.

**D3.** Hazırlanmış bir `.sps` dosyasının tek başına SPSS'in çalıştırıldığını veya bütün yeni veri hatalarının yakalandığını neden kanıtlamadığını açıklayın.

## G1–G4 — Rehberli çalışma

**G1.** Uyku farkları için `n`, ortalama ve standart sapmadan SH, t, sd ve %95 güven aralığını yeniden kurun. Paired Samples Correlations tablosundaki p değerinin neden fark testinin p değeri olmadığını açıklayın.

**G2.** ToothGrowth 1 mg/gün verisinde Welch ve Student modellerinin neden burada aynı t'yi fakat farklı sd, p ve güven aralığını verdiğini açıklayın. Levene `p=0.149126` hangi sonucu kanıtlamaz?

**G3.** `ID<=5` filtresi için kullanılan farkları, n'yi, ortalamayı ve t sonucunu bulun. Filtre kapatıldığında hangi n ve ortalamanın geri gelmesi gerekir? Data View'da 10 satır görmek neden yeterli kontrol değildir?

**G4.** Kurgusal çalışma kopyasında ID1'in `kosul2`, ID2'nin `kosul1` hücresini eksik yapın. Her koşuldaki geçerli sayı, tam çift sayısı ve yeni fark ortalamasını bulun. `fark` sütununun neden yeniden hesaplanması gerektiğini açıklayın.

## B1–B3 — Bağımsız çalışma

**B1.** Fark yönünü `kosul1-kosul2` yaparsanız ortalama fark, t, iki yönlü p ve güven aralığı nasıl değişir?

**B2.** Her çifte frekans ağırlığı 2 verildiğinde ortalama değişmeden SH'nin neden küçüldüğünü gösterin. Mekanik `n=20` neden 20 bağımsız kişi değildir?

**B3.** İki yazılım aynı ham ortalamaları fakat farklı güven aralıklarını veriyor. Kayıt/eksik kümesi, etkin durum, fark yönü, eşli-bağımsız tasarım, Student-Welch seçimi, güven düzeyi, yön ve çoklu düzeltme bakımından bir denetim sırası yazın.

## H1 — Hatalı raporu onarma

Aşağıdaki iddiaların her birini birim, hipotez, yöntem ve yürütme kanıtı bakımından düzeltin:

> “Uyku dosyasında 20 satır olduğu için bağımsız t kullandık. Korelasyon tablosundaki .005965 artışın p'sidir. Levene .149 olduğundan varyanslar kanıtla eşittir; daha küçük p verdiği için Student satırını seçtik. Ağırlık 2 ile 20 kişiye ulaştık. İki hücreyi gizledik ama eski fark sütununu kullandık. Syntax dosyası bulunduğu için SPSS çalıştırılmıştır.”

## P1 — Denetlenebilir analiz teslimi

Bir ana analiz seçin ve tek teslim paketinde şunları bağlayın: veri kaynağı/sözlüğü, bağımsız birim, oturum ayarları, eksik/dışlama kuralları, tam syntax, kullanılan n, tahmin ve güven aralığı, etki tanımı, kısa akademik rapor, sınırlılıklar ve yeniden üretim kaydı. Karşı örnekleri ana sonuçtan ayrı tutun.

**Rubrik:** kaynak/birim 20, içe aktarma/durum 25, model/hesap 25, yorum/sınırlılık 20, yeniden üretim 10 puan.
