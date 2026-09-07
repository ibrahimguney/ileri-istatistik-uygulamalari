# Bölüm 5 — Güç Analizi ve Örneklem Planlamayı Akademik Raporlama

Bu rehber, örneklem büyüklüğünü tek bir sayı olarak vermek yerine, bu sayının **hangi araştırma tasarımı, etki varsayımı, hata düzeyi, güç hedefi ve analiz birimi altında elde edildiğini** bilimsel olarak raporlamaya yardımcı olur.

Temel zincir:

**Araştırma hedefi → Tasarım → Test → Etki girdisi → α → Yön → Hedef güç → Tahsis → Minimum n → Kayıp → Duyarlılık → Hassasiyet → Yöntem sınırı → Akademik raporlama**

## 1. Güç analizinin zamanını ve amacını belirtin

Örneklem planlaması ideal olarak sonuçlar görülmeden önce yapılır.

Bu bölümde ana eğitim puanı senaryosu varsayımsaldır; gözlenmiş bir eğitim çalışmasının geriye dönük sonucu değildir.

Örnek ifade:

> Varsayımsal iki gruplu bir eğitim çalışması için, veri toplanmadan önce gerekli analiz edilebilir örneklem büyüklüğünü belirlemeye yönelik güç planı oluşturulmuştur.

## 2. Tasarımı açıkça tanımlayın

Ana plan:

- iki bağımsız grup,
- eşit varyanslı normal model,
- pooled Student t testi,
- iki yönlü test,
- eşit 1:1 tahsis.

Örnek ifade:

> Ana örneklem planı, eşit tahsisli iki bağımsız grubun ortalamalarını karşılaştıran iki yönlü pooled Student t testi için oluşturulmuştur.

Bu tasarım başka testlerin örneklem gereksinimini otomatik olarak vermez.

## 3. Ham ve standartlaştırılmış etkiyi birlikte belirtin

Ana girdiler:

- `Δ=5` eğitim puanı,
- `σ=10` puan,
- `d=Δ/σ=.50`.

Örnek ifade:

> Planlamada 5 puanlık varsayımsal grup farkı ve 10 puanlık ortak standart sapma kullanılmış, böylece standartlaştırılmış etki `d=.50` olarak tanımlanmıştır.

Bu değerlerin kaynağının öğretim senaryosu olduğu açıkça yazılmalıdır.

## 4. Etki girdisini gözlenen sonuç gibi sunmayın

`d=.50`:

- gözlenmiş bir eğitim etkisi değildir,
- gerçek etkinin garantisi değildir,
- klinik/eğitsel önem eşiği değildir.

Uygun ifade:

> `d=.50` planlama varsayımı olarak kullanılmış ve gerçek etkinin bilinen değeri olarak değerlendirilmemiştir.

## 5. Alfa, yön ve hedef gücü belirtin

Ana plan:

- α=.05,
- iki yönlü,
- hedef güç=.80.

Örnek ifade:

> Tip I hata düzeyi iki yönlü α=.05 ve hedef güç .80 olarak belirlenmiştir.

Bu üç bilgi verilmeden “gerekli n=64” ifadesi eksiktir.

## 6. n birimini mutlaka belirtin

Ana sonuç:

`64 kişi/grup`.

Toplam:

`128 analiz edilebilir kişi`.

Örnek ifade:

> Gerekli minimum örneklem büyüklüğü grup başına 64, toplam 128 analiz edilebilir kişi olarak bulundu.

Yalnız “n=64” yazmak belirsizdir.

## 7. Minimum tamsayıyı doğrulayın

Sürekli çözüm:

`63.765611`.

Kontrol:

- 63/grup → güç `.795168`,
- 64/grup → güç `.801460`.

Örnek ifade:

> Sürekli çözüm 63.77 kişi/grup olup tamsayı minimalitesi ayrıca kontrol edildi; 63 kişi/grup hedef gücün altında (`.795`), 64 kişi/grup ise üzerinde (`.801`) kaldığından minimum 64 kişi/grup seçildi.

Bu, yalnız yukarı yuvarlama değil, minimalite doğrulamasıdır.

## 8. Duyarlılık analizini raporlayın

Etki büyüklüğü belirsiz olduğundan tek senaryo yeterli değildir.

| d | n/grup |
|---:|---:|
| .20 | 394 |
| .30 | 176 |
| .50 | 64 |
| .80 | 26 |

Örnek ifade:

> Etki büyüklüğü duyarlılık analizinde gerekli grup başı örneklem `d=.20` için 394, `d=.30` için 176, `d=.50` için 64 ve `d=.80` için 26 olarak değişmiştir.

Bu tablo planın etki varsayımına ne kadar duyarlı olduğunu gösterir.

