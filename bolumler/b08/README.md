# Bölüm 8 — Çoklu ve Lojistik Regresyon

Bu bölümde aynı veri üzerinden iki farklı araştırma sorusu ele alınır. İlk olarak `G1` ve yaş kullanılarak yıl sonu notunun (`G3`) koşullu ortalaması çoklu doğrusal regresyonla yordanır. İkinci olarak öğretim amacıyla tanımlanan `G3 ≥ 14` olayının olasılığı lojistik regresyonla modellenir.

Amaç yalnızca iki model kurmak değil; **sürekli ve ikili hedef arasındaki farkı, kısmi regresyon katsayılarını, odds oranını, sınıflandırma eşiklerini ve model performansını doğru yorumlamaktır.**

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- çoklu doğrusal regresyonda kısmi regresyon katsayılarını yorumlayabilir,
- `R²`, düzeltilmiş `R²` ve `ΔR²` kavramlarını ayırt edebilir,
- ek değişken F testi ile ilgili t testinin ilişkisini açıklayabilir,
- merkezlemenin katsayıların yorumuna etkisini açıklayabilir,
- VIF ile çoklu doğrusal bağlantıyı değerlendirebilir,
- klasik ve HC3 standart hatalarını karşılaştırabilir,
- lojistik regresyonda logit, odds, odds oranı ve olasılığı birbirinden ayırabilir,
- odds oranını olasılık oranı gibi yorumlamaktan kaçınabilir,
- duyarlılık, özgüllük ve doğruluk ölçülerini hesaplayabilir,
- AUC ve Brier skorunun farklı performans özelliklerini özetlediğini açıklayabilir,
- karar eşiğinin sınıflandırma sonuçlarına etkisini değerlendirebilir,
- eğitim ve sabit-model aktarım sonuçlarını birbirinden ayırabilir,
- model sonuçlarını akademik bir raporda uygun biçimde sunabilirsiniz.

## Çalışma akışı

Bu bölümü aşağıdaki sırayla çalışmanız önerilir:

1. [VERI.md](VERI.md) dosyasını okuyarak veri kaynağını, değişkenleri, `age_c` ve `hedef14` türetmelerini inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki analiz öncesi ve rehberli görevleri tamamlayın.
3. `calisma.ipynb` defterindeki öğrenci alanlarını doldurun.
4. Python veya R ile referans analizini çalıştırın.
5. Doğrusal ve lojistik modellerin farklı araştırma sorularına yanıt verdiğini açıklayın.
6. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
7. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla sonuçları bilimsel rapor diline dönüştürün.
8. Son olarak model performansını, eşik kararlarını ve genellenebilirlik sınırlarını tartışın.

## Veri ve iki araştırma sorusu

Uygulamada UCI Student Performance veri kümesinden hazırlanmış 80 kayıtlık yerel bir alıntı kullanılmaktadır. Ayrıntılı kaynak, lisans, seçim ve değişken bilgileri [VERI.md](VERI.md) dosyasındadır.

İlk 60 kayıt model kurma amacıyla kullanılır. Sonraki 20 kayıtta katsayılar yeniden tahmin edilmez; ilk 60 kayıtta kurulan sabit modeller uygulanır. Bununla birlikte kayıtlar aynı okulun sıralı alıntısından geldiği için bu bölümdeki aktarım bağımsız yeni okul veya yeni yıl dış doğrulaması değildir.

### 1. Çoklu doğrusal regresyon

Sürekli sonuç değişkeni `G3` için model:

`G3 = β₀ + β₁ G1 + β₂ age_c + ε`

Burada `age_c = age - 16` olarak tanımlanmıştır. Merkezleme, özellikle sabit terimin 16 yaş için yorumlanmasını kolaylaştırır; tek başına model uyumunu iyileştirmez.

### 2. Lojistik regresyon

Öğretim amacıyla:

`hedef14 = 1`, eğer `G3 ≥ 14`; aksi halde `0`.

Lojistik model:

`logit[P(hedef14=1)] = β₀ + β₁ G1 + β₂ age_c`

Buradaki 14 puan **resmî geçme veya başarı sınırı değildir**. Yalnızca lojistik regresyon ve sınıflandırma kavramlarını öğretmek amacıyla kullanılan bir olay tanımıdır.

## Python ile çalıştırma

Öğrenci deposunun kökünden:

