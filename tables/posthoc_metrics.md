# Post hoc analyses of the stored partitions

Everything on this page is **post hoc**: it was computed after the main results, from the partitions behind Table I of the paper, without any new clustering. Scoring as in the paper: classes with fewer than five recordings are not scored, every value is the mean over the 20 k-means seeds, and intervals are 95% percentile intervals of the dependency-group bootstrap (B = 200, fixed partitions, the 20 seeds averaged in every resample). Names: *Baseline* = `C2`, *WR* = `C7-`, *FT+WR* = `FT+C7-`.

## Effect of the reduction step for five frozen encoders

WR minus within-recording whitening without the reduction (whitening only), AMI difference [95% interval].

| encoder | DS | HMS | VL | SE |
|---|---|---|---|---|
| BEATs | +0.052 [+0.025, +0.074] | -0.004 [-0.011, +0.001] | -0.001 [-0.003, +0.001] | -0.026 [-0.042, -0.001] |
| AudioMAE | +0.001 [-0.008, +0.010] | -0.000 [-0.004, +0.003] | -0.000 [-0.002, +0.001] | +0.065 [+0.019, +0.102] |
| EAT | -0.016 [-0.035, -0.002] | -0.002 [-0.006, +0.003] | +0.002 [+0.000, +0.005] | +0.010 [-0.007, +0.033] |
| CLAP | -0.005 [-0.020, +0.011] | -0.004 [-0.014, +0.006] | -0.001 [-0.003, +0.002] | -0.001 [-0.028, +0.036] |
| Dasheng | +0.049 [+0.027, +0.074] | +0.004 [-0.003, +0.011] | +0.000 [-0.001, +0.002] | -0.004 [-0.033, +0.012] |

Over the 20 encoder-corpus cells the difference is positive in 8, its interval lies above zero in 4 and below zero in 2; the other 14 intervals contain zero. The effect of the reduction therefore depends on the encoder; with BEATs it is clearly positive only on DeepShip.

## Labelling accuracy with one label per cluster

An analyst labels one randomly chosen recording per cluster and gives its class to the whole cluster (K labels in total). The expected fraction of correctly labelled recordings is (1/N) sum_k sum_c n_kc^2 / n_k, computed on the scored recordings (n_kc: recordings of class c in cluster k). The majority-class rate (every recording given the most frequent class, which the analyst does not know in advance) is shown for reference.

| corpus | K | majority-class rate | Baseline | WR | FT+WR | WR - Baseline | FT+WR - Baseline |
|---|---|---|---|---|---|---|---|
| DeepShip | 4 | 0.394 | 0.417 | 0.466 | 0.486 | +0.049 [+0.022, +0.072] | +0.069 [+0.042, +0.092] |
| HearMyShip | 5 | 0.624 | 0.608 | 0.628 | 0.633 | +0.020 [-0.000, +0.039] | +0.025 [+0.005, +0.041] |
| VLIZ | 16 | 0.459 | 0.318 | 0.321 | 0.321 | +0.003 [-0.002, +0.009] | +0.003 [-0.003, +0.010] |
| ShipsEar | 5 | 0.333 | 0.448 | 0.367 | 0.378 | -0.080 [-0.141, -0.047] | -0.069 [-0.138, -0.037] |

All rows of Table I:

| method | DS | HMS | VL | SE |
|---|---|---|---|---|
| Baseline | 0.417 | 0.608 | 0.318 | 0.448 |
| LEACE (session) | 0.366 | 0.595 | 0.317 | 0.315 |
| ComBat (session) | 0.417 | 0.597 | 0.317 | 0.341 |
| TURTLE x Z | 0.420 | 0.558 | 0.311 | 0.415 |
| PET-TURTLE x Z | 0.379 | 0.555 | 0.310 | 0.362 |
| TURTLE x W_frozen | 0.404 | 0.583 | 0.314 | 0.378 |
| PET-TURTLE x W_frozen | 0.412 | 0.581 | 0.315 | 0.350 |
| WR | 0.466 | 0.628 | 0.321 | 0.367 |
| SPLINCE | 0.396 | 0.445 | 0.291 | 0.321 |
| TURTLE x W_FT | 0.399 | 0.580 | 0.315 | 0.368 |
| PET-TURTLE x W_FT | 0.428 | 0.572 | 0.315 | 0.346 |
| FT+WR shuffled labels | 0.482 | 0.634 | 0.309 | 0.381 |
| FT+WR | 0.486 | 0.633 | 0.321 | 0.378 |

