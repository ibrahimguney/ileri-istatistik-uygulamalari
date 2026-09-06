# Veri kaynağı ve hesap sözleşmesi

Bu CSV, kitap arşivindeki `bfi-ilk100-AC.csv` dosyasının aynı baytlarla alınmış
kopyasıdır. Kaynak: William Revelle, psych paketinin `bfi` gösterim verisi;
SAPA projesinde 2010 ilkbaharında toplanan IPIP yanıtlarının Rdatasets aktarımı.
Tam gösterim verisi 2800 kayıt içerir; burada yalnız ilk 100 kaydın A1–A5 ve
C1–C5 alanları vardır. Demografik değişkenler aktarılmamıştır.
Bu, John ve arkadaşlarının Big Five Inventory testi veya Türkçe uyarlama değildir.

- Veri tanımı: https://www.personality-project.org/r/html/bfi.html
- CSV aktarımı: https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/psych/bfi.csv
- Rdatasets kaynak/kullanım açıklaması: https://vincentarelbundock.github.io/Rdatasets/
- IPIP madde kullanım açıklaması: https://ipip.ori.org/newPermission.htm
- Kitap arşivinin aktarım notu: 5 Eylül 2026; bu paket: 6 Eylül 2026.

Uzak CSV ile otomatik hücre karşılaştırması bu pakette yapılmadı. Yerel
arşiv eşitliği, uzak kaynak doğrulaması veya temsili örnekleme kanıtı değildir.
İlk-sıra alıntısından Türkiye, klinik gruplar veya tüm SAPA katılımcıları
hakkında genelleme yapılmaz. Yanıt uydurulmamış, boş hücre doldurulmamıştır.

## Alanlar

| Alan | Tanım |
|---|---|
| `kaynak_satir` | Başlık hariç aktarım sırası, 1–100; benzersiz ve boş değil. |
| `kaynak_kayit` | Yayımlanmış CSV satır etiketi; benzersiz, boş değil; gerçek kişi kimliği değil. |
| `A1`–`A5` | Uyumlulukla ilişkilendirilen beş ordinal madde. |
| `C1`–`C5` | Sorumlulukla ilişkilendirilen beş ordinal madde. |

Madde yanıtları 1–6 tamsayıdır; boş hücre eksiktir. 0, 99, 2.5 ve metin
geçerli yanıt değildir. Makinece okunabilir sözlük: [veri_sozlugu.csv](veri_sozlugu.csv).
A1, C4, C5 yeni `_t` sütunlarında `7-x` ile anahtarlanır; ham sütunlar korunur.
`A_n`/`C_n` geçerli madde sayılarıdır. `A_ort5`/`C_ort5` beş tam yanıtla
ortalama; `_ort4` en az dört yanıtla duyarlılık ortalamasıdır. `_top5` yalnız
beş tam yanıtla toplamdır. 4/5 kuralı onaylanmış test kılavuzu değil, öğretim
karşılaştırmasıdır; eksik veri mekanizmasını çözmez.

Normalize LF SHA-256:
`8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557`.
Betik CRLF satır sonlarını LF'ye dönüştürüp sonda tek satır sonuyla denetler;
bu işlem ham dosyaya yazılmaz.

## Kullanım notu

Bölüm 2'nin CC BY 4.0 bilgisi bu farklı veriye uygulanmaz. IPIP maddelerinin
kullanım açıklaması her veri aktarımına otomatik lisans olarak genişletilmez.
Rdatasets veri lisansına ilişkin belirsizliği kendi kaynak sayfasında açıklar.
Bu pakette veri için yeni bir lisans atanmamıştır; kamusal paylaşım öncesinde
kaynak kullanım koşullarını ayrıca değerlendirin. Yazara ait kod ve öğrenci
metinleri için de yeni lisans seçilmedi. Kitabın tam metni dağıtılmaz.