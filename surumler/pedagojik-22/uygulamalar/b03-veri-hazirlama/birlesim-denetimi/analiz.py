"""Gerçek BFI alt puanlarında birleştirme denetimi; ayrı sızıntı kurgusu."""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
import pandas as pd

SOURCE_HASH = '8726fd25dbfc685be2d3d726e5511bbb31ba9c7b367b6864eb06e0d8669e6557'


def checked_join(left, right, key, how):
    if how not in {'inner', 'left', 'outer'}:
        raise ValueError('Bu örnek inner/left/outer bire bir ilişki içindir')
    for frame in [left, right]:
        if key not in frame or frame[key].isna().any() or frame[key].duplicated().any():
            raise ValueError('Anahtar yok, eksik veya tekrarlı')
        if frame[key].astype('string').str.strip().eq('').any():
            raise ValueError('Boş metin anahtar kabul edilmez')
    if left[key].dtype != right[key].dtype:
        raise ValueError('Anahtar türleri sözleşmede eşleşmeli; sessiz dönüştürmeyin')
    if (set(left) & set(right)) - {key}:
        raise ValueError('Anahtar dışındaki ortak sütun adlarını açıklığa kavuşturun')
    return left.merge(right, on=key, how=how, validate='one_to_one', indicator=True, sort=True)


def fit_center(training):
    values = np.asarray(training, dtype=float)
    if not len(values) or not np.isfinite(values).all():
        raise ValueError('Eğitim dizisi boş veya sonlu değil')
    return float(values.mean())


def main():
    directory = Path(__file__).parent
    parent = directory.parent
    source = parent.parent/'b17-guvenirlik/kaynak/bfi-ilk100-AC.csv'
    original = source.read_bytes()
    assert hashlib.sha256(original.replace(b'\r\n', b'\n').rstrip(b'\n')+b'\n').hexdigest() == SOURCE_HASH
    spec = importlib.util.spec_from_file_location('b03_original', parent/'analiz.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    raw = pd.read_csv(source)
    module.validate(raw)
    assert len(raw) == 100
    scores = raw[['kaynak_satir']].copy()
    for prefix in ['A', 'C']:
        items = [f'{prefix}{i}' for i in range(1,6)]
        values = raw[items].copy()
        for item in set(items) & set(module.REVERSE):
            values[item] = 7-values[item]
        scores[prefix+'_ort5'] = module.score(values,5)
    left = scores[['kaynak_satir','A_ort5']].dropna().copy()
    right = scores[['kaynak_satir','C_ort5']].dropna().copy()
    assert len(left) == 99 and len(right) == 98
    output = directory/'sonuclar'
    output.mkdir(exist_ok=True)
    audit = []
    for how, expected in [('inner',97), ('left',99), ('outer',100)]:
        merged = checked_join(left, right, 'kaynak_satir', how)
        assert len(merged) == expected and merged.kaynak_satir.is_unique
        count = merged['_merge'].value_counts()
        audit.append({'join':how, 'rows':len(merged), 'A_valid':int(merged.A_ort5.count()),
                      'C_valid':int(merged.C_ort5.count()), 'both':int(count.get('both',0)),
                      'left_only':int(count.get('left_only',0)), 'right_only':int(count.get('right_only',0)),
                      'A_mean_available':float(merged.A_ort5.mean()),
                      'C_mean_available':float(merged.C_ort5.mean())})
        merged.to_csv(output/(how+'-birlesim.csv'),index=False)
    np.testing.assert_allclose(audit[1]['A_mean_available'], scores.A_ort5.mean())
    np.testing.assert_allclose(audit[2]['C_mean_available'], scores.C_ort5.mean())
    assert audit[2]['left_only'] == 2 and audit[2]['right_only'] == 1
    # Başka bir deney: gerçek BFI verisinden ayrı, yalnız merkezleme sızıntısı.
    training, test = np.array([0.,2.]), np.array([100.,102.])
    train_center = fit_center(training)
    pooled_center = fit_center(np.r_[training,test])
    np.testing.assert_array_equal(training-train_center, [-1.,1.])
    assert train_center == 1 and pooled_center == 51
    result = {'scope':'İlk 100 BFI kaydının hazırlama denetimi; tahmin modeli veya nedensel analiz yok',
              'source_normalized_sha256':SOURCE_HASH, 'raw_rows':100,
              'score_available':{'A':99,'C':98,'both':97}, 'joins':audit,
              'analysis_sets':{'A_only_complete':99, 'C_only_complete':98, 'A_C_common_complete':97},
              'leakage_synthetic':{'training':training.tolist(),'test':test.tolist(),
                                   'training_only_center':train_center, 'pooled_center_wrong_for_training':pooled_center,
                                   'training_centered_correct':(training-train_center).tolist(),
                                   'training_centered_leaked':(training-pooled_center).tolist(),
                                   'prediction_model_fitted':False},
              'versions':{'numpy':np.__version__,'pandas':pd.__version__}}
    pd.DataFrame(audit).to_csv(output/'birlesim-denetimi.csv',index=False)
    (output/'ozet.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    assert source.read_bytes() == original
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
