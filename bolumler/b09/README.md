# Bölüm 9 — Aracılık ve Düzenleyicilik

> **Önemli:** Bu bölümdeki bütün veriler simülasyondur. Gerçek katılımcılardan elde edilmiş veri veya gerçek bir araştırmanın bulguları değildir.

Bu bölümde regresyonun iki önemli genişletmesi ayrı örnekler üzerinden incelenir: **aracılık (mediation)** ve **düzenleyicilik (moderation)**. Aracılık örneğinde X ile Y arasındaki ilişkinin M üzerinden taşınan dolaylı bileşeni; düzenleyicilik örneğinde ise X ile Y arasındaki ilişkinin W düzeyine göre değişip değişmediği ele alınır.

İki mekanizma öğretim amacıyla ayrı yanıt değişkenleri kullanılarak simüle edilmiştir. Bu nedenle aracılık ve düzenleyicilik sonuçlarını tek bir modelmiş gibi birleştirmeyin.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- aracılık modelindeki `a`, `b`, `c`, `c'` ve `ab` yollarını ayırt edebilir,
- toplam, doğrudan ve dolaylı etki arasındaki model-temelli ilişkiyi açıklayabilir,
- dolaylı etki için satır bazlı bootstrap uygulayabilir,
- bootstrap yeniden örnekleme biriminin neden tüm gözlem satırı olduğunu açıklayabilir,
- persentil bootstrap güven aralığını BCa aralığı ve p değeriyle karıştırmadan yorumlayabilir,
- etkileşim teriminin düzenleyicilik modelindeki anlamını açıklayabilir,
- merkezlemenin etkileşim katsayısı ile alt terimlerin yorumuna etkisini ayırt edebilir,
- belirli W düzeylerinde basit eğimleri ve belirsizliklerini hesaplayabilir,
- basit eğimlerin ayrı p değerlerini doğrudan etkileşim testi yerine kullanmaktan kaçınabilir,
- simülasyon sonuçları ile gerçek araştırma kanıtı arasındaki farkı açıklayabilir,
- aracılık ve düzenleyicilik sonuçlarını akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

Bu bölümü aşağıdaki sırayla çalışmanız önerilir:

1. [VERI.md](VERI.md) dosyasını okuyarak simülasyon tasarımını ve değişken rollerini inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki tasarım sorularını yanıtlayın.
3. Aracılık ve düzenleyicilik örneklerinin **iki ayrı mekanizma** olduğunu belirleyin.
4. `calisma.ipynb` içindeki öğrenci alanlarını tamamlayın.
5. Python veya R ile referans analizini çalıştırın.
6. Bootstrap dağılımını ve basit eğim grafiğini inceleyin.
7. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
8. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla sonuçları bilimsel rapor diline dönüştürün.
9. Son olarak hangi nedensel ve genellenebilirlik iddialarının kurulamayacağını açıklayın.

## İki ayrı araştırma sorusu

### 1. Aracılık

Aracılık örneğinde temel modeller:

`M = i_M + aX + e_M`

`Y = i_Y + c'X + bM + e_Y`

ve toplam ilişki için:

`Y = i_T + cX + e_T`

şeklindedir.

Dolaylı etki `ab` yol çarpımıyla özetlenir. Bu simülasyondaki doğrusal modellerde `c = c' + ab` ilişkisi denetlenir.

Dolaylı etkinin belirsizliği için 5000 satır-bootstrap yeniden örneklemesi kullanılır. X, M ve Y sütunlarını birbirinden bağımsız örneklemek doğru değildir; aynı gözleme ait değişkenler birlikte taşınmalıdır.

### 2. Düzenleyicilik

Düzenleyicilik örneğinde ayrı bir yanıt değişkeni kullanılır:

`Y = β₀ + β₁X + β₂W + β₃(XW) + ε`

Burada `β₃` etkileşim katsayısıdır. X'in Y ile ilişkisinin W düzeyine göre değişip değişmediği doğrudan bu terim üzerinden değerlendirilir.

Basit eğimler W'nin ortalaması ve ortalama ±1 standart sapma düzeylerinde incelenir. Bu üç noktasal sonuç Johnson–Neyman analizi veya eşzamanlı güven bandı değildir.

## Python ile çalıştırma

Öğrenci deposunun kökünden:

```sh
python -m pip install -r bolumler/b09/requirements.txt
python bolumler/b09/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

Kod kendi klasöründeki `veri.csv` dosyasını okur. Kitap veya başka bir bölüm dosyası gerekmez ve ağ erişimi kullanılmaz. `python -O` kullanmayın; bu seçenek betikteki doğrulama denetimlerini kapatabilir.

`calisma.ipynb` depo kökünden veya B09 klasöründen Jupyter ortamında çalıştırılabilir. Jupyter, `analiz.py` betiğinin bağımlılığı değildir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b09/analiz.R
```

Bölüm klasöründen:

```sh
Rscript analiz.R
```

