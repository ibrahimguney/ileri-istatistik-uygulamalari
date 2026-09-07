# B18 — Raporlama ve çıktı okuma rehberi

## 1. Önce analiz birimi ve etkin durum

Bir SPSS tablosunu yorumlamadan önce şu sırayı izleyin: doğru kaynak dosyası → bağımsız birim → geçerli n → filtre/ağırlık/SPLIT FILE → eksik değer kuralları → model/hipotez → tahmin/SH/sd/p/güven aralığı → sınırlılık → yürütme kaydı.

`.000` görüntüsü p'nin sıfır olduğu anlamına gelmez; uygun durumda `p < .001` yazılır. İki yönlü p'yi sonucu gördükten sonra yarıya indirmek aynı analiz planı değildir.

## 2. Eşli testte üç tabloyu ayırın

- **Paired Samples Statistics:** iki koşulun ortalama, s ve geçerli çift sayılarını verir.
- **Paired Samples Correlations:** aynı kişilerin iki ölçümü arasındaki doğrusal ilişkiyi sınar. Bu tablonun p'si ortalama fark testinin p'si değildir.
- **Paired Samples Test:** fark ortalaması, SH, güven aralığı, t, sd ve fark hipotezinin p'sini verir. Ana eşli karşılaştırma bu tablodur.

### Örnek rapor

“Tarihsel arşivdeki 10 tam çiftte koşul 2 eksi koşul 1 ortalama farkı 1.58 saatti (farkların s'si 1.23). Bağımsız kişiler ve normal fark modeli altında eşli t testi `t(9)=4.062`, iki yönlü `p=.0028`, %95 GA `[.700, 2.460]` verdi. Sıfır fark korunmuş, kayıt dışlanmamıştır. `dz=1.285` olarak hesaplandı. Bu sayılar Python referans hesabıdır; SPSS sonucu ancak gerçek SPSS oturumu çalıştırılıp kaydedildiğinde öyle adlandırılacaktır.”

## 3. Bağımsız testte iki satırı ayırın

1 mg/gün ToothGrowth karşılaştırmasında Welch ana yöntemdir. Student satırı karşılaştırma amacıyla tutulur. Levene p değerini “otomatik anahtar” gibi kullanıp daha küçük p veren satırı seçmeyin.

Örnek teknik özet: OJ−VC `5.93`, Welch `t=4.032770`, `sd=15.357672`, `p=.001038`, %95 GA `[2.802148, 9.057852]`.

## 4. Karşı örnekleri ana sonuç diye raporlamayın

- ID≤5 filtresi yeni bağımsız çalışma değildir.
- Her kayda ağırlık 2 vermek 20 bağımsız kişi yaratmaz.
- İki hücrenin gizlendiği dosya bir öğretim senaryosudur; gerçek kayıp değildir.
- Değişmiş koşullarla eski fark sütunu birlikte kullanılmaz.

## 5. Teslimde yürütme dili

**Doğru:** “`analiz.sps` hazırlanmıştır; SPSS çalıştırılmamıştır. Sayısal kontrol `analiz.py` ile üretilmiştir.”

**Doğru — gerçek oturumdan sonra:** “SPSS [sürüm] ile [tarih] tarihinde `analiz.sps` çalıştırıldı; Viewer/SPV çıktısı ve uyarı kaydı arşivlendi. Sonuçlar `beklenen.json` referansıyla karşılaştırıldı.”

**Yanlış:** “Syntax dosyası var, dolayısıyla SPSS doğrulandı.”

## 6. Son kontrol

Raporunuzda kaynak, analiz birimi, geçerli n, fark/grup yönü, eksik/dışlama, filtre-ağırlık durumu, model, tahmin, belirsizlik, etki tanımı, sınırlılıklar ve yazılım/yürütme kaydı bulunmalıdır.
