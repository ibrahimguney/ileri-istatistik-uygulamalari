import hashlib
import json
from itertools import combinations, permutations, product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import stats
from statsmodels.stats.multitest import multipletests

SEED = 202612
RESAMPLES = 99999


def holm(probabilities):
    values = np.asarray(probabilities)
    order = np.argsort(values)
    adjusted = np.empty(len(values))
    adjusted[order] = np.minimum(1, np.maximum.accumulate(values[order] * np.arange(len(values), 0, -1)))
    np.testing.assert_allclose(adjusted, multipletests(values, method="holm")[1])
    return adjusted


def independent(first, second):
    ranks = stats.rankdata(np.concatenate([first, second]))
    first_n, second_n = len(first), len(second)
    statistic = ranks[:first_n].sum() - first_n * (first_n + 1) / 2
    tested = stats.mannwhitneyu(first, second, method="asymptotic", use_continuity=True)
    np.testing.assert_allclose(statistic, tested.statistic)
    wins = np.sum(first[:, None] > second)
    ties = np.sum(first[:, None] == second)
    superiority = (wins + .5 * ties) / (first_n * second_n)
    np.testing.assert_allclose(superiority, statistic / (first_n * second_n))
    rank_sums = np.fromiter((sum(ranks[list(indices)]) for indices in combinations(range(len(ranks)), first_n)), dtype=float)
    observed = ranks[:first_n].sum()
    exact_p = min(1, 2 * min(np.mean(rank_sums <= observed), np.mean(rank_sums >= observed)))
    permuted = stats.mannwhitneyu(first, second, method=stats.PermutationMethod(n_resamples=np.inf, batch=2048))
    np.testing.assert_allclose(exact_p, permuted.pvalue)
    return {"U_first": float(statistic), "U_second": float(first_n * second_n-statistic),
            "mean_ranks": [float(ranks[:first_n].mean()), float(ranks[first_n:].mean())],
            "medians": [float(np.median(first)), float(np.median(second))],
            "wins": int(wins), "ties_between_groups": int(ties), "A": float(superiority),
            "rank_biserial": float(2*superiority-1), "p_asymptotic_continuity": float(tested.pvalue),
            "p_exhaustive": float(exact_p), "allocations": len(rank_sums)}


def signed(differences):
    nonzero = differences[differences != 0]
    ranks = stats.rankdata(abs(nonzero))
    positive = ranks[nonzero > 0].sum()
    negative = ranks[nonzero < 0].sum()
    possible = np.array(list(product([0, 1], repeat=len(nonzero)))) @ ranks
    probability = min(1, 2*min(np.mean(possible <= positive), np.mean(possible >= positive)))
    tested = stats.wilcoxon(differences, zero_method="wilcox", method=stats.PermutationMethod(n_resamples=np.inf))
    np.testing.assert_allclose([min(positive, negative), probability], tested)
    asymptotic = stats.wilcoxon(differences, zero_method="wilcox", method="asymptotic", correction=True)
    return {"n_pairs": len(differences), "n_zero": int(np.sum(differences == 0)),
            "differences": differences.tolist(), "W_plus": float(positive), "W_minus": float(negative),
            "T": float(min(positive, negative)), "p_exhaustive": float(probability),
            "sign_patterns": len(possible), "p_asymptotic_continuity": float(asymptotic.pvalue),
            "rank_biserial_nonzero": float((positive-negative)/(positive+negative))}


def kruskal_dunn(groups):
    values = np.concatenate(groups)
    ranks = stats.rankdata(values)
    sizes = np.array([len(group) for group in groups])
    total_n = len(values)
    rank_groups = np.split(ranks, np.cumsum(sizes)[:-1])
    means = np.array([group.mean() for group in rank_groups])
    sums = np.array([group.sum() for group in rank_groups])
    counts = np.unique(values, return_counts=True)[1]
    tie_sum = np.sum(counts**3-counts)
    correction = 1-tie_sum/(total_n**3-total_n)
    raw = 12/(total_n*(total_n+1))*np.sum(sums**2/sizes)-3*(total_n+1)
    statistic = raw/correction
    tested = stats.kruskal(*groups)
    np.testing.assert_allclose([statistic, stats.chi2.sf(statistic, len(groups)-1)], tested)
    variance = total_n*(total_n+1)/12 - tie_sum/(12*(total_n-1))
    np.testing.assert_allclose(variance, ranks.var(ddof=1))
    pairs = []
    for lower, upper in combinations(range(len(groups)), 2):
        delta = means[upper]-means[lower]
        standard = np.sqrt(variance*(1/sizes[lower]+1/sizes[upper]))
        statistic_z = delta/standard
        pairs.append({"comparison": [lower, upper], "mean_rank_difference": float(delta),
                      "z": float(statistic_z), "p_raw": float(2*stats.norm.sf(abs(statistic_z)))})
    for pair, probability in zip(pairs, holm([pair["p_raw"] for pair in pairs])):
        pair["p_holm"] = float(probability)
    return {"rank_sums": sums.tolist(), "mean_ranks": means.tolist(), "tie_correction": float(correction),
            "H_raw": float(raw), "H": float(statistic), "df": len(groups)-1,
            "p": float(tested.pvalue), "dunn_holm": pairs}


