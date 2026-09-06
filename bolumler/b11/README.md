# Bölüm 11 — Varyans Analizi (ANOVA)

Tek yönlü ANOVA, Welch, Tukey/Games–Howell ve iki faktörlü etkileşim için
bağımsız öğrenci paketi. **Toplu aktarım için yerel olarak hazırlanmıştır;
GitHub'da yayımlandığı iddia edilmez.** Kitap veya Bölüm 10 klasörü gerekmez.

## Çalışma sırası
1. `VERI.md` ve `veri_sozlugu.csv`: kaynak, birim, faktörler ve aileler.
2. `GOREVLER.md`: kitaptaki D/G/B/H/P etkinlikleriyle uyumlu görevler.
3. `calisma.ipynb`: önce boş hesapları tamamlayın, sonra referans hücrelerini çalıştırın.
4. `COZUMLER.md` ve `beklenen.json`: gerekçeli yorum ve sayısal kontrol.
5. `DOGRULAMA.json`: yapılmış denetimler ve çalıştırılmamış yazılımlar.

## Çalıştırma
Python ve requirements.txt içindeki paketlerin kurulu olduğu ortamda, öğrenci deposu kökünden:

```sh
python bolumler/b11/analiz.py
```

Bölüm klasöründe `python analiz.py` de kullanılabilir. Kod ağdan veri indirmez,
bağımlılık kurmaz ve başka bölümün dosyalarına erişmez. requirements.txt bu
ortamda kullanılan sürümleri kaydeder. Notebook için ayrıca Jupyter ortamı gerekir.

R kuruluysa `Rscript bolumler/b11/analiz.R` kullanılabilir; R içinde etkileşimli
çalışmada bölüm dizininden `source("analiz.R")` çağırın. R, yerel verileri kurulu
`datasets::ToothGrowth` ile de karşılaştırır. **R bu ortamda çalıştırılmadı**;
karşılaştırmanın geçtiği iddia edilmez. R betiği HC3 denetimi ve Python grafiklerini
üretmez. SPSS komut dosyası bu öğrenci paketinde yoktur; kitapta yöntem/menü açıklamaları vardır.

## Analiz planı
- OJ: 30 hayvanda üç doz; klasik ANOVA ve üç çiftlik Tukey ailesi.
- Aynı OJ kayıtları: Welch/Games–Howell alternatif varyans modeli; Levene ile otomatik seçim yok.
- VC: 30 kayıtta bağımsız çözüm; OJ hata varyansı taşınmaz.
- Tüm 60 kayıt: iki sabit faktör, uygulama × kategorik doz etkileşimli model.
- Üç dozun OJ−VC farkları: ortak MSE ve df=54; tek ailede Bonferroni p/aralıkları.
- HC3 ortak etkileşim testi: yaklaşık Wald F duyarlılığı; robust kareler toplamı değildir.

OJ, VC ve basit etkiler **ayrı öğretim aileleridir**. Tüm bölüm için tek .05 aile
hatası kontrolü iddia edilmez. Tekrarlı ölçüm yoktur; 60 ayrı hayvan kaydı vardır.
Bölüm 10'da aynı kaynağın kullanılması bağımsız tekrar araştırması değildir.

## Çıktılar
`sonuclar/`: ozet.json, hucreler.csv, faktoriyel_anova.csv, basit_etkiler.csv,
ikili_OJ.csv, ikili_VC.csv, analiz_veri.csv.

`grafikler/`: b11-oj-tukey.pdf, b11-etkilesim.pdf, b11-tanilar.pdf.

CSV/JSON tablolarındaki sayılar tam hassasiyetlidir; yuvarlama yalnız rapordadır.
Bu çıktılar yeniden üretilir; ZIP'te bulunmaz. ToothGrowth.csv değiştirilmez.
Kaynak açıklaması ve GPL-2.txt ham CSV ile birlikte korunmalıdır.

## Temel kontrol
OJ F(2,27)=31.441504; eta²=.699610, omega²=.669905.
Genel test anlamlıyken OJ 2−1 Tukey aralığı [−.800395,7.520395] sıfırı içerir.
Etkileşim F(2,54)=4.106991, p=.021860; HC3 F=3.522846, p=.036471.
Bu bulgular tasarımın doğrulanması, nedensellik veya tedavi önerisi değildir.