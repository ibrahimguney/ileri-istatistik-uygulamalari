# Bölüm 4 — Hipotez testi

## Gerçek veri ve sınırı
Kaynak `../b06-parametrik-testler/kaynak/sleep.csv`: R datasets/sleep aktarımı.
https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/sleep.html
20 ölçüm satırı aynı 10 kişiye aittir; iki bağımsız grup değildir. `extra` kontrole
göre uyku artışı (saat), `group` koşul, `ID` eşleştirme anahtarıdır. Sıfır ve negatif
extra değerleri korunur. Koşul2−koşul1 farkı ana analizdir.
Bölüm 6'nın kaynak/aktarım ve GPL bildirimleri geçerlidir; dosya değiştirilmez.
Veri, R `datasets::sleep` ile birebir aynıdır. Rastgeleleştirme,
uygulama sırası, taşıma etkisi ve temsil ayrıntıları bu kısa arşivden doğrulanmaz.
Bu bir yöntem öğretimidir, tedavi önerisi veya yeni deney değildir.
Normalize LF SHA-256: `adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e`.
Hash yalnız arşivin değişmediğini denetler. Erişim: 6 Eylül 2026.

## Çalıştırma
Kitap kökünden `python uygulamalar/b04-hipotez-testi/analiz.py`.
numpy/scipy/pandas/matplotlib kullanılır; ağ bağlantısı gerekmez.
R betiği aynı gerçek kayıtları ID'den eşler ve aynı t testini verir. R ve NumPy aynı tohum sayısıyla aynı rastgele diziyi üretmek zorunda değildir;
R simülasyonu Python'un tam sayılarıyla değil kuramsal hedef ve MC hatasıyla kıyaslanır.
SPSS betiği Python'un oluşturduğu `esli_veri.csv` dosyasını okur; iki yönlü t testi
ve %95 aralık içindir. Betikler SPSS/R ile çalıştırılmış doğrulama sayılmaz.

## Hesaplar
n=10, fark ortalaması1.58, s=1.229995, SH=.388959; t(9)=4.062128,
iki yönlü p=.002832890, GA95=[.700114,2.459886]. Standartlaştırıcı fark s'si;
d_z=1.284558, d_z*sqrt(10)=t. d_z için güven aralığı hesaplanmaz.
Sağ kuyruk p=.001416445; sol kuyruk p=.998583555. Bunlar farklı alternatiflerdir;
en küçüğü seçilmez. Ana iki yönlü tercih tarihsel veride öğretim sözleşmesidir,
gerçekten önkayıt yapılmış olduğu iddia edilmez. Ölçüm sırası terslenirse t ve
fark işaret değiştirir, iki yönlü p değişmez, aralık uçları terslenir.
Klasik sonlu-örneklem t çıkarımı bağımsız kişiler ve normal fark modeli altında
tamdır. Küçük n ve 4.6 saatlik fark incelenir, hiçbir kişi silinmez. Varsayımlar
kanıtlanmış, bootstrap/permutasyon ya da normallik testi yapılmış değildir.

## Gerçek veriden ayrı öğretim kurguları
- Ders özeti n16, ortalama74.5, s8, referans70: t=2.25, sd15,
  sağ p=.019944, iki p=.039888, GA95=[70.237101,78.762899].
- Dolum özeti n25, ortalama496, s10, referans500: t=−2, sd24,
  iki p=.056940, sol p=.028470, sağ p=.971530, GA95=[491.872203,500.127797].
- İleri1 özeti n36, ortalama52, s12, referans50: t=1, sd35, iki p=.324174.
Bu özetler için yeni ham gözlemler üretilmez; formüller doğrudan özetlerden hesaplanır.
- Kurgusal tablo [[20,30],[30,20]]: n100, beklenen her hücre25,
  düzeltmesiz Pearson ki-kare4, sd1, p=.045500, Cramer V=.2.
  Yates veya Fisher sonucu diye etiketlenmez; yöntem p'ye göre değiştirilmez.

## İdeal model simülasyonu
Tohum20260906, her koşulda20000 tekrar, her tekrarda25 bağımsız normal gözlem,
sigma1. İki yönlü t testi mu0=0, alfa.05. d0 için1004 red, oran.0502,
MC SH=.001544; gerçek ortalama kapsama.9498. Veriden işaret seçip tek kuyruk
p raporlayan yanlış kural aynı d0 örneklerinde.1016 red verir (kuramsal.10).
d.5 için13334 red, oran.6667; kuramsal noncentral-t gücü.669708, MC SH=.003333.
Gerçek ortalama.5'i kapsayan aralıkların oranı.9474; sıfırı içermeme oranı ise güçtür.
Bu simülasyon uyku verisinin gerçek gücü veya varsayım doğrulaması değildir.
Gözlenen etkiyi kullanarak post-hoc güç raporu yapılmaz. Sabit n, yön ve durdurma
kuralı vardır. 20 bağımsız doğru H0 testinde aile hatası1−.95^20=.641514;
bağımlı testlerde bu eşitlik varsayılmaz.

## Dosyalar ve denetimler
- `esli_veri.csv`: ID, koşul1, koşul2, fark; 10 gerçek çift.
- `sonuclar/testler.csv`: ana ve kurgusal özet testler.
- `sonuclar/kurgu_capraz.csv`: yalnız kurgusal kategori sayıları.
- `sonuclar/simulasyon.csv`, `ozet.json`: sayılar, tohum, sürümler.
- `../../assets_figures/b04-test-mantigi.pdf`: ham farklar, t dağılımı ve kuyruklar.
ID/koşul benzersizliği, tam çift sayısı, karıştırılmış satır sırasının etkisizliği,
eksik/çiftlenmiş kayıt reddi, elle t ve SciPy eşli/tek örneklem t eşitliği,
aralıklar, işaret dönüşümü, varyans-kovaryans özdeşliği ve kuramsal güç kontrol edilir.
Her simülasyon tekrarında iki yönlü red ile sıfırın GA95 dışında olması eşleştirilir.

Yöntem belgeleri:
https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.nct.html
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html
https://stat.ethz.ch/R-manual/R-devel/library/stats/html/t.test.html