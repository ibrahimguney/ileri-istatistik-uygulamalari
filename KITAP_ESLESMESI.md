# Kitap–depo eşleştirmesi

Kontrol tarihi: 7 Eylül 2026. Referans: İbrahim Güney, *İleri İstatistik Uygulamaları*, `ileri-istatistik-izü6.pdf`. Sayfalar PDF görüntüleyicisinin sıra numarası değil, kitapta basılı sayfalardır.

Bu kayıt bölüm sırası, başlıklar ve öğrenci paketinin dosya kapsamı içindir. Bütün formüllerin, tabloların, alıştırmaların ve sayısal değerlerin kitapla tek tek karşılaştırıldığı anlamına gelmez. Python analiz ve notebook yürütmeleri ayrıca `DOGRULAMA.json` içinde kayıtlıdır.

## Bölüm eşleştirmesi

| Bölüm | Kitaptaki başlık | Başlangıç sayfası | Depodaki başlık | Öğrenci paketi |
|---|---|---:|---|---|
| [B01](bolumler/b01/README.md) | İstatistiksel Mekanizma | 1 | İstatistiksel Düşünme: Sorudan Kanıta | 8/8 dosya mevcut |
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

## B01 başlık farkı

Referans PDF’nin içindekilerinde bölüm adı “İstatistiksel Mekanizma”, 1.2 başlığı ise “İstatistiksel Mekanizma: Sorudan Kanıta” olarak yer alıyor. Depodaki bölüm başlığı “İstatistiksel Düşünme: Sorudan Kanıta”dır. Önceki yazar kararında 1.2 için “İstatistiksel Düşünme Süreci” benimsenmiştir. Depo eski PDF başlığına geri çevrilmedi; sonraki kitap derlemesinde başlık ve içindekiler birlikte kontrol edilmelidir.

B05, B06, B07, B11, B15, B16 ve B17 depo başlıklarında açıklayıcı ek, kısaltma veya sadeleştirme vardır; tabloda iki biçim ayrı gösterilmiştir.

## Atıflar ve kaynaklara erişim

Sekiz bölüm README dosyasındaki 68 sohbet içi dosya atfı GitHub üzerinde çözümlenmiyordu. Bunların yerine bu eşleştirme kaydına giden kitap bölümü bağlantıları kondu. Bu bağlantılar okura bölümün kitap içindeki yerini gösterir; her paragraf için ayrı sayfa doğrulaması veya yeni bir dış kaynak doğrulaması değildir. Veri kaynakları ve lisanslar ilgili bölümün `VERI.md` dosyasında korunur. Tam kitap dosyası depoya eklenmemiştir.

## Kalan kontroller

- Kitabın güncel derlemesinde B01 ve 1.2 başlıklarının kontrolü.
- B01–B18 için alt başlık, görev, tablo, formül ve sayısal sonuçların ayrıntılı karşılaştırması.
- R, SPSS, PROCESS ve AMOS yürütmelerinin sürüm ve çıktı kayıtlarıyla doğrulanması. Bu ortamda Rscript bulunmadığından R çalıştırılmış olarak işaretlenmedi.

## Referans dosyanın kimliği

- SHA-256: `47c0c233bfce35aea59a1402b18cf292c4eb5743fa920d31624dbc010f8fdf89`
- Denetlenen depo başlangıcı: `52a206de7dca5b5a8b536ea0f4240b195bc536b4`.
