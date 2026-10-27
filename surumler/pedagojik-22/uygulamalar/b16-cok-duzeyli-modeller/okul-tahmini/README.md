# Hedef ortalama ve okul tahmini — Revizyon 19

Ana HSB verisi ve analizleri korunur. Bu ek, aynı öğrencilerle boş modeli
okul başına yeterli istatistiklerden REML profiliyle bağımsız hesaplar.

```bash
python dogrula.py
python analiz.py
```

Sonuçlar `sonuclar/ozet.json` ve `sonuclar/okul-tahminleri.csv` dosyalarındadır.
Öğrenci ağırlıklı ham ortalama 12.747853; eşit okul ağırlıklı ham ortalama
12.620755; boş modelin hassasiyet ağırlıklı sabiti 12.636974'tür.
Bu sonuncu ham öğrenci ortalaması veya tasarım ağırlıklı ulusal kestirim değildir.

Eşit büyüklük yaklaşımı DE=8.918571; gerçek örneklem büyüklükleriyle
DE=9.479471 ve yalnız ağırlıksız öğrenci ortalaması için n_eff=757.953649.
Ortak ICC modeli ve bağımsız okullar varsayılır. Başka bir katsayıya veya
karmaşık tarama tasarımına aynı etkili örneklem sayısı uygulanmaz.
Örneklenen öğrenci sayısı, okulun toplam öğrenci mevcudu `Size` değildir.

Okul seçimi başarıya göre değil, en küçük/en büyük örneklem büyüklüğüne
göredir; eşitlikte okul kimliği sırası kullanılır. Tahmin tablosu bir okul
başarı sıralaması değildir. Koşullu okul ortalaması belirsizliği ile aynı
okuldaki yeni öğrencinin belirsizliği ayrıdır. Yeni okul için rastgele
kesişim bilinmediğinden okul varyansı da tahmine eklenir.

**Sınır:** normal boş modelde tak-yerine-koy hesapları; sabit etki ve varyans
bileşenlerinin kestirim belirsizliği aralıklara eklenmez. Yeni okullarda
kalibrasyon sınaması veya çapraz doğrulama yapılmadı. Okul büyüklüğü sonuçla
ilişkiliyse standart rastgele-etki varsayımı sorgulanmalıdır; örneklem hedefi
ve gerekirse büyüklük/ağırlık modeli ayrıca tanımlanır. Tarama ağırlığı burada
uygulanmadı. Nedensel, güncel Türkiye veya ulusal temsil iddiası yok.

Yeni ek yalnız Python ile doğrulandı; R/SPSS yeniden çalıştırılmadı.
Yedi test: yoğun matris REML, eşit kümeler, blok kovaryans, doğrudan normal
koşullama, tahmin hedefleri, satır sırası ve sınır/geçersiz veri denetimleri.
