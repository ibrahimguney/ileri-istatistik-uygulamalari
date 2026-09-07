# İleri İstatistik Uygulamaları

## Kitap için öğrenci uygulama materyalleri

Bu depo, **Prof. Dr. İbrahim Güney** tarafından hazırlanan *İleri İstatistik Uygulamaları* kitabına eşlik eden öğrenci çalışma ortamıdır.

Burada kitabın tam metni değil; **Bölüm 1–18 için veri setleri, uygulama kodları, çalışma defterleri, görevler, çözümler ve akademik raporlama rehberleri** yer alır.

> **Önerilen kullanım:** Kitapta ilgili bölümü çalışın → aşağıdan bölümü seçin → veri açıklamasını okuyun → görevleri çözün → analizi çalıştırın → sonuçları yorumlayın → akademik raporlamayı tamamlayın.

## Bölümünüzü seçin

| Bölüm | Konu | Uygulamaya git |
|---|---|---|
| **B01** | İstatistiksel Düşünme: Sorudan Kanıta | [Bölümü aç](bolumler/b01/README.md) |
| **B02** | Betimsel İstatistik | [Bölümü aç](bolumler/b02/README.md) |
| **B03** | Veri Hazırlama | [Bölümü aç](bolumler/b03/README.md) |
| **B04** | Hipotez Testleri | [Bölümü aç](bolumler/b04/README.md) |
| **B05** | Güç Analizi ve Örneklem Planlama | [Bölümü aç](bolumler/b05/README.md) |
| **B06** | Korelasyon | [Bölümü aç](bolumler/b06/README.md) |
| **B07** | Regresyon | [Bölümü aç](bolumler/b07/README.md) |
| **B08** | Çoklu ve Lojistik Regresyon | [Bölümü aç](bolumler/b08/README.md) |
| **B09** | Aracılık ve Düzenleyicilik | [Bölümü aç](bolumler/b09/README.md) |
| **B10** | Parametrik Testler | [Bölümü aç](bolumler/b10/README.md) |
| **B11** | Varyans Analizi | [Bölümü aç](bolumler/b11/README.md) |
| **B12** | Parametrik Olmayan Testler | [Bölümü aç](bolumler/b12/README.md) |
| **B13** | Ölçek Uyarlama ve Güvenirlik | [Bölümü aç](bolumler/b13/README.md) |
| **B14** | Faktör Analizi | [Bölümü aç](bolumler/b14/README.md) |
| **B15** | Doğrulayıcı Faktör Analizi | [Bölümü aç](bolumler/b15/README.md) |
| **B16** | Yapısal Eşitlik Modeli | [Bölümü aç](bolumler/b16/README.md) |
| **B17** | Kovaryans Analizi | [Bölümü aç](bolumler/b17/README.md) |
| **B18** | IBM SPSS Uygulamaları | [Bölümü aç](bolumler/b18/README.md) |

**Kapsam:** Öğrenci uygulama deposu artık kitabın **Bölüm 1–18** yapısının tamamına karşılık verir. Kitabın tam metni bu depoda yayımlanmaz.

## Her bölümde nasıl çalışacağım?

Bölümlerde genel olarak aşağıdaki öğrenme yolu izlenir:

**Problem → Veri → Yöntem seçimi → Analiz → Görselleştirme → Yorum → Akademik raporlama → Çözüm**

Dosyaları şu sırayla kullanmanız önerilir:

1. **`README.md`** — Bölümün amacı, öğrenme hedefleri, çalışma akışı ve önemli yorum sınırları.
2. **`VERI.md`** — Verinin kaynağı, değişkenleri, seçim/aktarım bilgileri ve kullanım sınırları.
3. **`GOREVLER.md`** — Analize başlamadan önce çözmeniz gereken öğrenci görevleri.
4. **`calisma.ipynb`** — Kod ve yorum alanlarını sizin tamamlayacağınız çalışma/kontrol defteri.
5. **`analiz.py` / `analiz.R` / `analiz.sps`** — Bölümün yeniden üretilebilir analizleri. Yazılım desteği bölüme göre değişir.
6. **`RAPORLAMA.md`** — Bulguları bilimsel/akademik bir metne dönüştürme rehberi.
7. **`COZUMLER.md` ve `beklenen.json`** — Çalışmanızı tamamladıktan sonra kontrol amacıyla kullanacağınız referanslar.

B18 ayrıca SPSS oturum durumları için **`SPSS-KONTROL-LISTESI.md`** içerir.

> **Önce görevi çözün, sonra çözüme bakın.** Bu depo yalnız sonuç üretmek için değil, analiz kararlarını ve bilimsel yorumlamayı öğrenmek için hazırlanmıştır.

## Hızlı başlangıç

### 1. Depoyu indirin

Yalnız tek bir Python, R veya SPSS Syntax dosyasını indirmek yerine depoyu bütün olarak kullanmanız önerilir. Bölüm analizleri veri ve yardımcı dosyalara ihtiyaç duyabilir.

### 2. İlgili bölümü açın

Örneğin istatistiksel düşünme bölümünü çalışıyorsanız:

`bolumler/b01/`

SPSS uygulamalarını çalışıyorsanız:

`bolumler/b18/`

klasörüne gidin ve önce bölüm `README.md` dosyasını okuyun.

### 3. Python analizi

Gerekli paketleri depo kökünde kurmak için:

```sh
python -m pip install -r requirements.txt
```

