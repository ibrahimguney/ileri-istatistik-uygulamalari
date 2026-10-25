# Aynı doz desteğinde hedef dağılımı

Üst dizinin mevcut tasarım/OLS/HC3 fonksiyonları kullanılır. Kaynak B06
ToothGrowth60 CSV'sidir; normalleştirilmiş SHA-256 denetlenir. Doz ön-test
değildir. Hiçbir hayvan veya ölçüm eklenmez; üç hedef yeni gözlem grupları değil.

```sh
python uygulamalar/b14-kovaryans-analizi/hedef-dagilim/dogrula.py
python uygulamalar/b14-kovaryans-analizi/hedef-dagilim/analiz.py
```

Doz(.5,1,2) için sabit ağırlıklar eşit(1/3,1/3,1/3), düşük(.6,.3,.1),
yüksek(.1,.1,.8). Her iki gruba aynı ağırlık uygulanır. Bunlar gerçek dış
anakütle tahmini veya önkayıt değildir; küçük p seçimi için arama yapılmaz.
Hücre farkları5.25/5.93/−.08; hedef farkları3.700/4.921/1.054.
OLS üçlü aile aralıkları[1.3833,6.0167],[2.1995,7.6425],[-2.2059,4.3139].
HC3/t yaklaşık aralıklar[1.2579,6.1421],[2.0534,7.7886],[-2.6047,4.7127].

Hücre/ayrı eğim için üç hedef tek aile; ortak modelde aynı kontrast olduğundan
aile1. Modeller arası arama ve eski doz aileleri için ortak kontrol iddiası yok.
Farklı hedefler genel olarak aynı parametrenin sağlamlık koşusu değildir. Tam
kontrast kovaryansı kullanılır; aralık uçları ağırlıklandırılmaz. Hücre modeli
ara dozda tanımlanmaz; gözlenen hücreleri ağırlıklandırmak ara doz üretmez.

Her altı hücrede en az2 gözlem gerekir; eksik destek sessizce tamamlanmaz.
Ağırlıklar biliniyor kabul edilir; tahmin edilse belirsizliği ayrıca gerekirdi.
Nedensel taşıma, bootstrap veya dış popülasyon verisi yok. Yeni ek yalnız
Python; R/SPSS yeniden çalıştırılmadı. Eski ana kod/veri/sonuçlar korunur.
Yedi test: dengeli ham fark, tek noktaya ağırlık, geçersiz ağırlık, satır
sırası, grup tersleme, eksik hücre reddi, doğrusal ortalamanın cebirsel özdeşliği.
Çıktılar: `sonuclar/ozet.json`, `sonuclar/hedef-karsilastirmalari.csv`.
Kitabın yeni ön-test/değişim tartışması Senn (2006):
https://doi.org/10.1002/sim.2682 . Dozdan değişim puanı üretilmez.
