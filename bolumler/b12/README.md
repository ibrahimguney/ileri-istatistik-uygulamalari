# Bölüm 12 — Parametrik Olmayan Testler

Bu bölümde **Mann–Whitney U, Wilcoxon işaretli sıralar, Kruskal–Wallis, Dunn–Holm, Friedman ve kategorik sayım testleri** farklı veri yapıları üzerinden incelenir.

Amaç parametrik olmayan yöntemleri yalnızca “normallik bozulduğunda kullanılan testler” olarak öğrenmek değildir. Asıl hedef; **analiz birimini, bağımlılık yapısını, sıra ve fark yönünü, bağları, sıfırları, kesin/yaklaşık p hesaplarını ve çoklu karşılaştırma ailelerini doğru tanımlayabilmektir.**

Bölüm bağımsız çalışır; kitabın veya başka bir bölümün klasörlerine ihtiyaç duymaz.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- bağımsız ve eşli veri yapılarını ayırt edebilir,
- Mann–Whitney U istatistiğini sıra toplamlarından hesaplayabilir,
- U'nun yalnızca “medyan testi” olmadığını açıklayabilir,
- üstünlük olasılığı `A` ve sıra-biserial etki büyüklüğünü yorumlayabilir,
- Wilcoxon analizinde sıfır ve bağlı farkların nasıl işlendiğini açıklayabilir,
- kesin işaret sayımı ile normal yaklaşım p değerlerini ayırabilir,
- Kruskal–Wallis H istatistiğini bağ düzeltmesiyle hesaplayabilir,
- Dunn karşılaştırmalarına Holm düzeltmesini uygulayabilir,
- Friedman testinde bağımsız analiz biriminin blok olduğunu belirleyebilir,
- Kendall W etki büyüklüğünü hesaplayabilir,
- Monte Carlo p değerini tam sayım p değerinden ayırabilir,
- Pearson ki-kare, Fisher ve Cramér V sonuçlarını birlikte değerlendirebilir,
- farklı çoklu karşılaştırma ailelerini birbirine karıştırmadan raporlayabilir,
- parametrik olmayan testlerin de varsayım ve tasarım koşulları olduğunu açıklayabilir,
- sonuçları akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` dosyalarını okuyarak kaynakları, analiz birimlerini, bağları ve sıfırları inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki analiz öncesi soruları yanıtlayın.
3. `calisma.ipynb` içindeki boş hesapları tamamlayın.
4. Mann–Whitney U ve Wilcoxon analizlerinde kesin ve yaklaşık p hesaplarını karşılaştırın.
5. OJ ve VC için Kruskal–Wallis ve Dunn–Holm ailelerini ayrı ayrı inceleyin.
6. RoundingTimes verisinde Friedman, Kendall W ve Monte Carlo hesabını değerlendirin.
7. Friedman sonrası eşli karşılaştırmaların ayrı Holm ailesini inceleyin.
8. Kategorik sayım örneğinde Pearson ki-kare, Fisher ve Cramér V sonuçlarını karşılaştırın.
9. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile kontrol edin.
10. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla sonuçları bilimsel rapor diline dönüştürün.

## Veri yapıları

Bu bölümde üç tarihsel veri kaynağının yerel kopyaları kullanılmaktadır.

### Sleep

- 20 ölçüm,
- 10 kişi,
- aynı kişinin iki koşuldaki ölçümleri,
- dolayısıyla eşli veri yapısı.

### ToothGrowth

- 60 ayrı hayvan kaydı,
- OJ ve VC uygulamaları,
- 0.5, 1 ve 2 doz düzeyleri.

Ayrı hayvan kayıtları bulunması bağımsızlığı tek başına kanıtlamaz; özgün kafes, ortak çevre ve atama bilgileri ayrıca önemlidir.

### RoundingTimes

- yayımlanmış kod matrisinden 22 blok,
- her blokta üç koşul,
- toplam 66 hücre değeri.

Bu 66 değer 66 bağımsız kişi değildir. Her hücre iki koşunun ortalamasıdır ve 132 ayrı gözleme çoğaltılmaz. Yerel kaynak notunda açıklamanın 18 oyuncudan, kod matrisinin ise 22 satırdan söz ettiği uyuşmazlık korunarak raporlanmalıdır; özgün deney sayısı bu paket tarafından doğrulanmamıştır.

## Hangi analiz hangi soruya karşılık geliyor?

| Analiz | Yöntem ve kapsam |
|---|---|
| OJ–VC, doz 1 | Mann–Whitney U; süreklilik düzeltmeli normal yaklaşım ve 184756 etiket atamasının tam sayımı |
| Sleep, koşul 2−1 | Wilcoxon; bir sıfır için `wilcox` kuralı ve kalan 9 farkın 512 işaret örüntüsü |
| OJ ve VC dozları | Ayrı Kruskal–Wallis analizleri; her uygulama için ayrı Dunn–Holm üçlü ailesi |
| RoundingTimes | Friedman; ki-kare yaklaşımı ve 99999 rastgele blok içi permütasyon |
| Friedman sonrası | Üç eşli Wilcoxon normal yaklaşımı ve ayrı Holm ailesi |
| `len ≥ 20` tablosu | Düzeltmesiz Pearson ki-kare, iki yönlü Fisher ve Cramér V |

Friedman Monte Carlo hesabında tohum `202612`'dir ve

`p_MC = (b + 1) / (B + 1)`

kullanılır. Bu hesap bütün olası blok permütasyonlarının tam sayımı değildir.

## Python ile çalıştırma

Öğrenci deposunun kökünden:

```sh
python bolumler/b12/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

