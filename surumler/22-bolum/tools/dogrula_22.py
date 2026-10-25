"""22 bölümlük öğrenci paketinin yapı ve isteğe bağlı Python doğrulaması."""
from pathlib import Path
import argparse,ast,csv,hashlib,json,math,os,shutil,subprocess,sys,tempfile,time
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from importlib.metadata import version as package_version

ROOT=Path(__file__).resolve().parents[1]
SKIP_KEYS={'versions','surum','surumler','elapsed_seconds','runtime_seconds','optimizer_alternate_success'}

def compare(expected,actual,path=''):
    differences=[]
    if isinstance(expected,dict):
        if not isinstance(actual,dict):return [path+': nesne türü farklı']
        for key,value in expected.items():
            if key in SKIP_KEYS or (path=='.bootstrap' and key=='seconds'):continue
            if key not in actual:differences.append(path+'.'+key+': alan yok')
            else:differences.extend(compare(value,actual[key],path+'.'+key))
    elif isinstance(expected,list):
        if not isinstance(actual,list) or len(expected)!=len(actual):return [path+': dizi boyutu farklı']
        for i,(a,b) in enumerate(zip(expected,actual)):differences.extend(compare(a,b,path+f'[{i}]'))
    elif isinstance(expected,bool) or expected is None:
        if expected!=actual:differences.append(path+f': {expected!r} != {actual!r}')
    elif isinstance(expected,(int,float)):
        if not isinstance(actual,(int,float)) or not math.isclose(expected,actual,rel_tol=1e-5,abs_tol=1e-7):differences.append(path+f': {expected!r} != {actual!r}')
    elif expected!=actual:differences.append(path+': metin/değer farklı')
    return differences

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.redirect=False
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='a' and d.get('href'):self.links.append(d['href'])
        if tag=='link' and d.get('href'):self.links.append(d['href'])
        if tag=='meta' and d.get('http-equiv','').lower()=='refresh':self.redirect=True

def structure(root):
    mapping=json.loads((root/'BOLUM_ESLESMESI.json').read_text())['chapters']
    assert [e['number'] for e in mapping]==list(range(1,23))
    required=['README.md','VERI.md','GOREVLER.md','RAPORLAMA.md','COZUMLER.md','calisma.ipynb','analiz.py','beklenen.json','DOGRULAMA.json']
    for e in mapping:
        chapter=root/e['page']
        for name in required:assert (chapter/name).is_file(),str(chapter/name)
        ast.parse((chapter/'analiz.py').read_text())
        notebook=json.loads((chapter/'calisma.ipynb').read_text());assert notebook['nbformat']==4
        for cell in notebook['cells']:
            if cell['cell_type']=='code':
                assert cell['execution_count'] is None and not cell['outputs']
                ast.parse(''.join(cell['source']))
        assert (root/e['application']/'analiz.py').is_file()
        json.loads((chapter/'beklenen.json').read_text())
    checked=0
    for page in root.rglob('*.html'):
        parser=Links();parser.feed(page.read_text());assert not parser.redirect,str(page)
        for link in parser.links:
            if urlsplit(link).scheme or link.startswith('#'):continue
            target=(page.parent/unquote(urlsplit(link).path)).resolve()
            if target.name=='ogrenci-paketi-22-bolum.zip' and not target.exists():continue # arşiv paketleme sonunda üretilir
            assert target.exists(),f'{page}: {link}'
            checked+=1
    for source in (root/'uygulamalar').rglob('*.py'):ast.parse(source.read_text())
    return {'chapters':22,'notebooks_syntax_checked':22,'local_links_checked':checked,'chapter_redirects':0}