```sh
python -m pip install -r bolumler/b08/requirements.txt
python bolumler/b08/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

`veri.csv` kodla aynı klasörde kalmalıdır. Betik çevrimdışı çalışır ve uzak kaynakla otomatik karşılaştırma yapmaz. `python -O` kullanmayın; bu seçenek betikteki doğrulama denetimlerini kapatabilir.

`calisma.ipynb` Jupyter ortamında depo kökünden veya bölüm klasöründen çalıştırılabilir. Jupyter, `analiz.py` betiğinin çalışması için zorunlu değildir.

## R ile çalıştırma

Depo kökünden:

```sh
Rscript bolumler/b08/analiz.R
```

Bölüm klasöründen:

```sh
Rscript analiz.R
```

Temel R yeterlidir ve Python çıktısının önceden üretilmesi gerekmez. R betiği OLS, GLM, Wald odds oranı aralıkları, HC3 standart hataları, VIF ve eşik tablolarını ekrana yazar. Python ile aynı kapsamda dosya, grafik veya AUC çıktısı üretmez. Bu dağıtım hazırlanırken R betiği çalıştırılarak doğrulanmamıştır.

Bu öğrenci paketinde SPSS syntax veya SPSS çıktısı bulunmamaktadır. Python/R sonuçları SPSS sonucu olarak sunulmamalıdır.

## Analizde inceleyeceğiniz temel kavramlar

### Çoklu doğrusal regresyon

- kısmi regresyon katsayıları,
- `R²`, düzeltilmiş `R²` ve `ΔR²`,
- ek değişken F testi,
- merkezleme,
- VIF,
- artık ve etki tanıları,
- klasik ve HC3 standart hataları.

### Lojistik regresyon

- logit ve olasılık,
- odds ve odds oranı,
- Wald güven aralıkları,
- olay olasılığı,
- karar eşikleri,
- karışıklık matrisi,
- duyarlılık, özgüllük ve doğruluk,
- AUC,
- Brier skoru.

## Üretilen dosyalar

Analiz çalıştırıldığında başlıca şu dosyalar üretilir:

- `sonuclar/hazirlanmis.csv`: 80 kayıt ile `age_c` ve `hedef14` değişkenlerini içeren çalışma kopyası,
- `sonuclar/ozet.json`: OLS/HC3, VIF, ek değişken F testi, logit/Wald OR, model uyumu ve eşik sonuçları,
- `sonuclar/tani.csv`: ilk 60 kayıt için artık, kaldıraç, Cook uzaklığı ve olay olasılığı,
- `sonuclar/aktarim.csv`: son 20 kayda sabit modellerin tahminleri,
- `sonuclar/profiller.csv`: örnek `G1` ve yaş profillerinin tahminleri,
- `grafikler/b08-uci-modeller.pdf`: koşullu ortalama ve olay olasılığı,
- `grafikler/b08-uci-tani.pdf`: doğrusal modelin artık ve etki grafikleri.

Ham `veri.csv` değiştirilmez. Analizi yeniden çalıştırmak üretilen dosyaları yeniler. Kendi raporunuzu `sonuclar/` ve `grafikler/` klasörlerinden ayrı bir yerde saklayın.

## Sonuçları yorumlarken dikkat

Bu bölümde özellikle aşağıdaki kavramları birbirine karıştırmayın:

- **14 not puanı** olay tanımıdır; **0.3, 0.5 ve 0.7** ise olasılık karar eşikleridir.
- **Odds oranı (OR)** olasılık oranı değildir.
- Düşük **VIF**, bütün regresyon varsayımlarının sağlandığını göstermez.
- `R²` artışı bir değişkenin nedensel etkisini kanıtlamaz.
- OLS `R²` ile lojistik model için kullanılan McFadden `R²` aynı ölçü değildir.
- Yüksek AUC tek başına iyi kalibrasyon anlamına gelmez.
- Brier skoru yalnızca kalibrasyon ölçüsü değildir; olasılık tahminlerinin kare hatasını özetler.
- `0.50` evrensel olarak en iyi sınıflandırma eşiği değildir.
- Aktarım kümesindeki sonuçlara bakarak eşik seçip aynı kümeyi yeniden bağımsız test gibi kullanmak uygun değildir.
- `hedef14` değişkenini G3'ü açıklayan bir yordayıcı olarak kullanmak yanıt sızıntısı oluşturur.

## Akademik raporlama

Çoklu ve lojistik regresyon sonuçlarının nasıl bilimsel biçimde raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın. Özellikle kısmi eğim, odds oranı, olasılık farkı, sınıflandırma performansı ve model sınırlılıklarının ayrı ayrı ifade edilmesine dikkat edin.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Hangi kontrollerin gerçekten çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir. Yerel bütünlük kontrolleri veri kaynağının temsiliyetini veya bağımsız dış doğrulamayı kanıtlamaz.