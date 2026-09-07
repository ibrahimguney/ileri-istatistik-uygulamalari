# Bölüm 3 — Veri Hazırlama

Bu bölümde veri hazırlama, analize geçmeden önce yapılan mekanik bir “temizlik” işlemi olarak değil, **ham veriyi koruyan, her dönüşümü açıkça tanımlayan, eksikliği görünür tutan ve analiz kararlarını yeniden üretilebilir hale getiren bilimsel bir süreç** olarak ele alınır.

Uygulama, `psych::bfi` gösterim verisinin ilk 100 kaydındaki A1–A5 ve C1–C5 maddelerini kullanır. Bu veri **John ve arkadaşlarının Big Five Inventory testi değildir ve Türkçe ölçek uyarlaması değildir**. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- ham veri ile türetilmiş veri arasındaki farkı açıklayabilir,
- gözlem anahtarlarını ve şema kurallarını denetleyebilir,
- geçerli yanıt, eksik değer ve geçersiz kodu ayırabilir,
- eksik hücre oranı ile eksik kayıt oranını ayrı hesaplayabilir,
- ters puanlamayı ham sütunları koruyarak uygulayabilir,
- tam 5/5 puan ile 4/5 duyarlılık puanını ayırabilir,
- toplam ve ortalama puanların paydalarını açıkça tanımlayabilir,
- geniş ve uzun veri biçimleri arasında kayıpsız dönüşümü kontrol edebilir,
- bire bir birleşme ve kişi–madde anahtarı denetimlerinin önemini açıklayabilir,
- z-standardizasyonun ne yaptığını ve ne yapmadığını açıklayabilir,
- basit ortalama atamasının varyansı neden azaltabildiğini gösterebilir,
- veri hazırlama kararlarını bir karar günlüğüyle belgeleyebilir,
- ana analiz ile duyarlılık analizini ayırabilir,
- veri hazırlama sürecini akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` dosyalarını okuyun.
2. [GOREVLER.md](GOREVLER.md) içindeki D görevleriyle satır, hücre, anahtar ve geçerli kodları tanımlayın.
3. Ham CSV'yi değiştirmeden şema ve anahtar denetimlerini yapın.
4. Eksikliği hem hücre hem kayıt düzeyinde özetleyin.
5. A1, C4 ve C5 için yeni ters-puan sütunları oluşturun.
6. 5/5 ana puanları ve 4/5 duyarlılık puanlarını ayrı hesaplayın.
7. Veriyi uzun biçime çevirin, eksikleri koruyun ve tekrar geniş biçime dönerek eşitliği kontrol edin.
8. A ana puanını standartlaştırın ve yalnız cebirsel denetimleri yapın.
9. Kurgusal hataları yalnız geçici kopyalarda deneyin; gerçek kaynağa atfetmeyin.
10. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
11. [RAPORLAMA.md](RAPORLAMA.md) ile veri hazırlama kararlarını bilimsel rapor diline dönüştürün.

## Veri kaynağı ve kapsam

Yerel `veri.csv`, kitap arşivindeki `bfi-ilk100-AC.csv` dosyasının aynı baytlarla paketlenmiş kopyasıdır. Kaynak William Revelle'nin `psych` paketindeki `bfi` gösterim verisidir; tam gösterim verisi 2800 kayıt içerirken bu bölüm yalnız ilk 100 kaydın A1–A5 ve C1–C5 alanlarını kullanır. Demografik değişkenler aktarılmamıştır. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

Alanlar:

| Alan | Anlam |
|---|---|
| `kaynak_satir` | Yerel aktarım sırası; 1–100, benzersiz |
| `kaynak_kayit` | Yayımlanmış CSV satır etiketi; gerçek kişi kimliği değildir |
| `A1`–`A5` | Uyumlulukla ilişkilendirilen beş ordinal madde |
| `C1`–`C5` | Sorumlulukla ilişkilendirilen beş ordinal madde |

Madde yanıtları `1–6` tamsayıdır. Boş hücre eksiktir. `0`, `99`, `2.5` ve metin geçerli yanıt değildir.

Bu ilk-sıra alıntısından Türkiye, klinik gruplar veya bütün SAPA katılımcıları hakkında genelleme yapılmaz.

## Ham veri değişmez

Bu bölümün temel ilkesi:

**Ham veri korunur; dönüşümler yeni sütunlarda veya yeni dosyalarda yapılır.**

Bu nedenle:

- `veri.csv` üzerine yazılmaz,
- ham A1/C4/C5 sütunları değiştirilmez,
- ana dosyadan satır silinmez,
- atama ana veriye uygulanmaz,
- deneysel hata senaryoları yalnız geçici kopyalarda oluşturulur.

Her analiz yeniden ham CSV'den başlamalıdır.

## Şema ve anahtar denetimleri

Analizden önce şu sorular yanıtlanmalıdır:

- Beklenen sütunlar var mı?
- `kaynak_satir` ve `kaynak_kayit` boş mu?
- Anahtarlar benzersiz mi?
- Madde sütunları yalnız izin verilen değerleri içeriyor mu?
- Eksikler gerçekten boş olarak mı tutulmuş?

Kurgusal kopyalarda `99`, `2.5`, metin, boş anahtar ve yinelenen anahtar eklenerek doğrulama sisteminin hata verdiği gösterilir. Bu denemeler gerçek kaynak verinin hatalı olduğunu göstermez. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

## Eksik veri: iki farklı payda

100 kayıt × 10 madde = `1000` olası madde hücresi vardır.

Eksikler:

- A2, kaynak satırı 66,
- C1, kaynak satırı 63,
- C3, kaynak satırı 90.

Dolayısıyla:

- eksik hücre oranı = `3/1000 = %0.3`,
- en az bir eksiği olan kayıt oranı = `3/100 = %3`,
- on maddede ortak tam kayıt sayısı = `97`.

Bu iki yüzde aynı şeyi ölçmez. Ayrıca düşük eksik oranı **MCAR kanıtı değildir**; bu bölümde MCAR testi yapılmaz. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

## Ters puanlama

A1, C4 ve C5 yeni `_t` sütunlarında:

`7 − x`

ile ters puanlanır.

Örneğin `6 → 1`, `1 → 6` olur.

Eksik yanıt eksik kalır.

Ters puanlanmış dosyayı tekrar terslemek güvenli bir “kontrol” değildir:

`7 − (7 − x) = x`.

Bu işlem ilk terslemeyi geri alır. Bu nedenle analiz daima ham veri ve açık anahtarlama kuralından başlamalıdır.

## Ana puan ve duyarlılık puanı

Bu bölümde iki ayrı hesap tanımı vardır:

### 5/5 ana puanı

Bir yapı için beş maddenin beşi de gözlenmişse puan hesaplanır.

### 4/5 duyarlılık puanı

En az dört madde gözlenmişse mevcut yanıtların ortalaması hesaplanır.

Bu 4/5 kuralı onaylanmış bir test kılavuzu değildir; yalnız öğretim amaçlı duyarlılık karşılaştırmasıdır ve eksik veri mekanizmasını çözmez. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

Sonuçlar:

| Puan | Geçerli n | Ortalama |
|---|---:|---:|
| A 5/5 | 99 | 4.563636 |
| A 4/5 | 100 | 4.565500 |
| C 5/5 | 98 | 4.187755 |
| C 4/5 | 100 | 4.191500 |

Ana ve duyarlılık puanları birbirinin yerine raporlanmamalıdır. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

## Toplam ile ortalamayı ayırın

Beş tam yanıt için:

`toplam = 5 × ortalama`.

Ancak dört gözlenen maddeyle hesaplanan ortalamayı beş maddelik toplam diye adlandırmak yanlıştır.

Örneğin `[6,4,5,3,NA]` için:

- 4/5 ortalama = `4.5`,
- 5/5 puanı = eksik.

Puan üretilemeyen hücre boş kalır; kayıt silinmez.

## Eksik örnek kayıtları

- Satır 63: `A_n=5`, `A_ort4=5.6`; `C_n=4`, `C_ort4=5.25`.
- Satır 66: `A_n=4`, `A_ort4=4.75`; `C_n=5`, `C_ort4=5.0`.
- Satır 90: `A_n=5`, `A_ort4=4.4`; `C_n=4`, `C_ort4=3.5`.

Bu örnekler puanın hangi maddeler ve hangi payda üzerinden üretildiğinin açıkça belgelenmesi gerektiğini gösterir. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

## Geniş ve uzun veri biçimi

Veri uzun biçime çevrildiğinde:

- `1000` kişi–madde satırı,
- `997` gözlenen yanıt

bulunur.

Boş yanıtlar uzun biçimde de korunur.

Kişi–madde anahtarı benzersiz olmalıdır. Uzun veri tekrar geniş biçime çevrildiğinde, eksikler dahil özgün değerlerle eşleşmelidir.

Bu dönüşüm yalnız dosya biçimi değişikliğidir; yeni veri üretmez.

## Birleşme ve pivot güvenliği

Bire bir olması gereken birleştirmede yinelenen anahtar varsa işlem durmalıdır.

`validate="one_to_one"` gibi denetimler, fark edilmeden satır çoğalmasını önler.

Benzer biçimde yinelenen kişi–madde kayıtlarını `pivot_table` ile sessizce ortalamak veri problemini çözmez; sorunu gizleyebilir.

Önce anahtar problemi araştırılmalıdır. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

## Standardizasyon

A'nın 5/5 ana puanı 99 kullanılabilir kayıt üzerinde örneklem standart sapmasıyla standartlaştırılır.

Sonuçta z puanlarının:

- ortalaması yaklaşık `0`,
- örneklem standart sapması `1`

olur.

Bu cebirsel bir özelliktir.

**z-standardizasyon dağılımı normal yapmaz, normalliği kanıtlamaz ve ölçme geçerliği sağlamaz.**

## Ortalama ataması karşı örneği

C1 için gözlenen:

- `n=99`,
- ortalama = `4.454545`,
- örneklem varyansı = `1.515770`.

Tek eksik değer yalnız geçici kopyada gözlenen ortalamayla doldurulduğunda:

- ortalama değişmez,
- örneklem varyansı `1.500459`'a düşer.

Bu örnek, “ortalama değişmediğine göre atama zararsızdır” düşüncesinin yanlış olduğunu gösterir. Basit ortalama ataması dağılımı ve belirsizliği değiştirebilir. Ana veride bu atama yapılmaz. [Kitap, Bölüm 3](../../KITAP_ESLESMESI.md)

## Python ile çalıştırma

Depo kökünden:

```sh
python -m pip install -r bolumler/b03/requirements.txt
python bolumler/b03/analiz.py
```

Yalnız bölüm klasörünü indirdiyseniz:

```sh
python analiz.py
```

kullanabilirsiniz.

`veri.csv` betikle aynı klasörde kalmalıdır. Python betiği çalışma dizininden bağımsızdır.

Python'u `-O` seçeneğiyle çalıştırmayın; iç hesap denetimleri korunmalıdır.

`calisma.ipynb` içindeki `None` alanları öğrenci görevleridir. Jupyter ayrı bir çalışma ortamıdır ve bölümün Python bağımlılık listesine dahil değildir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b03/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

R betiği temel puanlama ve reshape denetimlerini ekrana basar; Python ile aynı çıktı dosyalarının tamamını üretme iddiası yoktur.

**R bu dağıtım hazırlanırken çalıştırılarak doğrulanmamıştır.**

Bu pakette çalıştırılmış SPSS çıktısı veya SPSS syntax dosyası yoktur.

## Üretilen dosyalar

- `puanlar.csv`: 100 kayıt, korunmuş ham maddeler, ters sütunlar ve puanlar.
- `uzun.csv`: 1000 kişi–madde satırı; eksikler korunur.
- `sonuclar/`: eksik özeti, desenler, puan özetleri, çift paydaları, karar günlüğü, standartlaştırma, üretilmiş sözlük ve `ozet.json`.
- `grafikler/b03-eksik-puan-paydalari.pdf`: eksik deseni ve puan paydaları.

Her çalıştırma bu türetilmiş çıktıları yeniler. Kendi raporunuzu ayrı yerde saklayın.

Kaynak `veri.csv` ve dağıtılan `veri_sozlugu.csv` değiştirilmez.

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- Boş hücreyi `0` olarak kodlamayın.
- `0`, `99`, `2.5` ve metni geçerli 1–6 yanıt gibi kabul etmeyin.
- `%0.3` eksik hücre ile `%3` eksik kayıt oranını karıştırmayın.
- Düşük eksik oranından MCAR sonucu çıkarmayın.
- Ham maddelerin üzerine ters puan yazmayın.
- Terslenmiş dosyayı tekrar terslemeyin.
- 4/5 ortalamayı 5 maddelik toplam diye raporlamayın.
- Puan üretilemeyen kaydı otomatik silmeyin.
- Ortalama atamasını dağılımı değiştirmeyen nötr işlem gibi sunmayın.
- Yinelenen anahtarları sessizce çoğaltmayın veya ortalamayın.
- z puanlarını normallik kanıtı saymayın.
- 4/5 kuralını onaylanmış ölçek puanlama kılavuzu gibi sunmayın.
- Kurgusal hata testlerini gerçek veri kusuru gibi raporlamayın.
- Bu bölümü güvenirlik veya ölçek geçerliği analizi yapılmış gibi sunmayın.
- İlk 100 kayıttan geniş bir evrene genelleme yapmayın.
- Yerel hash eşitliğini uzak kaynak doğrulaması veya temsiliyet kanıtı saymayın.

## Bu bölümde yapılmayan analizler

Bu veri hazırlama uygulamasında:

- MCAR testi,
- çoklu atama,
- model tabanlı eksik veri analizi,
- güvenirlik analizi,
- faktör analizi,
- normallik testi,
- ölçek geçerliği analizi

yapılmamıştır.

Bu işlemleri yapılmış gibi raporlamayın.

## Akademik raporlama

Veri hazırlama sürecinin yöntem bölümünde nasıl raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi veri hazırlama raporu yalnız “veriler temizlendi” demez. **Kaynak, şema, geçerli kodlar, eksiklik paydaları, ters puanlama, puanlama eşiği, reshape denetimi, standardizasyon, duyarlılık ve yapılmayan işlemler** açıkça belgelenmelidir.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Gerçekte hangi yazılım ve denetimlerin çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir.

Yerel dosya hash'i yeniden üretilebilirliği destekler; uzak kaynakla otomatik hücre karşılaştırması, örneklem temsiliyeti veya bilimsel geçerlik kanıtı değildir.