Temel R yeterlidir ve Python çıktısı gerekmez. R betiğinde de 5000 satır-bootstrap ve %95 persentil aralık tanımlanmıştır. R betiği 11 Eylül 2026 tarihinde GitHub Actions üzerinde R 4.5.2 ile hatasız tamamlandı ([çalıştırma kaydı](https://github.com/ibrahimguney/ileri-istatistik-uygulamalari/actions/runs/34604378870)). Bu kayıt çalıştırma başarısını gösterir; bütün R sonuçlarının Python ile otomatik sayısal karşılaştırması değildir.

Aynı seed değerinin R ve NumPy'da aynı bootstrap örneklerini üretmesi beklenmez. Bu nedenle R ve Python bootstrap uçlarının birebir aynı olması zorunlu değildir.

## SPSS 29 ve PROCESS ile doğrulama

[SPSS-PROCESS-KONTROL.md](SPSS-PROCESS-KONTROL.md) rehberini izleyin. Önce [analiz.sps](analiz.sps) ile OLS modellerini, ardından [process-modeller.sps](process-modeller.sps) ile PROCESS Model 4 ve Model 1 çağrılarını çalıştırın. Dosyalardaki yerel yolları kendi bilgisayarınıza göre düzenleyin.

11 Eylül 2026 tarihinde kullanıcının yerel SPSS ve PROCESS 5.0 oturumundan paylaştığı ekran çıktıları incelendi. SPSS regresyonları, PROCESS Model 1 katsayıları ve üç basit eğim ile Model 4'ün görüntülenen a yolu, toplam/doğrudan etkileri ve dolaylı etki nokta tahmini referansla görüntülenen hassasiyette eşleşti. Model 4 için N=160, seed=202610, 5000 persentil bootstrap ve %95 güven düzeyi doğrulandı; dolaylı etki 0.5218, BootSE=0.0819, bootstrap aralığı [0.3702, 0.6901] olarak gözlendi.

Bu kontrol ekran çıktılarıyla sınırlıdır; tam SPV/PDF arşivi ve tam duyarlıklı otomatik yazılımlar arası karşılaştırma değildir. Python/R sonuçları PROCESS çıktısı olarak sunulmamalıdır. Ayrıntılar [DOGRULAMA.json](DOGRULAMA.json) içindeki `SPSS_PROCESS_son_dogrulama` alanındadır.

## Analizde inceleyeceğiniz temel kavramlar

### Aracılık

- `a`, `b`, `c` ve `c'` yolları,
- dolaylı etki `ab`,
- satır bazlı bootstrap,
- bootstrap standart hatası,
- persentil %95 güven aralığı,
- doğrudan ve toplam ilişki,
- nedensellik sınırları.

### Düzenleyicilik

- X × W etkileşimi,
- ham ve merkezlenmiş değişkenler,
- etkileşim katsayısı,
- basit eğimler,
- eğim belirsizliğinde kovaryans terimi,
- W'nin ortalama ve ±1 SS düzeyleri,
- noktasal güven aralıkları.

## Üretilen dosyalar

Analiz çalıştırıldığında başlıca şu dosyalar üretilir:

- `sonuclar/ozet.json`: yollar, `ab`, persentil bootstrap aralığı, etkileşim ve basit eğimler,
- `sonuclar/bootstrap.csv`: 5000 yeniden örneklemenin `ab` değerleri,
- `sonuclar/basit-egimler.csv`: üç W düzeyinde basit eğimler ve noktasal t aralıkları,
- `sonuclar/merkezlenmis.csv`: ham sütunlar korunarak merkezlenmiş X/W çalışma kopyası,
- `grafikler/b09-simulasyon.pdf`: bootstrap dağılımı ve ayrı düzenleyicilik örneğinin basit eğimleri.

Analizi yeniden çalıştırmak bu çıktıları yeniler; ham `veri.csv` değiştirilmez. Kendi raporunuzu `sonuclar/` ve `grafikler/` klasörlerinden ayrı bir yerde saklayın.

## Simülasyonu yeniden üretme

Ana analizi çalıştırmak için veriyi yeniden üretmeniz gerekmez. Dondurulmuş simülasyon verisinin yeni bir kopyasını üretmek için depo kökünden:

```sh
python bolumler/b09/veri_uret.py --cikti bolumler/b09/veri-yeniden.csv
```

Var olan hedef dosyanın üzerine yazılmaz. Farklı simülasyon deneyleri yapmak istiyorsanız kodu ve veriyi ayrı bir kopyada değiştirin; özgün bölüm dosyalarını koruyun.

## Sonuçları yorumlarken dikkat

Bu bölümde özellikle aşağıdaki hatalardan kaçının:

- Simülasyon verisini gerçek öğrenci veya gerçek araştırma verisi olarak sunmayın.
- Dolaylı etki için kullanılan persentil bootstrap aralığını **BCa** olarak adlandırmayın.
- Bu analizde hesaplanmamış bir bootstrap p değeri raporlamayın.
- `c'` yolunun tekil anlamlılığına bakarak kesin “tam aracılık” sonucu çıkarmayın.
- Dolaylı etki aralığının sıfırı dışlamasını gerçek nedensel mekanizmanın kanıtı olarak yorumlamayın.
- Merkezlemenin etkileşimi ortadan kaldırdığını söylemeyin.
- Bir basit eğimin anlamlı, diğerinin anlamsız olmasını doğrudan etkileşim testi olarak kullanmayın.
- Aynı dosyada M ve W bulunmasını koşullu dolaylı etki veya aracılı düzenleyicilik analizi yapılmış olduğu şeklinde yorumlamayın.

Bu paket **koşullu dolaylı etki, aracılı düzenleyicilik, düzenleyicili aracılık veya Johnson–Neyman analizi yapmaz.**

## Akademik raporlama

Aracılık ve düzenleyicilik sonuçlarının nasıl bilimsel biçimde yazılabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın. Özellikle simülasyon etiketini, bootstrap yöntemini, yeniden örnekleme sayısını, dolaylı etki aralığını, etkileşim katsayısını ve basit eğimleri açıkça belirtin.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Hangi kontrollerin gerçekten çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir. Beklenen değerler bu bölümdeki dondurulmuş simülasyonun doğrulanmış hesaplarıdır; gerçek araştırma sonuçları değildir.