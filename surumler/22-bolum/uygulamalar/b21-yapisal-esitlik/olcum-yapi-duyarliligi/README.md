# Ölçüm ve yapısal varsayım duyarlılığı — Revizyon 24

```bash
python dogrula.py
python analiz.py
```

Ana veri/kod ve2000 çekilişli bootstrap sonuçları korunur. Aynı önceden
incelenmiş1316 B kaydı, kaynak SHA ve puan anahtarı doğrulanarak kullanılır.

## MIMIC türü ölçüm duyarlılığı

Ana modelde K'dan göstergelere doğrudan yollar0'dır. A1'e ve sonra A1+A2'ye
doğrudan K yolları ekleyen iki keşifsel senaryo bütün ölçüm/yapısal kısımla
yeniden kestirilir. Bunlar tek tip (uniform) DIF için duyarlılık örnekleridir;
çok gruplu yük/eşik/artık değişmezliğinin yerine geçmez. A5 yükü dahil önceki
değişmezlik sorunlarının tamamını çözmez. K→A1 yolunu serbest bırakmak,
A1'in1'e sabit yükünü veya latent birimin tanımını kaldırmaz.

std.nox dolaylı çarpımları ana/A1/A1+A2 için.190225/.185939/.161933;
doğrudan yollar.023679/.027912/.051931, toplamlar yaklaşık.2139'dur.
Ki-kare215.021837/203.760900/192.441685; sd39/38/37.
Yeni senaryolar seçilmiş ana model, nedensel DIF veya yanlılık kanıtı değildir.
Önceki2000 çekilişli aralıklar yeni senaryolara aktarılmaz; yeni bootstrap veya
aralık üretilmedi. Aynı B'deki önceki bulgular kullanıldığından doğrulayıcı test değil.

## Aynı uyumla farklı yapısal çarpım

Ana gizil modelde K'ya koşullu A/C kovaryansı [[u,w],[w,v]] olsun.
u=.08663657,v=.25622574,w=.05209155. a=.16095276,
toplam=.10882178. Varsayılan rho=Cor(zeta_A,zeta_C) için:

- psi_C(rho)=(v−w²/u)/(1−rho²)
- b(rho)=w/u−rho*sqrt(psi_C(rho)/u)
- c_prime(rho)=toplam−a*b(rho)

Her rho'da yeni yapısal artık kovaryansı rho*sqrt(u*psi_C) konur.
Tüm gözlenen11×11 kovaryans ve ki-kare215.021837 aynıdır; RAM hesabı doğrular.
rho0/.3/.6 için std.nox çarpım.190225/.029919/−.192082 olur.
Nokta çarpımının sıfır olduğu rho=.349627; bu rho tahmini veya güven
aralığının sıfırı içerme eşiği değildir. Rho−.3 örneği de JSON/CSV'de verilir.

Rho veriyle kestirilmedi; her rho için belirsizlik/bootstrap hesaplanmadı.
b ve artık ilişkisini ek kısıt olmadan birlikte serbest kestirmek burada
tekil çözüm vermez: aynı kovaryansın farklı ayrıştırmaları vardır.
Eski bağımsız-artık R² ayrıştırması bu senaryolara otomatik taşınmaz.
Bu, ölçüm hatası modellemenin ölçülmemiş karıştırıcılığı çözmediğini gösterir;
nedensel doğal dolaylı etki tanımlandığı iddiası yoktur.

İki duyarlılık ailesi ayrı çalıştırılır; MIMIC+rho birleşik model seçilmez.
K iki kaynak kodunun göstergesidir; evrensel cinsiyet sınıflaması veya müdahale
değişkeni değildir. Normal kuramlı/ yaklaşık sürekli yaklaşım; yeni ek yalnız
Python. R/Amos, sağlam/ordinal kestirim, seçim düzeltmesi ve yeni doğrulama yoktur.
