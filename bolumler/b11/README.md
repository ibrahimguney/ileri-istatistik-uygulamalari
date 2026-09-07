# Bölüm 11 — Varyans Analizi (ANOVA)

Bu bölümde **tek yönlü ANOVA, Welch ANOVA, Tukey ve Games–Howell çoklu karşılaştırmaları ile iki faktörlü ANOVA ve etkileşim** aynı tarihsel veri kaynağı üzerinden incelenir.

Amaç yalnızca genel bir F testi hesaplamak değildir. Öğrencinin **genel test ile ikili karşılaştırmaları, klasik ve alternatif varyans modellerini, ana etkiler ile etkileşimi ve farklı çoklu karşılaştırma ailelerini birbirinden ayırabilmesi** hedeflenir.

Bölüm bağımsız çalışır; kitabın veya Bölüm 10 klasörünün dosyaları gerekmez.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- tek yönlü ANOVA'nın araştırma sorusunu ve temel bileşenlerini açıklayabilir,
- gruplar arası, grup içi ve toplam kareler toplamlarını ayırabilir,
- F istatistiğini ve hata serbestlik derecesini hesaplayabilir,
- eta-kare ve omega-kare etki büyüklüklerini yorumlayabilir,
- klasik ANOVA ile Welch ANOVA'nın farklı varyans modellerini temsil ettiğini açıklayabilir,
- anlamlı genel F testinin bütün grup çiftlerinin farklı olduğu anlamına gelmediğini gösterebilir,
- Tukey ve Games–Howell sonuçlarını doğru karşılaştırma ailesi içinde yorumlayabilir,
- iki faktörlü ANOVA'da ana etkiler ile etkileşim hipotezlerini ayırt edebilir,
- kategorik doz modeli ile tek sayısal doğrusal eğim modelinin aynı olmadığını açıklayabilir,
- kısmi eta-kareyi tek yönlü eta-kare ile karıştırmadan yorumlayabilir,
- basit etkileri ayrı p değerlerini karşılaştırarak değil ortak model içinde değerlendirebilir,
- Bonferroni ailesinin kapsamını açıkça tanımlayabilir,
- klasik etkileşim testi ile HC3 duyarlılık sonucunu ayırt edebilir,
- ANOVA sonuçlarını akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` dosyalarını okuyarak faktörleri, düzeyleri, analiz birimini ve veri kaynağını inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki analiz öncesi soruları yanıtlayın.
3. OJ tek yönlü analizini ve kareler toplamı ayrıştırmasını elle veya notebook içinde yeniden üretin.
4. Tukey ve Games–Howell sonuçlarını aynı karşılaştırma ailesi içinde değerlendirin.
5. Tüm 60 kayıtla 2×3 faktöriyel modeli ve uygulama × doz etkileşimini inceleyin.
6. OJ−VC basit etkilerini ortak modelin hata varyansı altında değerlendirin.
7. VC grubundaki bağımsız uygulamayı tamamlayın.
8. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
9. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla sonuçları bilimsel rapor diline dönüştürün.

## Veri ve araştırma yapısı

Uygulamada tarihsel `ToothGrowth` verisinin yerel kopyası kullanılmaktadır. Kaynak, lisans, değişken ve seçim ayrıntıları [VERI.md](VERI.md) dosyasındadır.

İki faktör vardır:

- **uygulama:** OJ ve VC,
- **doz:** 0.5, 1 ve 2.

Böylece 2×3 = 6 hücre vardır ve her hücrede 10 ayrı hayvan kaydı bulunur. Toplam 60 kayıt aynı hayvanların tekrarlı ölçümleri değildir.

## Analiz planı

### 1. OJ — tek yönlü ANOVA

Yalnız OJ uygulamasındaki 30 kayıt kullanılarak üç kategorik doz ortalaması karşılaştırılır.

İncelenen başlıca sonuçlar:

- klasik tek yönlü ANOVA,
- eta-kare ve omega-kare,
- Tukey üç-çift ailesi,
- Welch ANOVA,
- Games–Howell üç-çift ailesi.

Welch/Games–Howell analizi klasik ANOVA/Tukey sonucunun otomatik yerine geçen bir yöntem seçme düğmesi değildir. Levene veya Brown–Forsythe testine bakılarak mekanik yöntem seçimi yapılmaz; alternatif varyans modeli ayrıca değerlendirilir.

### 2. VC — bağımsız öğrenci uygulaması

VC grubundaki 30 kayıt için aynı kavramsal analiz yeniden yapılır. OJ grubunun hata varyansı VC analizine taşınmaz. Bu çalışma bağımsız dış doğrulama değildir.

### 3. Tüm veri — 2×3 faktöriyel ANOVA

Tüm 60 kayıtla uygulama, kategorik doz ve uygulama × doz etkileşimi modellenir.

Etkileşim hipotezi kabaca şu soruyu sınar:

> OJ−VC farkı üç doz düzeyinde aynı mıdır?

Bu soru OJ ve VC için ayrı ayrı hesaplanan genel F testlerinin p değerlerini karşılaştırmakla yanıtlanmaz.

### 4. Üç OJ−VC karşılaştırması

Üç doz düzeyindeki OJ−VC farkları ortak faktöriyel modelin `MSE` ve `df=54` değerleri kullanılarak değerlendirilir. Bu üç karşılaştırma tek bir Bonferroni ailesi olarak ele alınır.

Bu aile bölümde yapılan bütün testleri kapsamaz.

## Python ile çalıştırma

Öğrenci deposunun kökünden:

```sh
python bolumler/b11/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

