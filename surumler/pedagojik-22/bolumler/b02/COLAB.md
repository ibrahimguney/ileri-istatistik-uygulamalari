# Bölüm 2 — GitHub ve Google Colab ile çalışma

1. [Colab’da çalıştır](https://colab.research.google.com/github/ibrahimguney/ileri-istatistik-uygulamalari/blob/main/surumler/pedagojik-22/bolumler/b02/colab.ipynb) bağlantısını açın; Google hesabınızla giriş yapın.
2. Kendi düzenlemelerinizi saklamak için **Dosya → Drive'a bir kopyasını kaydet** seçin.
3. CPU çalışma zamanı yeterlidir. **Çalışma zamanı → Tümünü çalıştır** veya hücrelerin
   solundaki çalıştır düğmelerini sırayla kullanın. İlk çalıştırmada internet gerekir.
4. Sonuç tablosunu ve iki grafiği okuyun; defterdeki kısa soruları yanıtlayın.
5. Son hücreden sonra Dosyalar panelini yenileyin ve `b02-atolye-ciktilar.zip`
   dosyasının menüsünden indirin. Geçici oturum kapanmadan çıktıları alın.

GitHub kaynakların ve sürümlerin ana yeridir; Colab defterleri de aynı depoda tutulur.
Bu defter Bölüm 2 başlangıç atölyesidir. Diğer 21 bölümün de ayrı Colab defterleri vardır; yerel uygulamalar korunur.
Colab'da R/SPSS/Amos yürütüldüğü iddia edilmez.

## Veri ve sürüm

Veri commit'i: `047d96c3d18ef77bc127ca5b106f6a64d3083e79`.
80 kaynak-sıralı GP okul kaydı; G1 ve G3; UCI Student Performance, CC BY 4.0.
Ayrıntılar [veri açıklamasında](VERI.md). Hash uymuyorsa veriyi değiştirerek
veya kontrolü kaldırarak devam etmeyin. Mevcut dosyayı ve bağlantıyı inceleyin.

Defter her çalışmada Python ve paket sürümlerini çıktı kaydına yazar. Colab
ortamının sürümleri sabitlenmez; dokuz sayısal/veri kontrolü uyumsuzlukları yakalar.
Yalnız eksik paketler kurulur. Yerel sabitlenmiş analiz ortamı için öğrenci
paketindeki `requirements-tested.txt` ayrıca korunur.

## Sorun giderme

- Bağlantı hatasında veri hücresini yeniden çalıştırın; kaynak URL hücrede görünür.
- Hücre sırası hatasında oturumu yeniden başlatıp baştan tümünü çalıştırın.
- Veri hash hatasında `b02-atolye/kaynak-notlar.csv` dosyasını doğrulayın;
  yanlış yerel dosyayı kaldırıp sabit kaynaktan yeniden indirin.
- Sonuçlar uyuşmuyorsa kaynak, hücre değişiklikleri ve sürüm kaydını inceleyin.
- Kaydetme, Colab kullanım koşulları ve çalışma zamanı sınırları Google hesabınıza bağlıdır.

Defter kodu temiz geçici Python ortamında yürütülerek denetlenir; bu kayıt
Google Colab arayüzünde yapılmış bir kullanıcı oturumu olarak sunulmaz.
