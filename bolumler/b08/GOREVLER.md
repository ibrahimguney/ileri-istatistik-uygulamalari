# Bölüm 8 — Öğrenci görevleri

## D — Başlamadan önce

1. G3 ortalaması ile G3≥14 olasılığı hangi farklı soruları yanıtlar?
2. Yaşı neden 16'da merkezliyoruz? Katsayıların ve sabitin yorumunu açıklayın.
3. 14 not eşiğini 0.50 olasılık eşiğinden ayırın. Hedef14 yordayıcı yapılırsa ne olur?

## G — Rehberli hesap

1. İlk 60 kayıtta OLS ve logit kurun. 16 yaş/G1=12 için ortalama ve olasılığı bulun.
2. Düzeltilmiş R², ΔR² ve ek yaş F testini bulun; F=t_age² özdeşliğini denetleyin.
3. G1'in kısmi eğimini yaşa göre artıklaştırmayla bulun; VIF ve HC3 SH'yi hesaplayın.
4. G1 logit katsayısı ve Wald aralığının üstelini alın. 16 yaşta G1=12→13
   değişimi için OR ile olasılık farkını karşılaştırın.

## B — Sabit modeli sonraki 20 kayda uygulayın

1. Modeli yeniden kurmadan kaynak 80 için ortalama G3 ve olay olasılığı hesaplayın.
2. 0.50 eşiğinde TP/FN/TN/FP, duyarlılık, özgüllük ve doğruluğu bulun.
   Herkesi 0 sayan sınıflandırıcının doğruluğuyla karşılaştırın.
3. AUC'yi çift karşılaştırması ve ortalama sıralarla; Brier'i kare hatalarla
   hesaplayın. Sabit olasılık referansında neden eğitimdeki 19/60 kullanılıyor?
4. 0.3/0.5/0.7 eşiklerinin hata türlerini karşılaştırın. 0.5 ve 0.7'nin aynı
   sınıfları vermesi mümkün mü? Aynı aktarım kümesinde en iyi eşik seçilebilir mi?
5. İlk kaydı yalnız duyarlılık kopyasında çıkarıp OLS/logit katsayılarını karşılaştırın.

## H — Hatalı raporu düzeltin

“VIF=1.23, bütün varsayımlar sağlandı. R² artınca yaşın nedensel etkisi
kanıtlandı. OR=5.22, olasılık 5.22 katıdır. 14 resmî geçme sınırıdır.
0.50 her zaman en iyi eşiktir. Eğitim doğruluğu %88; yeni okullarda
kullanılabilir. Aktarımda eşiği değiştirip aynı grubu yeniden bağımsız test ettik.”
Her iddiayı yöntem, veri veya kullanım sınırıyla düzeltin.

## P — Teslim

Kaynak/sözlük, çalıştırılabilir kod/notebook, iki grafik ve kısa rapor.
Rapor: iki hedef, katsayı/OR aralıkları, HC3/klasik ayrımı, ilk kayıt etkisi,
eğitim/aktarım ölçüleri, eşik kuralları ve sınırlılıklar.
Rubrik: kaynak/hedef 20, hesap/OR 30, tanı/aktarım 25, yorum 15, yeniden üretim 10.
R/SPSS çalıştırılmadıysa bunları yapılmış doğrulama olarak yazmayın.