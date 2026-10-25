# Profil olasılığı, farkı ve kalibrasyon ayrımı

Üst dizindeki UCI ilk80 yaş/not CSV'si; normalleştirilmiş SHA-256 doğrulanır.
İlk60 kayıtta19 olayla aynı cezasız Logit modeli korunur; son20'de5 olay.
Olay G3≥14 öğretim hedefidir, resmî geçme sınırı değildir.

```sh
python uygulamalar/b13-coklu-lojistik/olasilik-kalibrasyon/dogrula.py
python uygulamalar/b13-coklu-lojistik/olasilik-kalibrasyon/analiz.py
```

16 yaş/G1=12 olasılık.085985, G1=13 olasılık.329304; fark.243319,
delta SH.114630, yaklaşık Wald aralık[.01865,.46799]. OR5.219 sabitken
olasılık farkı başlangıç profiline bağlıdır. Tam katsayı kovaryansı kullanılır.
Noktasal olasılık GA'ları expit(eta±1.96SE_eta); binom GLM ile denetlenir.
Bunlar gelecekteki0/1 sonuç aralığı, birlikte güven bandı veya nedensel etki değildir.

Kontrol20'nin sabit logitleri c=.5/1/2 ile cebirsel dönüştürülür. Üçünde de
AUC.760/.50 doğruluk.850; Brier.13998/.13186/.13564, log-kayıp
.46328/.53429/.82157. c2 ortalama.26486 gözlenen.25'e daha yakın olsa
da bu bütün düzeylerde kalibrasyon değildir. Kontrolde c seçimi, yeniden
kalibrasyon uyumu veya kullanım önerisi yok. Log-kayıp kararlı logaddexp ile.

Yedi test: sıralama/kalibrasyon ayrımı, uç logitte sayısal kararlılık, profil
kovaryansı, delta gradyanının sayısal türevi, fark tersleme, aynı profilde
sıfır fark, geçersiz metrik girdisi. AUC ayrıca ortalama sıralarla denetlenir.
19/5 olay küçük örneklem; model-normal/delta aralıkları yaklaşık. Kalibrasyon
eğrisi/eğimi, performans güven aralıkları, ceza, bootstrap veya dış doğrulama
yok. Yeni ek yalnız Python; R/SPSS yeniden çalıştırılmadı. Çıktılar:
`sonuclar/ozet.json`, `sonuclar/profil-araliklari.csv`, `sonuclar/sirala-ve-kalibre-et.csv`.
Van Calster ve ark. (2019): https://doi.org/10.1186/s12916-019-1466-7 .