## 9. Hedef güç duyarlılığını raporlayın

`d=.50` için:

- güç .80 → 64/grup,
- güç .90 → 86/grup.

Örnek ifade:

> Hedef gücün `.80`den `.90`a çıkarılması gerekli örneklem büyüklüğünü 64'ten 86 kişi/gruba yükseltmiştir.

## 10. Alfa duyarlılığını raporlayın

`d=.50`, güç=.80:

- α=.05 → 64/grup,
- α=.01 → 96/grup.

Bu sonuç daha katı Tip I hata kontrolünün örneklem maliyetini görünür kılar.

## 11. Çoklu karşılaştırma düzeltmesini belirtin

Üç test için Bonferroni:

`α*=.05/3`

kullanıldığında:

`86 kişi/grup`

gerekir.

Örnek ifade:

> Üç planlı karşılaştırma için Bonferroni düzeltmesi (`α=.05/3`) kullanıldığında gerekli örneklem 86 kişi/gruba yükselmiştir.

Bu sonuç başka çoklu karşılaştırma yöntemlerinin sonucu olarak sunulmamalıdır.

## 12. Tek yönlü planı yalnız önceden gerekçelendirin

Önceden seçilmiş doğru yönlü tek taraflı testte:

`51 kişi/grup`

yeterlidir.

Ancak sonuç görüldükten sonra daha düşük örneklem gereksinimi veya daha küçük p için tek yönlü plana geçmek uygun değildir.

Örnek ifade:

> Tek yönlü alternatif yalnız araştırma hipotezinin veri görülmeden önce yönlü olarak belirlenmesi halinde ayrı bir planlama senaryosu olarak değerlendirilmiştir.

## 13. Eşit olmayan tahsisi doğru raporlayın

2:1 tahsis senaryosunda:

- n1=48,
- n2=96,
- toplam=144.

Örnek ifade:

> 2:1 tahsis varsayımında minimum grup büyüklükleri 48 ve 96 kişi, toplam örneklem 144 kişi olarak bulundu.

Bu sayı 1:1 tasarımın n'siyle karıştırılmamalıdır.

## 14. Eşli tasarımda n birimini değiştirin

`d_z=.50` için:

`34 tam çift/kişi`

gerekir.

Örnek ifade:

> Eşli tasarım için `d_z=.50` varsayımında gerekli örneklem 34 tam eşleşmiş kişi olarak hesaplandı.

Şunu yazmayın:

> “Her grupta 34 kişi gerekir.”

Çünkü aynı kişiler iki kez ölçülmektedir.

## 15. Bağımsız d ile d_z'yi karıştırmayın

Bağımsız grup d'si ortak grup içi standart sapmaya, `d_z` ise kişi-içi farkların standart sapmasına dayanır.

Aynı sayısal `.50` değeri aynı veri yapısı veya aynı örneklem büyüklüğü anlamına gelmez.

## 16. Tarihsel yayılımı pilot diye adlandırmayın

`sleep` verisinden:

`s_D=1.229995`

elde edilir.

Bu tarihsel arşiv değeridir; yeni pilot çalışma değildir.

Örnek ifade:

> Yayılım duyarlılığı için tarihsel sleep verisindeki eşleşmiş farkların standart sapması (`s_D=1.230`) ek bir senaryo girdisi olarak kullanılmış; bu değer yeni pilot veri olarak değerlendirilmemiştir.

## 17. Tarihsel ortalama farkı yeni etki olarak taşımayın

`sleep` verisindeki gözlenen ortalama fark `1.58` saattir.

Bu değer yeni çalışmanın beklenen etkisi olarak kullanılmamıştır.

Planlama etkisi ve tarihsel gözlenen etki farklı kavramlardır.

## 18. Yayılım duyarlılığını raporlayın

`Δ=.5` saat için:

- `σ_D=1` → 34 çift,
- tarihsel `s_D=1.229995` → `d_z≈.406506` → 50 çift,
- `σ_D=1.5` → 73 çift.

Örnek ifade:

> Eşli tasarımın yayılım duyarlılığında `.5` saatlik ham fark sabit tutulduğunda gerekli tam çift sayısı fark standart sapması 1, 1.230 ve 1.5 varsayımları için sırasıyla 34, 50 ve 73 olarak değişmiştir.

## 19. Eşleşme korelasyonu duyarlılığını raporlayın

Eşit marjinal σ=1 ve Δ=.5 varsayımı altında:

- ρ=.30 → 46 çift,
- ρ=.50 → 34 çift,
- ρ=.70 → 21 çift.

Bu sonuç gelecekteki korelasyonun bilindiği anlamına gelmez.

Örnek ifade:

> Eşleşme korelasyonuna yönelik duyarlılık analizinde varsayılan korelasyon yükseldikçe, bu model altında fark puanı varyansı azaldığından gerekli tam çift sayısı düşmüştür.

