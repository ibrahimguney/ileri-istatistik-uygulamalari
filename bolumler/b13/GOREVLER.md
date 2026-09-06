# Bölüm 13 — Görevler ve uyarlama kanıt şablonu

Kitabın D1–D3, G1–G3, B1–B3, H1 ve P1 sırasını izleyin. Önce VERI.md.
Kaynak, anahtar, eksik seçimi ve puanın kullanım sınırını raporunuzda belirtin.

## D1–D3: Analizden önce
1. kaynak_satir ve kaynak_kayit ne işe yarar? İlk 100 kayıt neden temsili
   örneklem veya yeni Türkçe uygulama sayılmaz?
2. A1=6 ve C5=1 için ters puanı hesaplayın. Eksik A2'ye neden sıfır verilmez?
3. A, C ve ortak on maddede n neden farklıdır? Maddeyi çıkardıktan sonra
   eksik seçimini yeniden yapmak silinirse alfa karşılaştırmasını nasıl değiştirir?

## G1–G3: Rehberli çözüm
1. A'nın madde varyansları ve toplam varyansından ham alfayı; ortalama r'den
   standart alfayı hesaplayın. A1 çevrilmeden önceki alfa farkını açıklayın.
2. A1 madde–kalan ve düzeltilmemiş madde–toplam korelasyonunu karşılaştırın.
   A4 silinirse alfa artışı ne kadardır? Bu artış otomatik silme kuralı mıdır?
3. Bootstrap neden hücreleri değil katılımcı satırlarını birlikte çeker?
   A için [.464423,.736637] aralığı Türkçe ölçeğin güvenirliğini kanıtlar mı?

## B1–B3: C maddelerinde bağımsız çözüm
1. C4/C5'i anahtarla çevirin; n, ham/standart alfa ve ortalama r'yi hesaplayın.
   Çevirmeden önce negatif alfa neden sıfıra kırpılmamalıdır?
2. C madde–kalan ve silinirse alfa tablosunu üretin. C5 silmenin kazancını
   içerik kaybıyla birlikte değerlendirin; bütün karşılaştırmalarda aynı 98 kayıt kalsın.
3. 100 kelimeyi aşmadan kapsam, puan yönü, eksik kuralı, bootstrap yöntemi,
   aralık ve kullanım sınırını raporlayın. Bu görev dış doğrulama değildir.

## H1: Altı hatalı iddia
“Alfa .70'i geçince ölçek Türkçeye uyarlanmış olur. Her negatif madde otomatik
çevrilmelidir. A1'in toplamla r=.51 olması iyi maddeyi kanıtlar. Maddeleri iki
kez eklemek gerçek güvenirliği artırır. Bootstrap temsili olmayan örneklemi
düzeltir. Omega için model incelemesi gerekmez.” Her iddiayı düzeltin.

## P1: Uyarlama kanıt dosyası
A4 için iki Türkçe ifade taslağı, en az üç bilişsel görüşme sorusu ve bir
revizyon kayıt şablonu hazırlayın. Aşağıdaki boş tablolar gerçek çalışma
sonucu değildir. Gerçekte yapılmamış görüşme, örneklem veya uzman onayı uydurmayın.
Türkçe ifadeler öğretim taslağıdır; onaylanmış çeviri değildir.

| Kanıt alanı | Bu paketteki durum | Yapılması planlanan işlem | Kanıt dosyası/tarih |
|---|---|---|---|
| Kaynak ve kullanım açıklaması | Yerel kaynak notu var; yeni doğrulama yok | Hedef kullanım için kaynak ve koşulları belgeleyin | Doldurulacak |
| İki dilsel taslak ve uzman incelemesi | Uzman incelemesi yapılmadı | İki taslağı karşılaştırın | Doldurulacak |
| Bilişsel görüşme | Yapılmadı | Anlama/yanıtlama sürecini inceleyin | Doldurulacak |
| Hedef grupta pilot | Yapılmadı | Hedef grup ve uygulama planını yazın | Doldurulacak |
| Faktör yapısı | Bu pakette incelenmedi | Modele uygun yapı kanıtını planlayın | Doldurulacak |
| Güvenirlik | Yerel A/C iç tutarlılığı hesaplandı; Türkçe veri yok | Hedef puan/örneklem için kanıt planlayın | Doldurulacak |
| Değişmezlik/eşdeğerlik | Yapılmadı | Karşılaştırılacak grupları ve modeli belirtin | Doldurulacak |
| Kullanım ve raporlama sınırı | Öğretim amaçlı | Uygun ve uygun olmayan kullanımları yazın | Doldurulacak |

| Madde/sürüm | Önceki taslak | Önerilen taslak | Gerekçe | Gerçek kanıt/uzman | Durum/tarih |
|---|---|---|---|---|---|
| A4/v1 | Doldurulacak | Doldurulacak | Doldurulacak | Henüz yok | Planlandı |

Teslim: kaynak/puanlama sözlüğü, tamamlanmış notebook, iki grafik, madde tabloları,
bir sayfalık rapor ve uyarlama kanıt planı.

| Ölçüt | Puan |
|---|---:|
| Kaynak ve puanlama | 20 |
| Hesaplar ve eksikler | 25 |
| Belirsizlik ve madde kararı | 20 |
| Uyarlama planı | 25 |
| Yeniden üretim | 10 |