"""New chapter identities must preserve the corresponding legacy scientific material."""
from pathlib import Path
import unittest,json
ROOT=Path(__file__).resolve().parents[1]
class ChapterIdentity(unittest.TestCase):
 def test_bijection_and_no_forward_core_prerequisite(self):
  entries=json.loads((ROOT/'BOLUM_ESLESMESI.json').read_text())['chapters']
  self.assertEqual([e['number'] for e in entries],list(range(1,23)))
  self.assertEqual(sorted(e['source_number'] for e in entries),list(range(1,23)))
  for e in json.loads((ROOT/'OGRENME-ROTALARI.json').read_text())['chapters']:
   self.assertTrue(all(p<e['number'] for p in e['prerequisites']))
 def test_scientific_material_and_frozen_colab_identity(self):
  legacy=ROOT.parent/'22-bolum'
  if legacy.is_dir():
   for f in (ROOT/'uygulamalar').rglob('*'):
    if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc':
     self.assertEqual(f.read_bytes(),(legacy/f.relative_to(ROOT)).read_bytes(),str(f))
  for e in json.loads((ROOT/'BOLUM_ESLESMESI.json').read_text())['chapters']:
   b=ROOT/e['page'];source=e['source_number'];n=e['number']
   self.assertIn(e['application'],(b/'analiz.py').read_text())
   if legacy.is_dir():self.assertEqual((b/'beklenen.json').read_bytes(),(legacy/f'bolumler/b{source:02}/beklenen.json').read_bytes())
   if n!=2:
    nb=json.loads((b/'colab.ipynb').read_text());code='\n'.join(''.join(c['source']) for c in nb['cells'])
    self.assertIn(f'run_script("bolumler/b{source:02}/analiz.py")',code)
    self.assertIn(f'root/"bolumler/b{source:02}/beklenen.json"',code)
if __name__=='__main__':unittest.main()