Bir bölümü depo kökünden çalıştırma örneği:

```sh
python bolumler/b01/analiz.py
```

Bölüm klasörünün içindeyseniz:

```sh
python analiz.py
```

Her bölümün kendi `requirements.txt` dosyası varsa, bölümün doğrulanmış ortamı açısından öncelikle o dosyayı dikkate alın.

### 4. R, SPSS ve diğer yazılımlar

R, SPSS, PROCESS, AMOS veya diğer yazılım yolları her bölümde aynı değildir. İlgili bölümün `README.md`, `DOGRULAMA.json` ve varsa yazılım notlarını kontrol edin.

B18'de `analiz.sps`, SPSS menü adımlarını denetlenebilir Syntax kaydına dönüştürür; `analiz.py` ise aynı sabit veriler için bağımsız sayısal kontrol üretir.

**Hazırlanmış bir R/SPSS/AMOS dosyasının bulunması, o yazılımda analizin çalıştırılmış ve doğrulanmış olduğu anlamına gelmez.**

## Öğrenme yaklaşımı

Bu materyallerde amaç yalnız “hangi düğmeye basılacağını” göstermek değildir. Öğrencinin şu sorulara cevap verebilmesi hedeflenir:

- Araştırma sorum nedir?
- Analiz birimim nedir?
- Verim nereden geliyor?
- Hangi yöntem bu soruya uygundur?
- Yöntemin varsayımları ve sınırlılıkları nelerdir?
- Katsayı, p değeri, güven aralığı veya etki büyüklüğü ne söylüyor?
- Grafik sonuçla uyumlu mu?
- Sonuç tek tek gözlemlere veya model kararlarına duyarlı mı?
- İstatistiksel ilişkiyi nedensellik olarak yorumluyor muyum?
- Bulguyu akademik bir metinde nasıl raporlamalıyım?
- Yazılım oturumunda filtre, ağırlık veya bölünmüş analiz sonucu değiştirmiş olabilir mi?

Bu nedenle her bölümde hesaplama kadar **yorumlama, duyarlılık, sınırlılık, yeniden üretilebilirlik ve akademik raporlama** da önemlidir.

## Çıktılar ve teknik doğrulama

Analizler bölüme göre `sonuclar/` ve `grafikler/` klasörlerinde dosya üretebilir. Bu iki klasör aynı amaçla kullanılmaz:

- **`sonuclar/`**: depoda sürümlenmiş **referans/doğrulama çıktılarıdır**. Kendi çalışmanızı tamamladıktan sonra kontrol amacıyla kullanılabilir. Analizi yerelde yeniden çalıştırdığınızda bu dosyalar değişebilir; öğrenci ödevi veya kişisel raporlarınızı buraya kaydetmeyin.
- **`grafikler/`**: yeniden üretilebilir çalışma çıktılarıdır ve **varsayılan olarak Git tarafından izlenmez**. Analiz çalıştırıldığında yerelde yeniden oluşabilir.

Kendi tablo, grafik, `.spv` ve raporlarınızı depo dışındaki kişisel klasörünüzde tutmanız önerilir. Ayrıntılı bakım kuralları için [CIKTI_POLITIKASI.md](CIKTI_POLITIKASI.md) dosyasına bakın.

Referans sayılar bölüm `beklenen.json` dosyalarında, gerçek çalıştırma ve yazılım doğrulama durumu ise bölüm `DOGRULAMA.json` dosyalarında tutulur. Toplu teknik kontrol bilgileri kökteki [DOGRULAMA.json](DOGRULAMA.json) dosyasında yer alır.

## Veri, kaynak ve kullanım sınırları

Her bölümün `VERI.md` dosyası veri kaynağını, seçimini, aktarım geçmişini, varsa lisans bildirimini ve yorum sınırlarını ayrıca açıklar. Bir bölümün veri lisansı otomatik olarak diğer bölümlere veya bütün depoya uygulanmaz.

Simülasyon verileri gerçek katılımcı verisi olarak sunulmamalıdır. Bu depo yeni özel öğrenci kayıtları, kimlik bilgileri veya kitabın tam metni için bir paylaşım alanı değildir.

Kod ve özgün öğrenci materyalleri için yazar adına genel bir açık kaynak lisansı seçilmemiştir. Ayrıntılar için [KULLANIM.md](KULLANIM.md) dosyasına bakın.

## Teknik ve yayınlama bilgileri

Bu README öğrenciler için ana giriş noktasıdır. Yayınlama ve teknik bakım ayrıntıları öğrenci çalışma akışından ayrı tutulur:

- [Kullanım ve kaynak sınırları](KULLANIM.md)
- [Çıktı dağıtım politikası](CIKTI_POLITIKASI.md)
- [Teknik doğrulama kaydı](DOGRULAMA.json)
- [Yayınlama notları](YAYINLAMA.md)
- [Web ana sayfası](index.html)

## Son söz

Bu depo, kitabın yerine geçen bir içerik arşivi değil, kitabı **uygulayarak öğrenmeyi** destekleyen bir çalışma ortamıdır.

Bir bölümde hedef yalnız doğru sayıya ulaşmak değildir:

**Doğru soruyu kurmak → doğru veriyi anlamak → uygun yöntemi seçmek → analizi yeniden üretmek → sonucu doğru yorumlamak → sınırlılıkları görmek → bilimsel biçimde raporlamak.**
