import argparse
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 202609
SAMPLE_SIZE = 160


def generate():
    generator = np.random.default_rng(SEED)
    predictor = generator.normal(size=SAMPLE_SIZE)
    moderator = generator.normal(size=SAMPLE_SIZE)
    mediator_error = generator.normal(size=SAMPLE_SIZE)
    mediation_error = generator.normal(size=SAMPLE_SIZE)
    moderation_error = generator.normal(size=SAMPLE_SIZE)
    mediator = 0.6 * predictor + mediator_error
    mediation_outcome = 0.2 * predictor + 0.7 * mediator + mediation_error
    moderation_outcome = (0.3 * predictor + 0.2 * moderator
                          + 0.5 * predictor * moderator + moderation_error)
    return pd.DataFrame({"kayit": np.arange(1, SAMPLE_SIZE + 1),
                         "x": predictor, "araci": mediator, "w": moderator,
                         "y_aracilik": mediation_outcome,
                         "y_duzenleyicilik": moderation_outcome})


def main():
    parser = argparse.ArgumentParser(description="Gerçek katılımcı içermeyen öğretim simülasyonu.")
    parser.add_argument("--cikti", type=Path, required=True)
    arguments = parser.parse_args()
    with arguments.cikti.open("x", encoding="utf-8", newline="") as destination:
        generate().to_csv(destination, index=False, float_format="%.10f", lineterminator="\n")
    print(f"Simülasyon üretildi: {arguments.cikti}; n={SAMPLE_SIZE}, seed={SEED}.")


if __name__ == "__main__":
    main()