# Bölüm 10 — Parametrik Testler

Bu bölümde **tek örneklem t testi, eşli örneklemler t testi ve bağımsız iki örneklem için Welch t testi** gerçek tarihsel veri arşivleri üzerinden uygulanır. Temel amaç yalnızca bir p değeri elde etmek değil; araştırma tasarımına göre doğru testi seçmek, farkın yönünü ve birimini açıkça tanımlamak, güven aralığını ve etki büyüklüğünü doğru yorumlamak ve varsayım/tanı sonuçlarını görünür biçimde raporlamaktır.

Bölüm bağımsız çalışır; kitabın veya başka bölümün dosyaları gerekmez.

## Öğrenme hedefleri

Bu bölümü tamamladığınızda:

- tek örneklem, eşli ve bağımsız iki örneklem t testlerini araştırma tasarımına göre ayırt edebilir,
- bağımsız gözlem birimi ile ham satır/ölçüm sayısını birbirinden ayırabilir,
- eşli verilerde kişi içi farkları doğru oluşturabilir,
- Welch ve Student t testlerinin varsayım ve serbestlik derecesi farklarını açıklayabilir,
- ham ortalama farkı ve %95 güven aralığını yorumlayabilir,
- `p > .05` sonucunun sıfır etki veya eşdeğerlik kanıtı olmadığını açıklayabilir,
- Cohen türü standartlaştırılmış etki büyüklüklerinde kullanılan standartlaştırıcının tasarıma göre değiştiğini fark edebilir,
- Shapiro, Q–Q grafiği, Levene ve Brown–Forsythe sonuçlarını otomatik karar kuralları yerine tanı bilgisi olarak değerlendirebilir,
- duyarlılık analizini sonuç seçme veya otomatik gözlem silme aracı olarak kullanmaktan kaçınabilir,
- birim ve yön değişiminin t, p, fark ve güven aralığı üzerindeki etkisini açıklayabilir,
- parametrik test sonuçlarını akademik biçimde raporlayabilirsiniz.

## Çalışma akışı

