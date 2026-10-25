# Bölüm 8 — Eksik izlem ve aynı model karşılaştırması

Özgün sleepstudy 2.–9. gün verisinde 18 kişi/144 tam ölçüm vardır. Ayrı öğretim
kopyası oluşturulur; kaynak ve mevcut ana analiz/reference sonuçlar değiştirilmez.
Yeni ek yalnız Python'da sınandı; R/SPSS eşdeğeri hazırlanmadı.

Kitap kökünden; öğrenci deposunda `surumler/22-bolum/` klasöründen:

```sh
python uygulamalar/b08-tekrarli-olcumler/eksik-izlem/dogrula.py
python uygulamalar/b08-tekrarli-olcumler/eksik-izlem/analiz.py
```

## Maske

İlk iki analiz günü korunur. DaysB>=2'de henüz çıkılmadıysa ziyaret başına
expit(-2+.025*(gözlenen temel Reaction-265)) olasılığıyla izlemden çıkılır;
sonraki ölçümler de gizlenir. NumPy default_rng seed20261025, kişi/gün sırası
sabitlenir. Mekanizma yalnız gözlenen temele bağlı MAR-türü öğretimdir; gerçek
kişilerin eksikliği veya gerçek veride mekanizma testi değildir.

40 ölçüm gizlenir; 18 kişide104 ölçüm kalır. Yalnız7 kişi sekiz ölçümde tamdır
(56 satır). Her kişide en az2 ölçüm korunur. Gözlenen değerler değiştirilmez.

## Aynı model

Üç veri kümesinde de Reaction~DaysB, rastgele kesişim/eğim, REML/lbfgs:

| Veri | Kişi/satır | Eğim | SH |
|---|---|---:|---:|
| Tam arşiv | 18/144 | 11.435 | 1.845 |
| Maskeli mevcut ölçümler | 18/104 | 12.753 | 1.794 |
| Maskeli tam kişiler | 7/56 | 10.411 | 1.863 |

Eğim ms/gün. Tam-arşiv eğimi bilinmeyen anakütle gerçeği değildir. Bir maskeden
yanlılık/verimlilik sıralaması çıkarılmaz. Daha küçük SH bilgi kazancı kanıtı
değildir; varyans bileşenleri yeniden kestirilmiştir. Tam arşivde artık SD25.53,
maskeli mevcut ölçümlerde22.23. Aynı kategorik ANOVA yerine aynı doğrusal model
kullanılarak hedef sabit tutulur. Gözlenen veri olabilirliği eksik hücre doldurmaz.

Yakınsama, pozitif kovaryans özdeğerleri ve uyarılar kaydedilir. Aralıklar normal
Wald yaklaşımıdır; Satterthwaite/Kenward–Roger sd düzeltmesi ve MNAR duyarlılığı
yoktur. Özellikle7 kişide küçük-örneklem kesin testi iddiası yoktur. MAR ve doğru
ortalama/kovaryans modeli yazılımın yakınsamasıyla doğrulanmaz.

## Orthodont öğretim ailesi

Her yaşta16 erkek/11 kız için ayrı Welch soruları; dört yaş ailesine Holm:
8/10/12/14 yaş için düzeltilmiş p .109487/.109487/.038228/.005306.
Bonferroni p .273898/.218973/.050970/.005306. Holm12/14, Bonferroni yalnız14
yaş sorusunu reddeder. Testler yaşlar arasında bağımlı olabilir; Holm geçerli
tekil p'ler altında bağımsızlık istemez. Bu, genel etkileşim veya doğrusal eğim
testi değildir; gerçek önkayıt/düzeltilmiş aralık iddiası yoktur.

Çıktılar `sonuclar/eksik-izlem-ogretim.csv`, `maske-kaydi.csv`,
`ayni-model-karsilastirma.csv`, `yas-ailesi.csv`, `ozet.json`.
Beş test maskenin tekrar üretimi/sıra değişmezliği, temel koruma/monotonluk,
gözlenen değerlerin korunması ve geçersiz anahtar/temel reddini denetler.
Ham kaynak hash'leri ve değişmezlik son kontrolde doğrulanır. Kaynak/GPL notları
üst README'de korunur; yeni kişi veya tedavi etkisi üretilmez.

Kuramsal kaynak: Gueorguieva ve Krystal (2004), https://doi.org/10.1001/archpsyc.61.3.310 ;
mevcut Little/Rubin ve Bates kaynakları.
