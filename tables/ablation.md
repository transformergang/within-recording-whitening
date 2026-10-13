# Ablations of the label-free part (frozen BEATs)

AMI, mean of 20 k-means seeds. Names: *Baseline* = `C2`, *WR* = `C7-`.

## Variants of the transform (all units scored)

| variant | DS | HMS | VL | SE |
|---|---|---|---|---|
| Baseline | 0.169 | 0.289 | 0.061 | 0.319 |
| whitening by the target's total scatter (2K principal directions) | 0.142 | 0.270 | 0.063 | 0.213 |
| within-recording whitening without the reduction | 0.229 | 0.334 | 0.075 | 0.230 |
| WR (within-recording whitening, 2K generalized eigendirections) | 0.281 | 0.330 | 0.074 | 0.204 |
| WR with windows shuffled across recordings before the covariance is estimated (control) | 0.041 | 0.031 | 0.048 | 0.034 |

Differences quoted in the paper: total-scatter whitening minus Baseline is -0.027, -0.018, +0.002 and -0.106;
WR minus the shuffled-window control is +0.240, +0.299, +0.026 and +0.170 (DS, HMS, VL, SE). With all units scored, WR on HMS is 0.330; with the final scoring used elsewhere it is 0.329.

## Effect of the reduction step (final scoring)

WR minus within-recording whitening without the reduction, with 95% percentile intervals of the dependency-group
bootstrap (B = 200, fixed partitions, 20 seeds per resample).

| corpus | without reduction | WR | difference [95% interval] |
|---|---|---|---|
| DS | 0.229 | 0.281 | +0.052 [+0.025, +0.074] |
| HMS | 0.334 | 0.329 | -0.004 [-0.011, +0.001] |
| VL | 0.075 | 0.074 | -0.001 [-0.003, +0.001] |
| SE | 0.230 | 0.204 | -0.026 [-0.042, -0.001] |