def friedman(values):
    ranks = stats.rankdata(values, axis=1)
    blocks, conditions = values.shape
    tie_sum = sum(np.sum(counts**3-counts) for counts in [np.unique(row, return_counts=True)[1] for row in values])
    correction = 1-tie_sum/(blocks*(conditions**3-conditions))
    def statistic(rank_totals):
        return (12/(blocks*conditions*(conditions+1))*np.sum(rank_totals**2, axis=-1)-3*blocks*(conditions+1))/correction
    observed = statistic(ranks.sum(axis=0))
    tested = stats.friedmanchisquare(*values.T)
    np.testing.assert_allclose([observed, stats.chi2.sf(observed, conditions-1)], tested)
    rng = np.random.default_rng(SEED)
    choices = np.array(list(permutations(range(conditions))))
    exceedances = 0
    for start in range(0, RESAMPLES, 2000):
        size = min(2000, RESAMPLES-start)
        indices = choices[rng.integers(0, len(choices), size=(size, blocks))]
        permuted_ranks = np.take_along_axis(np.broadcast_to(ranks, (size, blocks, conditions)), indices, axis=2)
        exceedances += np.count_nonzero(statistic(permuted_ranks.sum(axis=1)) >= observed-1e-10)
    monte_carlo = (exceedances+1)/(RESAMPLES+1)
    pairs = []
    for lower, upper in combinations(range(conditions), 2):
        differences = np.round(values[:, upper]-values[:, lower], 2)
        result = stats.wilcoxon(differences, zero_method="wilcox", method="asymptotic", correction=True)
        pairs.append({"comparison": [lower, upper], "median_difference": float(np.median(differences)),
                      "n_zero": int(np.sum(differences==0)), "T": float(result.statistic), "p_raw": float(result.pvalue)})
    for pair, probability in zip(pairs, holm([pair["p_raw"] for pair in pairs])):
        pair["p_holm"] = float(probability)
    return {"n_blocks": blocks, "rank_sums": ranks.sum(axis=0).tolist(), "tie_correction": float(correction),
            "Q": float(observed), "df": conditions-1, "p_chi_square": float(tested.pvalue),
            "Kendall_W": float(observed/(blocks*(conditions-1))), "p_monte_carlo": monte_carlo,
            "monte_carlo_se": float(np.sqrt(monte_carlo*(1-monte_carlo)/RESAMPLES)),
            "exceedances": int(exceedances), "resamples": RESAMPLES, "seed": SEED, "pairs_holm": pairs}


