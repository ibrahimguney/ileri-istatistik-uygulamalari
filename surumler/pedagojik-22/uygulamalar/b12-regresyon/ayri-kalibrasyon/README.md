# Ayrı kalibrasyonla split conformal tahmin öğretimi

Kaynak üst dizinin dondurulmuş UCI ilk80 CSV'si; SHA-256 eski özetle denetlenir.
Yeni ölçüm yok. Eğitim1–40 (sıfır not korunur), kalibrasyon41–60, kontrol61–80.
Önceki60 kayıtlık ana model bu ayrı deneye dönüştürülmez; eski sonuçlar korunur.

```sh
python uygulamalar/b12-regresyon/ayri-kalibrasyon/dogrula.py
python uygulamalar/b12-regresyon/ayri-kalibrasyon/analiz.py
```

40 eğitim kaydı: sabit7.167985, eğim.470810. m20/alpha.05 için k20,
en büyük mutlak kalibrasyon hatası q2.876083. Model kalibrasyondan sonra
yeniden kurulmaz. G1=12 nokta12.817702, split aralık[9.9416,15.6938].
Aynı40 kaydın klasik bireysel aralığı[9.9660,15.6694]; katsayılar SciPy,
klasik aralıklar statsmodels ile kontrol edilir. İki yöntem son20'de18/20
kapsar; bu oran geleceğe ait garanti veya dış doğrulama değildir.

Değiştirilebilir kalibrasyon/gelecek çiftler altında nominal garanti marjinaldir;
her x, her alt grup veya bütün20 yeni kişiye eşzamanlı garanti değildir.
Kaynak sırası/tek okul bunu kanıtlamaz. Zaman/küme kayması giderilmez.
Rank düzeltmesi k=ceil((m+1)(1-alpha)); k>m ise eşik sonsuz, sonlu max'a
sessizce çevrilmez. Sıradan enterpolasyonlu yüzdelik kullanılmaz.

Yedi test: OLS SciPy, sıra düzeltmesi, küçük m'de sonsuz eşik, rol kesişimi/
geçersiz tasarım, kontrol yanıtlarının aralığa sızmaması, kalibrasyonun
katsayıyı değiştirmemesi, pozitif affine yanıt dönüşümü. Yeni ek yalnız Python;
R/SPSS, normalize skor, küme/zaman/çapraz conformal ve koşullu kapsama yok.
Çıktılar: `sonuclar/ozet.json`, `sonuclar/kalibrasyon.csv`, `sonuclar/kontrol.csv`.
Lei ve ark. (2018): https://doi.org/10.1080/01621459.2017.1307116 .
