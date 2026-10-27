"""Öğretim sözleşmesi ve yanlış tamamlanma iddiasını engelleyen kontroller."""
import unittest,json,ast,copy,contextlib,io
from pathlib import Path
from ogretim_ekle import apply,ROOT
class TeachingContract(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.data=json.loads((ROOT/'OGRENME-ROTALARI.json').read_text())['chapters']
 def test_prerequisite_graph_has_no_cycle(self):
  graph={e['number']:e['prerequisites'] for e in self.data};visiting=set();done=set()
  def visit(n):
   self.assertNotIn(n,visiting)
   if n in done:return
   visiting.add(n)
   for p in graph[n]:self.assertIn(p,graph);visit(p)
   visiting.remove(n);done.add(n)
  for n in graph:visit(n)
  self.assertIn(10,graph[14])
 def test_every_chapter_has_three_core_outcomes_and_one_exit(self):
  self.assertEqual([e['number'] for e in self.data],list(range(1,23)))
  for e in self.data:
   self.assertEqual(len(e['core']),3);self.assertTrue(e['exit_question']);self.assertTrue(e['exit_answer']);self.assertTrue(e['advanced'])
 def test_local_rubric_totals_and_dimensions(self):
  for e in self.data:
   self.assertEqual(sum(r['points'] for r in e['local_rubric']),100)
   for row in e['local_rubric']:self.assertTrue(set(row['common_dimensions'])<=set(['K1','K2','K3','K4','K5','K6']))
 def test_blank_journal_is_not_completed_and_filled_is_only_review_ready(self):
  for e in self.data:
   nb=json.loads((ROOT/e['page']/'colab.ipynb').read_text());cell=next(c for c in nb['cells'] if c['id'].endswith('-gunluk'))
   code=''.join(cell['source']);namespace={}
   with contextlib.redirect_stdout(io.StringIO()):exec(compile(code,'student-journal','exec'),namespace)
   self.assertFalse(namespace['karar_gunlugu']['alanlar_dolu'])
   for key in namespace['zorunlu_alanlar']:namespace['karar_gunlugu'][key]='Öğrencinin örnek yanıtı'
   validation=code[code.index('zorunlu_alanlar ='):]
   with contextlib.redirect_stdout(io.StringIO()):exec(compile(validation,'student-journal','exec'),namespace)
   self.assertTrue(namespace['karar_gunlugu']['alanlar_dolu'])
   self.assertEqual(namespace['karar_gunlugu']['durum'],'Öğretim elemanı incelemesi gerekir')
 def test_teaching_overlay_is_idempotent_and_exports_once(self):
  for e in self.data:
   nb=json.loads((ROOT/e['page']/'colab.ipynb').read_text());first=apply(copy.deepcopy(nb),e);second=apply(copy.deepcopy(first),e)
   self.assertEqual(first,second)
   sources='\n'.join(''.join(c['source']) for c in first['cells'] if c['cell_type']=='code')
   self.assertEqual(sources.count('z.write(work/"ogrenci-karari.json"'),1)
   for c in first['cells']:
    if c['cell_type']=='code':ast.parse(''.join(c['source']))
if __name__=='__main__':unittest.main()