def main():
    directory = Path(__file__).resolve().parent
    paths = [directory/name for name in ["sleep.csv", "ToothGrowth.csv", "rounding-times.csv"]]
    original_bytes = [path.read_bytes() for path in paths]
    expected = ["adc729344227b4c76a9c3fb3588a46028909946aebf56676aca2d4860271231e",
                "654a2c36a26499006839c1c3ee2d899bf455eb14eef59ddb6764a49b39d838f3",
                "b286d277d7784cdcb0e4916f1240d2ad03ffd7f6b18a9f456ea2183458f3d869"]
    for content, checksum in zip(original_bytes, expected):
        assert hashlib.sha256(content.replace(b"\r\n", b"\n").rstrip(b"\n")+b"\n").hexdigest() == checksum, "Yerel kaynak kopyası değişmiş; kaynak ve kitap sonuçlarını birlikte denetleyin."
    sleep, teeth, rounding = [pd.read_csv(path) for path in paths]
    assert sleep.shape == (20, 4) and teeth.shape == (60, 4) and rounding.shape == (22, 4)
    np.testing.assert_array_equal(rounding.blok, np.arange(1, 23))
    assert all(not frame.isna().any().any() for frame in [sleep, teeth, rounding])
    assert (teeth.groupby(["supp", "dose"]).size() == 10).all()
    paired = sleep.pivot(index="ID", columns="group", values="extra").sort_index()
    shuffled = sleep.sample(frac=1, random_state=SEED).pivot(index="ID", columns="group", values="extra").sort_index()
    pd.testing.assert_frame_equal(paired, shuffled)
    differences = np.round(paired[2].to_numpy()-paired[1].to_numpy(), 1)
    mw = independent(teeth.loc[(teeth.supp=="OJ") & (teeth.dose==1), "len"].to_numpy(),
                     teeth.loc[(teeth.supp=="VC") & (teeth.dose==1), "len"].to_numpy())
    kw = {supp: kruskal_dunn([teeth.loc[(teeth.supp==supp) & (teeth.dose==dose), "len"].to_numpy()
                            for dose in [.5, 1, 2]]) for supp in ["OJ", "VC"]}
    table = pd.crosstab(teeth.supp, teeth.len >= 20).reindex(index=["OJ", "VC"], columns=[False, True]).to_numpy()
    chi = stats.chi2_contingency(table, correction=False)
    expected_counts = np.outer(table.sum(axis=1), table.sum(axis=0))/table.sum()
    np.testing.assert_allclose(expected_counts, chi.expected_freq)
    np.testing.assert_allclose(np.sum((table-expected_counts)**2/expected_counts), chi.statistic)
    results = {"sources": [{"path": path.name, "sha256": hashlib.sha256(content).hexdigest()}
                            for path, content in zip(paths, original_bytes)],
               "remote_automatic_comparison": False, "mann_whitney_dose1": mw,
               "sleep_wilcoxon": signed(differences), "kruskal_dunn": kw,
               "friedman": friedman(rounding.iloc[:, 1:].to_numpy()),
               "chi_square_threshold20": {"table": table.tolist(), "expected": expected_counts.tolist(),
                                         "chi2": float(chi.statistic), "df": int(chi.dof), "p": float(chi.pvalue),
                                         "cramers_V": float(np.sqrt(chi.statistic/table.sum())),
                                         "fisher_two_sided_p": float(stats.fisher_exact(table).pvalue)},
               "versions": {"numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__}}
    output = directory/"sonuclar"
    output.mkdir(exist_ok=True)
    paired.rename(columns={1: "ilac1", 2: "ilac2"}).to_csv(output/"uyku_genis.csv")
    teeth.assign(supp_kod=teeth.supp.map({"OJ": 1, "VC": 2}),
                 dose_kod=teeth.dose.map({.5: 1, 1: 2, 2: 3}),
                 esik20=(teeth.len >= 20).astype(int)).to_csv(output/"dis_analiz.csv", index=False)
    (output/"ozet.json").write_text(json.dumps(results, indent=2)+"\n", encoding="utf-8")
    pd.DataFrame({"ID": paired.index, "fark_2_eksi_1": differences}).to_csv(output/"uyku_farklar.csv", index=False)
    for supp in ["OJ", "VC"]:
        pd.DataFrame(kw[supp]["dunn_holm"]).to_csv(output/f"dunn_{supp}.csv", index=False)
    pd.DataFrame(results["friedman"]["pairs_holm"]).to_csv(output/"friedman_ikili.csv", index=False)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
    figures = directory/"grafikler"
    figures.mkdir(exist_ok=True)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.5), constrained_layout=True)
    for supp, color in [("OJ", "#781e2d"), ("VC", "#3c3c41")]:
        values = np.sort(teeth.loc[(teeth.supp==supp) & (teeth.dose==1), "len"])
        axes[0].step(values, np.arange(1, len(values)+1)/len(values), where="post", label=supp, color=color)
    axes[0].legend(frameon=False)
    axes[0].set(xlabel="Uzunluk (kaynak birimi)", ylabel="Ampirik birikimli oran", title="(a) 1 mg/gün: OJ ve VC")
    axes[1].axhline(0, color="#3c3c41", linewidth=1)
    axes[1].scatter(paired.index, differences, color="#781e2d")
    axes[1].set(xlabel="Eşleştirme ID", ylabel="İlaç 2 − ilaç 1 (saat)", title="(b) Uyku: 10 çift")
    figure.savefig(figures/"b12-sira-ve-fark.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    figure, axes = plt.subplots(1, 2, figsize=(6.4, 3.4), constrained_layout=True)
    for row in rounding.iloc[:, 1:].to_numpy():
        axes[0].plot([0, 1, 2], row, color="#3c3c41", alpha=.35, marker="o", markersize=2)
    axes[0].set(xticks=[0, 1, 2], xticklabels=["Round", "Narrow", "Wide"], ylabel="Süre (kaynak birimi)", title="(a) 22 blok: bağlı ölçümler")
    axes[1].bar([0, 1, 2], results["friedman"]["rank_sums"], color=["#781e2d", "#c49b5c", "#3c3c41"])
    axes[1].set(xticks=[0, 1, 2], xticklabels=["Round", "Narrow", "Wide"], ylabel="Blok içi sıra toplamı", title="(b) Küçük sıra: kısa süre")
    figure.savefig(figures/"b12-friedman.pdf", metadata={"CreationDate": None, "ModDate": None})
    plt.close(figure)
    assert original_bytes == [path.read_bytes() for path in paths]
    print(json.dumps(results, indent=2))
    print("Doğrulama başarılı: U, işaret örüntüleri, bağ düzeltmeleri, Holm, Friedman ve beklenen frekanslar.")


if __name__ == "__main__":
    main()