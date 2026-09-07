# Bölüm 4 — Hipotez Testi

Bu bölümde hipotez testi yalnız “p değeri hesaplama” işlemi olarak değil, **araştırma sorusu → tasarım → analiz birimi → hipotez → test istatistiği → belirsizlik → etki büyüklüğü → karar → yorum sınırı** zinciri içinde ele alınır.

Uygulamada üç bilgi türü kesin biçimde ayrılır:

1. **Gerçek eşleşmiş veri:** `sleep` verisindeki 10 kişi ve iki koşul.
2. **Kurgusal örnekler:** yalnız verilen özet istatistikler ve 2×2 tablo.
3. **İdeal model simülasyonu:** açık tohum ve normal modelle oluşturulan yapay tekrarlar.

Bu üç kaynak birbirine karıştırılmamalıdır. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- gözlem satırı ile bağımsız analiz birimini ayırabilir,
- eşleşmiş tasarımda ID anahtarının önemini açıklayabilir,
- fark yönünü analizden önce tanımlayabilir,
- sıfır ve alternatif hipotezleri açıkça yazabilir,
- iki yönlü ve tek yönlü testlerin farklı araştırma sorularına yanıt verdiğini açıklayabilir,
- eşleşmiş t testini fark puanları üzerinden yeniden kurabilir,
- standart hata, t istatistiği, serbestlik derecesi ve p değerini yorumlayabilir,
- %95 güven aralığını nokta tahminiyle birlikte raporlayabilir,
- eşleşmiş tasarım için `d_z` etki büyüklüğünü hesaplayabilir,
- `t=d_z√n` ilişkisini doğrulayabilir,
- p değerinin ne olmadığını açıklayabilir,
- reddetmemenin eşdeğerlik kanıtı olmadığını ayırt edebilir,
- Tip I hata, güç ve güven aralığı kapsamasını simülasyonla inceleyebilir,
- Monte Carlo hatasını raporlayabilir,
- çoklu testlerde aile hata oranının neden büyüdüğünü gösterebilir,
- gerçek veri, kurgu ve simülasyon sonuçlarını akademik olarak ayrı raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) dosyasını okuyarak gözlem birimini ve eşleştirme yapısını belirleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki D sorularında fark yönünü, hipotezleri ve α düzeyini hesaplamadan önce yazın.
3. ID üzerinden 10 eşleşmiş çifti oluşturun.
4. `koşul2 − koşul1` farklarını hesaplayın.
5. Ortalama fark, standart sapma ve standart hatayı bulun.
6. Eşleşmiş t testi, %95 güven aralığı ve `d_z` değerini hesaplayın.
7. Fark yönünü ters çevirerek işaret, p değeri ve güven aralığındaki değişimi inceleyin.
8. Kurgusal tek örneklem ve 2×2 tablo görevlerini gerçek veriden ayrı çözün.
9. Simülasyonda Tip I hata, güç, kapsama ve yanlış yön-seçme kuralını inceleyin.
10. Sonuçları [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
11. [RAPORLAMA.md](RAPORLAMA.md) ile sonuçları akademik rapor diline dönüştürün.

## Veri ve araştırma sorusu

Yerel `veri.csv`, R `datasets` paketindeki `sleep` verisinin kitap arşivindeki aktarımından gelir. Dosyada 20 ölçüm satırı vardır; bunlar **20 bağımsız kişi değildir**. Aynı 10 kişi iki koşulda ölçülmüştür ve eşleştirme anahtarı `ID`'dir. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

Temel değişkenler:

| Alan | Anlam |
|---|---|
| `ID` | 10 kişinin eşleştirme kodu |
| `group` | Koşul 1 veya 2 |
| `extra` | Kontrole göre uyku artışı, saat |

`extra` mutlak uyku süresi değildir. Sıfır ve negatif değerler geçerli kaynak değerleridir ve korunur.

Ana öğretim sözleşmesi:

- fark: `koşul2 − koşul1`,
- `H₀: μ_D = 0`,
- `H₁: μ_D ≠ 0`,
- `α = .05`.

Bu seçim tarihsel araştırmanın önkayıtlı analiz planı olarak sunulmaz; bölümün öğretim sözleşmesidir. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Gerçek eşleşmiş veri analizi

10 kişi için farkların özeti:

- `n=10`,
- ortalama fark = `1.58` saat,
- farkların örneklem standart sapması = `1.229995`,
- standart hata = `.388959`.

Eşleşmiş t testi:

- `t(9)=4.062128`,
- iki yönlü `p=.002832890`,
- %95 GA `[.700114, 2.459886]` saat.

Eşleşmiş etki büyüklüğü:

- `d_z=1.284558`.

Bu değerler için:

`t = d_z × √10`

ilişkisi sağlanır. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Eşleşmiş test neden farklar üzerinden çalışır?

Her kişinin iki ölçümü önce kendi içinde eşleştirilir:

`D_i = koşul2_i − koşul1_i`.

Daha sonra temel soru:

> Bu 10 farkın ortalaması sıfırdan farklı mı?

şeklinde tek örneklem problemine dönüşür.

Bu nedenle eşleşmiş t testi ile farkların sıfıra karşı tek örneklem t testi aynı temel hesabı verir.

20 ölçüm satırını 20 bağımsız kişi gibi kullanmak tasarımı bozar.

## Eşleştirme anahtarının önemi

Satırların dosyadaki sırası eşleştirme anahtarı değildir. `ID` kullanılarak eşleştirme yapıldığında satırlar karıştırılsa bile sonuç değişmemelidir.

Buna karşılık:

- bir kişinin bir koşulu eksikse,
- aynı kişi–koşul kaydı yinelenmişse

analiz sessizce devam etmemelidir.

Önce veri yapısı düzeltilmeli veya durum açıkça ele alınmalıdır. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Fark yönü ve test yönü

Ana fark `koşul2−koşul1` olarak tanımlanmıştır.

Bu yön ters çevrilirse:

- t istatistiğinin işareti değişir,
- iki yönlü p değeri değişmez,
- güven aralığının işaretleri ve uç sırası değişir.

Ana sonuçta:

`[.700114, 2.459886]`

olan aralık ters fark için:

`[−2.459886, −.700114]`

olur. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

Fark yönü sonuç görüldükten sonra daha küçük p elde etmek için seçilmemelidir.

## Tek yönlü ve iki yönlü test

Gerçek eşleşmiş örnekte:

- iki yönlü p = `.002832890`,
- sağ kuyruk p = `.001416445`,
- sol kuyruk p = `.998583555`.

Bu üç sayı aynı araştırma sorusuna verilen alternatif cevaplar değildir. Sağ ve sol kuyruk farklı alternatif hipotezleri temsil eder.

**En küçük p değerini sonradan seçmek geçerli analiz stratejisi değildir.**

## p değeri ne değildir?

`p=.0028` şu anlama gelmez:

> “H₀'ın doğru olma olasılığı %0.28'dir.”

p değeri, belirli model ve H₀ altında gözlenen veya daha uç bir test istatistiğinin olasılığıyla ilgilidir.

Ayrıca küçük p değeri tek başına:

- pratik önemi,
- büyük etkiyi,
- nedenselliği,
- varsayımların doğruluğunu

kanıtlamaz.

## Güven aralığı neden önemlidir?

Ana fark için %95 güven aralığı:

`[.700114, 2.459886]` saattir.

Bu aralık, yalnız “reddet / reddetme” kararından daha fazla bilgi verir; tahminin büyüklüğünü ve belirsizliğini birlikte gösterir.

Ancak güven aralığı da kullanılan model ve varsayımlara bağlıdır.

## Etki büyüklüğü: d_z

Eşleşmiş tasarımda bu bölümde:

`d_z = ortalama fark / farkların standart sapması`

kullanılır.

Sonuç:

`d_z=1.284558`.

Bu bölümde `d_z` için güven aralığı hesaplanmamıştır; rapora uydurma bir aralık eklenmemelidir.

## Küçük örneklem ve uç fark

Örneklem yalnız `n=10` kişidir. En büyük fark `4.6` saattir ve analizde korunur.

Bu gözlem:

- otomatik hata,
- otomatik aykırı değer,
- otomatik silme gerekçesi

olarak değerlendirilmez.

Klasik t hesabı bağımsız kişiler ve normal fark modeli altında öğretilmektedir; bu koşulların veri tarafından kanıtlandığı iddia edilmez. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Kurgusal özet örnekleri

Bu bölümde bazı örnekler yalnız özet istatistiklerden oluşur. Arkalarında yeni üretilmiş ham veri yoktur. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

### Dolum örneği

- `n=25`,
- ortalama = `496`,
- s = `10`,
- referans = `500`.

Sonuç:

- `t(24)=−2`,
- iki yönlü `p=.056940`,
- %95 GA `[491.872203, 500.127797]`,
- sol kuyruk `p=.028470`.

İki yönlü sonuç görüldükten sonra sola tek yönlü teste geçmek uygun değildir.

Ayrıca `p>.05`, sıfır etki veya eşdeğerlik kanıtı değildir.

### Ders özeti

- `n=16`,
- ortalama = `74.5`,
- s = `8`,
- referans = `70`,
- `t(15)=2.25`,
- iki yönlü `p=.039888`,
- sağ kuyruk `p=.019944`,
- %95 GA `[70.237101, 78.762899]`.

### İleri özet

- `n=36`,
- ortalama = `52`,
- s = `12`,
- referans = `50`,
- `t(35)=1`,
- iki yönlü `p=.324174`.

Bu sonuç da “ortalama kesinlikle 50'dir” anlamına gelmez.

## Kurgusal 2×2 tablo

Kurgusal tablo:

`[[20,30],[30,20]]`.

Beklenen her hücre `25`'tir.

Düzeltmesiz Pearson testi:

- `χ²=4`,
- `sd=1`,
- `p=.045500`,
- Cramer `V=.2`.

Bu sonuç **Yates düzeltmeli ki-kare veya Fisher kesin testi sonucu değildir**. Kullanılan test doğru adıyla raporlanmalıdır. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## İdeal model simülasyonu

Her koşulda:

- `20,000` tekrar,
- `n=25`,
- `σ=1`,
- normal model,
- Python tohumu `20260906`

kullanılır.

Sonuçlar:

| Gerçek d | İki yönlü red | Kuramsal red | MC SH | Gerçek ortalama kapsaması |
|---|---:|---:|---:|---:|
| 0 | .0502 | .0500 | .001544 | .9498 |
| .5 | .6667 | .669708 | .003333 | .9474 |

`d=0` koşulunda red oranı yaklaşık `.05` olup Tip I hata davranışını gösterir.

`d=.5` koşulunda red oranı yaklaşık `.667` olup bu **ideal simülasyon modelindeki güçtür**; gerçek `sleep` verisinin gücü değildir. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Monte Carlo hatası

Simülasyondaki oranlar sonsuz tekrarın kesin değerleri değildir. Sonlu tekrar sayısından kaynaklanan Monte Carlo belirsizliği vardır.

Bu nedenle simülasyon oranları kuramsal hedeflerle birlikte ve Monte Carlo standart hatası belirtilerek değerlendirilir.

Aynı tohumun R ve Python'da aynı rastgele sayı dizisini üretmesi gerekmez.

## Veriden yön seçmenin Tip I hata etkisi

`d=0` altında, veriye bakıp daha uygun görünen tek kuyruğu seçen yanlış kuralın red oranı yaklaşık:

`.1016`

olmuştur.

Bu, nominal `.05` düzeyinin yaklaşık iki katıdır ve yönün sonuç görüldükten sonra seçilmesinin hata oranını bozabileceğini öğretir. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Test ile güven aralığının ilişkisi

Simülasyonda her tekrarda iki yönlü `.05` düzeyindeki red kararı, sıfırın %95 güven aralığının dışında kalmasıyla eşleşir.

Ancak `d=.5` altında:

- gerçek `.5` değerinin aralık tarafından kapsanması,
- sıfırın aralık dışında kalması

aynı olay değildir.

Birincisi kapsama, ikincisi test kararıyla ilgilidir.

## Çoklu test ve aile hata oranı

20 bağımsız doğru H₀ testi, her biri α=.05 düzeyinde yürütülürse en az bir yanlış red olasılığı:

`1 − .95^20 = .641514`.

Bu formül bağımsızlık varsayımına dayanır; bağımlı testlere doğrudan uygulanamaz. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Python ile çalıştırma

Depo kökünden:

```sh
python -m pip install -r bolumler/b04/requirements.txt
python bolumler/b04/analiz.py
```

Bölüm klasöründen:

```sh
python analiz.py
```

kullanabilirsiniz.

CSV betikle aynı klasörde kalmalıdır. Bu bölüm NumPy, pandas, matplotlib yanında SciPy kullanır; bölümün kendi `requirements.txt` dosyasını kullanın.

`python -O` kullanmayın; iç hesap denetimleri devre dışı kalabilir.

`calisma.ipynb` içindeki `None` alanları öğrenci görevleridir. Jupyter analiz betiğinin zorunlu bağımlılığı değildir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b04/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

Temel R yeterlidir. R betiği sonuçları ekrana basar; Python'un bütün çıktı dosyalarını üretme iddiası yoktur.

**R bu paket hazırlanırken çalıştırılmamıştır.** Aynı tohum R ve Python'da aynı rastgele diziyi garanti etmez.

Bu pakette SPSS syntax veya çalıştırılmış SPSS çıktısı yoktur.

## Üretilen dosyalar

- `esli_veri.csv`: ID ile eşlenmiş 10 çift; koşul1, koşul2 ve fark.
- `sonuclar/testler.csv`: gerçek analiz ve açıkça etiketlenmiş kurgu testleri.
- `sonuclar/kurgu_capraz.csv`: yalnız kurgusal çapraz tablo.
- `sonuclar/simulasyon.csv`: simülasyon sonuçları.
- `sonuclar/ozet.json`: hesap ve doğrulama özeti.
- `grafikler/b04-test-mantigi.pdf`: kişi farkları, t dağılımı ve iki yönlü kuyruklar.

Ham CSV değiştirilmez. Yeniden çalıştırma türetilmiş çıktıları yeniler; kendi raporunuzu bu klasörlerin dışında saklayın.

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- 20 ölçüm satırını `n=20` bağımsız kişi saymayın.
- ID eşleştirmesini satır sırasına bırakmayın.
- Negatif `extra` veya negatif farkı otomatik hata saymayın.
- Fark yönünü sonuç görüldükten sonra değiştirmeyin.
- En küçük tek yönlü p değerini seçmeyin.
- p değerini H₀'ın doğru olma olasılığı diye yorumlamayın.
- `p>.05` sonucunu sıfır etki veya eşdeğerlik kanıtı saymayın.
- Küçük p değerini pratik önem veya nedensellik kanıtı saymayın.
- Güven aralığını varsayımlardan bağımsız kesin sınır gibi sunmayın.
- Büyük farkı otomatik silmeyin.
- Simülasyon gücünü gerçek `sleep` verisinin gücü diye sunmayın.
- Kurgu özetlerin arkasında gözlenmiş ham veri varmış gibi yazmayın.
- Pearson ki-kareyi Yates veya Fisher sonucu diye etiketlemeyin.
- R ve Python'da aynı tohumun aynı Monte Carlo sayılarını vermesini beklemeyin.
- 20 bağımsız test için aile hata formülünü bağımlı testlere otomatik taşımayın.

## Bu bölümde yapılmayan analizler

Bu pakette:

- normallik testi,
- bootstrap,
- permütasyon testi,
- `d_z` güven aralığı,
- eşdeğerlik testi,
- gerçek veri için güç analizi

yapılmamıştır.

Bunları yapılmış gibi raporlamayın. [Kitap, Bölüm 4](../../KITAP_ESLESMESI.md)

## Akademik raporlama

Sonuçların yöntem ve bulgular bölümlerinde nasıl sunulabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi bir hipotez testi raporu yalnız `p<.05` yazmaz. En azından **tasarım, analiz birimi, fark yönü, n, tahmin, standart hata/belirsizlik, test istatistiği ve sd, p değeri, güven aralığı, etki büyüklüğü ve yorum sınırını** birlikte verir.

## Çözüm ve teknik doğrulama

Önce görevleri kendiniz çözün. Daha sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.

Gerçekte hangi analizlerin çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında kayıtlıdır.

Yerel dosya hash'i yalnız yerel kopyanın bütünlüğünü destekler; uzak kaynak doğrulaması, tarihsel araştırmanın yeniden analizi veya bilimsel varsayım doğrulaması değildir.