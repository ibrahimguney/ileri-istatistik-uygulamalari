# B17 — SPSS ANCOVA çalıştırma

[b17-analiz.sps](b17-analiz.sps) dosyası veriyi kendi içinde taşır; CSV yolu ve PROCESS gerekmez.

1. SPSS 29'da dosyayı açın ve **Run > All** seçin.
2. İlk çapraz tabloda her supp×dose hücresinde 10, toplam N=60 olmalı.
3. Ortak eğim modelinde beklenen F değerleri: grup F=11.446768 (p=.001301), doz F=123.988774 (p<.001).
4. Ayrı eğimler modelinde etkileşim testi F(1,56)=5.333483, p=.024631.
5. Altı hücre modeliyle doğrusal biçim testi F(2,54)=8.399425, p=.000667.
6. Hücre modelinde OJ−VC farkları (Bonferroni aile aralığı): doz .5: 5.25 [1.237,9.263], doz 1: 5.93 [1.917,9.943], doz 2: −.08 [−4.093,3.933].
7. Çıktıyı B17_SPSS_YYYY-AA-GG.spv adıyla kaydedin; SPSS sürümünü ve uyarıları not edin.

 dose işlem öncesi ön-test değildir; bu örnek klasik ön-test ANCOVA tasarımı olarak yorumlanmamalıdır. HC3, Levene ve tek-kayıt dışlama bu dosyada yoktur. Gerçek SPSS yürütmesi yapılmadan doğrulama kaydını başarılı olarak işaretlemeyin. Ayrıntılı yöntem ve sınırlamalar README, VERI.md ve spss-kontrol-listesi.md'dedir.
