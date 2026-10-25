# Bölüm 2 — Özet seçimi ve ampirik dağılım

Mevcut 80 gerçek GP kaydı üzerinde ek betimsel uygulama. Ana `analiz.py` ve ham
veri değiştirilmez. Güven aralığı, bootstrap, hipotez testi veya nedensel etki yoktur.

Kitap kökünden (öğrenci deposunda `surumler/22-bolum/` klasöründen):

```sh
python uygulamalar/b02-betimsel-istatistik/ozet-secimi/dogrula.py
python uygulamalar/b02-betimsel-istatistik/ozet-secimi/analiz.py
```

Ortak NumPy/pandas/SciPy/matplotlib bağımlılıklarını kullanır. Bu ek yalnız
Python'da sınandı; R/SPSS karşılığı hazırlanmadı.

- Ortalama, medyan ve her kuyruktan %20 kırpılmış ortalama ayrı hedeflerdir.
  Kırpma g=floor(.2n)=16, hesapta kalan 48 değerdir; dosyada 80 kayıt korunur.
  Kırpılmış ortalama bağımsız SciPy `trim_mean` hesabıyla karşılaştırılır.
- G3 ortalama=12.6375, medyan=12, kırpılmış ortalama=12.4583333333.
  G1 karşılıkları 12.175, 12 ve 12.1875'tir.
- Ampirik dağılım F(t)=count(x<=t)/n'dir. G3'te >15 oranı 9/80=%11.25,
  >=15 oranı 15/80=%18.75'tir. Eşiğe eşit altı kayıt farklılığı yaratır.
- G1 için ters ampirik dağılım Q3=13, ana tip 7 Q3=13.25'tir. Tanımlar ayrı
  belirtilir; ana bölümün algoritması değiştirilmez.
- Gerçek eşleşmiş farklar: ortalama .4625, medyan 0, artış/eşit/azalış 32/31/17.
  Medyanların farkı ile fark medyanının eşit olmadığı ayrı bir üç-kayıt kurgusuyla
  gösterilir; kurgudaki 100/101 değerleri gerçek not olarak sunulmaz.

Çıktılar `sonuclar/konum-hedefleri.csv`, `ampirik-dagilim.csv`,
`eslesmis-farklar.csv`, `ozet.json`; grafik `../../../assets_figures/b02-ampirik-eslesmis.pdf`
konumunda, kitap/öğrenci sürüm kökünün assets_figures dizininde üretilir.

`dogrula.py` elle hesaplanabilir kırpma, sıra/ölçek/öteleme değişmezliği, bağlar ve
eşik eşitsizliği ile geçersiz girdi durumlarını sınar. Ana betik kayıp fonksiyonlarını,
fark ortalaması özdeşliğini, sayımları ve kaynak hash'ini ayrıca denetler.
Kaynak verinin UCI CC BY 4.0 bildirimi üst uygulama README'sinde korunur.

Kuramsal kaynaklar:
- Hyndman ve Fan (1996), https://doi.org/10.1080/00031305.1996.10473566
- Weissgerber ve arkadaşları (2015), https://doi.org/10.1371/journal.pbio.1002128

Rapor sunumunda iki ondalık kullanılması, ara hesapların yuvarlanması anlamına
gelmez. Makine çıktıları tam hesaplama hassasiyetini korur.