## 20. Kayıp düzeltmesini doğru tanımlayın

Basit `%15` kayıp düzeltmesi:

`ceil(64/.85)=76 kişi/grup`.

Bu hesap yalnız beklenen tutulma payına dayanır.

Uygun ifade:

> %85 tutulma varsayımı altında basit beklenen-sayı düzeltmesiyle başlangıç hedefi 76 kişi/grup olarak hesaplanmıştır.

“76 kişi alınırsa kesin 64 kalır” denmemelidir.

## 21. Kayıp olasılığını ayrıca raporlayın

Bağımsız Bernoulli `%85` tutulma modelinde 76 kişi/grup ile iki grupta da en az 64 kişinin kalma olasılığı:

`.422777`.

Bu çarpıcı fark, beklenen sayı düzeltmesinin olasılık garantisi olmadığını gösterir.

## 22. Hedef olasılık yaklaşımını raporlayın

İki grupta da en az 64 kişinin kalması için `.90` olasılık hedeflenirse:

- 81/grup → `.896208`,
- 82/grup → `.935473`.

Minimum `82 kişi/grup` olur.

Örnek ifade:

> Bağımsız %85 tutulma modeli altında her iki grupta da en az 64 analiz edilebilir kişinin kalması için en az %90 ortak olasılık hedeflendiğinde başlangıç örneklemi 82 kişi/grup olarak bulundu.

Bu da model altında bir olasılıktır, garanti değildir.

## 23. Sabit n için gücü raporlayın

`n=40/grup`, `d=.50` için:

`güç=.598147`.

Örnek ifade:

> Örneklem büyüklüğü 40 kişi/grupla sınırlandığında `d=.50` etkisi için iki yönlü testin planlanan gücü yaklaşık `.598` idi.

Bu, kaynak kısıtı ile bilimsel hedef arasındaki farkı görünür kılar.

## 24. Minimum saptanabilir etkiyi doğru yorumlayın

`n=40/grup` ve güç=.80 için:

`d≈.634299`.

Uygun ifade:

> 40 kişi/grup ile `.80` güce karşılık gelen minimum planlama etkisi yaklaşık `d=.634` idi.

Bu sayı gerçek etkinin alt sınırı değildir.

## 25. Korelasyon planının yaklaşık olduğunu belirtin

Fisher-z yaklaşımıyla `ρ=.30` için:

- n84 → güç `.795517`,
- n85 → `.800346`.

Minimum yaklaşık n85'tir.

Örnek ifade:

> Fisher-z normal yaklaşımı altında `ρ=.30` için `.80` güç hedefi yaklaşık 85 gözlem gerektirmiştir.

“Tam korelasyon güç analizi” veya “G*Power ile doğrulandı” yazılmamalıdır.

## 26. Güç ve hassasiyet hedefini ayırın

%95 t-aralığı için planlanan yarı genişlik `.2σ` hedefinde:

- 193/grup → `.200150σ`,
- 194/grup → `.199630σ`.

Minimum 194/gruptur.

Ana güç planındaki 64/grup için yarı genişlik `.349836σ`'dır.

Örnek ifade:

> Tahmin hassasiyeti ayrı bir planlama hedefi olarak değerlendirildi; %95 aralığın planlanan yarı genişliğini `.2σ` altında tutmak için 194 kişi/grup gerekti ve bu sayı `.80` güç hedefinden elde edilen 64 kişi/gruptan belirgin biçimde yüksekti.

Gerçekleşen güven aralığı genişliği garanti edilmez.

## 27. Küme tasarım etkisini sınırlı biçimde raporlayın

Kurgusal `m=20`, ICC=.05 için:

`DE=1+(20−1)×.05=1.95`.

Örnek ifade:

> Kurgusal küme örneğinde ortalama küme büyüklüğü 20 ve ICC=.05 varsayımıyla basit tasarım etkisi 1.95 olarak hesaplandı.

Ardından mutlaka:

> Bu hesap tam çok düzeyli/küme güç analizi değildir.

sınırı eklenmelidir.

## 28. Yazılım doğrulamasını doğru tanımlayın

Python'da merkezsiz F, merkezsiz t ve `statsmodels` denetimleri aynı hesap ortamında yapılmıştır.

Bunlar bağımsız yazılım doğrulaması değildir.

R kodu hazırlanmış ancak çalıştırılmamıştır. G*Power çalıştırılmamış ve SPSS çıktısı üretilmemiştir.

Uygun ifade:

> Referans hesaplar Python ortamında birden fazla sayısal yöntemle içsel olarak karşılaştırılmıştır; R ve G*Power ile bağımsız çalıştırma doğrulaması yapılmamıştır.

