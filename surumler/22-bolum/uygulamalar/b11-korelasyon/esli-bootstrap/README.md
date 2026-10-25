# Aynı satırları koruyan korelasyon bootstrap'ı

Kaynak B12'nin dondurulmuş ilk80 CSV'sidir; ilk60 GP kaydı, sıfır not dahil.
Kaynak SHA-256 eski B11 özetiyle eşleştirilir; yeni ölçüm yok. Rastgele/temsili
örneklem değil; iid satır bootstrap'ı bir model varsayımıdır. Küme bilgisi yoktur.

```sh
python uygulamalar/b11-korelasyon/esli-bootstrap/dogrula.py
python uygulamalar/b11-korelasyon/esli-bootstrap/analiz.py
```

Seed20261025, 20000 tekrar: bütün öğrenci satırları, iki katsayı için aynı çekiliş;
Spearman sıraları her çekilişte ham notlardan yeniden hesaplanır. Dejenere tekrar
varsa sessizce atılmaz, hata verilir; bu veride0.

| Hedef | Tahmin | Yaklaşık percentile %95 |
|---|---:|---:|
| Pearson | .7466 | [.6216,.9091] |
| Spearman | .8311 | [.7064,.9092] |
| rs−r | .0845 | [-.0865,.2018] |

Ayrı marjinal aralıklar; birleşik %95 kapsama değil. Aynı kişilerdeki iki farklı
hedef, bağımsız Pearson katsayısı testine sokulmaz. Sıfırı içeren fark aralığı
yöntem doğruluğu/eşdeğerlik kanıtı değildir. BCa, kapsama simülasyonu, küme
bootstrap'ı ve bağımlı Pearson-eşitliği testi yapılmadı.

İlk satır7164 tekrarda yok (Pearson medyanı.8675), 12836'da var (medyan.7200).
Bunlar koşullu bootstrap dağılımları; anakütle aralığı/yeni doğrulama grubu değil.
G1² duyarlılığı: Pearson.8391524, Spearman.8310857. Cebirsel Ydagger=X+5
öğretim kopyasında r=1, her fark5; yeni not veya uyum analizi değildir.

Yedi test: SciPy katsayıları, affine/işaret dönüşümü, monoton sıra, satır sırası,
aynı katsayıda sıfır fark, geçersiz/dejenere örnek reddi, korelasyon/uyum ayrımı.
İlk beş bootstrap örneğinde SciPy ile katsayılar ayrıca karşılaştırılır.
Yeni ek yalnız Python; R/SPSS yeniden çalıştırılmadı. Çıktılar:
`sonuclar/ozet.json`, `sonuclar/araliklar.csv`. Schober ve ark. (2018):
https://doi.org/10.1213/ANE.0000000000002864 .
