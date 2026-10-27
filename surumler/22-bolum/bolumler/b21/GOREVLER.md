# Bölüm 21 — görevler

Güncel Revizyon 24 görevleri; önce kendiniz çözün.

## D1–D3: Modelden Önce

1.  Bu bölümdeki 1316 kişi Bölüm 18 ve Bölüm 19 ile nasıl ilişkilidir? Bu küme YEM için bağımsız doğrulama mıdır?

2.  Gösterge hatası ile C’nin yapısal artığı nasıl ayrılır? İkisinin de çizilmesi neden gereklidir?

3.  A ve C arasındaki oka bakarak hangi nedensel iddia kurulamaz? Cinsiyet dışsal değişken olarak modele girince bu sorun ortadan kalkar mı?

# Rehberli ve Bağımsız Etkinlikler

## G1–G4: Rehberli Çözüm

1.  On göstergeden 55 bilgiyi ve ileri modeldeki 24 parametreyi sayın. Sıfır-yol kısıtı sd’yi nasıl değiştirir? Aracılık modelinde moment ve sd neden 66 ve 39’dur?

2.  Gerçek $\gamma$, $u$ ve $\psi$ değerlerinden C’nin toplam varyansını, standart yolu ve $R^2$’yi hesaplayın.

3.  Sıfır-yol modeline karşı LR testini bulun. Bu test ileri ve ters yönü karşılaştırıyor mu?

4.  A1’in yükü 1’e sabitken standart yükünün .292 olması nasıl mümkündür? Ham $\gamma$ ile standart $\beta$ için Wald $z$ değerlerinin neden farklı olduğunu açıklayın.

## B1–B3: Bağımsız Çözüm

1.  Aynı gizil kovaryanstan ters $\delta$ ve $\psi_A$ değerlerini bulun. Daha küçük ham ters yol daha zayıf uyum demek midir?

2.  Aracılık tablosundan std.nox ölçeğinde $ab$ ve toplam etkiyi $a$, $b$, $c'$ değerlerinden yeniden hesaplayın. Doğrudan etkinin aralığı sıfırı içerirken “tam aracılık bulundu” demek neden yanıltıcıdır?

3.  Dolaylı etki için delta ve bootstrap standart hatalarını karşılaştırın. Bootstrap’te neden kişi yeniden örneklenir ve bütün YEM yeniden kestirilir?

## H1: Hatalı Raporu Onarma

Altı iddiayı ölçekleme, varyans, uyum, eşdeğerlik, nedensellik ve bootstrap bakımından düzeltin.

## P1: Denetlenebilir YEM Protokolü

Yeni bir araştırma için yapı/gösterge, ölçüm zamanı, veri türü, ölçekleme, sıfır/eşitlik kısıtları, tanımlanabilirlik, kestirici, eksikler, örneklem planı, uyum/yol aralıkları, alternatif ve eşdeğer modeller ve yeniden üretim dosyalarını belirleyin. Aracılık planlanıyorsa zaman sırasını (örneğin üç ölçüm dalgası), bootstrap birimini, çekiliş sayısını ve başarısız çözüm kuralını yazın. Yapılmamış veri toplama veya model doğrulaması sonuç gibi sunulmaz. Rubrik: kuram/ölçüm 25, model/tanımlama 25, tahmin/belirsizlik 25, yorum/sınırlılıklar 15, yeniden üretim 10 puan.

Yanıtlar Ek F, Bölüm 21’dedir (s. kitaptaki ilgili sayfa).

## T1–T3: Ölçüm ve Yapısal Duyarlılık

1.  $K\to A1,A2$ yolları eklenince dolaylı ve doğrudan std.nox değerler nasıl değişir? Bu hesap neden çok gruplu değişmezliğin veya yeni doğrulamanın yerine geçmez?

2.  $\rho=.30$ senaryosunda kovaryans ve $T$ aynı kalırken dolaylı çarpım nasıl değişir? Aynı uyumdan hangi artık varsayımının doğru olduğu seçilebilir mi?

3.  $\rho=.349627$ neyin eşiğidir, neyin değildir? Ana bootstrap aralığını yeni MIMIC veya rho satırlarına aktarmak neden yanlıştır?

P1 planına ölçüm duyarlılığını, yapısal artık kısıtlarını, tanımlama gerekçesini ve her senaryonun ayrı belirsizlik/doğrulama gereğini ekleyin.

# Alıştırmalar

## Kolay Düzey

1.  YEM hangi iki temel bileşenden oluşur?

2.  Dolaylı etki nedir?

3.  $R^2$ değeri neyi gösterir?

4.  Bootstrap güven aralığı sıfırı içermiyorsa ne düşünülür?

5.  YEM’de iyi uyum indeksleri tek başına yeterli midir?

## Orta Düzey

1.  CFI=0.92, TLI=0.91, RMSEA=0.064, SRMR=0.055 bulunmuştur. Açıklayınız.

2.  Doğrudan etki anlamsız, dolaylı etki anlamlıdır. Nasıl yorumlanabilir?

3.  Bir içsel değişken için $R^2=0.18$ bulunmuştur. Açıklayınız.

4.  Bir yol anlamlı, standartlaştırılmış katsayısı 0.07’dir. Nasıl yorumlanır?

5.  Aracılık modelinde dolaylı etki için bootstrap neden önerilir?

## İleri Düzey

1.  Global uyum kabul edilebilir, fakat iki merkezi yol anlamsızdır. Ne sonuç çıkarılır?

2.  Araştırmacı modifikasyon indekslerine dayanarak çok yol ve hata kovaryansı ekliyor. Bu neden sorunludur?

3.  Yapısal modeli yorumlamadan önce ölçüm modelini değerlendirmek neden daha güvenlidir?

4.  Küçük örneklem ve karmaşık YEM hangi riskleri doğurur?

5.  Güçlü bir YEM raporunda en az beş unsur yazınız.

Yöntem belgelerine erişim: 6 Eylül 2026.

## Çekirdek öğrenme rotası

1. Ölçüm ve yapısal modeli ayırır.
2. Yol katsayısını, belirsizliği ve uyumu birlikte okur.
3. Eşdeğer uyumdan nedensel yön çıkarmaz.

**İleri rota:** Gizil aracılık, MIMIC ve artık-rho duyarlılığı; Bölüm 15 ve 19 sonrasında.

**Ç1:** Ok yönü ters çevrilince aynı kovaryans ve uyum elde edilmesi hangi yönün nedensel olduğunu belirler mi?

**Karar görevi:** Yapısal rho=0 veya .3 varsayımını seçin; toplam ve dolaylı ilişkiyi aynı uyum altında karşılaştırın.

[Rubrik ve teslim rehberi](RUBRIK.md).
