# Protocol details

Details that the four-page paper only summarizes. Names: the paper's *Baseline*, *WR* and *FT+WR* are `C2`, `C7-` and
`FT+C7-` in the tables and in the code.

## Setting

- Four corpora; each is the target in turn and the other three are the sources.
- The target contributes its unlabeled windows, their recording membership and the number of classes `K`.
  Target labels are read only for scoring.
- `K` counts the classes with at least five units and is given to every method.
- Dependency groups (recording, voyage or vessel) and sessions (date, station or deployment) come from the metadata of
  the corpora.
- Recordings are cut into 2 s windows at 16 kHz. A window vector is the mean over tokens of the encoder output,
  L2-normalized; a recording vector is the plain mean of its window vectors.

## Label-free part (WR)

- Shrinkage `gamma = 0.1` and the `2K` retained directions are fixed hyper-parameters.
- k-means++ with 20 fixed seeds, 20 restarts each.

## Optional fine-tuning (FT+WR)

- The last two BEATs transformer layers are trained on the three source corpora; the first ten stay frozen.
- A batch holds 64 recordings with two windows each from one source corpus; corpora alternate.
- Loss: supervised contrastive, temperature 0.1, projection 768 -> 256 -> 128. Positives share a class but differ in
  dependency group and session. Labels are never compared across corpora.
- Optional recording discriminator behind a gradient-reversal layer with weight `lambda` in {0, 0.5}. `lambda` is
  selected inside the three source corpora by leave-one-source-out validation; the selected value was 0 with DeepShip or
  HearMyShip as the target and 0.5 with ShipsEar or VLIZ as the target.
- AdamW, learning rate 2e-5 for the layers and 1e-3 for the heads, weight decay 0.01, 1500 steps, at most eight windows
  per recording.
- The target takes no part in fine-tuning or in the choice of `lambda`.
- The main tables use one fine-tuning seed; two more are in `tables/sensitivity.md`.
- Shuffled-label control: the same training with the class labels permuted inside every source corpus.

## Baseline

A per-dimension z-score fitted on the three other corpora, L2 normalization, k-means.

## Compared methods

Every method receives the same embeddings, `K`, 20 seeds and scoring.

- Inputs of the clustering heads: `Z` (the baseline input before L2 normalization), `W_frozen` (WR of frozen BEATs) and
  `W_FT` (FT+WR). The `W` inputs are centered and rescaled to unit mean variance.
- TURTLE: cold start; `gamma` in {1, 10, 100}.
- PET-TURTLE: warm start; the final iterate is returned instead of a checkpoint chosen by label accuracy;
  `(gamma, alpha)` in {(50, 0.5), (250, 0.01), (250, 0.5)}.
- The hyper-parameters of both heads are chosen per target by leave-one-source-out AMI inside the source corpora;
  `W_FT` reuses the choice made for `W_frozen`.
- LEACE erases the linear information that predicts the target's session; ComBat adjusts per-session location and scale
  by empirical Bayes. Both act on `Z` of the target with session metadata and no class label. Single-unit sessions form
  one batch. On DeepShip, where 247 of the 363 sessions hold a single unit, ComBat corrected no dimension and equals
  the baseline.
- SPLINCE is fitted on the source corpora, erasing the session while preserving covariance with each corpus's class
  indicators, and applied to the target. The condition of its estimator fails here, because session and class
  indicators are collinear across corpora.

## Scoring and intervals

- AMI is the mean over the 20 k-means seeds; Hungarian-matched accuracy is in `tables/main_comparison.md`.
- Final scoring: units of classes with fewer than five units are not scored (VLIZ 3 units, HearMyShip 6 units);
  clustering always uses all units.
- Intervals are 95% percentile intervals of a bootstrap over dependency groups with `B = 200` on fixed partitions, with
  four paired seeds per resample. The frozen-encoder comparison refits both arms on every resample. The reduction row of
  `tables/ablation.md` uses all 20 seeds per resample.
