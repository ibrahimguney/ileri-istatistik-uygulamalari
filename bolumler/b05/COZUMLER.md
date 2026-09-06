# Bölüm 5 — Çözüm rehberi

Önce görevleri çözün; tüm sayılar beklenen.json içindedir.

## Ana plan ve duyarlılık

Sürekli çözüm63.765611 → grup başına64, toplam128 kişi. n63 güç=.795168;
n64 güç=.801460. Analize uygun kişi sayısı ile davet sayısı farklıdır.

| Senaryo | n birimi | Minimum |
|---|---|---:|
| d=.2 | Her grup | 394 |
| d=.3 | Her grup | 176 |
| d=.5 | Her grup | 64 |
| d=.8 | Her grup | 26 |
| Güç .90, d=.5 | Her grup | 86 |
| Alfa .01, d=.5 | Her grup | 96 |
| Üç test, alfa .05/3 | Her grup | 86 |
| Önceden seçilmiş tek yön, d=.5 | Her grup | 51 |
| Tahsis 2:1, d=.5 | n1/n2 | 48/96 |
| Eşli d_z=.5 | Tam çift/kişi | 34 |

Diğer girdiler ana planla aynı tutulmuştur. Tek yön seçimi sonuçtan sonra yapılmaz.
n40/grup ve d=.5 için güç .598147; .80 güç için saptanabilir d≈.634299.

## Kayıp beklentisi ile olasılığı ayırma

ceil(64/.85)=76/grup; bu yalnız beklenen sayı payıdır. Bağımsız %85 tutulma
modelinde iki grupta da en az64 kalma olasılığı .422777'dir. .90 olasılık hedefi
82/grup gerektirir: 81'de .896208, 82'de .935473. Bu da kesinlik değildir.

## Yayılım ve eşli plan

Tarihsel s_D=1.229995; Δ=.5 için d_z≈.406506 ve50 tam çift gerekir.
σ_D=1 ve1.5 alternatiflerinde sırasıyla34 ve73 tam çift gerekir. Tarihsel
ortalama1.58 yeni planın etkisi değildir. Eşit marjinal σ=1 ve Δ=.5 için
rho=.3,.5,.7 varsayımları sırasıyla46,34,21 tam çift verir.

## Yaklaşım ve hassasiyet

Fisher-z normal yaklaşımı, rho=.3: n85; n84 güç=.795517, n85=.800346.
Bu tam korelasyon gücü değildir. Yerine-konmuş σ ile .2σ yarı genişlik planı
194/grup verir; 193'te .200150σ, 194'te .199630σ. n64'te .349836σ'dır.
Güç ile hassasiyet farklı hedeflerdir; gerçekleşen aralık genişliği garanti edilmez.
Küme kurgu örneği DE=1+(20−1)×.05=1.95'tir; tam küme güç analizi yapılmamıştır.

## Denetimler ve yorum

Merkezsiz t/F ve statsmodels denetimleri aynı Python ortamındadır; R veya
G*Power çalıştırması sayılmaz. Sıfır etkide iki yönlü güç alfa; işaret simetrisi
iki yönlü test için korunur. Yanlış yöndeki tek yönlü alternatif aynı gücü vermez.
Örneklem büyüklüğü temsil veya nedensellik sağlamaz; plan girdileri ve kapsam
raporlanır. Bu pakette rastgele örneklem simülasyonu yoktur.