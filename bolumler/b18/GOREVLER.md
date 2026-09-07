# Bölüm 18 — Öğrenci görevleri

Görevleri önce SPSS'te ve kendi yorumunuzla tamamlayın. Daha sonra `COZUMLER.md` ve `beklenen.json` ile kontrol edin.

## G1 — Oturum sözleşmesi

SPSS'i açtıktan sonra analizden önce aşağıdakileri kontrol edin ve kısa bir kontrol kaydı yazın:

- aktif veri seti,
- aktif filtre,
- aktif ağırlık,
- aktif Split File,
- eksik değer tanımları,
- analizde kullanılacak bağımsız birim.

**Soru:** Filtre veya ağırlığın açık olduğunu fark etmeden yapılan bir analiz neden teknik olarak doğru komutla çalışsa bile bilimsel olarak yanlış olabilir?

## G2 — `sleep.csv` içe aktarımı

1. `sleep.csv` dosyasını SPSS'e aktarın.
2. 20 satır ve 4 değişken bulunduğunu doğrulayın.
3. Her ID'nin iki kez geçtiğini kontrol edin.
4. Eşli test için veriyi ID temelinde geniş biçime dönüştürün.
5. `group2 − group1` fark yönünü açıkça belirleyin.

**Beklenen:** 10 geçerli çift.

## G3 — Eşli t-testi: üç tabloyu ayırın

SPSS eşli t-test çıktısında şu üç bölümü ayrı ayrı tanımlayın:

1. Paired Samples Statistics,
2. Paired Samples Correlations,
3. Paired Samples Test.

Aşağıdaki değerleri bulun:

- group1 ortalaması ve SS,
- group2 ortalaması ve SS,
- eşler arası korelasyon,
- ortalama fark,
- farkın %95 güven aralığı,
- t, df ve iki yönlü p.

Ardından tek paragraf akademik rapor yazın.

## G4 — `ToothGrowth.csv`: filtreli bağımsız t-testi

1. Dosyayı açın ve N=60 olduğunu doğrulayın.
2. Yalnız `dose=1` kayıtlarını filtreleyin.
3. Aktif analiz N'sinin 20 olduğunu doğrulayın.
4. OJ ve VC için grup ortalamalarını/SS'leri bulun.
5. Bağımsız t-testini çalıştırın.
6. Levene testini ve iki t-testi satırını ayrı ayrı okuyun.

**Ana raporlama satırı:** Welch / “Equal variances not assumed”.

## G5 — Levene otomatik anahtar değildir

Şu iki cümleden hangisinin daha doğru olduğunu gerekçelendirin:

A. “Levene p>.05 olduğu için eşit varyans satırı zorunlu olarak kullanılmalıdır.”

B. “Levene tanısal bilgi sağlar; Welch testi varyans eşitliğini zorunlu kılmadığı için önceden belirlenmiş ana yöntem olarak raporlanabilir.”

## G6 — Aynı dosyada farklı n

Aşağıdaki dört durumu karşılaştırın:

| Durum | Dosya/süzme | Beklenen analiz n |
|---|---|---:|
| Sleep uzun veri | `sleep.csv` satırları | 20 satır |
| Sleep eşli analiz | 10 ID | 10 çift |
| ToothGrowth tam veri | filtre yok | 60 kayıt |
| ToothGrowth dose=1 | filtre açık | 20 kayıt |
| Sleep eksik kopya | `sleep_eksik.csv` | 9 geçerli çift |

**Soru:** Neden “dosyada 20 satır var” ifadesi tek başına testin örneklem büyüklüğünü söylemez?

## G7 — Eksik kopyada eski farkı kullanmayın

`sleep_eksik.csv` dosyasını analiz edin.

- geçerli çift sayısını,
- ortalama farkı,
- t ve p değerini

bulun. Sonucu `sleep.csv` ana analiziyle karşılaştırın. Eski 10-çift sonucunu yeni dosyaya kopyalamanın neden yanlış olduğunu açıklayın.

## G8 — Ağırlıkla yeni kişi yaratılmaz

Bir analiz ağırlığı değişkeninin frekansları/katkıları değiştirebileceğini, ancak gözlenmemiş yeni bağımsız bireyler yaratmadığını açıklayan 3–4 cümlelik bir not yazın.

SPSS'te herhangi bir ağırlık denemesinden sonra `WEIGHT OFF` komutunun çalıştığını doğrulayın.

## G9 — Yöntem haritası

Bölüm 1–17'den beş farklı araştırma sorusu seçin. Her biri için:

- bağımlı değişken,
- bağımsız/gruplama değişkeni,
- analiz birimi,
- önerilen yöntem,
- SPSS'te kontrol edilmesi gereken kritik ayar

başlıklarıyla mini karar tablosu hazırlayın.

## G10 — Denetlenebilir analiz teslimi

Tesliminizde en az şunlar bulunsun:

- kullanılan veri dosyasının adı,
- aktif filtre/ağırlık/split durumu,
- analiz Syntax'ı,
- ilgili SPSS çıktı tabloları,
- kontrol sayıları,
- akademik raporlama paragrafı,
- yöntem ve genelleme sınırlılığı.
