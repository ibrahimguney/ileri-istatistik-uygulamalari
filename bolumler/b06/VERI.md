# Bölüm 6 — Kaynak ve hesap sözleşmesi

Cortez, P. (2008). Student Performance [Veri seti]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T. Kaynak lisansı CC BY 4.0.
Özgün çalışma: Cortez, P. ve Silva, A. (2008). Using data mining to predict
secondary school student performance. FUBUTEC 2008.

- Kaynak: https://archive.ics.uci.edu/dataset/320/student+performance
- Lisans: https://creativecommons.org/licenses/by/4.0/

Tam Portekizce dersi verisi 649 kayıt; yerel alıntı ilk 80 kaydın okul/G1/G3
alanları ve ek kaynak_satir dizinidir. Kitabın tarayıcıdan aktarılmış CSV'si,
aynı baytlarla veri.csv adıyla sunulur. Değerler değiştirilmez. Tümü GP okuludur;
sıfır not geçerlidir, eksik yoktur. Sonuçlar makalenin bulguları değil, yerel
alıntıda kitap için yapılan hesaplardır. Uzak kaynakla otomatik hücre
karşılaştırması bu pakette yapılmaz. Kod/açıklamalara yeni lisans atanmadı;
veri lisansı bütün depoya genişletilmez. Kitabın tam metni dağıtılmaz.

[Sözlük CSV](veri_sozlugu.csv): kaynak_satir aktarım sırası, school okul kodu,
G1 birinci dönem, G3 yıl sonu notu (0–20). Sıra kişi kimliği değildir.

- Kaynak 1–60: ana analiz, n=60.
- Ana kümeden yalnız kaynak 1 hariç: n=59 duyarlılık; silme önerisi değil.
- Kaynak 61–80: n=20 bağımsız çözüm etkinliği; yeni doğrulama örneklemi değil.
- Ham CSV: bütün 80 kayıt; hiçbir kayıt silinmez veya doldurulmaz.

Normalize LF SHA-256:
`51dcab9aeaa121123dd28a00156d4dfa398c38eecad69bd5699ae4cea03e5ee9`.
CRLF→LF ve sonda tek satır sonu yalnız hash denetiminde kullanılır, dosyaya yazılmaz.
Hash uzak kaynak doğrulaması veya temsili örnekleme kanıtı değildir.

Pearson merkezlenmiş çapraz çarpımlarla, Spearman bağlı notlara ortalama sıra
verilip sıraların Pearson korelasyonuyla kontrol edilir. Bağsız kısa sıra farkı
formülü kullanılmaz. Pearson r² aynı kayıtlarda sabit terimli tek yordayıcılı OLS
R²'sine eşittir; Spearman karesi ham notlardaki açıklanan varyans değildir.

Pearson testi/Fisher aralığı model koşullarına bağlıdır. Permütasyon bağımsızlık
altında eşleşmelerin değiştirilebilirliğini gerektirir; kümelenme/seçimi çözmez.
İlk-sıra tek okul alıntısı rastgele veya temsili değildir. Korelasyon, dönem
farkı, bireysel gelişme veya nedensellik kanıtı olarak sunulmaz.