"""Colab defterlerini ayrı çalışma dizinlerinde gerçek Jupyter çekirdeğinde yürütür."""
from pathlib import Path
import argparse,json,os,sys,tempfile,hashlib,zipfile,time
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager
ROOT=Path(__file__).resolve().parents[1]

def execute(n,output,run_twice=False,isolated=False):
 notebook=ROOT/f'bolumler/b{n:02}/colab.ipynb';original=notebook.read_bytes();started=time.monotonic()
 nb=nbformat.read(notebook,as_version=4);nbformat.validate(nb)
 for c in nb.cells:
  if c.cell_type=='code':assert c.execution_count is None and not c.outputs
 with tempfile.TemporaryDirectory(prefix=f'colab-b{n:02}-') as temp:
  work=Path(temp);kernels=work/'kernels';spec=kernels/'kitap-python';spec.mkdir(parents=True)
  (spec/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],'display_name':'Kitap sınama Python','language':'python'}))
  runs=[]
  for repetition in range(2 if run_twice else 1):
   fresh=nbformat.read(notebook,as_version=4)
   if isolated and n!=2:
    fresh.cells.insert(0,nbformat.v4.new_code_cell('FORCE_ISOLATED=True'))
   manager=KernelManager(kernel_name='kitap-python',kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(kernels)]))
   client=NotebookClient(fresh,km=manager,timeout=1200,resources={'metadata':{'path':str(work)}},allow_errors=False)
   try:executed=client.execute()
   finally:
    if manager.has_kernel:manager.shutdown_kernel(now=True)
   assert not any(o.output_type=='error' for c in executed.cells if c.cell_type=='code' for o in c.outputs)
   z=work/('b02-atolye-ciktilar.zip' if n==2 else f'b{n:02}-colab-ciktilar.zip')
   with zipfile.ZipFile(z) as archive:
    assert archive.testzip() is None
    m=json.loads(archive.read('calisma-kaydi.json'))
    journal=json.loads(archive.read('ogrenci-karari.json'))
    assert journal['bolum']==n and journal['alanlar_dolu'] is False
    assert journal==m['ogrenci_karari']
    if n==2:assert len(m['checks'])==9 and all(m['checks'].values())
    else:
     assert m['chapter']==n and all(not differences for differences in m['checks'].values())
     assert any(name.endswith('.log') for name in archive.namelist())
    assert any(name.endswith('.pdf') for name in archive.namelist())
   images=sum(o.output_type=='display_data' and 'image/png' in o.get('data',{}) for c in executed.cells if c.cell_type=='code' for o in c.outputs)
   # B02 calls plt.show(); the inline backend must also be exercised in the kernel.
   assert images>0,f'B{n:02}: grafik hücre içinde gösterilmedi'
   runs.append({'run':repetition+1,'executed_code_cells':sum(c.cell_type=='code' for c in executed.cells),'inline_images':images,'output_zip_verified':True})
   nbformat.write(executed,output/f'b{n:02}-calistirilmis.ipynb')
  assert notebook.read_bytes()==original
  return {'chapter':n,'status':'passed','source_notebook_sha256':hashlib.sha256(original).hexdigest(),'jupyter_kernel':True,'colab_ui_executed':False,'runs':runs,'seconds':round(time.monotonic()-started,2)}

def main():
 p=argparse.ArgumentParser();p.add_argument('--chapters',default=','.join(map(str,range(1,23))));p.add_argument('--report',type=Path,required=True);p.add_argument('--repeat',action='store_true');p.add_argument('--isolated',action='store_true');a=p.parse_args()
 ns=list(map(int,a.chapters.split(',')));assert ns and set(ns)<=set(range(1,23))
 a.report.parent.mkdir(parents=True,exist_ok=True);output=a.report.parent/'executed';output.mkdir(exist_ok=True)
 rows=[]
 for n in ns:
  try:row=execute(n,output,a.repeat,a.isolated)
  except Exception as exc:row={'chapter':n,'status':'failed','error':str(exc)[-12000:],'jupyter_kernel':True,'colab_ui_executed':False}
  rows.append(row);a.report.write_text(json.dumps({'results':rows,'note':'Gerçek Jupyter çekirdeği; Google hesabıyla Colab arayüzü testi değildir.'},ensure_ascii=False,indent=2)+'\n');print(f'B{n:02}: '+row['status'],flush=True)
 if any(r['status']!='passed' for r in rows):raise SystemExit(1)
if __name__=='__main__':main()
