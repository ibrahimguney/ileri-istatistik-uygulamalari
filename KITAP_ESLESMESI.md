# Kitap–depo eşleştirmesi

Kontrol tarihi: 7 Eylül 2026. Referans: İbrahim Güney, *İleri İstatistik Uygulamaları*, `ileri-istatistik-izü6.pdf`. Sayfalar PDF görüntüleyicisinin sıra numarası değil, kitapta basılı sayfalardır.

Bu kayıt bölüm sırası, başlıklar ve öğrenci paketinin dosya kapsamı içindir. Bütün formüllerin, tabloların, alıştırmaların ve sayısal değerlerin kitapla tek tek karşılaştırıldığı anlamına gelmez. Python analiz ve notebook yürütmeleri ayrıca `DOGRULAMA.json` içinde kayıtlıdır.

## Bölüm eşleştirmesi

| Bölüm | Kitaptaki başlık | Başlangıç sayfası | Depodaki başlık | Öğrenci paketi |
|---|---|---:|---|---|
| [B01](bolumler/b01/README.md) | İstatistiksel Düşünme: Sorudan Kanıta | 1 | İstatistiksel Düşünme: Sorudan Kanıta | 8/8 dosya mevcut |
| [B02](bolumler/b02/README.md) | Betimsel İstatistik | 15 | Betimsel İstatistik | 8/8 dosya mevcut |
| [B03](bolumler/b03/README.md) | Veri Hazırlama | 29 | Veri Hazırlama | 8/8 dosya mevcut |
| [B04](bolumler/b04/README.md) | Hipotez Testi | 43 | Hipotez Testi | 8/8 dosya mevcut |
| [B05](bolumler/b05/README.md) | Güç Analizi | 57 | Güç Analizi ve Örneklem Planlama | 8/8 dosya mevcut |
| [B06](bolumler/b06/README.md) | Korelasyon Analizi | 71 | Korelasyon | 8/8 dosya mevcut |
| [B07](bolumler/b07/README.md) | Regresyon Analizi | 91 | Regresyon | 8/8 dosya mevcut |
| [B08](bolumler/b08/README.md) | Çoklu ve Lojistik Regresyon | 113 | Çoklu ve Lojistik Regresyon | 8/8 dosya mevcut |
| [B09](bolumler/b09/README.md) | Aracılık ve Düzenleyicilik | 131 | Aracılık ve Düzenleyicilik | 8/8 dosya mevcut |
| [B10](bolumler/b10/README.md) | Parametrik Testler | 141 | Parametrik Testler | 8/8 dosya mevcut |
| [B11](bolumler/b11/README.md) | Varyans Analizi | 161 | Varyans Analizi (ANOVA) | 8/8 dosya mevcut |
| [B12](bolumler/b12/README.md) | Parametrik Olmayan Testler | 181 | Parametrik Olmayan Testler | 8/8 dosya mevcut |
| [B13](bolumler/b13/README.md) | Ölçek Uyarlama ve Güvenirlik | 195 | Ölçek Uyarlama ve Güvenirlik | 8/8 dosya mevcut |
| [B14](bolumler/b14/README.md) | Faktör Analizi | 209 | Faktör Analizi | 8/8 dosya mevcut |
| [B15](bolumler/b15/README.md) | Doğrulayıcı Faktör Analizi | 223 | Doğrulayıcı Faktör Analizi (DFA/CFA) | 8/8 dosya mevcut |
| [B16](bolumler/b16/README.md) | Yapısal Eşitlik Modeli | 237 | Yapısal Eşitlik Modeli (YEM/SEM) | 8/8 dosya mevcut |
| [B17](bolumler/b17/README.md) | Kovaryans Analizi | 253 | Kovaryans Analizi (ANCOVA) | 8/8 dosya mevcut |
| [B18](bolumler/b18/README.md) | IBM SPSS Uygulamaları | 267 | IBM SPSS Uygulamaları | 8/8 dosya mevcut |

Kontrol edilen sekiz dosya: `README.md`, `VERI.md`, `GOREVLER.md`, `calisma.ipynb`, `RAPORLAMA.md`, `COZUMLER.md`, `analiz.py`, `beklenen.json`. Dosyanın bulunması, içeriğinin bütünüyle bilimsel doğrulandığı anlamına gelmez.

## B01 başlık güncellemesi

