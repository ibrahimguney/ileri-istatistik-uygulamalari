# Bölüm 2 — Betimsel İstatistik

Bu bölümde betimsel istatistik, yalnız birkaç özet sayı hesaplamak için değil, **bir veri setini doğru tanımak, dağılımı incelemek, eşleşmiş ölçümleri ayırt etmek, uç gözlemleri sorgulamak ve sayısal özetleri grafiklerle birlikte yorumlamak** için kullanılır.

Uygulama, UCI Student Performance arşivinden alınmış 80 yerel kayıt üzerindeki `G1` ve `G3` notlarını kullanır. Aynı kişinin iki dönem notu iki bağımsız kişi değildir; analizde **80 eşleşmiş kayıt** vardır. İlk kayıttaki `G1=0` geçerli bir kaynak değeridir ve ana analizden silinmez.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- gözlem birimi, değişken ve ölçüm düzeyini ayırabilir,
- geçerli sıfır ile eksik değeri ayırt edebilir,
- ortalama, medyan, varyans ve standart sapmayı hesaplayıp yorumlayabilir,
- `n−1` ve `n` bölenli varyansların hangi sorulara karşılık geldiğini açıklayabilir,
- çeyrek, IQR, tarama sınırı ve kutu grafiği bıyıklarını ayırabilir,
- farklı çeyrek tanımlarının uç gözlem işaretlerini değiştirebileceğini gösterebilir,
- kovaryans ve korelasyonu eşleşmiş ölçümler bağlamında yorumlayabilir,
- fark puanlarının ortalama ve varyansını inceleyebilir,
- ağırlıklı ortalama ile basit ortalamayı ayırabilir,
- konum ve ölçek dönüşümlerinin özet istatistiklere etkisini açıklayabilir,
- duyarlılık analizini otomatik veri silme kuralından ayırabilir,
- betimsel sonuçları akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) dosyasını okuyarak veri kaynağını ve değişkenleri tanıyın.
2. [GOREVLER.md](GOREVLER.md) içindeki D görevleriyle gözlem birimini, sıfır değerini ve örneklem kapsamını açıklayın.
3. `calisma.ipynb` üzerinde temel özetleri ve grafik görevlerini tamamlayın.
4. Python analizini çalıştırın.
5. Ortalama, varyans, çeyrekler, IQR, kovaryans, korelasyon ve fark puanlarını inceleyin.
6. İlk 60 ve son 20 kaydı yalnız betimsel karşılaştırma amacıyla değerlendirin.
7. Çeyrek yöntemi ve ilk kayıt dışlama duyarlılıklarını ana analizden ayrı tutun.
8. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
9. [RAPORLAMA.md](RAPORLAMA.md) ile sayısal sonuçları bilimsel rapor diline dönüştürün.

## Veri ve araştırma soruları

Yerel `veri.csv`, UCI Student Performance veri setinin Portekizce dersi kaynağından alınmış ilk 80 satırdaki `school`, `G1` ve `G3` alanlarının paketlenmiş kopyasıdır. İzleme amacıyla `kaynak_satir` eklenmiştir.

| Değişken | Anlam | Not |
|---|---|---|
| `kaynak_satir` | Yerel alıntıdaki sıra | Kişi kimliği değildir |
| `school` | Okul kodu | Bu alıntıda yalnız GP; nominal |
| `G1` | Birinci dönem notu | 0–20; sıfır geçerli |
| `G3` | Yıl sonu notu | 0–20; sıfır geçerli |

80 satırda eksik hücre yoktur. İlk satır `G1=0`, `G3=11` değerlerini içerir.

Bu bölümde temel sorular şunlardır:

- G1 ve G3 dağılımları nasıl özetlenir?
- Ortalama, medyan ve değişkenlik ölçüleri bize ne söyler?
- Kutu grafiğinde hangi kayıtlar işaretlenir ve bu işaretler nasıl yorumlanmalıdır?
- G1 ile G3 birlikte nasıl değişmektedir?
- Aynı öğrencinin G3−G1 farkları nasıl dağılmaktadır?
- Özetler çeyrek tanımına veya ilk kaydın dışlanmasına ne kadar duyarlıdır?

## Python ile çalıştırma

Depo kökünden:

```sh
python bolumler/b02/analiz.py
```

Bölüm klasöründen:

```sh
python analiz.py
```

kullanabilirsiniz.

Gerekli paketlerin birleşimi depo kökündeki `requirements.txt` dosyasında listelenmiştir.

