# Bölüm 11 — Aynı not verisinde Pearson ve Spearman

## Ortak veri ve kapsam
Bu paket yeni veri üretmez veya indirmez; Bölüm 12'nin dondurulmuş kaynağını okur:
`../b12-regresyon/kaynak/uci-portekizce-ilk80-notlar.csv`.
İlk 60 kaynak sırası ana analiz, 61–80. sıralar bağımsız çözüm etkinliğidir.
G1 birinci dönem, G3 yıl sonu notudur (0–20). Bütün seçili kayıtlar GP okulundandır.
Sıfır notu dahil hiçbir değer değiştirilmez. Kaynak sıra numarası öğrenci kimliği değildir.

Kaynak: Cortez, P. (2008). Student Performance [Veri seti]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T. CC BY 4.0.
Özgün çalışma: Cortez, P., & Silva, A. (2008). Using data mining to predict
secondary school student performance. FUBUTEC 2008.
Kaynak sayfası: https://archive.ics.uci.edu/dataset/320/student+performance

Tam Portekizce dersi verisi 649 kayıttır; burada yalnızca ilk 80 satırın ilgili
sütunları vardır. Bölüm 12 README'sindeki kaynak doğrulama yönergesi geçerlidir.
Sayısal tutarlılık denetimi örneklem temsiliyetinin yerine geçmez.
Sonuçlar bu kitap için yeniden hesaplanmıştır; makalenin bulguları değildir.

## Çalıştırma
Komutları `03-AdvancedStaticalAppTR` dizininden çalıştırın:

```sh
python uygulamalar/b11-korelasyon/analiz.py
Rscript uygulamalar/b11-korelasyon/analiz.R
```

Python numpy, scipy, pandas ve matplotlib kullanır; yeni paket gerekmez.
R temel paketleri kullanır. SPSS'te aynı dizinden analiz.sps dosyasını çalıştırın.
SPSS betiği TEMPORARY seçimleriyle ana/duyarlılık/aktarım gruplarını ayrı hesaplar;
kaynak dosyasını değiştirmez. R betiği Python ile aynı katsayıları verir.

Python çıktıları:
- sonuclar/ozet.json: katsayılar, Fisher aralığı, test yöntemleri ve sürümler.
- sonuclar/siralar.csv: 60 kaydın bağlı değerlere ortalama sıra verilmiş hali.
- sonuclar/duyarlilik.csv: 60 ayrı birini-dışarıda-bırakma karşılaştırması.
- assets_figures/b06-uci-korelasyon.pdf: ham notlar ve sıralar grafiği (kitap kökünde).

## Beklenen sonuçlar
| Veri | n | Pearson r | Spearman rs |
|---|---:|---:|---:|
| Ana alt küme | 60 | 0.746612792 | 0.831085662 |
| Kaynak sıra 1 hariç | 59 | 0.865833531 | 0.826699998 |
| Aktarım (61–80) | 20 | 0.627307114 | 0.570535504 |

Ana Pearson için klasik t(58)=8.547100; p=7.46694e-12;
yaklaşık Fisher %95 GA=[0.607944246, 0.841082238].
r²=0.557430662, Bölüm 12'de aynı verinin sabit terimli OLS R²'sine eşittir.
Spearman'ın karesi, ham notlardaki açıklanan varyans olarak yorumlanmaz.

## Sıralar ve test ayrımı
Spearman katsayısı, iki değişkenin ortalama sıralarının Pearson korelasyonudur.
Bağlı notlar bulunduğu için bağsız veriye ait kısa sıra farkı formülü kullanılmaz.
Spearman için SciPy/R'nin yaklaşık p-değeri çıktıda açıkça asimptotik diye etiketlenir;
bu değer kesin küçük örneklem testi olarak sunulmaz.

İleri etkinlik: seed=202606, 19999 bağımsız rastgele G3-sıra permütasyonu,
mutlak katsayıyla iki yönlü uçluk; p=(uç sayısı+1)/(19999+1).
Python çalıştırmasında uç sayısı 0, Monte Carlo p=0.00005 bulunur. Bu sıfır
olasılık veya tam kesin test değildir; seçilen tekrar sayısının çözünürlük sınırıdır.
R ve NumPy'nin aynı seed sayısı aynı permütasyon dizisini garanti etmez.
SPSS betiği bu Monte Carlo adımını gerçekleştirmez; yazılımların p-değerlerini
ancak aynı test yöntemi kullanıldığında karşılaştırın.

Pearson'ın klasik testi ve Fisher aralığı model koşullarına bağlıdır; sıralı
tek okul alt kümesinde normal model, bağımsız gözlem ve temsil kanıtlanmış değildir.
Permütasyon bağımsızlık altında eşleşmelerin değiştirilebilirliğini gerektirir;
kümelenmeyi ve seçilim sorununu gidermez. Önce grafik ve gözlem etkisi, sonra
katsayı ve çıkarım değerlendirilir. İlk kaydı çıkarmak ana analiz kararı değildir.

## Denetimler
Pearson merkezlenmiş çarpımlarla ve NumPy ile; Spearman SciPy, pandas ortalama
sıraları ve sıraların Pearson korelasyonuyla; Fisher aralığı elle formülle;
permütasyonların ilk beşi doğrudan yeniden sıralamayla kontrol edilir.
Bölüm 12'nin ozet.json dosyası varsa kaynak hash'i, n, R² ve eğim eşleşmesi de
zorunludur. Hash karşılaştırmasında yalnızca dosya sonundaki satır sonu farkı
tolere edilir; güncel ham dosya hash’i ayrıca kaydedilir. İlk 60 kayıt, Bölüm 12
not_basari.csv dosyasıyla da hücre hücre karşılaştırılır. Kaynak dosyasının işlem
sonunda değişmediği denetlenir.