kullanabilirsiniz.

Gerekli paket sürümleri `requirements.txt` dosyasında kayıtlıdır. Kod veri indirmez ve paket kurmaz. Notebook için ayrıca Jupyter ortamı gerekir. Tam U etiket sayımı ve blok permütasyonları nedeniyle bazı hesaplar anlık olmayabilir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b12/analiz.R
```

kullanılabilir. Etkileşimli R oturumunda bölüm klasöründen `source("analiz.R")` çağrılabilir.

**R betiği bu dağıtım hazırlanırken çalıştırılarak doğrulanmamıştır.** R betiği yaklaşık testleri, Dunn–Holm'u ve sleep verisinin tam işaret sayımını içerir; U'nun bütün etiket atamalarını ve Friedman Monte Carlo hesabını üretmez.

Bu öğrenci paketinde SPSS komut dosyası veya doğrulanmış SPSS çıktısı bulunmamaktadır. Python/R sonuçlarını SPSS sonucu olarak sunmayın.

## Analizde inceleyeceğiniz temel kavramlar

- bağımsız ve eşli tasarım,
- sıra toplamları,
- Mann–Whitney U,
- üstünlük olasılığı,
- sıra-biserial etki büyüklüğü,
- Wilcoxon işaretli sıralar,
- sıfır ve bağlı farklar,
- kesin ve yaklaşık p değerleri,
- Kruskal–Wallis,
- bağ düzeltmesi,
- Dunn karşılaştırmaları,
- Holm düzeltmesi,
- Friedman testi,
- blok yapısı,
- Kendall W,
- Monte Carlo permütasyonu,
- Pearson ki-kare,
- Fisher kesin testi,
- Cramér V,
- çoklu karşılaştırma ailesi.

## Üretilen dosyalar

`sonuclar/` klasöründe başlıca:

- `ozet.json`,
- `uyku_genis.csv`,
- `dis_analiz.csv`,
- `uyku_farklar.csv`,
- `dunn_OJ.csv`,
- `dunn_VC.csv`,
- `friedman_ikili.csv`

üretilir.

`grafikler/` klasöründe:

- `b12-sira-ve-fark.pdf`,
- `b12-friedman.pdf`

oluşturulur.

Dunn karşılaştırma indeksleri `0/1/2 → 0.5/1/2 mg/gün`; Friedman indeksleri `0/1/2 → Round Out/Narrow Angle/Wide Angle` biçimindedir. Fark ve sıra farkı daima ikinci indeks eksi ilk indeks yönündedir.

Ham CSV dosyaları değiştirilmez. Kaynak açıklamalarını ve `GPL-2.txt` dosyasını veri dosyalarıyla birlikte koruyun.

## Sonuçları yorumlarken dikkat

Bu bölümde özellikle şu hatalardan kaçının:

- “Parametrik olmayan testlerin varsayımı yoktur” demeyin.
- Yalnız Shapiro sonucuna bakarak otomatik biçimde parametrik/nonparametrik yöntem seçmeyin.
- Mann–Whitney U'yu koşulsuz olarak yalnız medyanların testi şeklinde yorumlamayın.
- “Kesin p” ifadesini “varsayımsız p” olarak anlamayın.
- Bağlar varken yazılımın `exact` etiketine yöntemi kontrol etmeden güvenmeyin.
- Wilcoxon'da sıfır farkın ham veriden silindiğini söylemeyin; yalnız ilgili sıralama kuralında dışarıda bırakılır.
- Sleep sıra-biserial değerinin 1 olmasını “herkes yarar gördü” şeklinde yorumlamayın; bir sıfır fark vardır ve karşılaştırma yalnız koşul 2−1 farkına aittir.
- Kruskal–Wallis genel testi anlamlı olduğunda bütün çiftleri düzeltmesiz raporlamayın.
- Dunn için her çiftte yeniden sıra üretmeyin; ortak grup sıraları kullanılır.
- Holm düzeltmesini her p değerini yalnızca üçle çarpmakla karıştırmayın; bu Bonferroni yaklaşımıdır.
- Friedman'da 66 hücreyi 66 bağımsız kişi olarak yorumlamayın; bağımsız analiz birimi bloktur.
- Monte Carlo standart hatasını etki büyüklüğü güven aralığı olarak sunmayın.
- Friedman sonrası Wilcoxon p değerlerini Friedman'ın Monte Carlo p değerleriymiş gibi raporlamayın.
- `len ≥ 20` eşiğini resmî veya biyolojik başarı eşiği olarak sunmayın.
- Dozların birleştirildiği kategorik tabloyu doza göre düzeltilmiş etki olarak yorumlamayın.
- Etki büyüklüğü nokta tahminlerini bu pakette üretilmeyen güven aralıklarıyla raporlamayın.

## Akademik raporlama

Mann–Whitney U, Wilcoxon, Kruskal–Wallis/Dunn–Holm, Friedman ve kategorik sayım testlerinin nasıl bilimsel biçimde raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

Raporunuzda yalnız test adı ve p değerini değil; **analiz birimini, bağımlılık yapısını, fark yönünü, bağ/sıfır kuralını, p hesap yöntemini, etki büyüklüğünü, çoklu karşılaştırma ailesini ve sınırlılıkları** birlikte belirtin.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Hangi denetimlerin gerçekten çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir.

Yerel hash eşleşmesi dosya bütünlüğünü destekler; uzak veri doğrulaması veya özgün deney tasarımının doğrulanması anlamına gelmez.