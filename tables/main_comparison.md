# Main comparison (BEATs, final scoring)

AMI: adjusted mutual information, mean of 20 k-means seeds. Final scoring: units of classes with fewer than five units are not scored (VLIZ 3 units, HearMyShip 6 units); clustering uses all units. Differences are given with 95% percentile intervals of the dependency-group bootstrap (B=200, fixed partitions, four paired seeds per resample). Group U: no source labels. Group S: source labels. Accuracy: Hungarian-matched.

## DeepShip (DS)

| row | group | AMI | accuracy | FT+C7- minus row [95% interval] | C7- minus row [95% interval] |
|---|---|---|---|---|---|
| C2 (standardized baseline) | U | 0.169 | 0.445 | +0.117 [+0.074, +0.158] | +0.112 [+0.068, +0.153] |
| LEACE (session) | U | 0.121 | 0.414 | +0.165 [+0.119, +0.211] | +0.160 [+0.105, +0.203] |
| ComBat (session) | U | 0.169 | 0.445 | +0.117 [+0.074, +0.158] | +0.112 [+0.068, +0.153] |
| TURTLE x Z | U | 0.184 | 0.500 | +0.102 [+0.062, +0.143] | +0.097 [+0.055, +0.140] |
| PET-TURTLE x Z | U | 0.122 | 0.439 | +0.164 [+0.120, +0.207] | +0.159 [+0.111, +0.203] |
| TURTLE x W_frozen | U | 0.162 | 0.441 | +0.124 [+0.082, +0.174] | +0.119 [+0.072, +0.169] |
| PET-TURTLE x W_frozen | U | 0.182 | 0.443 | +0.104 [+0.065, +0.137] | +0.099 [+0.061, +0.135] |
| C7- (within-recording whitening, frozen BEATs) | U | 0.281 | 0.578 | +0.005 [-0.016, +0.033] | - |
| SPLINCE | S | 0.146 | 0.410 | +0.140 [+0.106, +0.187] | +0.135 [+0.095, +0.176] |
| TURTLE x W_FT | S | 0.153 | 0.439 | +0.133 [+0.090, +0.174] | +0.128 [+0.089, +0.165] |
| PET-TURTLE x W_FT | S | 0.200 | 0.468 | +0.086 [+0.045, +0.159] | +0.081 [+0.028, +0.159] |
| FT+C7- (optional fine-tuning, then whitening) | S | 0.286 | 0.572 | - | - |
| FT+C7- with shuffled source labels (control) | - | 0.282 | n/a | +0.004 [-0.014, +0.025] | - |
| fine-tuning without whitening (ablation) | - | 0.168 | n/a | +0.118 [+0.085, +0.156] | - |

## HearMyShip (HMS)

| row | group | AMI | accuracy | FT+C7- minus row [95% interval] | C7- minus row [95% interval] |
|---|---|---|---|---|---|
| C2 (standardized baseline) | U | 0.289 | 0.471 | +0.049 [+0.022, +0.068] | +0.041 [+0.015, +0.059] |
| LEACE (session) | U | 0.269 | 0.457 | +0.069 [+0.038, +0.090] | +0.060 [+0.032, +0.085] |
| ComBat (session) | U | 0.276 | 0.461 | +0.062 [+0.035, +0.082] | +0.053 [+0.027, +0.077] |
| TURTLE x Z | U | 0.234 | 0.490 | +0.104 [+0.056, +0.140] | +0.095 [+0.045, +0.136] |
| PET-TURTLE x Z | U | 0.211 | 0.402 | +0.127 [+0.075, +0.164] | +0.119 [+0.065, +0.157] |
| TURTLE x W_frozen | U | 0.261 | 0.441 | +0.077 [+0.011, +0.115] | +0.068 [+0.001, +0.104] |
| PET-TURTLE x W_frozen | U | 0.250 | 0.429 | +0.088 [-0.007, +0.135] | +0.080 [-0.013, +0.126] |
| C7- (within-recording whitening, frozen BEATs) | U | 0.329 | 0.576 | +0.009 [-0.002, +0.019] | - |
| SPLINCE | S | 0.037 | 0.289 | +0.301 [+0.235, +0.345] | +0.293 [+0.227, +0.338] |
| TURTLE x W_FT | S | 0.257 | 0.437 | +0.081 [+0.033, +0.115] | +0.073 [+0.026, +0.106] |
| PET-TURTLE x W_FT | S | 0.237 | 0.432 | +0.101 [+0.042, +0.138] | +0.092 [+0.030, +0.130] |
| FT+C7- (optional fine-tuning, then whitening) | S | 0.338 | 0.574 | - | - |
| FT+C7- with shuffled source labels (control) | - | 0.340 | n/a | -0.002 [-0.009, +0.004] | - |
| fine-tuning without whitening (ablation) | - | 0.310 | n/a | +0.028 [-0.001, +0.050] | - |

