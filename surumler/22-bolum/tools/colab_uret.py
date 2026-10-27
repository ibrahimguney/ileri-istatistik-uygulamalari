"""Yerel analizleri değiştirmeden 21 Colab defteri üretir; B02 pilotunu korur."""
from pathlib import Path
from ogretim_ekle import apply as teaching_layer, main as sync_teaching
import json,re,textwrap
ROOT=Path(__file__).resolve().parents[1]
COMMIT='23acf4be23823aa139523c8f4db34cff248c285d'
ZIP_HASH='ce6440f5ee3b4dde9709e1fb250e7b7d8ac86be101b6ababacdab240443560f6'
PINS={'numpy':'2.5.4','scipy':'1.18.1','pandas':'3.1.0','matplotlib':'3.11.2','statsmodels':'0.15.0','PyMuPDF':'1.26.6'}

def build(e):
 n=e['number'];chapter=ROOT/e['page'];title=e['title'];app=e['application'];base='https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/surumler/22-bolum/'+e['page'];cells=[]
 def add(kind,source):
  cell={'cell_type':kind,'id':f'b{n:02}-{len(cells):02}','metadata':{},'source':textwrap.dedent(source).strip().splitlines(keepends=True)}
  if kind=='code':cell.update(execution_count=None,outputs=[])
  cells.append(cell)
 def md(s):add('markdown',s)
 def code(s):add('code',s)
 local=json.loads((chapter/'calisma.ipynb').read_text());allcode='\n'.join(''.join(c['source']) for c in local['cells'] if c['cell_type']=='code')
 modules=[str(f.parent.relative_to(ROOT)) for f in sorted((ROOT/app).rglob('analiz.py')) if f.parent!=ROOT/app and (f.parent/'sonuclar/ozet.json').is_file()]
 md(f'''# Bölüm {n} · {title}

[Atölye]({base}) · [Veri ve lisans]({base}VERI.md) · [Görevler]({base}GOREVLER.md) · [Raporlama]({base}RAPORLAMA.md) · [Çözümler]({base}COZUMLER.md)

**Başlangıç:** Google hesabınızla açın, **Dosya → Drive'a bir kopyasını kaydet** seçin. CPU yeterlidir. Hücreleri sırayla veya **Çalışma zamanı → Tümünü çalıştır** ile yürütün. İlk kurulum internet ve birkaç dakika gerektirebilir. Özellikle bootstrap ve yapısal modeller daha uzun sürebilir.

Bu defter, aynı GitHub deposundaki ana Python analizini ve bölümün ileri eklerini çalıştırır. Dosya yüklemeniz veya önce başka bölümü elle yürütmeniz gerekmez. Gerçek veri, öğretim alt kümesi ve simülasyon ayrımı veri rehberinde açıklanır; bunları aynı örneklem türü saymayın. R/SPSS/Amos burada çalıştırılmaz.''')
 md('''## 1 · Kaynakları hazırla

Sabit bir GitHub sürümündeki öğrenci paketi SHA256 ile doğrulanır. Her çalıştırma ayrı bir geçici çalışma kopyası açar; önceki sonuçlarınız silinmez. Kod ve veri, bu doğrulanan sürümden gelir. Oturum kapanmadan sonuçları indirin.''')
 code(f'''from pathlib import Path
import sys, os, json, hashlib, urllib.request, zipfile, io, tempfile, subprocess, importlib.metadata
DATA_COMMIT = {COMMIT!r}
ARCHIVE_SHA256 = {ZIP_HASH!r}
ARCHIVE_URL = f"https://raw.githubusercontent.com/ibrahimguney/ileri-istatistik-uygulamalari/{{DATA_COMMIT}}/surumler/22-bolum/ogrenci-paketi-22-bolum.zip"
cache = Path.cwd()/"kitap-colab-kaynak.zip"
if cache.exists():
    raw = cache.read_bytes()
else:
    try:
        with urllib.request.urlopen(ARCHIVE_URL, timeout=60) as response: raw=response.read()
    except Exception as exc:
        raise RuntimeError("Kaynak indirilemedi. İnterneti kontrol edip hücreyi yeniden çalıştırın: "+ARCHIVE_URL) from exc
if hashlib.sha256(raw).hexdigest()!=ARCHIVE_SHA256:
    raise ValueError("Öğrenci paketi SHA256 denetimi başarısız. Kontrolü kaldırmayın; yerel kitap-colab-kaynak.zip dosyasını doğrulayın.")
cache.write_bytes(raw)
work = Path(tempfile.mkdtemp(prefix="b{n:02}-atolye-",dir=Path.cwd()))
with zipfile.ZipFile(io.BytesIO(raw)) as z:
    assert len(z.infolist())<10000 and sum(i.file_size for i in z.infolist())<134217728
    for member in z.infolist():
        target=(work/member.filename).resolve()
        if work.resolve() not in target.parents or ((member.external_attr>>16)&0o170000)==0o120000:
            raise ValueError("Güvenli olmayan arşiv yolu")
    z.extractall(work)
root = work/"ileri-istatistik-22-bolum"
assert (root/"BOLUM_ESLESMESI.json").is_file()
application=root/{app!r}
modules={modules!r}
expected_main=json.loads((root/"bolumler/b{n:02}/beklenen.json").read_text())
expected_extra={{m:json.loads((root/m/"sonuclar/ozet.json").read_text()) for m in modules}}
print("Kaynak doğrulandı; Bölüm {n} çalışma kopyası hazır.")
''')
 md('''## 2 · Analiz ortamını hazırla

Sınanmış paket sürümleri kullanılır. Mevcut çekirdek bu sürümlerdeyse doğrudan kullanılır. Farklıysa analizler ayrı bir Python ortamında kurulur; Colab çekirdeğindeki paketler topluca değiştirilmez. Kurulum başarısız olursa hücredeki hatayı inceleyin. Python 3.12 veya üzeri çalışma zamanı önerilir. GPU gerekmez.''')
 code(f'''FORCE_ISOLATED=globals().get("FORCE_ISOLATED",False)
PINS={PINS!r}
def package_versions(executable):
    check="import importlib.metadata,json; names="+repr(list(PINS))+";print(json.dumps({{n:importlib.metadata.version(n) for n in names}}))"
    attempt=subprocess.run([str(executable),"-c",check],capture_output=True,text=True)
    return json.loads(attempt.stdout) if attempt.returncode==0 else {{}}
python=Path(sys.executable)
if FORCE_ISOLATED or package_versions(python)!=PINS:
    environment=Path.cwd()/".kitap-colab-python"
    if not (environment/"bin/python").exists():
        subprocess.run([sys.executable,"-m","venv",str(environment)],check=True)
    python=environment/"bin/python"
    if package_versions(python)!=PINS:
        subprocess.run([str(python),"-m","pip","install",*[name+"=="+version for name,version in PINS.items()]],check=True)
assert package_versions(python)==PINS,"Paket sürümleri sınanmış ortamla eşleşmiyor"
versions=package_versions(python)
run_env={{**os.environ,"MPLBACKEND":"Agg","MPLCONFIGDIR":str(work/"mpl"),"OPENBLAS_NUM_THREADS":"1","OMP_NUM_THREADS":"1","PYTHONDONTWRITEBYTECODE":"1"}}
(work/"logs").mkdir(exist_ok=True)
def run_script(relative):
    print("Çalışıyor:",relative,flush=True)
    result=subprocess.run([str(python),str(root/relative)],cwd=root,env=run_env,capture_output=True,text=True,timeout=900)
    (work/"logs"/(relative.replace("/","__")+".log")).write_text(result.stdout+"\\n"+result.stderr)
    if result.returncode: raise RuntimeError(result.stdout[-4000:]+"\\n"+result.stderr[-4000:])
    print("Tamamlandı.")
print("Analiz ortamı hazır:",versions)
''')
 if n in [19,20,21]:
  md('''## 3 · Ortak faktör analizi girdilerini üret

Bu bölüm Bölüm 18'in sabit A/B bölmesini ve ortak veri dosyalarını kullanır. Aşağıdaki adım aynı kaynaktan bunları yeniden üretir; başka bir defter açmanız gerekmez. Bu işlem yeni örneklem veya dış doğrulama oluşturmaz.''')
  code('run_script("bolumler/b18/analiz.py")')
 md('''## Ana analiz

Kaynak ve yöntem için yukarıdaki veri rehberini okuyun. Ana analiz ve sonradan eklenen duyarlılık uygulamaları ayrı çalıştırılır. Sonuçlar önceden gösterilen tabloların kopyası olarak değil, kod yeniden yürütülerek üretilir.''')
 code(f'''before_figures=set((root/"assets_figures").glob("*.pdf"))
run_script("bolumler/b{n:02}/analiz.py")
main_result=json.loads((application/"sonuclar/ozet.json").read_text())
from IPython.display import display, JSON, HTML, Image
print("Ana sonuçlar — ayrıntıları açmak için okları kullanın:")
display(JSON(main_result,expanded=False))
''')
 if modules:
  md('''## İleri uygulamalar ve duyarlılık

Her ekin açıklaması atölye sayfasındadır. Bu sonuçları ana analizle veya birbirinden farklı tahmin hedefleriyle karıştırmayın. Hazır kontrol betikleri varsa önce onlar, ardından ek analiz çalışır.''')
  code('''extra_results={}
for module in modules:
    if (root/module/"dogrula.py").is_file(): run_script(module+"/dogrula.py")
    run_script(module+"/analiz.py")
    extra_results[module]=json.loads((root/module/"sonuclar/ozet.json").read_text())
    print(module)
    display(JSON(extra_results[module],expanded=False))
''')
 md('''## Sonuçları referanslarla karşılaştır

Kitabın sayısal referansları, önceki sürümden değişmeden alınır. Sürüm/zaman gibi hesap dışı alanlar mevcut karşılaştırma politikasına göre dışlanır. Hata oluşursa veri, sürüm ve günlük dosyalarını kontrol edin; referansları sonuca uydurmayın. Bu kontrol bilimsel varsayımları veya SPSS yürütmesini doğrulamaz.''')
 code('''sys.path.insert(0,str(root/"tools"))
from dogrula_22 import compare
checks={"main":compare(expected_main,main_result)}
for module in modules:
    checks[module]=compare(expected_extra[module],json.loads((root/module/"sonuclar/ozet.json").read_text()))
assert all(not differences for differences in checks.values()),checks
print("Ana analiz ve",len(modules),"ileri ek için sayısal referanslar eşleşti.")
''')
 md('''## Grafikler ve özet tablolar

Grafikler bu çalıştırmada üretilir. Ön koşul olarak çalıştırılan Bölüm 18'in şekilleri burada tekrar gösterilmez. CSV tablolarının ilk 12 satırı görüntülenir; tam dosyalar çıktı paketindedir. Şekil sayısı bölüme göre değişir.''')
 code('''import csv,html
new_figures=sorted(set((root/"assets_figures").glob("*.pdf"))-before_figures)
for figure in new_figures:
    png=figure.with_suffix(".png")
    renderer="import fitz,sys;d=fitz.open(sys.argv[1]);d[0].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(sys.argv[2])"
    subprocess.run([str(python),"-c",renderer,str(figure),str(png)],check=True)
    print(figure.name)
    display(Image(filename=str(png)))
for table in sorted((application/"sonuclar").glob("*.csv"))[:3]:
    with table.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.reader(f))
    content="<h4>"+html.escape(table.name)+"</h4><table>"
    for i,row in enumerate(rows[:13]):
        tag="th" if i==0 else "td"
        content+="<tr>"+"".join("<"+tag+">"+html.escape(value)+"</"+tag+">" for value in row)+"</tr>"
    display(HTML(content+"</table>"))
''')
 tasks=(chapter/'GOREVLER.md').read_text().split('\n## Çekirdek öğrenme rotası')[0]
 md('## Sıra sizde\n\n'+tasks+f'\n\nÖnce kendi yorumunuzu yazın; sonra [çözümlerle]({base}COZUMLER.md) karşılaştırın. Sonuç, belirsizlik, varsayım ve sınırlılıkları [raporlama rehberine]({base}RAPORLAMA.md) göre ayırın.')
 code('''yanitlarim={"bulgular":"", "belirsizlik":"", "varsayimlar":"", "sinirliliklar":""}
# Metinleri doldurun; sayısal kontrolü geçmek bu yorumları tamamlamaz.
''')
 md('''## Çıktıları indir

Son hücre sonuç JSON/CSV'lerini, grafiklerin PDF/PNG dosyalarını, günlükleri ve kendi yanıtlarınızı paketler. Colab'ın solundaki Dosyalar panelini yenileyin ve aşağıda yazan ZIP'i indirin. Geçici çalışma zamanı kapanmadan bunu yapın; kod Drive'a otomatik erişmez.''')
 code(f'''manifest={{"chapter":{n},"source_commit":DATA_COMMIT,"source_archive_sha256":ARCHIVE_SHA256,"versions":versions,"checks":checks,"answers":yanitlarim,"scope":"Python ana analiz ve ileri ekler; SPSS/R/Amos çalıştırılmadı"}}
(work/"calisma-kaydi.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
archive=Path.cwd()/"b{n:02}-colab-ciktilar.zip"
with zipfile.ZipFile(archive,"w",zipfile.ZIP_DEFLATED) as z:
    z.write(work/"calisma-kaydi.json","calisma-kaydi.json")
    for module in [{app!r},*modules]:
        for f in sorted((root/module/"sonuclar").rglob("*")):
            if f.is_file() and f.suffix in [".json",".csv"]:z.write(f,str(f.relative_to(root)))
    for figure in new_figures:
        for f in [figure,figure.with_suffix(".png")]: z.write(f,"grafikler/"+f.name)
    for f in (work/"logs").glob("*.log"):z.write(f,"logs/"+f.name)
print("İndirmeye hazır:",archive.name)
''')
 return {'cells':cells,'metadata':{'colab':{'name':f'Bölüm {n} — {title}','provenance':[]},'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.12'}},'nbformat':4,'nbformat_minor':5}

def main():
 mapping=json.loads((ROOT/'BOLUM_ESLESMESI.json').read_text())['chapters']
 for e in mapping:
  if e['number']==2:continue
  record=next(c for c in json.loads((ROOT/'OGRENME-ROTALARI.json').read_text())['chapters'] if c['number']==e['number'])
  nb=teaching_layer(build(e),record);(ROOT/e['page']/'colab.ipynb').write_text(json.dumps(nb,ensure_ascii=False,indent=2)+'\n')
 sync_teaching()
 print('21 Colab defteri üretildi; B02 başlangıç defteri ve öğretim katmanı korundu.')
if __name__=='__main__':main()
