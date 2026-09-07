# GitHub'a toplu yükleme — Bölüm 2–17

6 Eylül 2026. Hedef depo:
https://github.com/ibrahimguney/ileri-istatistik-uygulamalari

Bu çalışma ortamında GitHub yazma kimliği bağlı değildir; yükleme/push yapılmadı.
Parola veya erişim anahtarını sohbet içine göndermeyin. Yetkili GitHub oturumunuzdan
veya kendi bilgisayarınızdaki GitHub Desktop/Git üzerinden yükleyin.

## 1. Doğru paketi seçin

`ileri-istatistik-uygulamalari-tam-yukleme.zip` dosyasını indirip açın.
İçindeki `index.html`, `assets/`, `bolumler/`, README ve diğer kök dosyaları hedef
GitHub deposunun **kökünde** olmalıdır; `ogrenci-deposu/` diye ek seviye oluşturmayın.
ZIP dosyasını tek dosya olarak yüklemek siteyi kurmaz. Gizli `.nojekyll` ve
`.gitignore` dosyalarını da koruyun. Tam kitap klasörünü yüklemeyin.

Kaynak bildirimleri ve GPL metinleri dağıtıma dahildir. Veri lisansını bütün
kod/metne uygulanmış saymayın; yazar adına yeni lisans seçilmedi. Ayrıntı KULLANIM.md.
Mevcut uzak dosyalar varsa yedekleyip farkları inceleyin; geçmişi zorla değiştirmeyin.

## 2A. GitHub Desktop ile tek aktarım

Yetkili hesabınızla hedef depoyu klonlayın. Açılmış tam ZIP'in içindekileri
klonun köküne kopyalayın. Changes listesinde yalnız öğrenci dosyaları olduğunu
kontrol edin. Açıklama olarak “Bölüm 2–17 öğrenci materyalleri” yazıp değişiklikleri
commit edin; ardından Push origin / Publish branch işlemini yapın. main dalını
hedefleyin; mevcut çalışma varsa önce eşitleyin. Kitabın çalışma deposunu push etmeyin.

## 2B. Tarayıcıyla, 100 dosya sınırını aşmadan

GitHub bir yüklemede en fazla 100 dosya kabul ettiğinden tam paketi tek seferde
sürüklemeyin. Ayrı `web-00-kok.zip`, `web-01-...zip` vb. parçalar da hazırlanır;
her biri en fazla 90 dosyadır. ZIP'leri ayrı ayrı açın ve şu sırada yükleyin:

1. Önce `web-00-kok.zip` içindekiler. Boş depoda “uploading an existing file”;
   dosyalar varsa “Add file → Upload files” yolunu kullanın.
2. Yükleme listesinde `index.html` ve `assets/site.css` gibi kök yolları kontrol edin.
   “Commit changes” ile kaydedin; ana dalın main olduğunu doğrulayın.
3. Sonra numara sırasıyla her bölüm parçasını açın. Her parça içindeki `bolumler`
   klasörünü depo kökünden yükleyin; klasör yapısını düzleştirmeyin.
4. Her yüklemeyi ayrı commit edin. Önceki parçanın klasörüne girerek yüklemeyin.
5. Gizli `.nojekyll` yüklenmediyse depoda “Add file → Create new file” ile
   kökte `.nojekyll` adlı boş dosyayı ekleyin.

Bu parçalar tam ZIP ile aynı dosyaları içerir; iki yöntemi üst üste uygulamanız gerekmez.

## 3. GitHub Pages

Tüm parçalar tamamlandıktan sonra **Settings → Pages** altında:
- Source: **Deploy from a branch**
- Branch: **main**
- Folder: **/(root)**
- **Save**

Dağıtımın başarıyla bitmesini bekleyin. Ayar için depo yönetim yetkisi gerekir.
Hedef site: https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/

## 4. Yayın sonrası denetim

Oturum açılmamış tarayıcıyla ana sayfa ve 16 bölümün tamamını açın.
CSV, kod, defter ve çözüm indirmelerini kontrol edin. Depoyu yeniden indirip
B02 ve B17 analizlerini çalıştırın; bölüm gereksinimlerine göre diğerlerini de sınayın.
Telefon ve PDF üzerinden karekodları deneyin. Yalnız gerçekten doğrulanan
bölümlerde yerel `ogrenciYayinHazirfalse` anahtarını değiştirmeyi değerlendirin;
bu yükleme hazırlığında kitabın yayın anahtarları değiştirilmemiştir.

## Resmî yönergeler

6 Eylül 2026'da kontrol edilen belgeler:
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site