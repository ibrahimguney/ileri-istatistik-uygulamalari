# Google Colab ile 22 bölümlük atölye

Her bölüm sayfasındaki **Colab’da çalıştır** bağlantısını kullanın. Google hesabıyla
açın, Drive'a bir kopya kaydedin ve hücreleri sırayla yürütün. CPU yeterlidir.
Yerel çalışmak isterseniz tam öğrenci paketini açıp `calisma.ipynb` kullanın.

## Kaynak ve hesap

Bölüm 2 başlangıç defteri sabit commit'ten tek CSV indirir. Diğer 21 defter
`23acf4be23823aa139523c8f4db34cff248c285d` commit'indeki öğrenci ZIP'ini
SHA256 ile doğrular. Bu değişmeyen sürüm ana verileri, analizleri ve referansları
içerir. Her çalışma ayrı geçici kopyada yürür. Defterlerin kendileri güncel ana
daldadır; veri/kod kaynağı güncellenirse bu seçim ayrıca sürümlenir.

Bölüm 19–21 önce ortak Bölüm 18 girdilerini otomatik üretir. Ana analizler ve
ileri ekler ayrı yürür, mevcut sayısal karşılaştırma politikasıyla denetlenir.
Bölüm 2 başlangıç defteri kendi dokuz kontrolünü kullanır. Diğer defterler
Bölüm 3'teki çoklu atama dahil bütün kayıtlı ileri uygulamaları çalıştırır.

## Ortam ve sonuçlar

Bölüm 2 mevcut NumPy/pandas/SciPy/Matplotlib ortamını kullanır; sürümleri kaydeder.
Diğer defterlerde sınanmış beş analiz paketi ve PyMuPDF kullanılır. Çekirdek
sürümleri farklıysa ayrı Python ortamı kurulur; Colab'ın paketleri topluca
değiştirilmez ve oturum yeniden başlatmak gerekmez. Python 3.12+ önerilir.
İlk kurulum internet ve zaman gerektirir. Bootstrap ve yapısal modeller daha
uzun sürebilir; çekme sayıları hız için azaltılmamıştır.

Grafikler defter içinde görüntülenir. Çıktı ZIP'inde sonuçlar, grafikler,
çalışma/sürüm kaydı ve günlükler bulunur. Dosyalar panelinden indirin; oturum
kapanmadan çıktı ve defterinizi kaydedin. Kod Drive'a otomatik erişmez.

## Hata giderme

- İndirme hatası: interneti kontrol edip kaynak hücresini yeniden çalıştırın.
- Hash hatası: yerel kaynak ZIP/CSV'sini doğrulayın; hatalı önbelleği kaldırıp
  yeniden indirin. Kontrolü kaldırmayın veya hash'i dosyaya uydurmayın.
- Kurulum hatası: Python sürümünü ve pip çıktısını inceleyin; Python 3.12+ kullanın.
- Analiz/sayısal kontrol hatası: çıktı günlüklerini, veri ve paket sürümlerini
  inceleyin. Referans sonuçları değiştirmeyin.
- Yarım kalan işlem: ilgili hücreyi veya tümünü yeniden çalıştırabilirsiniz;
  her yeni hazırlık adımı yeni çalışma kopyası üretir.

## Doğrulamanın kapsamı

`tools/colab_defter_dogrula.py` her defteri gerçek ve ayrı bir Jupyter
çekirdeğinde çalıştırır; hücre hataları, sayısal referanslar, hücre içi resimler
ve çıktı arşivleri kontrol edilir. Ayrı ortam kurulumu/tekrar çalışma ayrıca sınanır.
Bu, Google hesabıyla yapılmış bir Colab arayüzü testi değildir. Böyle bir
oturum bu ortamda yürütülmedi. R/SPSS/Amos da çalıştırılmış sayılmaz.

GitHub Actions **Colab Notebook Execution** dört grupta tüm defterleri sınar.
Çalıştırılmış defterler ve raporlar bu iş akışının kanıt dosyalarında korunur.
Ana analiz ve veri dosyaları değiştirilmemiştir.

## Öğrenci kararı ve kısa savunma

Her defterin sonunda `karar_gunlugu` alanlarını kendi çalışmanızla doldurun.
Tek değişiklik, önce/sonra kanıtı, gerekçe, belirsizlik/sınır, savunma ve Ç1 yanıtı
istenir. Sonra çıktı ZIP’i hücresini tekrar çalıştırın. `ogrenci-karari.json`
ZIP’e ve çalışma kaydına eklenir. Alanların dolu olması otomatik akademik onay
değildir; öğretim elemanı kanıtı ve savunmayı değerlendirir.
