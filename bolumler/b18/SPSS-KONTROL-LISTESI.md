# B18 — SPSS gerçek oturum kontrol listesi

Bu liste `.sps` dosyasının hazırlanmasını değil, **gerçek SPSS yürütmesini** belgelemek içindir.

- [ ] SPSS sürümü ve lisans kapsamı kaydedildi.
- [ ] Çalıştırma tarihi/saat bilgisi kaydedildi.
- [ ] `sleep.csv` ve `ToothGrowth.csv` kaynak bütünlüğü kontrol edildi.
- [ ] Ana oturum başında `FILTER OFF`, `WEIGHT OFF`, `SPLIT FILE OFF` durumu doğrulandı.
- [ ] CSV ayırıcı, UTF-8 ve ondalık nokta ayarları doğrulandı.
- [ ] Uyku dosyasında 10 ID ve ID başına iki koşul görüldü.
- [ ] `uyku_esli.csv` fark yönü `kosul2-kosul1` olarak yeniden kontrol edildi.
- [ ] Paired Samples Statistics, Correlations ve Test tabloları birbirinden ayrıldı.
- [ ] Ana eşli testte `n=10`, `t≈4.062128`, `sd=9`, `p≈.002832890`, GA≈`[.700114,2.459886]` bulundu.
- [ ] ToothGrowth analizinde yalnız `dose=1` filtresi altında OJ ve VC'de 10'ar kayıt kullanıldı.
- [ ] Welch satırı ana yöntem olarak okundu; Levene p'si eşitlik kanıtı olarak yazılmadı.
- [ ] Filtre kapatıldıktan sonra üç dozda 20'şer kayıt yeniden görüldü.
- [ ] `durum-deneyi.sps` çıktıları ana analizden ayrı tutuldu.
- [ ] Viewer/SPV çıktısı sürümlü adla kaydedildi.
- [ ] Uyarı ve hata mesajları teslim kaydına eklendi.
- [ ] Rapor, gerçek SPSS çıktısı ile Python referans hesabını açıkça ayırıyor.