1. [VERI.md](VERI.md) ve `veri_sozlugu.csv` dosyalarını okuyarak kaynak, ölçüm birimi ve eşleşme yapısını inceleyin.
2. [GOREVLER.md](GOREVLER.md) içindeki analiz öncesi soruları yanıtlayın.
3. Her araştırma sorusu için **birim, yön, n ve uygun test türünü** analizden önce belirleyin.
4. `calisma.ipynb` içindeki öğrenci alanlarını tamamlayın.
5. Python veya R ile referans analizini çalıştırın.
6. Q–Q, varyans ve duyarlılık sonuçlarını ana testlerle birlikte değerlendirin.
7. Sonuçlarınızı [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın.
8. [RAPORLAMA.md](RAPORLAMA.md) yardımıyla sonuçları bilimsel rapor diline dönüştürün.

## Üç araştırma sorusu

| Soru | Tasarım | Yön |
|---|---|---|
| Koşul 1'de ortalama artış 0'dan farklı mı? | Tek örneklem | koşul 1 − 0 saat |
| Aynı kişilerin iki koşulu arasında fark var mı? | Eşli ölçüm | koşul 2 − koşul 1 |
| Doz 1'de OJ ve VC grupları farklı mı? | Bağımsız gruplar | OJ − VC |

Bütün ana testler iki yönlüdür; `α = .05` ve farklar için %95 güven aralıkları kullanılır.

### 1. Tek örneklem t testi

`sleep` verisindeki koşul 1 artışları 0 saatlik referans değere karşı sınanır. Buradaki soru, örneklem ortalamasının referans değerden ne ölçüde farklı olduğudur.

### 2. Eşli örneklemler t testi

Aynı 10 kişinin iki koşuldaki ölçümleri ID üzerinden eşleştirilir ve her kişi için `koşul 2 − koşul 1` farkı oluşturulur. Veri dosyasında 20 ölçüm bulunması 20 bağımsız kişi olduğu anlamına gelmez; eşli analizde bağımsız birim 10 kişidir.

### 3. Bağımsız gruplar için Welch t testi

`ToothGrowth` verisinde doz 1 düzeyindeki 10 OJ ve 10 VC kaydı karşılaştırılır. Ana yöntem Welch t testidir. Eşit grup büyüklüğü eşit varyansın kanıtı değildir.

## Python ile çalıştırma

Öğrenci deposunun kökünden:

```sh
python bolumler/b10/analiz.py
```

Bölüm klasöründeyseniz:

```sh
python analiz.py
```

Gerekli Python paketleri `requirements.txt` dosyasında belirtilmiştir. Kod ağ erişimine, kitap klasörüne veya uzak veri indirmesine ihtiyaç duymaz. Notebook için ayrıca bir Jupyter ortamı gerekir.

## R ile çalıştırma

R kuruluysa depo kökünden:

```sh
Rscript bolumler/b10/analiz.R
```

kullanılabilir. R betiği yerel CSV dosyalarını kurulu R `datasets` tablolarıyla da karşılaştırır. Ancak bu dağıtım hazırlanırken **R betiği çalıştırılarak doğrulanmamıştır**. R çıktıları Python'daki grafik ve bütün tanı çıktılarının birebir eşdeğeri değildir.

Bu öğrenci paketinde SPSS komut dosyası veya doğrulanmış SPSS çıktısı bulunmamaktadır. Python/R sonuçlarını SPSS sonucu olarak sunmayın.

## Analizde inceleyeceğiniz temel kavramlar

- tek örneklem t testi,
- eşli örneklemler t testi,
- Welch bağımsız örneklemler t testi,
- Student ve Welch karşılaştırması,
- ortalama fark ve standart hata,
- serbestlik derecesi,
- %95 güven aralığı,
- standartlaştırılmış etki büyüklüğü,
- Shapiro–Wilk ve Q–Q tanıları,
- Levene ve Brown–Forsythe tanıları,
- eşleşme ve bağımsızlık,
- birim/yön dönüşümleri,
- çift-dışarıda-bırakma duyarlılık analizi,
- çoklu karşılaştırma ve eşdeğerlik sınırları.

## Üretilen dosyalar

Analiz çalıştırıldığında başlıca şu dosyalar üretilir:

- `sonuclar/ozet.json`: testler, tanılar, duyarlılık sonuçları, kaynak hash'leri ve sürümler,
- `sonuclar/uyku_esli.csv`: ID ile eşlenmiş 10 kişi ve koşul 2−1 farkı,
- `sonuclar/dis_veri.csv`: 60 hayvan kaydı ve ek `supp_kod` sütunu,
- `sonuclar/cift_duyarlilik.csv`: her bir çift sırayla dışarıda bırakıldığında elde edilen sonuçlar,
- `grafikler/b10-uyku-eslestirme.pdf`: eşli ölçümler ve farkların Q–Q grafiği,
- `grafikler/b10-welch-farklar.pdf`: doz 1 ham değerleri ve doz 1/2 fark aralıkları.

Bu çıktılar yeniden üretilebilir; ham CSV dosyaları değiştirilmez. `sleep.csv`, `ToothGrowth.csv`, `GPL-2.txt` ve kaynak açıklamalarını birlikte koruyun.

## Sonuçları yorumlarken dikkat

Bu bölümde özellikle şu hatalardan kaçının:

- 20 ölçümü 20 bağımsız kişi olarak yorumlamayın.
- Eşli verileri bağımsız gruplar gibi analiz etmeyin.
- `p > .05` sonucunu “etki tam sıfırdır” biçiminde yorumlamayın.
- Anlamlı olmayan farkı otomatik olarak **eşdeğerlik** kanıtı saymayın.
- Levene testinin anlamlı olmamasını varyansların kesin eşit olduğunun kanıtı olarak sunmayın.
- Shapiro testini tek başına mekanik test-seçim kuralı olarak kullanmayın.
- Farkların Shapiro sonucundaki yaklaşık `p = .0333` bulgusunu ve Q–Q grafiğindeki üst kuyruk kaygısını gizlemeyin.
- Tanı sonucuna bakarak gözlemleri otomatik silmeyin.
- Birden fazla doz arasından yalnızca en küçük p değerini seçip raporlamayın.
- Ortalama fark için güven aralığını bireylerin %95'inin sonucunu kapsayan aralık gibi yorumlamayın.
- Tarihsel öğretim verilerinden tedavi önerisi veya doğrulanmamış nedensel sonuç çıkarmayın.

## Akademik raporlama

Tek örneklem, eşli ve Welch t testi sonuçlarının nasıl bilimsel biçimde raporlanabileceğini görmek için [RAPORLAMA.md](RAPORLAMA.md) dosyasını kullanın. Her sonuçta **tasarım, n, fark yönü, ölçüm birimi, t, serbestlik derecesi, p, %95 güven aralığı ve uygun etki büyüklüğünü** açıkça belirtmeye dikkat edin.

## Çözüm ve teknik doğrulama

Çalışmanızı tamamladıktan sonra [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile karşılaştırın. Hangi analiz ve kontrollerin gerçekten çalıştırıldığı [DOGRULAMA.json](DOGRULAMA.json) dosyasında belirtilmiştir. Python analizinin çalışması R veya SPSS sonuçlarının doğrulandığı anlamına gelmez.