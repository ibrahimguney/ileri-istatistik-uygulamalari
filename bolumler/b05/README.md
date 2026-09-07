# Bölüm 5 — Güç Analizi ve Örneklem Planlama

Bu bölümde güç analizi, yazılıma bir etki büyüklüğü girip tek bir örneklem sayısı elde etme işlemi olarak değil, **araştırma tasarımının varsayımlarını sayısallaştıran bir planlama süreci** olarak ele alınır.

Temel soru şudur:

> Hangi etkiyi, hangi testle, hangi alfa düzeyinde, hangi güç hedefiyle ve hangi analiz birimiyle saptamak istiyoruz?

Ana eğitim puanı senaryosu varsayımsaldır. `sleep` arşivi yalnız tarihsel fark standart sapmasını örneklemek için kullanılır; ana eğitim puanı senaryosunun verisi değildir. Yeni pilot veri veya rastgele örneklem simülasyonu üretilmez. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- güç, Tip II hata ve etki büyüklüğü arasındaki ilişkiyi açıklayabilir,
- örneklem planlamasının girdilerini analizden önce tanımlayabilir,
- ham fark `Δ`, standart sapma `σ` ve standartlaştırılmış etki `d` arasındaki ilişkiyi kurabilir,
- grup başına n ile toplam kişi sayısını ayırabilir,
- minimum tamsayı örneklem büyüklüğünü `n−1` kontrolüyle doğrulayabilir,
- etki büyüklüğü, alfa ve hedef gücün örneklem büyüklüğüne etkisini inceleyebilir,
- çoklu karşılaştırma düzeltmesinin örneklem gereksinimine etkisini gösterebilir,
- tek yönlü planın yalnız önceden gerekçelendirilmiş alternatif için kullanılabileceğini açıklayabilir,
- eşit ve eşit olmayan grup tahsislerini ayırabilir,
- bağımsız grup `d` ile eşli tasarım `d_z` değerini karıştırmadan planlama yapabilir,
- kayıp için beklenen sayı düzeltmesi ile hedef tutulma olasılığını ayırabilir,
- sabit n için güç ve minimum saptanabilir etkiyi hesaplayabilir,
- Fisher-z korelasyon planlamasının yaklaşık olduğunu açıklayabilir,
- güç hedefi ile güven aralığı hassasiyet hedefini ayırabilir,
- basit tasarım etkisi hesabının tam çok düzeyli güç analizi olmadığını açıklayabilir,
- güç analizini varsayımları ve sınırlılıklarıyla akademik olarak raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) dosyasından ana planın hangi girdilerinin varsayımsal olduğunu belirleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki D sorularıyla `Δ`, `σ`, `d`, α, yön, güç ve tahsisi analizden önce yazın.
3. Ana iki bağımsız grup planında minimum tamsayı n'yi bulun.
4. `n−1` ve `n` güçlerini karşılaştırarak minimaliteyi doğrulayın.
5. Farklı etki büyüklüğü, güç ve alfa senaryolarını karşılaştırın.
6. Kayıp düzeltmesinde beklenen sayı ile olasılık hedefini ayrı hesaplayın.
7. Sabit n için güç ve minimum saptanabilir etkiyi bulun.
8. Eşli tasarım, 2:1 tahsis, korelasyon ve hassasiyet planlarını ayrı yöntemler olarak inceleyin.
9. Tarihsel `sleep` yayılımını yalnız duyarlılık girdisi olarak kullanın.
10. Sonuçları [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
11. [RAPORLAMA.md](RAPORLAMA.md) ile planınızı akademik yöntem diline dönüştürün.

## Varsayımsal ana plan

Ana öğretim senaryosu:

| Girdi | Değer |
|---|---:|
| Öngörülen ham fark `Δ` | 5 eğitim puanı |
| Ortak `σ` | 10 puan |
| Standartlaştırılmış etki `d=Δ/σ` | .50 |
| Alfa | .05 |
| Test yönü | İki yönlü |
| Hedef güç | .80 |
| Tahsis | 1:1 |
| Tasarım | İki bağımsız grup |
| n birimi | Analiz edilebilir kişi, grup başına |

Bu değerler gözlenmiş bir eğitim çalışmasının sonuçları değildir. `Δ=5` öğretim girdisidir; klinik/eğitsel önem standardı olarak sunulmaz. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

## Ana örneklem büyüklüğü sonucu

Sürekli çözüm:

`n = 63.765611`

kişidir ve bu sayı **grup başınadır**.

Örneklem büyüklüğü tamsayı olmalıdır. Minimum çözüm:

- `n=64` kişi/grup,
- toplam `128` analiz edilebilir kişi.

Minimalite kontrolü:

- `n=63` için güç = `.795168`,
- `n=64` için güç = `.801460`.

Dolayısıyla 63 hedef `.80` güce ulaşmazken 64 ulaşır. Sürekli çözümü `63`e aşağı yuvarlamak doğru değildir. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

## “64 kişi yeterlidir” neden yanlış?

Ana planda `n` **grup başına kişi sayısıdır**.

Bu nedenle:

- 64 kişi/grup,
- 2 grup,
- toplam 128 analiz edilebilir kişi

gerekir.

`n` birimi her güç analizinde açıkça belirtilmelidir.

## Etki büyüklüğü duyarlılığı

Ana planın diğer girdileri sabit tutulduğunda:

| d | Minimum n / grup |
|---:|---:|
| .20 | 394 |
| .30 | 176 |
| .50 | 64 |
| .80 | 26 |

Daha küçük etkileri aynı güçle saptamak daha büyük örneklem gerektirir. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Bu tablo “gerçek etki şu kadardır” demez; farklı planlama varsayımlarının örneklem sonucuna etkisini gösterir.

## Hedef güç değişirse

`d=.5`, α=.05 ve iki yönlü eşit tahsis korunurken:

- güç `.80` → `64` kişi/grup,
- güç `.90` → `86` kişi/grup.

Daha yüksek saptama olasılığı hedeflemek daha fazla örneklem gerektirir.

## Alfa değişirse

`d=.5`, güç=.80 ve iki yönlü plan için:

- α=.05 → `64` kişi/grup,
- α=.01 → `96` kişi/grup.

Daha katı Tip I hata eşiği, diğer koşullar sabitken örneklem gereksinimini artırır. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

## Çoklu karşılaştırma planı

Üç karşılaştırma için basit Bonferroni planında:

`α* = .05/3`

kullanıldığında minimum:

`86 kişi/grup`

bulunur.

Bu sayı, belirli Bonferroni planının sonucudur; bütün çoklu test stratejileri için evrensel örneklem büyüklüğü değildir.

## Tek yönlü plan

`d=.5`, güç=.80 ve α=.05 için önceden seçilmiş doğru yönlü tek taraflı alternatifte:

`51 kişi/grup`

yeterlidir. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Ancak bu avantaj sonuç görüldükten sonra tek yönlü teste geçmek için kullanılamaz. Test yönü araştırma sorusuna göre **analizden önce** belirlenmelidir.

Yanlış yöndeki tek yönlü alternatif aynı gücü vermez.

## Eşit olmayan tahsis

2:1 tahsis senaryosunda `d=.5` için minimum:

- `n1=48`,
- `n2=96`,
- toplam `144` kişi.

Bu sonuç 1:1 tasarımdaki 128 toplam kişiden farklıdır.

Tahsis oranı, maliyet ve erişim gerekçeleriyle değiştirilebilir; fakat aynı toplam n'nin aynı gücü vereceği varsayılmamalıdır.

## Eşli tasarım farklı bir problemdir

Eşli tasarımda `d_z=.5` için:

`34 tam çift/kişi`

gerekir. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Buradaki n:

- grup başına kişi değildir,
- 68 bağımsız kişi değildir,
- `34` tam eşleşmiş kişidir.

Bağımsız grup Cohen d'si ile eşli tasarım `d_z` aynı standartlaştırıcıyı kullanmaz.

## Tarihsel sleep yayılımının sınırlı rolü

`sleep` verisindeki 10 eşleşmiş kişiden tarihsel fark standart sapması:

`s_D=1.229995`

olarak hesaplanır. Bu değer **yeni pilot veri değildir**. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Varsayımsal `Δ=.5` saat için:

- `σ_D=1` → `d_z=.5` → `34` tam çift,
- tarihsel `s_D=1.229995` → `d_z≈.406506` → `50` tam çift,
- `σ_D=1.5` → `d_z≈.3333` → `73` tam çift.

Bu karşılaştırma yayılım varsayımının planı ne kadar değiştirebildiğini gösterir. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Tarihsel gözlenen ortalama fark `1.58` saat yeni planın beklenen etkisi olarak alınmaz.

## Eşli tasarımda korelasyonun rolü

Eşit marjinal `σ=1` ve `Δ=.5` varsayımında, iki ölçüm arasındaki korelasyon farkların varyansını etkiler.

Sonuçlar:

| Varsayılan ρ | Gerekli tam çift |
|---:|---:|
| .30 | 46 |
| .50 | 34 |
| .70 | 21 |

Daha yüksek eşleşme korelasyonu bu özel modelde fark puanlarının varyansını azaltır ve gereken tam çift sayısını düşürür. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Bu değerler planlama varsayımlarıdır; gelecekteki korelasyonun garantisi değildir.

## Kayıp: beklenen sayı ile olasılığı ayırın

Ana analiz için 64 kişi/grup gerekmektedir. `%15` kayıp varsayımı altında basit düzeltme:

`ceil(64/.85)=76`

kişi/grup verir.

Ancak 76 kişi davet etmek **her grupta kesin 64 kişi kalacağı anlamına gelmez**.

Bağımsız `%85` tutulma modeli altında 76 kişi/grup ile iki grupta da en az 64 kişinin kalma olasılığı yalnız:

`.422777`

olur. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Bu, “beklenen sayı” ile “hedefe ulaşma olasılığı” arasındaki önemli farktır.

## %90 tutulma hedefi

Aynı bağımsız Bernoulli tutulma modelinde, iki grupta da en az 64 kişinin kalması için en az `.90` olasılık hedeflenirse:

- 81 kişi/grup → `.896208`,
- 82 kişi/grup → `.935473`.

Dolayısıyla minimum `82 kişi/grup` gerekir. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Bu da garanti değildir; belirli kayıp modelindeki olasılık hesabıdır.

## Sabit n için güç

Eğer yalnız:

`40 kişi/grup`

alınabiliyorsa ve `d=.5` ise güç:

`.598147`

olur.

Dolayısıyla örneklem büyüklüğü sabit olduğunda soru tersine çevrilebilir:

> Bu tasarım hangi etkileri makul güçle saptayabilir?

## Minimum saptanabilir etki

`n=40/grup`, α=.05 ve iki yönlü test için `.80` güce ulaşan minimum standartlaştırılmış etki yaklaşık:

`d=.634299`.

Bu değer “gerçek etki en az .634 olacaktır” anlamına gelmez. Belirli plan koşullarında `.80` güce karşılık gelen etki büyüklüğüdür. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

## Korelasyon için Fisher-z yaklaşımı

Varsayımsal `ρ=.30` için Fisher-z normal yaklaşımı:

- `n=84` → güç `.795517`,
- `n=85` → güç `.800346`.

Dolayısıyla minimum yaklaşık `n=85`'tir. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Bu:

- tam korelasyon güç hesabı değildir,
- G*Power doğrulaması değildir,
- bütün korelasyon tasarımlarına otomatik uygulanmaz.

## Güç ile hassasiyet aynı hedef değildir

Yerine konmuş `σ` kullanılarak iki bağımsız grup ortalama farkı için %95 t-aralığının planlanan yarı genişliği `.2σ` hedeflenirse:

- `n=193/grup` → yarı genişlik `.200150σ`,
- `n=194/grup` → `.199630σ`.

Dolayısıyla minimum `194 kişi/grup` olur. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Ana güç planındaki `n=64/grup` için aynı planlanan yarı genişlik yaklaşık `.349836σ`'dır.

Güç:

> H₀'dan belirli bir uzaklıktaki etkiyi saptama olasılığı

ile ilgilenirken, hassasiyet:

> tahminin ne kadar dar bir belirsizlik aralığıyla elde edilmesinin planlandığı

ile ilgilenir.

Gerçekleşen güven aralığı genişliği önceden garanti edilmez.

## Küme tasarım etkisi örneği

Kurgusal:

- ortalama küme büyüklüğü `m=20`,
- `ICC=.05`

için basit tasarım etkisi:

`DE = 1 + (20−1)×.05 = 1.95`.

Bu yalnız öğretici bir tasarım etkisi hesabıdır. **Tam çok düzeyli/küme güç analizi yapılmamıştır.** [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Örneklem sayısını yalnız DE ile çarpmak; küme sayısı, dengesizlik, ICC belirsizliği, analiz modeli ve küçük küme düzeltmeleri gibi konuları çözmez.

## Hesap yöntemleri ve doğrulama sınırı

Ana model:

- iki bağımsız grup,
- normal model,
- eşit varyans,
- sabit örneklem,
- pooled Student t testi,
- iki yönlü α=.05,
- eşit tahsis

üzerine kuruludur.

Güç iki yönlü merkezsiz F kuyruğundan (`T²` özdeşliği) hesaplanır; merkezsiz t ve `statsmodels` aynı Python ortamında ek denetim olarak kullanılır. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

Bu denetimler bağımsız yazılım doğrulaması değildir.

## Python ile çalıştırma

Depo kökünden:

```sh
python -m pip install -r bolumler/b05/requirements.txt
python bolumler/b05/analiz.py
```

Bölüm klasöründen:

```sh
python analiz.py
```

kullanabilirsiniz.

`veri.csv` aynı klasörde kalmalıdır. Bu bölüm SciPy yanında `statsmodels` kullanır; kendi `requirements.txt` dosyasını kullanın.

`python -O` kullanmayın; hesap denetimleri devre dışı kalabilir.

`calisma.ipynb` içindeki `None` alanları öğrenci görevleridir. Jupyter analiz betiğinin zorunlu bağımlılığı değildir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b05/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

Temel R yeterlidir. R kodu sonuçları ekrana basar ve Python'un bütün çıktı dosyalarını üretmez. İki yönlü hesaplarda `strict=TRUE` kullanır.

**R bu paket hazırlanırken çalıştırılmamıştır.**

Bu pakette:

- çalıştırılmış G*Power doğrulaması,
- SPSS syntax,
- SPSS çıktısı

yoktur.

Yazılım adının geçmesi bağımsız doğrulama anlamına gelmez. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

## Üretilen dosyalar

- `sonuclar/ozet.json`
- `senaryolar.csv`
- `pilot_yayilim.csv`
- `esli_rho.csv`
- `kayip.csv`
- `guc_egrileri.csv`
- `grafikler/b05-guc-planlama.pdf`

`pilot_yayilim.csv` adı kitapla uyumluluk için korunur; içeriği yeni pilot veri değil, tarihsel yayılım ve varsayımsal alternatif yayılım senaryolarıdır.

Hesaplar deterministiktir; rastgele veri üretilmez. Ham CSV değiştirilmez.

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- `64`ü toplam kişi sayısı diye yazmayın; ana planda 64/grup, toplam 128'dir.
- Sürekli çözümü aşağı yuvarlamayın; minimum tamsayıyı güçle doğrulayın.
- Gözlenen etkiyi gelecekteki gerçek etki diye kabul etmeyin.
- `sleep` verisini ana eğitim puanı senaryosunun verisi veya yeni pilot diye sunmayın.
- Tarihsel 1.58 saat farkı yeni çalışmanın beklenen etkisi olarak kullanmayın.
- Bağımsız grup `d` ile eşli `d_z`yi karıştırmayın.
- 34 tam çifti 34/grup veya 68 bağımsız kişi diye yorumlamayın.
- Sonuca bakıp tek yönlü plana geçmeyin.
- `%15` kayıp düzeltmesini kesin yeterlilik garantisi saymayın.
- 76/grup ile her grupta 64 kişinin kesin kalacağını söylemeyin.
- Minimum saptanabilir etkiyi gerçek etkinin alt sınırı saymayın.
- Fisher-z sonucunu tam korelasyon gücü veya G*Power doğrulaması diye sunmayın.
- Güç hedefi ile güven aralığı hassasiyet hedefini aynı şey saymayın.
- Basit DE hesabını tam çok düzeyli güç analizi diye sunmayın.
- Daha büyük n'nin temsil, ölçüm geçerliği veya nedenselliği otomatik sağladığını varsaymayın.

## Bu bölümde yapılmayan analizler

Bu pakette:

- yeni pilot çalışma,
- rastgele örneklem simülasyonu,
- G*Power çalıştırması,
- tam korelasyon güç analizi,
- tam çok düzeyli/küme güç analizi,
- eksik veri mekanizması modeli,
- önkayıt

yapılmamıştır.

Bunları yapılmış gibi raporlamayın. [Kitap, Bölüm 5](../../KITAP_ESLESMESI.md)

## Akademik raporlama

Örneklem planının yöntem bölümünde nasıl sunulabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi bir güç analizi raporu yalnız “G*Power ile 64 kişi bulundu” demez. En azından **tasarım, test, test yönü, etki girdisi ve kaynağı, α, hedef güç, tahsis, n birimi, minimum tamsayı kontrolü, kayıp varsayımı ve duyarlılık analizlerini** açıkça belirtir.

## Çözüm ve teknik doğrulama

Önce görevleri kendiniz çözün. Ardından [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.

Gerçekte hangi yazılımların çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir.

Bu bölümün ana öğrenme zinciri:

**Araştırma hedefi → Tasarım → Etki varsayımı → α → Güç → Tahsis → Minimum n → Kayıp → Duyarlılık → Hassasiyet → Sınırlılık → Akademik raporlama**