def run_analyses(root,report_path,only=None):
    entries=json.loads((root/'BOLUM_ESLESMESI.json').read_text())['chapters'];rows=[]
    if only is not None:entries=[e for e in entries if e['number'] in only]
    logs=report_path.parent/'validation-logs';logs.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='kitap-22-') as d:
        work=Path(d)/'surum';shutil.copytree(root,work,ignore=shutil.ignore_patterns('*.zip','__pycache__','validation-logs'))
        env={**os.environ,'MPLBACKEND':'Agg','MPLCONFIGDIR':str(Path(d)/'mpl'),'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'}
        for e in entries:
            start=time.monotonic();name=e['id'];script=work/e['page']/'analiz.py'
            result=subprocess.run([sys.executable,str(script)],cwd=work,env=env,capture_output=True,text=True,timeout=240)
            (logs/(name+'.log')).write_text(result.stdout+'\n'+result.stderr)
            diffs=[]
            if result.returncode==0:
                actual=json.loads((work/e['application']/'sonuclar/ozet.json').read_text());expected=json.loads((root/e['page']/'beklenen.json').read_text());diffs=compare(expected,actual)
            row={'chapter':e['number'],'id':name,'title':e['title'],'status':'passed' if result.returncode==0 and not diffs else 'failed','exit_code':result.returncode,'seconds':round(time.monotonic()-start,3),'differences':diffs[:30]}
            rows.append(row);print(name,row['status'],flush=True)
            report_path.write_text(json.dumps({'python':sys.version,'results':rows},ensure_ascii=False,indent=2))
        extra=work/'uygulamalar/b03-veri-hazirlama/coklu-atama/dogrula.py'
        r=subprocess.run([sys.executable,str(extra)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
        (logs/'b03-mi-tests.log').write_text(r.stdout+'\n'+r.stderr)
        assert r.returncode==0,'Çoklu atama kontrolleri başarısız'
        mi=work/'uygulamalar/b03-veri-hazirlama/coklu-atama/analiz.py'
        r=subprocess.run([sys.executable,str(mi)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
        (logs/'b03-mi.log').write_text(r.stdout+'\n'+r.stderr);assert r.returncode==0
        expected=json.loads((root/'uygulamalar/b03-veri-hazirlama/coklu-atama/sonuclar/ozet.json').read_text());actual=json.loads((mi.parent/'sonuclar/ozet.json').read_text());mi_diffs=compare(expected,actual)
        design=work/'uygulamalar/b01-istatistiksel-mekanizma/tasarim-belirsizligi'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(design/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b01-design-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Tasarım belirsizliği denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b01-istatistiksel-mekanizma/tasarim-belirsizligi/sonuclar/ozet.json').read_text())
        design_diffs=compare(expected,json.loads((design/'sonuclar/ozet.json').read_text()))
        summary=work/'uygulamalar/b02-betimsel-istatistik/ozet-secimi'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(summary/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b02-summary-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Özet seçimi denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b02-betimsel-istatistik/ozet-secimi/sonuclar/ozet.json').read_text())
        summary_diffs=compare(expected,json.loads((summary/'sonuclar/ozet.json').read_text()))
        preparation=work/'uygulamalar/b03-veri-hazirlama/birlesim-denetimi'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(preparation/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b03-preparation-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Birleştirme denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b03-veri-hazirlama/birlesim-denetimi/sonuclar/ozet.json').read_text())
        preparation_diffs=compare(expected,json.loads((preparation/'sonuclar/ozet.json').read_text()))
        decision=work/'uygulamalar/b04-hipotez-testi/esdegerlik-cokluk'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(decision/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b04-decision-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Eşdeğerlik/çokluk denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b04-hipotez-testi/esdegerlik-cokluk/sonuclar/ozet.json').read_text())
        decision_diffs=compare(expected,json.loads((decision/'sonuclar/ozet.json').read_text()))
        planning=work/'uygulamalar/b05-guc-analizi/esdegerlik-hassasiyet'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(planning/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b05-planning-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Eşdeğerlik gücü/hassasiyet denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b05-guc-analizi/esdegerlik-hassasiyet/sonuclar/ozet.json').read_text())
        planning_diffs=compare(expected,json.loads((planning/'sonuclar/ozet.json').read_text()))
        robustness=work/'uygulamalar/b06-parametrik-testler/welch-saglamlik'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(robustness/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b06-robustness-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Welch/Yuen denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b06-parametrik-testler/welch-saglamlik/sonuclar/ozet.json').read_text())
        robustness_diffs=compare(expected,json.loads((robustness/'sonuclar/ozet.json').read_text()))
        followup=work/'uygulamalar/b08-tekrarli-olcumler/eksik-izlem'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(followup/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b08-followup-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Eksik izlem denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b08-tekrarli-olcumler/eksik-izlem/sonuclar/ozet.json').read_text())
        followup_diffs=compare(expected,json.loads((followup/'sonuclar/ozet.json').read_text()))
        multivariate=work/'uygulamalar/b09-manova/hedef-aralik'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(multivariate/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b09-target-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Çok değişkenli hedef/aralık denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b09-manova/hedef-aralik/sonuclar/ozet.json').read_text())
        multivariate_diffs=compare(expected,json.loads((multivariate/'sonuclar/ozet.json').read_text()))
        rank_uncertainty=work/'uygulamalar/b10-parametrik-olmayan/ustunluk-belirsizlik'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(rank_uncertainty/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b10-uncertainty-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Üstünlük belirsizliği denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b10-parametrik-olmayan/ustunluk-belirsizlik/sonuclar/ozet.json').read_text())
        rank_diffs=compare(expected,json.loads((rank_uncertainty/'sonuclar/ozet.json').read_text()))
        correlation_pairs=work/'uygulamalar/b11-korelasyon/esli-bootstrap'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(correlation_pairs/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b11-pairs-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Korelasyon ortak satır denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b11-korelasyon/esli-bootstrap/sonuclar/ozet.json').read_text())
        correlation_diffs=compare(expected,json.loads((correlation_pairs/'sonuclar/ozet.json').read_text()))
        split_prediction=work/'uygulamalar/b12-regresyon/ayri-kalibrasyon'
        for name in ['dogrula.py','analiz.py']:
            r=subprocess.run([sys.executable,str(split_prediction/name)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
            (logs/('b12-split-'+name+'.log')).write_text(r.stdout+'\n'+r.stderr)
            assert r.returncode==0,'Ayrı kalibrasyon denetimi başarısız'
        expected=json.loads((root/'uygulamalar/b12-regresyon/ayri-kalibrasyon/sonuclar/ozet.json').read_text())
        split_diffs=compare(expected,json.loads((split_prediction/'sonuclar/ozet.json').read_text()))
    report={'python':sys.version,'package_versions':{n:package_version(n) for n in ['numpy','scipy','pandas','matplotlib','statsmodels']},'comparison_policy':{'excluded_metadata':sorted(SKIP_KEYS),'excluded_paths':['.bootstrap.seconds'],'optimizer_note':'Durdurma bayrağı eşitliği değil, betiğin amaç fonksiyonu/kovaryans/gradyan kontrolleri esas alınır.'},'results':rows,'multiple_imputation':{'tests':'passed','differences':mi_diffs},'design_uncertainty':{'tests':'passed','differences':design_diffs},'summary_selection':{'tests':'passed','differences':summary_diffs},'preparation_audit':{'tests':'passed','differences':preparation_diffs},'equivalence_multiplicity':{'tests':'passed','differences':decision_diffs},'power_precision':{'tests':'passed','differences':planning_diffs},'welch_robustness':{'tests':'passed','differences':robustness_diffs},'incomplete_followup':{'tests':'passed','differences':followup_diffs},'multivariate_targets':{'tests':'passed','differences':multivariate_diffs},'rank_uncertainty':{'tests':'passed','differences':rank_diffs},'correlation_pairs':{'tests':'passed','differences':correlation_diffs},'split_prediction':{'tests':'passed','differences':split_diffs},'tolerance':{'rtol':1e-5,'atol':1e-7},'not_run':['R','IBM SPSS','Amos'],'note':'Sürüm alanları dışlandı; atama mekanizması, kapsam veya her kitap sayısı için bilimsel hakemlik değildir.'}
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2))
    return not mi_diffs and not design_diffs and not summary_diffs and not preparation_diffs and not decision_diffs and not planning_diffs and not robustness_diffs and not followup_diffs and not multivariate_diffs and not rank_diffs and not correlation_diffs and not split_diffs and all(x['status']=='passed' for x in rows)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--analyses',action='store_true');p.add_argument('--chapters',help='Örn. 5,15,19,21; yalnız seçili Python analizlerini tekrarlar');p.add_argument('--report',type=Path,default=ROOT/'dogrulama/latest.json');a=p.parse_args();print(json.dumps(structure(ROOT),ensure_ascii=False))
    if a.analyses:
        a.report.parent.mkdir(parents=True,exist_ok=True)
        only=set(map(int,a.chapters.split(','))) if a.chapters else None
        if only is not None and (not only or not only<=set(range(1,23))):raise ValueError('Bölüm numarası 1–22 olmalı.')
        if not run_analyses(ROOT,a.report,only):raise SystemExit(1)