Python betiği CSV'nin şemasını, sırasını, değer aralığını ve yerel hash'ini kontrol eder. Hata varsa kaynağı incelemeden devam etmeyin. Python'u `-O` ile çalıştırmayın; doğrulama kontrolleri korunmalıdır.

Kaynak `veri.csv` üzerine yazılmaz.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b02/analiz.R
```

veya bölüm klasöründen:

```sh
Rscript analiz.R
```

kullanılabilir.

R kodu temel R ile hazırlanmıştır.

**Bu dağıtım hazırlanırken R betiği çalıştırılarak doğrulanmamıştır.** Python sonuçlarını R tarafından doğrulanmış gibi raporlamayın.

## Hesap sözleşmesi

Sonuçların yeniden üretilebilmesi için bölümde aşağıdaki tanımlar kullanılır:

- Örneklem varyansı ve kovaryansı: `n−1` böleni.
- Kapalı 80-kayıt çerçevesi varyansı: ayrıca `n` böleniyle gösterilir.
- Çeyrekler: NumPy `linear`, R `type=7`.
- Histogram: bir puan genişliğinde sınıflar.
- Kutu grafiği tarama sınırları: `Q1−1.5×IQR` ve `Q3+1.5×IQR`.
- Bıyık uçları: bu sınırlar içinde kalan gözlenen en uç değerler.
- MAD: ölçek çarpanı uygulanmamış ham medyan mutlak sapma.
- G1 ve G3: aynı 80 kaydın eşleşmiş ölçümleri.

`n−1` kullanılması veri setini rastgele veya temsili örnekleme dönüştürmez.

## Temel betimsel sonuçlar

G3 için:

- toplam = `1011`,
- ortalama = `12.6375`,
- kareli sapmalar toplamı = `324.4875`,
- `n−1` varyansı = `4.107437`,
- standart sapma = `2.026681`,
- `n` bölenli kapalı-çerçeve varyansı = `4.056094`.

Bu iki varyansın farklı olması bir hesap hatası değildir; farklı payda tanımlarından kaynaklanır.

## Çeyrekler, IQR ve kutu grafiği

Ana `type=7/linear` tanımında G1 için:

- `Q1=11`,
- `Q3=13.25`,
- `IQR=2.25`,
- alt tarama sınırı = `7.625`,
- üst tarama sınırı = `16.625`,
- alt bıyık = `8`,
- üst bıyık = `16`.

Kaynak sıraları `1, 16, 48 ve 61` işaretlenir.

**Tarama sınırı ile bıyık ucu aynı şey değildir.** Bıyıklar, teorik sınırların kendisi değil, bu sınırlar içinde kalan gözlenen uç değerlerdir.

Yarı-medyan yöntemi kullanıldığında çeyrekler ve işaretlenen kayıtlar değişebilir. Bu, verinin değiştiği anlamına gelmez; özet tanımının değiştiğini gösterir.

## İşaretlenen gözlem silinmek zorunda değildir

Kutu grafiğinde işaretlenmek:

- veri giriş hatası,
- ölçüm hatası,
- geçersiz gözlem

anlamına gelmez.

İlk satırdaki `G1=0` kaynakta geçerli olduğundan ana analizde korunur. Yalnız ayrı bir duyarlılık analizinde dışlanır.

Bu ayrım öğrencinin **ana analiz** ile **duyarlılık analizi**ni karıştırmaması için önemlidir.

## İlk 60 ve son 20 kayıt

G3 ortalamaları:

- ilk 60 kayıt: `12.783333`,
- son 20 kayıt: `12.200000`.

80 kaydın birleşik ortalaması kişi sayılarıyla ağırlıklandırıldığında:

`12.6375`

olur.

İki alt grubun ortalamalarının basit ortalaması ise:

`12.491667`

olur.

Buradaki ağırlıklar yalnız kayıt sayılarından gelir; örnekleme yanlılığını düzelten anket ağırlıkları değildir.

## Eşleşmiş ölçümler

G1 ve G3 aynı 80 kayda ait olduğundan birlikte incelenebilir.

- kovaryans = `3.456646`,
- korelasyon = `.702586`.

Bu pozitif ilişki, G1'i daha yüksek olan kayıtların G3'te de genel olarak daha yüksek olma eğiliminde olduğunu gösterir.

**Korelasyon nedensellik değildir.** Bu bölümde G1'in G3 üzerindeki nedensel etkisi tahmin edilmez.

## Fark puanları

`D = G3 − G1` olarak tanımlandığında:

- ortalama fark = `.4625`,
- fark varyansı = `3.087184`,
- fark standart sapması = `1.757038`.

Kayıtların:

- 32'sinde G3>G1,
- 31'inde G3=G1,
- 17'sinde G3<G1

olmuştur.

Dolayısıyla ortalama farkın pozitif olması **her öğrencinin notunun arttığı** anlamına gelmez.

Fark varyansı özdeşliği:

`Var(G3−G1) = Var(G3) + Var(G1) − 2Cov(G1,G3)`

şeklindedir. Aynı kayıtlar ve aynı varyans/kovaryans böleni kullanılmalıdır.

Bu betimsel farktan nedensel bir “dönem etkisi” çıkarılmaz.

## Konum ve ölçek dönüşümleri

G3'e `10` eklenirse:

- ortalama 10 artar,
- standart sapma değişmez.

G3 `5` ile çarpılırsa:

- ortalama 5 katına,
- standart sapma 5 katına çıkar.

Mekanik CV pozitif ölçeklemede aynı kalabilir fakat sabit eklemede değişir. Bu nedenle notlar için CV'yi “göreli yetenek değişkenliği” gibi yorumlamayın.

## İlk kayıt dışlama duyarlılığı

Yalnız duyarlılık kopyasında ilk kayıt dışlandığında 79 kayıt için:

- G1 ortalaması = `12.329114`,
- G1 standart sapması = `2.011005`,
- G1/G3 korelasyonu = `.793762`.

Ana korelasyon `.702586` iken bu değerin değişmesi ilk kaydın özeti etkilediğini gösterir; fakat kaydın hatalı olduğunu kanıtlamaz ve otomatik silme kararı doğurmaz.

## Bu bölümde yapılmayan analizler

Bu bölümün amacı betimsel istatistiktir. Python betiğinde:

- güven aralığı,
- normallik testi,
- bootstrap,
- hipotez testi,
- nedensel model

uygulanmaz.

Yapılmamış bir analizi sonuçlara eklemeyin.

## Üretilen dosyalar

Çalıştırma sırasında:

- `sonuclar/betimsel_ozet.csv`,
- `sonuclar/frekanslar.csv`,
- `sonuclar/ceyrek_yontemleri.csv`,
- `sonuclar/isaretli_kayitlar.csv`,
- `sonuclar/duyarlilik_satir1_haric.csv`,
- `sonuclar/ozet.json`,
- `grafikler/b02-gercek-betimsel.pdf`,
- türetilmiş `notlar.csv`

üretilir.

Kaynak `veri.csv` değiştirilmez. Grafik kitabın çizimiyle aynı veri ve tanımları kullanır; görsel yerleşimin birebir aynı olması gerekmez.

## Sonuçları yorumlarken dikkat

Şu hatalardan kaçının:

- 80 eşleşmiş kaydı 160 bağımsız kişi olarak saymayın.
- Geçerli `G1=0` değerini eksik veri olarak kodlamayın.
- `n−1` kullanıldığı için örneklemin temsili olduğunu söylemeyin.
- Ortalama medyandan büyük diye dağılımın kesin sağa çarpık olduğunu iddia etmeyin.
- Kutu grafiğinde işaretlenen her kaydı otomatik silmeyin.
- Tarama sınırı ile bıyık ucunu karıştırmayın.
- Farklı çeyrek tanımını veri değişikliği gibi sunmayın.
- Ortalama artışı herkesin notunun arttığı biçiminde yorumlamayın.
- Korelasyonu nedensel etki olarak yorumlamayın.
- CV'yi notlarda doğrudan göreli yetenek ölçüsü saymayın.
- Duyarlılık analizini ana veri temizleme kararı gibi sunmayın.
- Yerel hash kontrolünü uzak kaynak doğrulaması veya temsiliyet kanıtı saymayın.

## Akademik raporlama

Betimsel sonuçların yöntem ve bulgu bölümünde nasıl raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın.

İyi betimsel raporlama yalnız ortalama ve standart sapmayı sıralamaz. **Veri kaynağı, gözlem birimi, değişken tanımı, kullanılan çeyrek/varyans sözleşmesi, dağılım, eşleşmiş yapı, duyarlılık ve yorum sınırları** birlikte açıklanmalıdır.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Gerçekte hangi yazılım ve kontrollerin çalıştırıldığı `DOGRULAMA.json` dosyasında belirtilmiştir.

Yerel SHA-256 kontrolü dosya bütünlüğünü destekler; uzak UCI kaynağıyla yeniden hücre eşleştirmesi, rastgele örnekleme veya bilimsel geçerlik kanıtı değildir.