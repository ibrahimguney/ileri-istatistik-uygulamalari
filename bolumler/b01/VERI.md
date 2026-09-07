# B01 Veri Kaynağı ve Veri Sözlüğü

## Kaynak

Cortez, P. (2008). *Student Performance* [Veri seti]. UCI Machine Learning Repository. DOI: 10.24432/C5TG7T.

Kaynak adresi: https://archive.ics.uci.edu/dataset/320/student+performance

Veri lisansı: **CC BY 4.0**. Yeniden kullanımda kaynak ve lisans bildirimi korunmalıdır.

## Bu bölümde kullanılan dosya

`veri.csv`, UCI Student Performance veri setinin Portekizce dersi kaynağından seçilmiş ilk 80 kayda ait sınırlı bir alıntıdır. Öğretim amacıyla yalnız aşağıdaki alanlar tutulmuştur:

| Alan | Anlam | Tür / yorum |
|---|---|---|
| `kaynak_satir` | Kaynak alıntıdaki sıra numarası | İzleme alanı; gerçek kişi kimliği değildir |
| `school` | Kaynak okul kodu | Kategorik / nominal; bu alıntıda yalnız `GP` |
| `G1` | Birinci dönem notu | Nicel; 0–20 aralığında tamsayı |
| `G3` | Yıl sonu notu | Nicel; 0–20 aralığında tamsayı |
| `fark_G3_G1` | `G3 - G1` | Türetilmiş nicel değişken |

## Temel bütünlük kontrolleri

- Satır sayısı: **80**
- Eksik hücre: **0**
- `kaynak_satir`: 1–80 ve benzersiz
- `school`: yalnız `GP`
- İlk kayıt: `G1=0`, `G3=11`; `G1=0` geçerli gözlemdir ve eksik değer değildir.

## Analiz birimi

Her satır, seçilen veri alıntısındaki bir öğrenci kaydını temsil eder. Ancak aynı satırdaki `G1` ve `G3` aynı kayda ait iki nottur. Bu iki değer iki bağımsız öğrenci olarak yorumlanamaz.

## Örnekleme ve genelleme sınırı

Bu 80 kayıt:

- rastgele seçilmiş temsili bir örneklem değildir,
- UCI kaynağının 649 kaydının tamamını içermez,
- yalnız `GP` okul kodunu içermektedir,
- Türkiye verisi değildir,
- başka öğrenci gruplarına veya ülkelere doğrudan genelleme için kullanılmamalıdır.

B01'de yapılan sistematik örnekleme uygulaması, **mevcut 80 satır üzerinde örnekleme mantığını öğretmek içindir**. İlk 80 kaydın kendisinin nasıl seçildiğine ilişkin temsiliyet problemi bu işlemle ortadan kalkmaz.

## Veri türü ile ölçüm düzeyi

`G1` ve `G3` bilgisayar ortamında tamsayı olarak saklanır. Bu, tek başına ölçüm düzeyini belirlemez. Ölçüm düzeyi, değişkenin bilimsel anlamına ve fark/oran yorumunun geçerliliğine göre tartışılmalıdır. Bu bölümde amaç bu ayrımı görünür kılmaktır.

## Etik ve gizlilik

Bu dağıtımda ad, iletişim bilgisi, aile bilgileri, sağlık bilgileri ve analiz dışı kişisel alanlar bulunmaz. `kaynak_satir` alanı gerçek kimlik olarak yorumlanmamalı ve kayıtları yeniden kimliklendirme amacıyla kullanılmamalıdır.

## B02 ile ilişki

Aynı 80 kayıt B02 — Betimsel İstatistik bölümünde daha ayrıntılı betimsel analiz için kullanılmaktadır. B01'in amacı aynı veri üzerinde **soru, birim, örnekleme, değişken, frekans, grafik ve kanıt mantığını** kurmaktır.