Gerekli paket sürümleri `requirements.txt` dosyasında kayıtlıdır. Kod ağdan veri indirmez, bağımlılık kurmaz ve başka bölümün dosyalarına erişmez. Notebook için ayrıca Jupyter ortamı gerekir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b11/analiz.R
```

kullanılabilir. R içinde etkileşimli çalışırken bölüm klasöründen `source("analiz.R")` çağrılabilir.

R betiği yerel verileri kurulu `datasets::ToothGrowth` ile de karşılaştırır. Ancak bu dağıtım hazırlanırken **R betiği çalıştırılarak doğrulanmamıştır**. R betiği HC3 denetimini ve Python grafiklerini üretmez.

Bu öğrenci paketinde SPSS komut dosyası veya doğrulanmış SPSS çıktısı bulunmamaktadır. Python/R sonuçlarını SPSS sonucu olarak sunmayın.

## Analizde inceleyeceğiniz temel kavramlar

- tek yönlü ANOVA,
- kareler toplamı ayrıştırması,
- F testi,
- eta-kare ve omega-kare,
- Welch ANOVA,
- Tukey HSD,
- Games–Howell,
- çoklu karşılaştırma ailesi,
- iki faktörlü ANOVA,
- ana etkiler,
- uygulama × doz etkileşimi,
- kısmi eta-kare,
- basit etkiler,
- Bonferroni düzeltmesi,
- kategorik ve sayısal faktör modellemesi,
- HC3 ortak Wald F duyarlılığı,
- artık ve varyans tanıları.

## Üretilen dosyalar

`sonuclar/` klasöründe başlıca:

- `ozet.json`,
- `hucreler.csv`,
- `faktoriyel_anova.csv`,
- `basit_etkiler.csv`,
- `ikili_OJ.csv`,
- `ikili_VC.csv`,
- `analiz_veri.csv`

üretilir.

`grafikler/` klasöründe:

- `b11-oj-tukey.pdf`,
- `b11-etkilesim.pdf`,
- `b11-tanilar.pdf`

oluşturulur.

CSV ve JSON dosyalarındaki sayılar tam hassasiyetlidir; yuvarlama raporlama aşamasında yapılır. Ham `ToothGrowth.csv` değiştirilmez. Kaynak açıklaması ve `GPL-2.txt` dosyasını ham veriyle birlikte koruyun.

## Sonuçları yorumlarken dikkat

Bu bölümde özellikle şu hatalardan kaçının:

- Anlamlı genel F testini “bütün grup çiftleri birbirinden farklıdır” şeklinde yorumlamayın.
- Levene/Brown–Forsythe testinde büyük p değerini eş varyansın kanıtı saymayın.
- Tukey ve Games–Howell sonuçlarını hangi varyans modeli ve karşılaştırma ailesine ait olduklarını belirtmeden karıştırmayın.
- Dozu kategorik üç düzeyli faktör olarak modellemekle tek sayısal doğrusal eğim kullanmayı aynı model saymayın.
- Faktöriyel modelde toplam `df=59` değerini hata serbestlik derecesi olarak kullanmayın; altı hücreli tam modelde hata `df=54`'tür.
- Kısmi eta-kare değerlerini toplayarak toplam açıklanan varyans oranı elde etmeye çalışmayın.
- OJ ve VC'nin ayrı p değerlerini karşılaştırmayı etkileşim testi olarak sunmayın.
- HC3 ortak Wald F sonucunu “robust ANOVA kareler toplamı” olarak adlandırmayın.
- Doz 2'de sıfıra yakın farkı eşdeğerlik kanıtı olarak yorumlamayın.
- Bonferroni düzeltmesinin yalnız tanımlanan üç OJ−VC karşılaştırma ailesine ait olduğunu unutmayın.
- Tarihsel öğretim verisinden doğrudan nedensellik, insanlara genelleme veya tedavi önerisi çıkarmayın.

## Akademik raporlama

Tek yönlü ve faktöriyel ANOVA, çoklu karşılaştırmalar, etkileşim ve etki büyüklüklerinin nasıl bilimsel biçimde raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

Raporunuzda yalnız p değerini değil; **tasarımı, grup/hücre büyüklüklerini, F ve serbestlik derecelerini, etki büyüklüğünü, karşılaştırma ailesini, ham farkları, eşzamanlı güven aralıklarını, tanıları ve sınırlılıkları** birlikte belirtin.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Hangi kontrollerin gerçekten çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir. Yerel hash denetimi dosya bütünlüğünü destekler; uzak kaynak doğrulaması veya araştırma tasarımının bağımsız doğrulanması anlamına gelmez.