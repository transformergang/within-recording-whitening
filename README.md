# Within-recording whitening for clustering unseen ship-noise corpora

Companion material for the paper

> *Within-Recording Whitening with Optional Source Fine-Tuning for Clustering Unseen Ship-Noise Corpora*
> (submitted to IEEE ISCAS 2027).

The paper has four pages of technical content. This repository holds what does not fit there: the proofs,
the full tables, the digests of the sealed analysis plans, and a reference implementation of the core method.

## Contents

| path | what it is |
|---|---|
| `proofs/proofs.pdf` (`proofs.tex`) | Assumptions and proofs of Propositions 1 and 2 and of the two consequences stated in the paper. |
| `tables/main_comparison.md` | Every row of Tables I and II for the four target corpora: AMI, accuracy, and the differences to FT+C7- and to C7- with 95% bootstrap intervals. |
| `tables/encoders.md` | C7- against the baseline C2 for five frozen encoders (BEATs, AudioMAE, EAT, CLAP, Dasheng) on the four corpora. |
| `tables/sensitivity.md` | Post hoc sensitivity analyses: misspecified K, number of kept directions, shrinkage coefficient, covariance estimator, windows per recording, fine-tuning seeds. |
| `tables/model_checks.md` | Checks of the nested nuisance model on real and synthetic data; the ShipsEar class-by-date table. |
| `plans/PLAN_HASHES.md` | SHA-256 digests of the sealed analysis plans. |
| `code/c7minus.py` | Reference implementation of within-recording whitening (C7-), of the baseline C2, and of the k-means used in the paper. NumPy only. |

## The method in brief

For the target corpus only, and without any label:

1. `Sigma_e`: pooled covariance of the window vectors around their own recording mean, scaled to unit trace.
2. `Sigma~ = (1 - gamma) Sigma_e + gamma tr(Sigma_e) I / d`, with `gamma = 0.1`.
3. `S_B`: covariance of the recording means.
4. `W = Sigma~^(-1/2) U`, where `U` holds the top `2K` eigenvectors of `Sigma~^(-1/2) S_B Sigma~^(-1/2)`.
5. The recording embeddings `W^T m_i` are clustered by k-means (k-means++, 20 restarts, `K` given).

This is Fisher's criterion with recordings in place of classes.

```python
import numpy as np
from c7minus import c7_minus, kmeans

# X:   (n_windows, d) window vectors of the target corpus
# rec: (n_windows,)   recording index of every window, integers 0..R-1
E, W = c7_minus(X, rec, K)          # E: (R, 2K) recording embeddings
labels = kmeans(E, K, seed=0)       # one of the 20 seeds used in the paper
```

`python code/c7minus.py` runs a small synthetic demonstration.

Input convention of the paper: recordings are cut into 2 s windows at 16 kHz; a window vector is the mean
over tokens of the encoder output, L2-normalized; a recording mean is the plain mean of its window vectors.

**Check against the results of the paper.** On the frozen-BEATs window vectors of the four corpora, the
reference implementation reproduces the embeddings used for the paper with a maximal relative difference
below 1e-13, and the k-means partitions are identical for the seeds tested (0 and 1).

## What is not in this repository

- **Audio data.** The four corpora must be obtained from their providers:
  DeepShip (Irfan et al., *Expert Syst. Appl.* 183, 2021, doi:10.1016/j.eswa.2021.115270),
  ShipsEar (Santos-Dominguez et al., *Appl. Acoust.* 113, 2016, doi:10.1016/j.apacoust.2016.06.008),
  HearMyShip (Shipton et al., *Sci. Data* 12, 2025, doi:10.1038/s41597-025-04584-x),
  VLIZ (Decrop et al., *IEEE J. Sel. Topics Appl. Earth Observ. Remote Sens.* 18, 2025, doi:10.1109/JSTARS.2025.3593779).
- **Third-party code.** TURTLE, PET-TURTLE and SPLINCE were run from their authors' code
  (TURTLE commit `4674efab`, PET-TURTLE commit `62de89be`, SPLINCE commit `fced0d3b`), LEACE from the `concept-erasure` package (0.2.4)
  and ComBat from the `pycombat` package (0.20). None of it is redistributed here.
- **Fine-tuning and evaluation scripts.** This snapshot contains the reference implementation of the core
  method only.

## Conventions used in the tables

- AMI is the adjusted mutual information, mean of 20 k-means seeds.
- Final scoring: units of classes with fewer than five units are not scored (VLIZ 3 units, HearMyShip 6 units);
  clustering always uses all units. The frozen-encoder table scores all units, as stated there.
- Intervals are 95% percentile intervals of a dependency-group bootstrap with B = 200.
- DS = DeepShip, SE = ShipsEar, HMS = HearMyShip, VL = VLIZ.
