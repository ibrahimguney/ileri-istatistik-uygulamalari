# Bölüm 20 — raporlama

## Bölümdeki örnek ve açıklama

“İki ilişkili faktörlü ölçüm modelinin cinsiyet grupları (425 erkek, 891 kadın) arasında değişmezliği çok gruplu DFA ile sınandı (ML, ortalama yapılı). Biçimsel model kabul edilebilir uyum verdi ($\chi^2(62)=213.95$, CFI $=.941$, RMSEA $=.061$). Metrik değişmezlik desteklendi ($\Delta\chi^2(8)=16.00$, $p=.042$; $\Delta$CFI $=-.003$). Tam skaler değişmezlik sınırdaydı ($\Delta\chi^2(8)=36.88$, $p<.001$; $\Delta$CFI $=-.011$). Önceden belirlenen kurala göre A1’in kesişimi serbest bırakıldı; kısmi skaler model metrik modele göre $\Delta$CFI $=-.007$ verdi. Kısmi skaler modelde kadınların gizil ortalaması uyumlulukta .49, sorumlulukta .22 erkek gizil SD’si kadar yüksekti; A1’in serbest bırakılması sonucu anlamlı biçimde değiştirmedi. Katı değişmezlik desteklenmedi.”

## Teslim kontrolü

- Araştırma sorusu, hedef büyüklük, analiz birimi ve örneklem seçimi.
- Gerçek kullanılan n, eksik veri/puanlama kuralı ve veri kaynağı.
- Model, kestirici, varsayım/tanı ve karşılaştırma kararları.
- Tahmin/etki, belirsizlik aralığı ve kapsamla uyumlu yorum.
- Yazılım/sürüm/komut; yapılan doğrulama ile yapılmamış işlemlerin ayrımı.
- Yeniden üretim dosyaları; beklenen sonuçla fark varsa açıklaması.

Yalnız p değerine veya yazılımın başarı iletisine dayanmayın. Başka sürümün
aynı numaralı bölümünü bu bölümün sonucu olarak raporlamayın.

## Revizyon 23: çıpa duyarlılığı ve koşullu aralıklar

A1-serbest A farkı.487959 [.351373,.624546], A1+A2-serbest.435385
[.297154,.573615], erkek gizil SD'sinde. Yön aynı; büyüklük çıpaya duyarlıdır.
Model farkı/eşdeğerlik testi yapılmadı. Sabit çıpa kümesine koşullu normal
kuramlı aralıklar; veri temelli seçim belirsizliği ve yeni doğrulama dışarıda.
Her sabit senaryonun iki A/C farkına ait Bonferroni ailesi arama sürecini kapsamaz.
Kadın referansında erkek−kadın A farkı−.543980; işaretle birlikte birim değişir.
A ortalama puanı model farkı.054673 kesişim+.371693 gizil=.426366;
gözlenen.452416 ve kalan.026050 ham puandır. Nedensel ayrıştırma değildir.
A1+A2 yalnız duyarlılık senaryosu; p<.01 aramasının tüm adımları değildir.
Yeni ek yalnız Python; veri/ana model/arama korunur.
