# Bölüm 18 — IBM SPSS Uygulamaları

Bu klasör, *İleri İstatistik Uygulamaları* kitabının 18. bölümüne eşlik eden öğrenci çalışma paketidir.

Bölümün amacı yalnız SPSS menülerini ezberlemek değildir. Amaç, **veriyi doğru içe aktarmak, aktif filtre/ağırlık/split durumunu denetlemek, doğru analiz birimini korumak, çıktının doğru satırını okumak ve işlemi Syntax ile yeniden üretilebilir hale getirmektir.**

## Öğrenme hedefleri

Bu çalışmayı tamamladığınızda:

1. CSV içe aktarımında değişken türü ve ondalık ayarlarını denetleyebilir,
2. `sleep` verisinde ID üzerinden doğru eşleştirme yapabilir,
3. eşli t-testinde betimsel, korelasyon ve fark testi tablolarını birbirinden ayırabilir,
4. `ToothGrowth` verisinde `dose=1` filtresini bilinçli biçimde uygulayabilir,
5. bağımsız t-testinde Levene sonucunu otomatik yöntem seçme anahtarı olarak kullanmadan iki varyans modelini okuyabilir,
6. `FILTER`, `WEIGHT` ve `SPLIT FILE` durumlarının analiz örneklemini nasıl değiştirebildiğini açıklayabilir,
7. eksik bir eş olduğunda geçerli çift sayısının neden değiştiğini gösterebilir,
8. menü adımlarını SPSS Syntax ile denetlenebilir bir analiz kaydına dönüştürebilir,
9. çıktıyı akademik raporlama diline çevirebilirsiniz.

## Kitap bölümüyle eşleşme

| Kitap başlığı | Depodaki karşılığı |
|---|---|
| 18.3 Oturum Sözleşmesi | `SPSS-KONTROL-LISTESI.md`, `analiz.sps` |
| 18.4 Gerçek Veriyi İçe Aktarma | `sleep.csv`, `ToothGrowth.csv`, `VERI.md` |
| 18.5 Eşli Test | `sleep.csv`, `analiz.sps`, `analiz.py` |
| 18.6 Bağımsız Test | `ToothGrowth.csv`, `analiz.sps`, `analiz.py` |
| 18.7 Durum Deneyi | `sleep_eksik.csv`, filtre/ağırlık/split örnekleri |
| 18.8 Yöntem Haritası | `GOREVLER.md` ve bölüm sonu karar etkinliği |
| 18.9 Çıktı Okuma ve Teslim | `RAPORLAMA.md`, `SPSS-KONTROL-LISTESI.md` |

## Önerilen çalışma sırası

1. `VERI.md` — veri kaynaklarını ve analiz birimini okuyun.
2. `SPSS-KONTROL-LISTESI.md` — SPSS oturumunu temizleyin ve durum ayarlarını kontrol edin.
3. `GOREVLER.md` — görevleri önce kendiniz tamamlayın.
4. `analiz.sps` — menü yerine/yanında çalıştırılabilir SPSS Syntax kaydı oluşturun.
5. `calisma.ipynb` — SPSS sonuçlarınızı bağımsız sayısal kontrollerle karşılaştırın; bu defter SPSS'in yerine geçmez.
6. `RAPORLAMA.md` — sonuçları akademik dile dönüştürün.
7. `COZUMLER.md` ve `beklenen.json` — en son kontrol amacıyla kullanın.

## Ana uygulamalar

### 1. `sleep`: eşli t-testi

Veri uzun biçimde 20 satır içerir fakat **10 kişiye** aittir. Aynı ID'nin `group=1` ve `group=2` ölçümleri eşleştirilir. Ana fark yönü:

`group 2 − group 1`

Kontrol değerleri yaklaşık olarak:

- geçerli çift: 10,
- ortalama fark: 1.58,
- fark SS: 1.230,
- *t*(9) = 4.062,
- iki yönlü *p* = .00283,
- %95 GA: [0.700, 2.460].

Bu sonuç 20 bağımsız kişi analizi değildir.

### 2. `ToothGrowth`: bağımsız t-testi

Ana öğretim karşılaştırması yalnız `dose=1` satırlarında OJ ve VC grupları arasındadır.

- filtre öncesi kayıt: 60,
- `dose=1` sonrası kayıt: 20,
- OJ: n=10, ortalama=22.70,
- VC: n=10, ortalama=16.77,
- ortalama farkı OJ−VC=5.93.

SPSS bağımsız t-test tablosunda eş varyans varsayılmış ve varsayılmamış satırları birlikte verir. Bu bölümde **Welch satırı ana karşılaştırma olarak okunur**; Levene testi otomatik aç/kapa düğmesi gibi yorumlanmaz.

### 3. Eksik eş ve değişen n

`sleep_eksik.csv`, yalnız öğretim amacıyla `ID=10, group=2` değerinin eksik bırakıldığı türetilmiş kopyadır. Dosyada yine 20 satır vardır; ancak geçerli eşli analiz **9 çift** üzerinden yürür. Eski 10-çift farkını yeni dosyaya taşımayın.

## SPSS ve Python doğrulamasının rolleri

- `analiz.sps`: SPSS'te izlenebilir analiz yolu ve oturum durumu kontrolleri.
- `analiz.py`: aynı sabit veriler üzerinde sayısal kontrol değerlerini üretir ve GitHub Actions tarafından otomatik doğrulanır.

Python sonucunun SPSS yazılımının bizzat çalıştırıldığı anlamına gelmediğini unutmayın. SPSS'e özgü menü/çıktı doğrulaması kullanıcı tarafından SPSS içinde yapılmalıdır.

## Bilimsel yorum sınırları

- `sleep` tarihsel öğretim verisidir; sonuçlar klinik tedavi önerisi değildir.
- `ToothGrowth` hayvan verisidir; insan doz önerisine dönüştürülemez.
- Filtre, ağırlık veya split file ayarı araştırma tasarımını değiştirmez; yalnız aktif analiz kümesini/hesabı etkiler.
- Ağırlıklandırma gözlenmemiş yeni bağımsız kişiler yaratmaz.
- SPSS çıktısındaki *p* değeri tek başına bilimsel önem göstergesi değildir.
