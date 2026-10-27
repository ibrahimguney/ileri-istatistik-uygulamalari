# Güvenirlik modeli ve belirsizlik — Revizyon 20

```bash
python dogrula.py
python analiz.py
```

## Gerçek veri: ortak kayıtlarda alfa farkı

Kaynak ilk100 IPIP/SAPA kaydı değişmez. A1/C4/C5 anahtara göre çevrilir.
On maddede tam olan aynı97 kişi iki hesapta da korunur. Ham alfa A=.627614,
C=.722686; C−A=.095072. Tohum202617,20000 ortak kişi-satırı bootstrap
tekrarında persentil %95 aralık[−.062180,.268615]; sıfır varyanslı tekrar0.
Satır çekimi A ile C arasındaki bağımlılığı korur; iki alt kümeyi ayrı
yeniden örneklemek başka bir hesap olur. Önceki99/98 kişilik özetler korunur.

Bu seçilmiş tam kayıtlarda iki alfa fonksiyonelinin farkıdır. Eşitlik/eşdeğerlik
kanıtı, daha geçerli yapı veya “C her koşulda daha güvenilir” sonucu değildir.
Seçim ve eksiklik yanlılığı bootstrap ile giderilmez; A/C farklı yapılardır.

## Bilinen parametreli öğretim modelleri

Bu modeller IPIP verisine uydurulmaz; yeni katılımcı yanıtı üretilmez.
Var(F)=1 ve F ile artıklar ilişkisiz. Birim ağırlıklı puanın hedefi yalnız
F bileşenidir; artıkların tamamı bu hedefe göre hata sayılır.

1. Beş eşit yük .7, hata varyansları .51: alfa=omega=.827703.
2. Yükler[.8,.7,.6,.5,.4], hata varyansları1−yük²: alfa=.733471,
   hedef puan güvenirliği/omega=.743802.
3. İkinci modelin ilk iki artığına .2 kovaryans eklenir: alfa=.750000,
   hedef faktör payı=.720000. Hata toplam varyansı, kovaryansları da içerir.
   Bağımsız hata formülünü kullanmak burada yanlış olur.

Genel puan w'X için hedef payı (w'lambda)²/[ (w'lambda)²+w'Theta*w ].
Bu tanım, bütün araştırmalarda artıkların kalıcı/rasgele anlamını belirlemez;
ölçme evreni ve hedef farklıysa güvenirlik tanımı da incelenir.
Bu karşı örnek, veri içindeki omega kestirimi veya model uyumu kanıtı değildir.

İkinci modelin toplam puan SEM'i sqrt(3.1)=1.760682. Aynı sabit gerçek puan,
eşit hata varyansları ve zamanlar arasında bağımsız normal hatalar varsayılan
iki ölçüm farkı için 1.96*sqrt(2)*SEM=4.880271 öğretim eşiğidir.
Bu veride tekrar ölçüm yoktur; klinik anlamlı değişim, tanı veya bireysel
karar eşiği doğrulanmamıştır. Alfa takılarak kişiye özel güven aralığı üretilmez.
Yeni ek yalnız Python; R/SPSS yeniden çalıştırılmadı.
