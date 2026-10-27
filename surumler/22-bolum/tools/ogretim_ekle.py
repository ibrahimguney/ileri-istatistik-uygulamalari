"""Öğretim katmanını analiz kodundan ayrı, yeniden üretilebilir biçimde ekler."""
from pathlib import Path
import json,textwrap,re
ROOT=Path(__file__).resolve().parents[1]

def apply(nb,e):
 n=e['number'];tag=f'ogretim27-b{n:02}'
 nb['cells']=[c for c in nb['cells'] if c.get('metadata',{}).get('teaching_revision')!=27]
 def cell(kind,source,suffix):
  c={'cell_type':kind,'id':tag+'-'+suffix,'metadata':{'teaching_revision':27},'source':textwrap.dedent(source).strip().splitlines(keepends=True)}
  if kind=='code':c.update(execution_count=None,outputs=[])
  return c
 intro='## Üç çekirdek kazanım ve ileri rota\n\n'+'\n'.join(f'{i+1}. {t}' for i,t in enumerate(e['core']))+'\n\n**İleri rota:** '+e['advanced']+'\n\n**Ç1 · Çıkış sorusu:** '+e['exit_question']+'\n\nYanıtınızı çalışma sonunda öğrenci karar günlüğüne yazın. [Rubrik ve teslim rehberi](https://ibrahimguney.github.io/ileri-istatistik-uygulamalari/surumler/22-bolum/'+e['page']+'RUBRIK.md).'
 nb['cells'].insert(1,cell('markdown',intro,'rota'))
 decision='''## Öğrenci kararı ve kısa savunma

**Karar görevi:** '''+e['decision_task']+'''

Yalnız bir kararı değiştirin. Ana sonucu koruyun; gerekirse yeni bir hesap hücresi ekleyip denemeyi ayrı kaydedin. Sayısal referansları yeni sonuca uydurmayın. Önce/sonra kanıtını sonuç dosyası, tablo veya açık bir hesapla ilişkilendirin. Yapılmamış hesabı yapılmış gibi yazmayın.

**3–5 dakikalık savunma:** Hangi hedefi seçtiniz ve neden? Tam olarak ne değişti? Hangi belirsizlik ve kapsam sınırı kaldı? Karşılaştırma aynı hipotezi mi sınadı?

Aşağıdaki alanları kendi çalışmanızla doldurun. **Tümünü çalıştır**, bu alanları sizin yerinize tamamlamaz. Sayısal kontrollerin geçmesi öğrenci kararının tamamlandığı anlamına gelmez. Alanların dolu olması da kanıtın doğruluğunu otomatik onaylamaz.
'''
 code='''karar_gunlugu = {
    "bolum": '''+str(n)+''',
    "gorev": '''+repr(e['decision_task'])+''',
    "kararim": "",
    "gerekcem": "",
    "degistirdigim_tek_sey": "",
    "onceki_kanit": "",
    "sonraki_kanit": "",
    "belirsizlik_ve_sinir": "",
    "kisa_savunma": "",
    "cikis_yanitim": ""
}
zorunlu_alanlar = ["kararim","gerekcem","degistirdigim_tek_sey","onceki_kanit","sonraki_kanit","belirsizlik_ve_sinir","kisa_savunma","cikis_yanitim"]
karar_gunlugu["alanlar_dolu"] = all(isinstance(karar_gunlugu[k],str) and bool(karar_gunlugu[k].strip()) for k in zorunlu_alanlar)
karar_gunlugu["durum"] = "Öğretim elemanı incelemesi gerekir" if karar_gunlugu["alanlar_dolu"] else "Öğrenci kararı henüz tamamlanmadı"
print(karar_gunlugu["durum"])
# Bu hücreyi doldurduktan sonra çıktı ZIP'i hücresini yeniden çalıştırın.
'''
 # Export hücresinden önce yerleştir; diğer özgün kod/yanıt alanlarını koru.
 index=next(i for i,c in enumerate(nb['cells']) if c['cell_type']=='code' and 'manifest' in ''.join(c['source']) and 'ZipFile' in ''.join(c['source']))
 nb['cells'][index:index]=[cell('markdown',decision,'karar'),cell('code',code,'gunluk')]
 export=nb['cells'][index+2];source=''.join(export['source'])
 source=re.sub(r'# OGRETIM_EXPORT_BEGIN\n.*?# OGRETIM_EXPORT_END\n','',source,flags=re.S)
 source=source.replace('    z.write(work/"ogrenci-karari.json","ogrenci-karari.json")\n','')
 marker='(work/"calisma-kaydi.json").write_text'
 assert marker in source,n
 source=source.replace(marker,'# OGRETIM_EXPORT_BEGIN\nmanifest["ogrenci_karari"] = karar_gunlugu\n(work/"ogrenci-karari.json").write_text(json.dumps(karar_gunlugu,ensure_ascii=False,indent=2),encoding="utf-8")\n# OGRETIM_EXPORT_END\n'+marker,1)
 source=re.sub(r'(with zipfile.ZipFile\(archive,[^\n]+\) as z:\n)',r'\1    z.write(work/"ogrenci-karari.json","ogrenci-karari.json")\n',source,count=1)
 assert source.count('z.write(work/"ogrenci-karari.json"')==1,n
 export['source']=source.splitlines(keepends=True)
 return nb

def main():
 data=json.loads((ROOT/'OGRENME-ROTALARI.json').read_text())['chapters']
 for e in data:
  f=ROOT/e['page']/'colab.ipynb';nb=apply(json.loads(f.read_text()),e);f.write_text(json.dumps(nb,ensure_ascii=False,indent=2)+'\n')
 print('22 Colab defterine öğretim katmanı eklendi.')
if __name__=='__main__':main()
