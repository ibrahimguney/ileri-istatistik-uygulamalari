# Bölüm 7 — Regresyon

Bu bölümde birinci dönem notu (`G1`) kullanılarak yıl sonu notunun (`G3`) nasıl yordanabileceğini inceleyeceksiniz. Amaç yalnızca bir regresyon doğrusu elde etmek değil; modelin belirsizliğini, etkili gözlemleri, tahmin başarısını ve sonuçların hangi sınırlar içinde yorumlanabileceğini anlamaktır.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- basit doğrusal regresyon modelinin eğim ve sabit terimini hesaplayabilir,
- `R²`, artık standart sapması ve RMSE'yi doğru yorumlayabilir,
- ortalama güven aralığı ile bireysel tahmin aralığını ayırt edebilir,
- kaldıraç ve Cook uzaklığı gibi etki tanılarını değerlendirebilir,
- klasik ve HC3 standart hatalarını karşılaştırabilir,
- LOOCV ile eğitim hatası arasındaki farkı açıklayabilir,
- yordama ile nedensel etkiyi birbirinden ayırabilir,
- regresyon sonuçlarını akademik bir raporda uygun biçimde sunabilirsiniz.

## Çalışma akışı

Bu bölümü aşağıdaki sırayla çalışmanız önerilir:

1. [VERI.md](VERI.md) dosyasını okuyarak veri kaynağını, değişkenleri ve örneklem sınırlarını inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki analiz öncesi ve rehberli görevleri tamamlayın.
3. `calisma.ipynb` defterindeki öğrenci alanlarını doldurun.
4. Referans analizi Python veya R ile çalıştırın.
5. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
6. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla bulgularınızı bilimsel rapor diline dönüştürün.
7. Son olarak modelin sınırlılıklarını ve hangi iddiaların kurulamayacağını açıklayın.

## Veri ve araştırma sorusu

Uygulamada UCI Student Performance veri kümesinden hazırlanmış yerel bir öğrenci veri alıntısı kullanılmaktadır. Ayrıntılı kaynak, lisans, seçim ve değişken bilgileri [VERI.md](VERI.md) dosyasındadır.

Temel model:

`G3 = β₀ + β₁ G1 + ε`

Burada `G1` birinci dönem notu, `G3` ise yıl sonu notudur. Ana analiz ilk 60 kayıt üzerinde yapılır. Son 20 kayıt ayrı bir model kurma etkinliği için kullanılır; ana modelin dış doğrulaması olarak yorumlanmaz.

Bu gözlemsel uygulamada regresyon katsayısı nedensel müdahale etkisi değildir. `G1` ile `G3` arasındaki ilişki bir yordama ilişkisi olarak ele alınmalıdır.

## Python ile çalıştırma

Öğrenci deposunun kökünden:

```sh
python -m pip install -r bolumler/b07/requirements.txt
python bolumler/b07/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

Ham `veri.csv` dosyası kodla aynı klasörde kalmalıdır. Analiz ağ bağlantısı gerektirmez. `python -O` kullanmayın; bu seçenek betikteki doğrulama denetimlerini kapatabilir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b07/analiz.R
```

Bölüm klasöründen:

```sh
Rscript analiz.R
```

Temel R yeterlidir. Python analizinin önceden çalıştırılması gerekmez. R betiği tanı grafiklerini `grafikler/tani-R.pdf` dosyasına yazar. Bu dağıtım hazırlanırken R betiği çalıştırılarak doğrulanmamıştır.

Bu öğrenci paketinde SPSS syntax veya SPSS çıktısı bulunmamaktadır. Python sonuçları SPSS sonucu olarak sunulmamalıdır.

## Analizde inceleyeceğiniz temel kavramlar

Bu bölüm yalnızca OLS katsayılarını üretmez. Aşağıdaki konuları birlikte değerlendirir:

- regresyon doğrusu ve `R²`,
- artıklar ve model hatası,
- ortalama güven aralığı,
- bireysel tahmin aralığı,
- kaldıraç ve Cook uzaklığı,
- etkili gözlemlere duyarlılık,
- klasik ve HC3 standart hataları,
- LOOCV tahmin hatası,
- gözlenen veri aralığı dışında ekstrapolasyon,
- yordama, genellenebilirlik ve nedensellik sınırları.

## Üretilen dosyalar

Analiz çalıştırıldığında başlıca şu dosyalar üretilir:

- `sonuclar/not_basari.csv`: ilk 60 kaydın ana analiz kopyası,
- `sonuclar/aktarim.csv`: son 20 kaydın ayrı model kurma etkinliği,
- `sonuclar/ozet.json`: katsayılar, aralıklar, HC3, RMSE ve etkinlik sonuçları,
- `sonuclar/tani.csv`: tahmin, artık, kaldıraç ve Cook uzaklığı,
- `sonuclar/araliklar.csv`: `G1=12` için ortalama ve bireysel aralıklar,
- `sonuclar/duyarlilik.csv`: kayıt çıkarma ve LOOCV duyarlılık sonuçları,
- `grafikler/b07-ogrenme-senaryosu.pdf`: regresyon doğrusu, güven bandı ve artık grafiği.

Ham 80 kayıt değiştirilmez. Analizi yeniden çalıştırmak üretilen dosyaları yeniler. Kendi raporunuzu `sonuclar/` ve `grafikler/` klasörlerinden ayrı bir yerde saklayın.

## Sonuçları yorumlarken dikkat

Küçük bir p değeri regresyon varsayımlarının doğru olduğunu kanıtlamaz. `R²`, başarılı öğrenci oranı değildir. Yüksek Cook uzaklığı bir kaydın hatalı olduğunu tek başına göstermez. HC3 standart hatası bazı heteroskedastisite sorunlarına karşı katsayı belirsizliğini daha dayanıklı hesaplamaya yardımcı olur; ancak seçilim, kümelenme, yanlış model biçimi veya nedensellik sorunlarını çözmez.

Ana analizde gözlenen `G1` aralığı 0–17'dir. Bu nedenle `G1=20` için tahmin ekstrapolasyondur. Son 20 kayıtta yeni bir model kurmak da ana modelin bağımsız dış doğrulaması değildir.

## Akademik raporlama

Regresyon sonuçlarının nasıl bilimsel bir paragraf ve tablo halinde raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın. Buradaki amaç yalnızca sayıları aktarmak değil; katsayıları, belirsizliği, model uyumunu ve sınırlılıkları birlikte yorumlamaktır.

## Teknik doğrulama

Sayısal referans değerleri `beklenen.json` dosyasında, hangi kontrollerin gerçekten çalıştırıldığı ise [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir. Yerel hash denetimi kaynak dosyanın beklenen yerel kopyayla aynı kaldığını kontrol eder; uzak kaynağın güncelliğini veya örneklemin temsiliyetini kanıtlamaz.