7 Eylül 2026'da PDF bölüm başlığı “İstatistiksel Düşünme: Sorudan Kanıta”, 1.2 başlığı “İstatistiksel Düşünme Süreci” olarak güncellendi. İçindekiler, bölüm üstbilgileri, cevap anahtarı başlığı ve PDF yer imleri de eşitlendi. 401 sayfa, bağlantı sayıları ve diğer sayfaların metni korundu. Değişen başlıkların sayfa düzeni görsel olarak kontrol edildi.

Bu işlem PDF üzerinde yapıldı. Prism/LaTeX kaynakları bu depoda bulunmadığından yeniden derleme öncesinde aynı başlıklar kaynak dosyada da uygulanmalıdır.

B05, B06, B07, B11, B15, B16 ve B17 depo başlıklarında açıklayıcı ek, kısaltma veya sadeleştirme vardır; tabloda iki biçim ayrı gösterilmiştir.

## Atıflar ve kaynaklara erişim

Sekiz bölüm README dosyasındaki 68 sohbet içi dosya atfı GitHub üzerinde çözümlenmiyordu. Bunların yerine bu eşleştirme kaydına giden kitap bölümü bağlantıları kondu. Bu bağlantılar okura bölümün kitap içindeki yerini gösterir; her paragraf için ayrı sayfa doğrulaması veya yeni bir dış kaynak doğrulaması değildir. Veri kaynakları ve lisanslar ilgili bölümün `VERI.md` dosyasında korunur. Tam kitap dosyası depoya eklenmemiştir.

## Seçili sayısal kontroller

`tools/dogrula_kitap_ornekleri.py`, B01 s.5–6'dan 6 sayıyı ve B18 s.271–273'ten 41 sayıyı yeniden üretilmiş Python çıktılarıyla karşılaştırır. Yuvarlanmış kitap değerleri için son basamağın yarısı kadar mutlak tolerans, tam sayılar için birebir eşitlik kullanılır. Ayrıca B01'in iki seçim dizisi, rastgele/ilk-10 ortalamaları ve sekiz başlangıç ortalaması ham veriden kontrol edilir. Bu kontroller başarılıdır; bütün kitaptaki sayıların kontrol edildiği iddia edilmez.

| Kitap örneği | Basılı sayfa | Doğrulanan temel değer |
|---|---:|---|
| B01 sistematik seçim | 5–6 | N=80, n=10, r=3, j=8; G3 ortalaması 12.2 |
| B01 çerçeve ortalaması | 6 | 12.6375 |
| B01 tohum 20260906 ile seçim | 6 | 21,23,26,34,40,44,56,59,60,62; ortalama 13.2 |
| B18 eşli test | 271 | t=4.062128; p=.002832890; GA [.700114,2.459886] |
| B18 Welch | 272 | fark=5.93; sd=15.357672; GA [2.802148,9.057852] |
| B18 ilk beş ID | 273 | n=5; ortalama=1.24; t=3.260900 |

B18 ayrıca GitHub Actions üzerinde R 4.5.2 ile gerçekten yürütüldü. 71 sayısal sonuç hem `beklenen.json` hem yeniden üretilmiş Python sonuçlarıyla eşleşti. En büyük mutlak R–Python farkı yaklaşık 4.80e-14'tür. [Yürütme kaydı](https://github.com/ibrahimguney/ileri-istatistik-uygulamalari/actions/runs/34123341464) ve [sürümlenmiş R doğrulama raporu](bolumler/b18/R_DOGRULAMA.json) ayrıca incelenebilir. Bu R kontrolü SPSS yürütmesi değildir.

## Kalan kontroller

- PDF başlık güncellemesinin Prism/LaTeX kaynaklarına aktarılması.
- B01–B18 için alt başlık, görev, tablo, formül ve sayısal sonuçların ayrıntılı karşılaştırması.
- B18 dışındaki R bölümleri ile SPSS, PROCESS ve AMOS yürütmelerinin sürüm ve çıktı kayıtlarıyla doğrulanması.

## Referans dosyanın kimliği

- Güncellenmiş PDF SHA-256: `ac1b9bd7bd0604ee319fbb0b37cb2789c2e5c98bb2530bbc87fdba661f623a08`
- Başlık güncellemesi öncesi PDF SHA-256: `47c0c233bfce35aea59a1402b18cf292c4eb5743fa920d31624dbc010f8fdf89`
- Denetlenen depo başlangıcı: `52a206de7dca5b5a8b536ea0f4240b195bc536b4`.
