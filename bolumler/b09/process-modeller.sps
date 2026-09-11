* B09 - PROCESS cagri taslagi; gercek SPSS/PROCESS yurutmesi bekliyor.
* Once analiz.sps dosyasini calistirin ve n=160 oldugunu kontrol edin.
* PROCESS resmi dagitimini ayrica indirin; macro bu depoda dagitilmaz.
* Asagidaki yolu resmi process.sps dosyanizin tam yoluyla degistirin.
INSERT FILE='C:/PROCESS/process.sps'.
DATASET ACTIVATE B09.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.

* Model 4: X=x, M=araci, Y=ymed; W bu modele girmez.
* Varsayilan persentil bootstrap kullanilir; cikti yontemini kontrol edin.
PROCESS vars=x araci ymed
 /y=ymed /x=x /m=araci /model=4
 /boot=5000 /seed=202610 /conf=95 /total=1.

* Model 1: X=x, W=w, Y=ymod; araci bu modele girmez.
* center=1: urun terimindeki surekli degiskenleri ortalamadan merkezler.
* moments=1: W icin ortalama ve +/-1 orneklem SS duzeylerini ister.
PROCESS vars=x w ymod
 /y=ymod /x=x /w=w /model=1
 /center=1 /moments=1 /conf=95.

* PROCESS surum basligini, n, merkezleme ve bootstrap dipnotlarini saklayin.
* Bilinmeyen secenek/komut hatasi varsa dogrulamayi basarili saymayin.
* Python bootstrap uclariyla birebir esitlik beklemeyin.