## VLIZ (VL)

| row | group | AMI | accuracy | FT+C7- minus row [95% interval] | C7- minus row [95% interval] |
|---|---|---|---|---|---|
| C2 (standardized baseline) | U | 0.061 | 0.135 | +0.013 [+0.007, +0.023] | +0.013 [+0.006, +0.023] |
| LEACE (session) | U | 0.055 | 0.132 | +0.018 [+0.011, +0.028] | +0.018 [+0.010, +0.029] |
| ComBat (session) | U | 0.055 | 0.131 | +0.018 [+0.011, +0.028] | +0.018 [+0.011, +0.028] |
| TURTLE x Z | U | 0.054 | 0.212 | +0.020 [+0.013, +0.032] | +0.020 [+0.013, +0.031] |
| PET-TURTLE x Z | U | 0.050 | 0.156 | +0.023 [+0.016, +0.035] | +0.023 [+0.015, +0.035] |
| TURTLE x W_frozen | U | 0.061 | 0.128 | +0.012 [+0.007, +0.020] | +0.012 [+0.006, +0.020] |
| PET-TURTLE x W_frozen | U | 0.062 | 0.161 | +0.011 [+0.005, +0.020] | +0.011 [+0.004, +0.020] |
| C7- (within-recording whitening, frozen BEATs) | U | 0.074 | 0.174 | +0.000 [-0.002, +0.002] | - |
| SPLINCE | S | 0.009 | 0.123 | +0.064 [+0.047, +0.088] | +0.064 [+0.046, +0.087] |
| TURTLE x W_FT | S | 0.062 | 0.128 | +0.011 [+0.007, +0.019] | +0.011 [+0.006, +0.019] |
| PET-TURTLE x W_FT | S | 0.062 | 0.163 | +0.012 [+0.006, +0.018] | +0.012 [+0.006, +0.019] |
| FT+C7- (optional fine-tuning, then whitening) | S | 0.074 | 0.179 | - | - |
| FT+C7- with shuffled source labels (control) | - | 0.058 | n/a | +0.016 [+0.008, +0.027] | - |
| fine-tuning without whitening (ablation) | - | 0.060 | n/a | +0.014 [+0.008, +0.023] | - |

## ShipsEar (SE)

| row | group | AMI | accuracy | FT+C7- minus row [95% interval] | C7- minus row [95% interval] |
|---|---|---|---|---|---|
| C2 (standardized baseline) | U | 0.319 | 0.492 | -0.081 [-0.198, +0.015] | -0.115 [-0.221, -0.014] |
| LEACE (session) | U | 0.089 | 0.378 | +0.149 [-0.033, +0.242] | +0.115 [-0.060, +0.201] |
| ComBat (session) | U | 0.148 | 0.425 | +0.090 [-0.072, +0.184] | +0.056 [-0.096, +0.141] |
| TURTLE x Z | U | 0.280 | 0.476 | -0.042 [-0.157, +0.057] | -0.076 [-0.194, +0.034] |
| PET-TURTLE x Z | U | 0.190 | 0.434 | +0.048 [-0.091, +0.140] | +0.014 [-0.124, +0.115] |
| TURTLE x W_frozen | U | 0.216 | 0.435 | +0.022 [-0.108, +0.099] | -0.012 [-0.130, +0.067] |
| PET-TURTLE x W_frozen | U | 0.191 | 0.404 | +0.047 [-0.135, +0.153] | +0.013 [-0.158, +0.108] |
| C7- (within-recording whitening, frozen BEATs) | U | 0.204 | 0.418 | +0.034 [+0.001, +0.063] | - |
| SPLINCE | S | 0.108 | 0.379 | +0.130 [-0.048, +0.249] | +0.096 [-0.070, +0.212] |
| TURTLE x W_FT | S | 0.205 | 0.429 | +0.033 [-0.112, +0.109] | -0.001 [-0.126, +0.084] |
| PET-TURTLE x W_FT | S | 0.180 | 0.410 | +0.058 [-0.106, +0.160] | +0.024 [-0.126, +0.126] |
| FT+C7- (optional fine-tuning, then whitening) | S | 0.238 | 0.436 | - | - |
| FT+C7- with shuffled source labels (control) | - | 0.260 | n/a | -0.022 [-0.060, +0.034] | - |
| fine-tuning without whitening (ablation) | - | 0.288 | n/a | -0.050 [-0.154, +0.028] | - |

Notes.

- On DeepShip, 247 of 363 sessions contain a single unit; they form one batch for ComBat, which then corrected no dimension, so that row equals C2.
- The estimator condition of SPLINCE fails in this setting because session and class indicators are collinear across corpora.
- TURTLE and PET-TURTLE hyper-parameters were chosen per target by leave-one-source-out AMI inside the source corpora; W_FT reuses the choice for W_frozen.