## 29. Örnek bütünleşik ana plan paragrafı

> Varsayımsal iki bağımsız grubun ortalamalarını karşılaştırmak üzere eşit tahsisli, iki yönlü pooled Student t testi için a priori örneklem planı oluşturuldu. Beş puanlık ham fark ve 10 puanlık ortak standart sapma varsayılarak `d=.50`, iki yönlü `α=.05` ve hedef güç `.80` kullanıldı. Sürekli çözüm 63.77 kişi/grup olarak elde edildi. Tamsayı minimalite kontrolünde 63 kişi/grup için güç `.795`, 64 kişi/grup için `.801` olduğundan minimum analiz edilebilir örneklem 64 kişi/grup, toplam 128 kişi olarak belirlendi. Etki büyüklüğü, alfa, hedef güç, tahsis ve kayıp varsayımları için ayrıca duyarlılık analizleri yürütüldü. Kullanılan etki ve yayılım değerleri planlama girdileridir ve gelecekteki gerçek etkiyi garanti etmez.

## 30. Örnek bütünleşik kayıp paragrafı

> %15 kayıp varsayımı altında basit beklenen-sayı düzeltmesi `ceil(64/.85)=76` kişi/grup verdi. Bununla birlikte bağımsız %85 tutulma modeli altında 76 kişi/grup başlangıç örneklemiyle her iki grupta da en az 64 kişinin kalma olasılığı yalnız `.423` idi. Ortak olasılığın en az `.90` olması hedeflendiğinde minimum başlangıç büyüklüğü 82 kişi/grup olarak bulundu (`P=.935`). Bu olasılık hesabı belirli bağımsız Bernoulli tutulma modeline dayanmakta olup gerçek kayıp sürecinin garantisi değildir.

## 31. Raporlama kontrol listesi

Teslimden önce kontrol edin:

- Güç analizinin amacı belirtilmiş mi?
- Tasarım ve test açık mı?
- Bağımsız/eşli tasarım doğru ayrılmış mı?
- Δ ve σ verilmiş mi?
- d'nin nasıl elde edildiği belirtilmiş mi?
- Etki girdisinin kaynağı açıklanmış mı?
- α belirtilmiş mi?
- Test yönü belirtilmiş mi?
- Hedef güç belirtilmiş mi?
- Tahsis oranı belirtilmiş mi?
- n birimi açık mı?
- 64/grup ile toplam 128 ayrılmış mı?
- Sürekli çözüm ve minimum tamsayı kontrolü doğru mu?
- n−1'in hedef gücün altında olduğu gösterilmiş mi?
- Etki büyüklüğü duyarlılığı raporlanmış mı?
- Güç ve alfa duyarlılığı raporlanmış mı?
- Bonferroni senaryosu doğru etiketlenmiş mi?
- Tek yönlü plan sonuçtan sonra seçilmemiş mi?
- 2:1 tahsis doğru n birimleriyle verilmiş mi?
- Eşli `d_z` bağımsız d ile karıştırılmamış mı?
- 34 tam çift 68 bağımsız kişi diye sunulmamış mı?
- `sleep` yayılımı yeni pilot diye adlandırılmamış mı?
- Tarihsel 1.58 yeni beklenen etki olarak kullanılmamış mı?
- Kayıp için beklenen sayı ve olasılık ayrılmış mı?
- 76/grup kesin yeterlilik diye sunulmamış mı?
- Minimum saptanabilir etki gerçek etki alt sınırı sayılmamış mı?
- Fisher-z yaklaşımı yaklaşık olarak etiketlenmiş mi?
- Güç ve hassasiyet planı ayrılmış mı?
- DE hesabı tam küme güç analizi diye sunulmamış mı?
- R/G*Power/SPSS çalıştırılmış gibi yazılmamış mı?
- Büyük n'nin temsil veya nedenselliği otomatik sağlamadığı belirtilmiş mi?

## Son mesaj

Örneklem büyüklüğü tek başına bilimsel bir cevap değildir. Her `n` şu sorularla birlikte anlam kazanır:

**Hangi tasarım? → Hangi test? → Hangi etki? → Etkinin kaynağı ne? → Hangi α? → Hangi güç? → Hangi yön? → Hangi tahsis? → n'nin birimi ne? → Kayıp nasıl ele alındı? → Sonuç varsayımlara ne kadar duyarlı?**

Bu nedenle iyi güç analizi:

**tek bir “gerekli n” sayısı üretmekten çok, planlama varsayımlarını görünür ve denetlenebilir hale getirir.**

Çalışmanızı [VERI.md](VERI.md), [GOREVLER.md](GOREVLER.md), [COZUMLER.md](COZUMLER.md) ve `beklenen.json` ile birlikte değerlendirin.