# GitHub ve GitHub Pages yayınlama notları

7 Eylül 2026 itibarıyla bu depo GitHub'da `main` dalında yayımlanmış ve GitHub Pages canlılığı doğrulanmıştır.

Canlı öğrenci giriş sayfası:

`https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/`

Bu belge artık ilk yükleme yönergesi değil, **bakım ve yeniden yayınlama rehberi** olarak kullanılmalıdır.

## 1. Depo kökü

Aşağıdaki kök dosyaları ve klasörleri korunmalıdır:

- `index.html`
- `assets/`
- `.nojekyll`
- `.gitignore`
- `README.md`
- `KULLANIM.md`
- `CIKTI_POLITIKASI.md`
- `DOGRULAMA.json`
- `bolumler/`
- `.github/workflows/`
- `tools/`

Tam kitap metni, özel öğrenci kayıtları, kimlik bilgileri veya erişim anahtarları bu depoya eklenmemelidir.

## 2. GitHub Pages

Yayın kaynağı:

- Source: **Deploy from a branch**
- Branch: **main**
- Folder: **/(root)**

Kök `index.html` öğrenci giriş sayfasıdır. `.nojekyll` korunmalıdır.

Canlı site kontrolü `.github/workflows/pages-smoke-test.yml` ile otomatik yapılır. Ana sayfa, B01 dahil örnek bölüm bağlantıları ve stil dosyası HTTP düzeyinde denetlenir.

## 3. Notebook doğrulaması

B01–B17 için 17 `calisma.ipynb` dosyasının teknik kontrolü `.github/workflows/notebook-validation.yml` üzerinden yapılır.

Kontroller:

- Jupyter JSON yapısı,
- Python sözdizimi,
- bölüm içi yerel dosya yolları,
- temiz öğrenci çıktısı (`execution_count=null`, `outputs=[]`),
- 17 notebookun gerçek çalıştırma testi.

## 4. Tam Python analiz doğrulaması

B01–B17 arasındaki 17 `analiz.py` dosyası `.github/workflows/analysis-validation.yml` ile gerçek olarak çalıştırılır.

Her bölümde analiz sonrası `sonuclar/ozet.json`, ilgili `beklenen.json` sözleşmesiyle karşılaştırılır. Sayısal değerlerde toleranslı karşılaştırma (`rtol=1e-7`, `atol=1e-8`), diğer yapılarda anlamsal/birebir karşılaştırma kullanılır.

Ham `git diff`, tek başına bilimsel geçme/kalma ölçütü değildir; ortam veya kütüphane sürümüne bağlı yazımsal farklar olabilir.

## 5. `sonuclar/` ve `grafikler/` dağıtım politikası

Ayrıntılı kurallar `CIKTI_POLITIKASI.md` dosyasındadır.

Özet:

- `sonuclar/` klasörlerindeki mevcut dosyalar **sürümlenmiş referans/doğrulama çıktılarıdır**.
- Bu dosyalar yalnız analiz/veri değişikliği bilinçli olarak yapıldığında, analiz yeniden çalıştırılıp farklar doğrulandıktan sonra güncellenmelidir.
- `grafikler/` klasörleri yeniden üretilebilir çalışma çıktılarıdır ve varsayılan olarak Git tarafından izlenmez.
- Öğrenci ödevleri ve kişisel raporlar `sonuclar/` veya `grafikler/` içine kalıcı depo içeriği olarak gönderilmemelidir.
- Kalıcı web görselleri gerekiyorsa bakım amacı açık olacak şekilde `assets/` altında tutulmalıdır.

## 6. `.gitignore`

Kök `.gitignore` şu tür geçici/kişisel dosyaları dışlar:

- `bolumler/b*/grafikler/`
- `ogrenci-ciktilari/`
- bölüm içi `ogrenci-ciktilari/`
- Jupyter checkpoint'leri
- Python `__pycache__` ve `.pyc` dosyaları
- temel işletim sistemi/editör geçici dosyaları

Not: `.gitignore`, daha önce Git tarafından izlenmeye başlanmış `sonuclar/` dosyalarını etkilemez. Bunlar bilinçli referans çıktıları olarak sürümlenmeye devam eder.

## 7. Bir analiz değiştiğinde bakım sırası

1. İlgili bölümün `VERI.md`, `analiz.py` ve/veya `analiz.R` değişikliğini inceleyin.
2. Analizi temiz ortamda yeniden çalıştırın.
3. `sonuclar/` farklarını `beklenen.json` ve bölüm `DOGRULAMA.json` ile karşılaştırın.
4. Sayısal değişikliklerin nedenini açıklayın; yalnız kütüphane sürümü farkını otomatik kabul etmeyin.
5. Gerekirse `README.md`, `RAPORLAMA.md`, `COZUMLER.md` ve `beklenen.json` dosyalarını birlikte güncelleyin.
6. Full Analysis Validation kontrolünün başarılı olduğunu doğrulayın.
7. Notebook Validation kontrolünün başarılı olduğunu doğrulayın.
8. Web dosyası/bölüm README değiştiyse Pages Smoke Test sonucunu kontrol edin.
9. Kök `DOGRULAMA.json` yalnız gerçekten doğrulanan yeni durumu yansıtacak biçimde güncellenmelidir.

## 8. Yayın sonrası kontrol

Önemli bir sürümden sonra en az şu kontroller önerilir:

- canlı ana sayfa,
- bölüm kartlarından örnek bağlantılar,
- notebookların açılması,
- veri dosyalarının erişilebilirliği,
- `sonuclar/` referanslarının beklenen sonuçlarla tutarlılığı,
- telefon/karekod üzerinden giriş sayfası görünümü.

## 9. Lisans ve kaynak sınırı

Kaynak bildirimleri, veri lisansları ve varsa GPL metinleri korunmalıdır. Bir veri setinin lisansı bütün depo koduna veya özgün öğrenci materyallerine otomatik uygulanmaz.

Ayrıntılar için `KULLANIM.md` ve her bölümün `VERI.md` dosyasına bakın.
