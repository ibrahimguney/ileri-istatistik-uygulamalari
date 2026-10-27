"""B02 Colab defterini temiz dizinde iki kez, ardından bozuk kaynakla sınar.

Gerçek Colab arayüzünü çalıştırmaz. Yalnız Python hücrelerini yeni alt süreçte
ve paket kurulumu gerekmeyen sınanmış ortamda yürütür. İlk çalışmada GitHub'daki
sabit CSV indirilir; ikinci çalışmada yerel doğrulanmış kaynak kullanılır.
"""
from pathlib import Path
import argparse,ast,json,os,subprocess,sys,tempfile,zipfile,hashlib
ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--report',type=Path);args=parser.parse_args()
    notebook=ROOT/'bolumler/b02/colab.ipynb';nb=json.loads(notebook.read_text())
    assert nb['nbformat']==4 and nb['metadata']['kernelspec']['name']=='python3'
    cells=[]
    for i,cell in enumerate(nb['cells']):
        if cell['cell_type']=='code':
            assert cell['execution_count'] is None and not cell['outputs']
            code=''.join(cell['source']);ast.parse(code);cells.append((i,code))
    assert len(cells)==10
    with tempfile.TemporaryDirectory(prefix='b02-colab-') as temp:
        work=Path(temp)
        env={**os.environ,'MPLBACKEND':'Agg','MPLCONFIGDIR':str(work/'mpl'),'OPENBLAS_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'}
        script=work/'run.py'
        def runner(selected):
            return '\n'.join('exec(compile('+repr(code)+','+repr(f'colab-cell-{i}')+',"exec"),globals())' for i,code in selected)
        script.write_text(runner(cells))
        runs=[]
        for run in range(2):
            result=subprocess.run([sys.executable,str(script)],cwd=work,env=env,capture_output=True,text=True,timeout=180)
            if result.returncode:raise RuntimeError(result.stdout+'\n'+result.stderr)
            manifest=json.loads((work/'b02-atolye/calisma-kaydi.json').read_text())
            assert len(manifest['checks'])==9 and all(manifest['checks'].values())
            assert manifest['ogrenci_karari']['alanlar_dolu'] is False
            with zipfile.ZipFile(work/'b02-atolye-ciktilar.zip') as z:
                assert z.testzip() is None
                assert set(z.namelist())=={'betimsel-ozet.csv','duyarlilik.csv','dagilim.pdf','eslesmis-degisim.pdf','calisma-kaydi.json','ogrenci-karari.json'}
            runs.append({'run':run+1,'success':True,'checks':9})
        source=work/'b02-atolye/kaynak-notlar.csv'
        source.write_bytes(source.read_bytes()+b'corrupted\n')
        script.write_text(runner(cells[:2]))
        bad=subprocess.run([sys.executable,str(script)],cwd=work,env=env,capture_output=True,text=True,timeout=60)
        assert bad.returncode!=0 and 'SHA256' in bad.stderr,'Bozuk kaynak reddedilmedi'
        report={'notebook':'bolumler/b02/colab.ipynb','notebook_sha256':hashlib.sha256(notebook.read_bytes()).hexdigest(),
                'clean_directory':True,'runs':runs,'corrupt_source_rejected':True,'versions':manifest['versions'],
                'source_commit':manifest['data_commit'],'source_sha256':manifest['sha256'],
                'code_cells':len(cells),'colab_ui_executed':False,
                'scope':'Python hücreleri yeni alt süreçlerde yürütüldü; gerçek Google Colab oturumu değildir.'}
        if args.report:
            args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