## AMI, ARI and clustering accuracy of every row of Table I

ARI: adjusted Rand index. ACC: clustering accuracy after matching clusters to classes one to one (Hungarian algorithm). Rank 1 = best of the 13 rows.

### DeepShip

| method | AMI | ARI | ACC | rank AMI | rank ARI | rank ACC |
|---|---|---|---|---|---|---|
| Baseline | 0.169 | 0.116 | 0.445 | 7 | 10 | 6 |
| LEACE (session) | 0.121 | 0.135 | 0.414 | 13 | 7 | 12 |
| ComBat (session) | 0.169 | 0.116 | 0.445 | 7 | 10 | 6 |
| TURTLE x Z | 0.184 | 0.153 | 0.500 | 5 | 5 | 4 |
| PET-TURTLE x Z | 0.122 | 0.102 | 0.439 | 12 | 12 | 11 |
| TURTLE x W_frozen | 0.162 | 0.130 | 0.441 | 9 | 8 | 9 |
| PET-TURTLE x W_frozen | 0.182 | 0.140 | 0.443 | 6 | 6 | 8 |
| WR | 0.281 | 0.282 | 0.578 | 3 | 3 | 1 |
| SPLINCE | 0.146 | 0.091 | 0.410 | 11 | 13 | 13 |
| TURTLE x W_FT | 0.153 | 0.125 | 0.439 | 10 | 9 | 10 |
| PET-TURTLE x W_FT | 0.200 | 0.166 | 0.468 | 4 | 4 | 5 |
| FT+WR shuffled labels | 0.282 | 0.283 | 0.571 | 2 | 1 | 3 |
| FT+WR | 0.286 | 0.283 | 0.572 | 1 | 2 | 2 |

FT+WR minus Baseline: AMI +0.117 [+0.080, +0.154], ARI +0.167 [+0.124, +0.212], ACC +0.127 [+0.084, +0.160]. Best row: AMI FT+WR, ARI FT+WR shuffled labels, ACC WR; Spearman rank correlation with AMI: ARI 0.83, ACC 0.94.

### HearMyShip

| method | AMI | ARI | ACC | rank AMI | rank ARI | rank ACC |
|---|---|---|---|---|---|---|
| Baseline | 0.289 | 0.181 | 0.471 | 4 | 4 | 5 |
| LEACE (session) | 0.269 | 0.163 | 0.457 | 6 | 6 | 7 |
| ComBat (session) | 0.276 | 0.170 | 0.461 | 5 | 5 | 6 |
| TURTLE x Z | 0.234 | 0.155 | 0.490 | 11 | 7 | 4 |
| PET-TURTLE x Z | 0.211 | 0.104 | 0.402 | 12 | 12 | 12 |
| TURTLE x W_frozen | 0.261 | 0.146 | 0.441 | 7 | 9 | 8 |
| PET-TURTLE x W_frozen | 0.250 | 0.133 | 0.429 | 9 | 10 | 11 |
| WR | 0.329 | 0.238 | 0.576 | 3 | 3 | 1 |
| SPLINCE | 0.037 | 0.016 | 0.289 | 13 | 13 | 13 |
| TURTLE x W_FT | 0.257 | 0.150 | 0.437 | 8 | 8 | 9 |
| PET-TURTLE x W_FT | 0.237 | 0.124 | 0.432 | 10 | 11 | 10 |
| FT+WR shuffled labels | 0.340 | 0.239 | 0.575 | 1 | 2 | 2 |
| FT+WR | 0.338 | 0.240 | 0.574 | 2 | 1 | 3 |

