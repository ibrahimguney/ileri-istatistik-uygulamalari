# Yayınlama — yazar için kontrol listesi

Bu klasör bağımsız öğrenci deposunun kökü olacak şekilde hazırlanmıştır.
Henüz otomatik GitHub yüklemesi, commit, push veya Pages ayarı yapılmamıştır.

## 1. Yüklenecek kapsam

`ogrenci-deposu` klasörünün **içindekileri** hedef GitHub deposunun köküne aktarın.
Klasörün kendisini bir alt klasör olarak yüklemeyin; `index.html`, `README.md`,
`requirements.txt`, `bolumler/` ve `assets/` GitHub deposunun kökünde olmalıdır.
`.nojekyll` dosyasını da dahil edin.

Kitap klasörünü, cevap anahtarının tam metnini, özel öğrenci kayıtlarını,
kimlik bilgilerini, erişim anahtarlarını veya yerel derleme dosyalarını yüklemeyin.
Mevcut izinlerle başka verilerin de paylaşılabileceğini varsaymayın.
Bu pilotun veri kaynağı ve alıntı tanımı `bolumler/b02/VERI.md` içindedir.
Kod/içerik lisansının yazar tarafından seçilmesi yayın öncesi ayrı bir karardır.

## 2. GitHub Pages

Hedef: https://github.com/ibrahimguney/ileri-istatistik-uygulamalari

Dosyaları yükleyip `main` dalı oluştuktan sonra:

1. Depoda **Settings → Pages** sayfasını açın.
2. **Build and deployment → Source → Deploy from a branch** seçin.
3. Dal **main**, klasör **/(root)** seçip **Save** ile kaydedin.
4. Pages dağıtımının başarıyla tamamlandığını kontrol edin.

Resmî rehber:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

Hedef bölüm adresi:
https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/bolumler/b02/

Bu adresin şimdiden çalıştığı iddia edilmez. Alt klasör/Pages kaynak seçimi
farklı yapılırsa kitaptaki karekod yanlış yere gidebilir.

## 3. Yayın sonrası doğrulama

- Oturum açılmamış bir tarayıcıda ana sayfayı ve Bölüm 2 sayfasını açın.
- CSV, Python, R ve notebook bağlantılarını indirin.
- Yeni indirdiğiniz depo kopyasında `python bolumler/b02/analiz.py` çalıştırın.
- Notların 80 kayıt olduğunu, ilk G1=0'ın korunduğunu ve kontrol değerlerini doğrulayın.
- Kitabın Bölüm 2 karekodunu hem telefondan hem PDF bağlantısından deneyin.
- Yalnız bu kontrollerden sonra kitap `main.tex` dosyasında
  `\ogrenciYayinHazirfalse` satırını `\ogrenciYayinHazirtrue` yapın.
  Bu anahtar yayın uyarısını kaldırır; GitHub'a bir şey yüklemez.
- Son baskıdan önce bağlantıyı bir kez daha sınayın. Bölüm URL'sini sabit tutun.

## 4. Sonraki bölümler

Bölüm 2'nin düzeni onaylandıktan sonra her bölümün kaynağı, kodu, görevleri,
çözümleri ve çalışma durumu ayrı doğrulanarak eklenir. Henüz olmayan sayfalara
kitapta karekod eklemeyin. Diğer bölümlerin verisi/sonuçları bu pilotta yoktur.

Yerel sayfa önizlemesi için depo kökünde `python -m http.server 8000` çalıştırıp
`http://localhost:8000/` adresini açabilirsiniz. Bu komut GitHub yayını yapmaz.

## Hazır ZIP ile aktarım

Çalışma alanında `ileri-istatistik-uygulamalari-yukleme.zip` hazırlanmıştır.
ZIP'i bilgisayarınızda açın; ZIP dosyasını tek dosya olarak depoya yüklemeyin.
Paketin içindeki dosya ve klasörleri depo köküne yükleyin.
Boş depoda “uploading an existing file”, dolu depoda “Add file → Upload files”
yolunu kullanın. `bolumler/` ve `assets/` dizinlerini düzleştirmeyin.
Gizli `.nojekyll` ve `.gitignore` dosyalarını da dahil edin.
“Commit changes” ile kaydedin; sonra yukarıdaki Pages ayarını yapın.

Bu ortamda GitHub yazma kimliği bulunmadığı için doğrudan aktarım yapılmadı.
Parola veya erişim anahtarını sohbet içine göndermeyin.

Resmî dosya yükleme rehberi:
https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository