# Bölüm 18 — SPSS Oturum ve Teslim Kontrol Listesi

Bu kontrol listesi, analiz komutundan önce ve teslimden hemen önce uygulanmalıdır.

## A. Dosyayı açmadan önce

- [ ] Hangi veri dosyasını kullanacağım belli.
- [ ] Analiz birimini bir cümleyle yazdım.
- [ ] Eşli mi bağımsız mı olduğunu belirledim.
- [ ] Ana fark yönünü belirledim (`group2-group1`, `OJ-VC` vb.).

## B. Veri içe aktarıldıktan sonra

- [ ] Satır sayısını kontrol ettim.
- [ ] Değişken adlarını ve türlerini kontrol ettim.
- [ ] Sayısal değişkenlerin yanlışlıkla string gelmediğini doğruladım.
- [ ] Ondalık ayracının doğru okunduğunu kontrol ettim.
- [ ] Eksik değer sayısını kontrol ettim.
- [ ] Kategori kodlarının beklenen değerlerle sınırlı olduğunu kontrol ettim.

## C. SPSS oturum durumu

Analizden önce şu üç durum özellikle kontrol edilmelidir:

- [ ] `FILTER OFF` veya bilinçli olarak tanımlanmış doğru filtre açık.
- [ ] `WEIGHT OFF` veya gerekçelendirilmiş doğru ağırlık açık.
- [ ] `SPLIT FILE OFF` veya gerekçelendirilmiş doğru split açık.

Bir önceki analizden kalan durum ayarı, sonraki analizin n'sini ve sonuçlarını sessizce değiştirebilir.

## D. `sleep` eşli test

- [ ] 20 uzun-format satırın 10 ID'ye ait olduğunu doğruladım.
- [ ] ID temelinde eşleştirme yaptım.
- [ ] Her ID için iki koşul bulunduğunu kontrol ettim.
- [ ] Ana fark yönünü `group2-group1` olarak tanımladım.
- [ ] Paired Samples Statistics tablosunu okudum.
- [ ] Paired Samples Correlations tablosunu test sonucu sanmadım.
- [ ] Paired Samples Test tablosundan fark, GA, t, df, p değerlerini aldım.

Kontrol: geçerli çift n=10, ortalama fark yaklaşık 1.58, t≈4.062, df=9, p≈.00283.

## E. `ToothGrowth` bağımsız test

- [ ] Tam veride N=60 olduğunu doğruladım.
- [ ] `dose=1` filtresinden sonra N=20 olduğunu doğruladım.
- [ ] OJ n=10 ve VC n=10.
- [ ] Levene tablosunu tanı bilgisi olarak okudum.
- [ ] “Equal variances not assumed” / Welch satırını ana sonuç olarak okudum.
- [ ] Filtreyi analiz sonrasında kapattım.

Kontrol: OJ ortalama 22.70; VC ortalama 16.77; fark 5.93; Welch t≈4.033; df≈15.358; p≈.00104.

## F. Eksik eş deneyi

- [ ] `sleep_eksik.csv` dosyasında toplam satır sayısının hâlâ 20 olduğunu gördüm.
- [ ] Geçerli eş sayısının 9'a düştüğünü gördüm.
- [ ] Ana veri setinin eski t-test sonucunu kopyalamadım.

Kontrol: n=9 çift; ortalama fark≈1.60; t≈3.684; df=8; p≈.00618.

## G. Teslimden önce

- [ ] Syntax dosyasını kaydettim.
- [ ] Çıktıda kullanılan filtre/ağırlık/split durumunu yazdım.
- [ ] Raporladığım n'nin dosya satır sayısıyla değil analiz birimiyle uyumlu olduğunu kontrol ettim.
- [ ] Fark yönünü raporda açıkça yazdım.
- [ ] Güven aralığı ve p değerini doğru satırdan aldım.
- [ ] İstatistiksel sonucu nedensellik veya klinik öneri olarak aşırı yorumlamadım.
- [ ] Kendi çıktı ve raporumu depo `sonuclar/` klasörüne kaydetmedim.