FT+WR minus Baseline: AMI +0.049 [+0.020, +0.067], ARI +0.059 [+0.036, +0.081], ACC +0.103 [+0.075, +0.122]. Best row: AMI FT+WR shuffled labels, ARI FT+WR, ACC WR; Spearman rank correlation with AMI: ARI 0.93, ACC 0.82.

### VLIZ

| method | AMI | ARI | ACC | rank AMI | rank ARI | rank ACC |
|---|---|---|---|---|---|---|
| Baseline | 0.061 | 0.015 | 0.135 | 7 | 7 | 8 |
| LEACE (session) | 0.055 | 0.012 | 0.132 | 10 | 10 | 9 |
| ComBat (session) | 0.055 | 0.012 | 0.131 | 9 | 12 | 10 |
| TURTLE x Z | 0.054 | 0.021 | 0.212 | 11 | 4 | 2 |
| PET-TURTLE x Z | 0.050 | 0.012 | 0.156 | 12 | 11 | 7 |
| TURTLE x W_frozen | 0.061 | 0.012 | 0.128 | 6 | 9 | 11 |
| PET-TURTLE x W_frozen | 0.062 | 0.016 | 0.161 | 3 | 5 | 6 |
| WR | 0.074 | 0.023 | 0.174 | 2 | 3 | 4 |
| SPLINCE | 0.009 | 0.003 | 0.123 | 13 | 13 | 13 |
| TURTLE x W_FT | 0.062 | 0.013 | 0.128 | 4 | 8 | 12 |
| PET-TURTLE x W_FT | 0.062 | 0.016 | 0.163 | 5 | 6 | 5 |
| FT+WR shuffled labels | 0.058 | 0.028 | 0.275 | 8 | 1 | 1 |
| FT+WR | 0.074 | 0.025 | 0.179 | 1 | 2 | 3 |

FT+WR minus Baseline: AMI +0.013 [+0.005, +0.023], ARI +0.010 [+0.004, +0.014], ACC +0.044 [+0.033, +0.053]. Best row: AMI FT+WR, ARI FT+WR shuffled labels, ACC FT+WR shuffled labels; Spearman rank correlation with AMI: ARI 0.62, ACC 0.27.

### ShipsEar

| method | AMI | ARI | ACC | rank AMI | rank ARI | rank ACC |
|---|---|---|---|---|---|---|
| Baseline | 0.319 | 0.190 | 0.492 | 1 | 1 | 1 |
| LEACE (session) | 0.089 | 0.062 | 0.378 | 13 | 13 | 13 |
| ComBat (session) | 0.148 | 0.100 | 0.425 | 11 | 10 | 8 |
| TURTLE x Z | 0.280 | 0.174 | 0.476 | 2 | 2 | 2 |
| PET-TURTLE x Z | 0.190 | 0.117 | 0.434 | 9 | 5 | 6 |
| TURTLE x W_frozen | 0.216 | 0.128 | 0.435 | 5 | 3 | 5 |
| PET-TURTLE x W_frozen | 0.191 | 0.110 | 0.404 | 8 | 7 | 11 |
| WR | 0.204 | 0.098 | 0.418 | 7 | 11 | 9 |
| SPLINCE | 0.108 | 0.064 | 0.379 | 12 | 12 | 12 |
| TURTLE x W_FT | 0.205 | 0.120 | 0.429 | 6 | 4 | 7 |
| PET-TURTLE x W_FT | 0.180 | 0.104 | 0.410 | 10 | 9 | 10 |
| FT+WR shuffled labels | 0.260 | 0.108 | 0.442 | 3 | 8 | 3 |
| FT+WR | 0.238 | 0.115 | 0.436 | 4 | 6 | 4 |

FT+WR minus Baseline: AMI -0.081 [-0.183, -0.018], ARI -0.075 [-0.175, -0.011], ACC -0.056 [-0.156, +0.036]. Best row: AMI Baseline, ARI Baseline, ACC Baseline; Spearman rank correlation with AMI: ARI 0.80, ACC 0.91.

On DeepShip, HearMyShip and VLIZ the gain of FT+WR over the Baseline holds under all three measures (all intervals above zero); the order of the other rows changes between the measures.
