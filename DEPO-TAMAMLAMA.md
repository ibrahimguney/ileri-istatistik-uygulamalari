# Depo tamamlama — 25 Ekim 2026

Depo: https://github.com/ibrahimguney/ileri-istatistik-uygulamalari
Değişiklik: https://github.com/ibrahimguney/ileri-istatistik-uygulamalari/pull/4

## Bulgular ve yapılanlar

Eski depo 18 bölümlük sıralamayı taşıyordu. Güncel kitap 22 bölümdür; özellikle 6. bölümden itibaren numaralar farklı konulara karşılık gelebilir. Eski yollar korunarak `surumler/22-bolum/` altında güncel paket oluşturuldu. Özel GitHub deposuna yönlendiren bölüm açılışları yerine doğrudan öğrenci sayfaları hazırlandı.

22 bölümün veri açıklaması, görevleri, raporlama rehberi, çözümleri, temiz çalışma defteri, analiz başlatıcısı, beklenen sonuçları ve doğrulama durumu eklendi. Asıl uygulamaların veri ve kodları özgün baytlarıyla korundu. Çoklu atama ek uygulaması da taşındı. Tüm paketi kapsayan öğrenci ZIP'i ve sabitlenmiş Python paket sürümleri eklendi.

Yerel yürütmede 22 Python analizi ve çoklu atama kontrolleri geçti. 22 defter sözdizimi, 313 HTML bağlantısı ve 458 Markdown bağlantısı doğrulandı. Sayısal referans değerler değiştirilmedi; teknik sürüm/süre alanları ve bağımsız gradyan/amaç/kovaryans kontrolleri bulunan durdurma bayrağı ayrı değerlendirildi. R, SPSS ve Amos bu teslimde çalıştırılmadı.

Tam kitap metni/PDF'si ve ECLS-K SAV/DAT dosyaları öğrenci deposuna eklenmedi. Veri lisansları ve kod lisansının kapsamı korundu. Depo görünürlüğü değiştirilmedi.

## Yayın durumu

PR #4 GitHub CI testi başarılı oldu ve `a5c082e47b84e47397821c697c0c472d238a905a` ile ana dala birleştirildi. Pages Smoke Test (40182857982) ise ana adresin yedi denemede HTTP 404 dönmesi nedeniyle başarısız oldu; bölüm adresleri bu aşamada sınanamadı. Bu durumun kesin ayar nedeni API üzerinden görülemiyor. Depo görünürlüğü özel olarak korundu.

Gerekli sonraki kontrol: https://github.com/ibrahimguney/ileri-istatistik-uygulamalari/settings/pages adresinde Build and deployment / Source ayarı, Branch `main`, Folder `/ (root)` ve hesabın özel depoda Pages desteği kontrol edilmelidir. Pages yayımlandıktan sonra Actions / Pages Smoke Test / Run workflow ile 22 adres ve ZIP doğrulanmalıdır. Bu araç bağlantısı Pages yönetim ayarlarına yazma yeteneği sunmuyor.

Kitabın mevcut karekodları eski kökü kullanmaktadır. Yayın doğrulanmadığı için bu teslimde PDF değiştirilmedi. Doğrulama sonrasında yeni kök `https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/surumler/22-bolum` olacak ve PDF yeniden derlenecektir. Hedefler `karekod-hedefleri.csv` dosyasındadır.
