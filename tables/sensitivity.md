# Sensitivity and robustness analyses (post hoc)

All numbers are AMI under the final scoring (classes with fewer than 5 units not scored), mean over 20 k-means seeds. Each cell: AMI, then difference to the default setting (gamma 0.1, 2K dimensions, K known, all windows, pooled covariance) with the dependency-group bootstrap 95% interval (B=200). Post hoc: nothing here was used to select hyper-parameters or to change the main table.

## Plain summaries

- Misspecified K: AMI over all settings including the default, min to max per corpus. frozen BEATs: DS 0.256 (K'=2K (=8)) to 0.281 (default), default 0.281; HMS 0.329 (default) to 0.369 (K'=K-1 (=4)), default 0.329; VL 0.073 (K'=K-1 (=15)) to 0.080 (K'=2K (=32)), default 0.074; SE 0.204 (default) to 0.255 (K'=K-1 (=4)), default 0.204 | fine-tuned BEATs: DS 0.262 (K'=K-1 (=3)) to 0.286 (default), default 0.286; HMS 0.338 (K'=K+1 (=6)) to 0.366 (K'=K-1 (=4)), default 0.338; VL 0.073 (K'=K-1 (=15)) to 0.079 (K'=2K (=32)), default 0.074; SE 0.213 (K'=2K (=10)) to 0.258 (K'=K-1 (=4)), default 0.238
- Kept dimensions: AMI over all settings including the default, min to max per corpus. frozen BEATs: DS 0.270 (r=1K (=4)) to 0.284 (r=3K (=12)), default 0.281; HMS 0.329 (default) to 0.335 (r=1K (=5)), default 0.329; VL 0.073 (r=1K (=16)) to 0.074 (r=4K (=64)), default 0.074; SE 0.204 (default) to 0.249 (r=1K (=5)), default 0.204 | fine-tuned BEATs: DS 0.268 (r=1K (=4)) to 0.294 (r=4K (=16)), default 0.286; HMS 0.338 (r=4K (=20)) to 0.347 (r=1K (=5)), default 0.338; VL 0.073 (r=3K (=48)) to 0.074 (r=1K (=16)), default 0.074; SE 0.226 (r=3K (=15)) to 0.258 (r=1K (=5)), default 0.238
- Shrinkage coefficient: AMI over all settings including the default, min to max per corpus. frozen BEATs: DS 0.159 (gamma=1) to 0.281 (gamma=0.1), default 0.281; HMS 0.296 (gamma=1) to 0.343 (gamma=0.01), default 0.329; VL 0.059 (gamma=1) to 0.075 (gamma=0.01), default 0.074; SE 0.201 (gamma=0.3) to 0.296 (gamma=1), default 0.204 | fine-tuned BEATs: DS 0.168 (gamma=1) to 0.286 (gamma=0.1), default 0.286; HMS 0.302 (gamma=1) to 0.353 (gamma=0.01), default 0.338; VL 0.059 (gamma=1) to 0.074 (gamma=0.01), default 0.074; SE 0.212 (gamma=0.3) to 0.260 (gamma=1), default 0.238
- Covariance estimator: AMI over all settings including the default, min to max per corpus. frozen BEATs: DS 0.173 ((e) diagonal only) to 0.281 (default), default 0.281; HMS 0.289 ((e) diagonal only) to 0.331 ((d) OAS), default 0.329; VL 0.060 ((e) diagonal only) to 0.074 ((b) equal weight per recording), default 0.074; SE 0.203 ((d) OAS) to 0.301 ((e) diagonal only), default 0.204 | fine-tuned BEATs: DS 0.265 ((b) equal weight per recording) to 0.286 (default), default 0.286; HMS 0.338 ((a) pooled (default)) to 0.339 ((b) equal weight per recording), default 0.338; VL 0.073 ((b) equal weight per recording) to 0.074 (default), default 0.074; SE 0.220 ((b) equal weight per recording) to 0.238 (default), default 0.238
- Windows per recording: AMI over all settings including the default, min to max per corpus. frozen BEATs: DS 0.175 (m=2, sampling seed 1) to 0.281 (default), default 0.281; HMS 0.319 (m=2, sampling seed 2) to 0.345 (m=2, sampling seed 1), default 0.329; VL 0.066 (m=2, sampling seed 1) to 0.075 (m=16, sampling seed 0), default 0.074; SE 0.204 (default) to 0.335 (m=2, sampling seed 1), default 0.204 | fine-tuned BEATs: DS 0.147 (m=2, sampling seed 1) to 0.286 (default), default 0.286; HMS 0.324 (m=2, sampling seed 2) to 0.345 (m=4, sampling seed 0), default 0.338; VL 0.066 (m=2, sampling seed 1) to 0.074 (m=16, sampling seed 2), default 0.074; SE 0.209 (m=8, sampling seed 1) to 0.330 (m=2, sampling seed 1), default 0.238
- Fine-tuning seeds: see the fine-tuning seed table below.

## Misspecified K (K' in {K-1, K+1, 2K}, kept dimensions 2K')

| embedding | setting | DS | HMS | VL | SE |
|---|---|---|---|---|---|
| frozen BEATs | default | 0.281 (default) | 0.329 (default) | 0.074 (default) | 0.204 (default) |
| frozen BEATs | K'=K-1 (=3) | 0.280 -0.001 [-0.026, +0.023] | n/a | n/a | n/a |
| frozen BEATs | K'=K+1 (=5) | 0.277 -0.004 [-0.030, +0.027] | n/a | n/a | n/a |
| frozen BEATs | K'=2K (=8) | 0.256 -0.024 [-0.051, +0.015] | n/a | n/a | n/a |
| frozen BEATs | K'=K-1 (=4) | n/a | 0.369 +0.039 [+0.021, +0.057] | n/a | 0.255 +0.051 [-0.006, +0.077] |
| frozen BEATs | K'=K+1 (=6) | n/a | 0.332 +0.003 [-0.018, +0.030] | n/a | 0.212 +0.008 [-0.019, +0.035] |
| frozen BEATs | K'=2K (=10) | n/a | 0.335 +0.005 [-0.017, +0.040] | n/a | 0.224 +0.020 [-0.043, +0.111] |
| frozen BEATs | K'=K-1 (=15) | n/a | n/a | 0.073 -0.001 [-0.003, +0.001] | n/a |
| frozen BEATs | K'=K+1 (=17) | n/a | n/a | 0.075 +0.002 [-0.000, +0.004] | n/a |
| frozen BEATs | K'=2K (=32) | n/a | n/a | 0.080 +0.007 [+0.003, +0.015] | n/a |
| fine-tuned BEATs | default | 0.286 (default) | 0.338 (default) | 0.074 (default) | 0.238 (default) |
| fine-tuned BEATs | K'=K-1 (=3) | 0.262 -0.024 [-0.060, +0.002] | n/a | n/a | n/a |
| fine-tuned BEATs | K'=K+1 (=5) | 0.264 -0.022 [-0.050, +0.006] | n/a | n/a | n/a |
| fine-tuned BEATs | K'=2K (=8) | 0.279 -0.007 [-0.028, +0.022] | n/a | n/a | n/a |
| fine-tuned BEATs | K'=K-1 (=4) | n/a | 0.366 +0.028 [+0.009, +0.045] | n/a | 0.258 +0.020 [-0.040, +0.039] |
| fine-tuned BEATs | K'=K+1 (=6) | n/a | 0.338 -0.000 [-0.021, +0.026] | n/a | 0.224 -0.014 [-0.063, +0.028] |
| fine-tuned BEATs | K'=2K (=10) | n/a | 0.339 +0.001 [-0.024, +0.034] | n/a | 0.213 -0.025 [-0.069, +0.082] |
| fine-tuned BEATs | K'=K-1 (=15) | n/a | n/a | 0.073 -0.000 [-0.003, +0.001] | n/a |
| fine-tuned BEATs | K'=K+1 (=17) | n/a | n/a | 0.075 +0.001 [-0.001, +0.005] | n/a |
| fine-tuned BEATs | K'=2K (=32) | n/a | n/a | 0.079 +0.005 [+0.002, +0.012] | n/a |

## Kept dimensions, r in {K, 2K, 3K, 4K}

| embedding | setting | DS | HMS | VL | SE |
|---|---|---|---|---|---|
| frozen BEATs | default | 0.281 (default) | 0.329 (default) | 0.074 (default) | 0.204 (default) |
| frozen BEATs | r=1K (=4) | 0.270 -0.011 [-0.034, +0.013] | n/a | n/a | n/a |
| frozen BEATs | r=2K (=8) | 0.281 (default) | n/a | n/a | n/a |
| frozen BEATs | r=3K (=12) | 0.284 +0.003 [-0.024, +0.028] | n/a | n/a | n/a |
| frozen BEATs | r=4K (=16) | 0.279 -0.002 [-0.029, +0.019] | n/a | n/a | n/a |
| frozen BEATs | r=1K (=5) | n/a | 0.335 +0.005 [-0.004, +0.014] | n/a | 0.249 +0.045 [-0.004, +0.070] |
| frozen BEATs | r=2K (=10) | n/a | 0.329 (default) | n/a | 0.204 (default) |
| frozen BEATs | r=3K (=15) | n/a | 0.331 +0.002 [-0.004, +0.009] | n/a | 0.220 +0.016 [-0.019, +0.054] |
| frozen BEATs | r=4K (=20) | n/a | 0.333 +0.004 [-0.001, +0.010] | n/a | 0.226 +0.022 [-0.015, +0.056] |
| frozen BEATs | r=1K (=16) | n/a | n/a | 0.073 -0.000 [-0.003, +0.002] | n/a |
| frozen BEATs | r=2K (=32) | n/a | n/a | 0.074 (default) | n/a |
| frozen BEATs | r=3K (=48) | n/a | n/a | 0.074 +0.000 [-0.002, +0.002] | n/a |
| frozen BEATs | r=4K (=64) | n/a | n/a | 0.074 +0.001 [-0.003, +0.003] | n/a |
| fine-tuned BEATs | default | 0.286 (default) | 0.338 (default) | 0.074 (default) | 0.238 (default) |
| fine-tuned BEATs | r=1K (=4) | 0.268 -0.018 [-0.041, +0.006] | n/a | n/a | n/a |
| fine-tuned BEATs | r=2K (=8) | 0.286 (default) | n/a | n/a | n/a |
| fine-tuned BEATs | r=3K (=12) | 0.292 +0.006 [-0.011, +0.022] | n/a | n/a | n/a |
| fine-tuned BEATs | r=4K (=16) | 0.294 +0.008 [-0.011, +0.026] | n/a | n/a | n/a |
| fine-tuned BEATs | r=1K (=5) | n/a | 0.347 +0.009 [-0.005, +0.021] | n/a | 0.258 +0.020 [-0.024, +0.045] |
| fine-tuned BEATs | r=2K (=10) | n/a | 0.338 (default) | n/a | 0.238 (default) |
| fine-tuned BEATs | r=3K (=15) | n/a | 0.338 -0.000 [-0.008, +0.008] | n/a | 0.226 -0.012 [-0.053, +0.030] |
| fine-tuned BEATs | r=4K (=20) | n/a | 0.338 -0.000 [-0.007, +0.008] | n/a | 0.239 +0.001 [-0.051, +0.046] |
| fine-tuned BEATs | r=1K (=16) | n/a | n/a | 0.074 +0.000 [-0.003, +0.002] | n/a |
| fine-tuned BEATs | r=2K (=32) | n/a | n/a | 0.074 (default) | n/a |
| fine-tuned BEATs | r=3K (=48) | n/a | n/a | 0.073 -0.000 [-0.002, +0.002] | n/a |
| fine-tuned BEATs | r=4K (=64) | n/a | n/a | 0.073 -0.000 [-0.003, +0.004] | n/a |

## Shrinkage coefficient gamma

| embedding | setting | DS | HMS | VL | SE |
|---|---|---|---|---|---|
| frozen BEATs | default | 0.281 (default) | 0.329 (default) | 0.074 (default) | 0.204 (default) |
| frozen BEATs | gamma=0.01 | 0.264 -0.017 [-0.043, +0.004] | 0.343 +0.014 [+0.003, +0.024] | 0.075 +0.002 [-0.001, +0.005] | 0.229 +0.025 [-0.012, +0.065] |
| frozen BEATs | gamma=0.03 | 0.274 -0.007 [-0.024, +0.010] | 0.341 +0.011 [+0.006, +0.020] | 0.075 +0.001 [-0.002, +0.004] | 0.239 +0.035 [-0.001, +0.061] |
| frozen BEATs | gamma=0.1 | 0.281 (default) | 0.329 (default) | 0.074 (default) | 0.204 (default) |
| frozen BEATs | gamma=0.3 | 0.248 -0.033 [-0.058, -0.005] | 0.324 -0.005 [-0.013, +0.006] | 0.073 -0.001 [-0.003, +0.002] | 0.201 -0.003 [-0.033, +0.032] |
| frozen BEATs | gamma=1 | 0.159 -0.122 [-0.161, -0.075] | 0.296 -0.033 [-0.057, -0.004] | 0.059 -0.015 [-0.024, -0.008] | 0.296 +0.092 [-0.013, +0.206] |
| fine-tuned BEATs | default | 0.286 (default) | 0.338 (default) | 0.074 (default) | 0.238 (default) |
| fine-tuned BEATs | gamma=0.01 | 0.285 -0.001 [-0.027, +0.027] | 0.353 +0.015 [+0.004, +0.026] | 0.074 +0.001 [-0.001, +0.003] | 0.244 +0.006 [-0.035, +0.023] |
| fine-tuned BEATs | gamma=0.03 | 0.278 -0.009 [-0.032, +0.019] | 0.344 +0.006 [-0.002, +0.015] | 0.074 +0.000 [-0.002, +0.002] | 0.241 +0.003 [-0.027, +0.025] |
| fine-tuned BEATs | gamma=0.1 | 0.286 (default) | 0.338 (default) | 0.074 (default) | 0.238 (default) |
| fine-tuned BEATs | gamma=0.3 | 0.277 -0.010 [-0.035, +0.013] | 0.326 -0.012 [-0.020, -0.004] | 0.072 -0.001 [-0.004, +0.002] | 0.212 -0.026 [-0.050, +0.007] |
| fine-tuned BEATs | gamma=1 | 0.168 -0.118 [-0.165, -0.079] | 0.302 -0.036 [-0.059, -0.007] | 0.059 -0.014 [-0.023, -0.008] | 0.260 +0.022 [-0.054, +0.116] |

## Covariance estimator for Sigma_e (gamma = 0.1 shrinkage applied afterwards)

| embedding | setting | DS | HMS | VL | SE |
|---|---|---|---|---|---|
| frozen BEATs | default | 0.281 (default) | 0.329 (default) | 0.074 (default) | 0.204 (default) |
| frozen BEATs | (a) pooled (default) | 0.281 (default) | 0.329 (default) | 0.074 (default) | 0.204 (default) |
| frozen BEATs | (b) equal weight per recording | 0.276 -0.005 [-0.025, +0.019] | 0.330 +0.000 [-0.002, +0.004] | 0.074 +0.000 [-0.002, +0.003] | 0.207 +0.003 [-0.021, +0.030] |
| frozen BEATs | (c) Ledoit-Wolf | 0.281 -0.000 [-0.008, +0.004] | 0.330 +0.000 [-0.001, +0.003] | 0.074 -0.000 [-0.002, +0.002] | 0.204 +0.000 [-0.011, +0.009] |
| frozen BEATs | (d) OAS | 0.280 -0.000 [-0.008, +0.004] | 0.331 +0.001 [-0.001, +0.005] | 0.074 +0.000 [-0.002, +0.002] | 0.203 -0.001 [-0.011, +0.007] |
| frozen BEATs | (e) diagonal only | 0.173 -0.108 [-0.147, -0.068] | 0.289 -0.040 [-0.063, -0.013] | 0.060 -0.014 [-0.023, -0.007] | 0.301 +0.096 [+0.012, +0.201] |
| fine-tuned BEATs | default | 0.286 (default) | 0.338 (default) | 0.074 (default) | 0.238 (default) |
| fine-tuned BEATs | (a) pooled (default) | 0.286 (default) | 0.338 (default) | 0.074 (default) | 0.238 (default) |
| fine-tuned BEATs | (b) equal weight per recording | 0.265 -0.021 [-0.057, +0.007] | 0.339 +0.001 [-0.000, +0.004] | 0.073 -0.001 [-0.003, +0.002] | 0.220 -0.017 [-0.053, +0.045] |

## Windows per recording (m random windows kept; 3 sampling seeds)

| embedding | setting | DS | HMS | VL | SE |
|---|---|---|---|---|---|
| frozen BEATs | default | 0.281 (default) | 0.329 (default) | 0.074 (default) | 0.204 (default) |
| frozen BEATs | m=2, sampling seed 0 | 0.215 -0.066 [-0.094, -0.035] | 0.330 +0.001 [-0.010, +0.013] | 0.067 -0.007 [-0.013, -0.002] | 0.257 +0.053 [-0.011, +0.130] |
| frozen BEATs | m=2, sampling seed 1 | 0.175 -0.105 [-0.138, -0.069] | 0.345 +0.015 [+0.002, +0.029] | 0.066 -0.008 [-0.013, -0.003] | 0.335 +0.131 [+0.050, +0.232] |
| frozen BEATs | m=2, sampling seed 2 | 0.199 -0.082 [-0.112, -0.046] | 0.319 -0.010 [-0.026, +0.005] | 0.067 -0.007 [-0.011, -0.003] | 0.235 +0.031 [-0.026, +0.121] |
| frozen BEATs | m=4, sampling seed 0 | 0.258 -0.023 [-0.050, +0.008] | 0.337 +0.007 [-0.007, +0.019] | 0.071 -0.002 [-0.007, +0.001] | 0.227 +0.023 [-0.031, +0.061] |
| frozen BEATs | m=4, sampling seed 1 | 0.220 -0.061 [-0.088, -0.026] | 0.334 +0.005 [-0.008, +0.016] | 0.071 -0.002 [-0.005, +0.001] | 0.232 +0.028 [-0.034, +0.081] |
| frozen BEATs | m=4, sampling seed 2 | 0.226 -0.055 [-0.087, -0.019] | 0.333 +0.003 [-0.006, +0.014] | 0.069 -0.005 [-0.009, -0.001] | 0.232 +0.028 [-0.026, +0.095] |
| frozen BEATs | m=8, sampling seed 0 | 0.241 -0.040 [-0.063, -0.015] | 0.334 +0.005 [-0.004, +0.014] | 0.074 -0.000 [-0.003, +0.003] | 0.231 +0.027 [-0.017, +0.070] |
| frozen BEATs | m=8, sampling seed 1 | 0.260 -0.021 [-0.044, +0.001] | 0.334 +0.005 [-0.001, +0.010] | 0.072 -0.001 [-0.004, +0.001] | 0.210 +0.006 [-0.027, +0.046] |
| frozen BEATs | m=8, sampling seed 2 | 0.248 -0.033 [-0.058, -0.002] | 0.332 +0.003 [-0.006, +0.011] | 0.073 -0.001 [-0.004, +0.002] | 0.216 +0.012 [-0.032, +0.069] |
| frozen BEATs | m=16, sampling seed 0 | 0.278 -0.003 [-0.023, +0.024] | 0.329 +0.000 [+0.000, +0.000] | 0.075 +0.001 [-0.002, +0.004] | 0.228 +0.024 [-0.010, +0.053] |
| frozen BEATs | m=16, sampling seed 1 | 0.273 -0.008 [-0.034, +0.017] | 0.329 +0.000 [+0.000, +0.000] | 0.074 +0.000 [-0.002, +0.003] | 0.215 +0.011 [-0.027, +0.055] |
| frozen BEATs | m=16, sampling seed 2 | 0.265 -0.016 [-0.042, +0.007] | 0.329 +0.000 [+0.000, +0.000] | 0.074 +0.000 [-0.002, +0.003] | 0.218 +0.014 [-0.029, +0.068] |
| frozen BEATs | m=2, mean of 3 sampling seeds | 0.197 (0.175-0.215) -0.084 [-0.111, -0.054] | 0.331 (0.319-0.345) +0.002 [-0.008, +0.012] | 0.067 (0.066-0.067) -0.007 [-0.011, -0.004] | 0.276 (0.235-0.335) +0.072 [+0.017, +0.136] |
| frozen BEATs | m=4, mean of 3 sampling seeds | 0.235 (0.220-0.258) -0.046 [-0.069, -0.020] | 0.334 (0.333-0.337) +0.005 [-0.001, +0.013] | 0.071 (0.069-0.071) -0.003 [-0.006, -0.000] | 0.230 (0.227-0.232) +0.026 [-0.022, +0.070] |
| frozen BEATs | m=8, mean of 3 sampling seeds | 0.250 (0.241-0.260) -0.031 [-0.052, -0.010] | 0.334 (0.332-0.334) +0.004 [-0.000, +0.009] | 0.073 (0.072-0.074) -0.001 [-0.003, +0.001] | 0.219 (0.210-0.231) +0.015 [-0.022, +0.047] |
| frozen BEATs | m=16, mean of 3 sampling seeds | 0.272 (0.265-0.278) -0.009 [-0.030, +0.010] | 0.329 (0.329-0.329) +0.000 [-0.000, +0.000] | 0.074 (0.074-0.075) +0.001 [-0.001, +0.003] | 0.221 (0.215-0.228) +0.017 [-0.015, +0.045] |
| fine-tuned BEATs | default | 0.286 (default) | 0.338 (default) | 0.074 (default) | 0.238 (default) |
| fine-tuned BEATs | m=2, sampling seed 0 | 0.203 -0.083 [-0.116, -0.052] | 0.337 -0.001 [-0.016, +0.012] | 0.069 -0.005 [-0.011, -0.001] | 0.291 +0.053 [-0.019, +0.152] |
| fine-tuned BEATs | m=2, sampling seed 1 | 0.147 -0.139 [-0.180, -0.097] | 0.326 -0.012 [-0.027, +0.006] | 0.066 -0.008 [-0.013, -0.003] | 0.330 +0.092 [+0.012, +0.177] |
| fine-tuned BEATs | m=2, sampling seed 2 | 0.189 -0.097 [-0.137, -0.059] | 0.324 -0.014 [-0.029, -0.002] | 0.067 -0.007 [-0.011, -0.003] | 0.216 -0.022 [-0.070, +0.042] |
| fine-tuned BEATs | m=4, sampling seed 0 | 0.245 -0.041 [-0.076, -0.003] | 0.345 +0.007 [-0.007, +0.020] | 0.070 -0.003 [-0.007, +0.000] | 0.243 +0.005 [-0.060, +0.060] |
| fine-tuned BEATs | m=4, sampling seed 1 | 0.211 -0.075 [-0.105, -0.051] | 0.339 +0.000 [-0.010, +0.011] | 0.071 -0.003 [-0.007, +0.001] | 0.234 -0.004 [-0.063, +0.077] |
| fine-tuned BEATs | m=4, sampling seed 2 | 0.221 -0.066 [-0.094, -0.034] | 0.337 -0.001 [-0.012, +0.011] | 0.068 -0.006 [-0.011, -0.002] | 0.244 +0.006 [-0.056, +0.091] |
| fine-tuned BEATs | m=8, sampling seed 0 | 0.247 -0.039 [-0.065, -0.008] | 0.336 -0.002 [-0.009, +0.005] | 0.072 -0.001 [-0.004, +0.001] | 0.223 -0.015 [-0.052, +0.023] |
| fine-tuned BEATs | m=8, sampling seed 1 | 0.257 -0.029 [-0.064, +0.002] | 0.338 -0.000 [-0.006, +0.006] | 0.073 -0.001 [-0.004, +0.002] | 0.209 -0.029 [-0.076, +0.017] |
| fine-tuned BEATs | m=8, sampling seed 2 | 0.256 -0.030 [-0.065, +0.005] | 0.335 -0.003 [-0.011, +0.004] | 0.072 -0.002 [-0.005, +0.001] | 0.243 +0.005 [-0.067, +0.080] |
| fine-tuned BEATs | m=16, sampling seed 0 | 0.272 -0.014 [-0.044, +0.021] | 0.338 +0.000 [+0.000, +0.000] | 0.073 -0.001 [-0.003, +0.001] | 0.234 -0.004 [-0.046, +0.042] |
| fine-tuned BEATs | m=16, sampling seed 1 | 0.265 -0.022 [-0.057, +0.007] | 0.338 +0.000 [+0.000, +0.000] | 0.073 -0.000 [-0.003, +0.002] | 0.244 +0.006 [-0.040, +0.068] |
| fine-tuned BEATs | m=16, sampling seed 2 | 0.248 -0.038 [-0.067, -0.010] | 0.338 +0.000 [+0.000, +0.000] | 0.074 +0.000 [-0.002, +0.002] | 0.240 +0.002 [-0.055, +0.075] |
| fine-tuned BEATs | m=2, mean of 3 sampling seeds | 0.180 (0.147-0.203) -0.106 [-0.135, -0.077] | 0.329 (0.324-0.337) -0.009 [-0.021, +0.002] | 0.067 (0.066-0.069) -0.007 [-0.011, -0.003] | 0.279 (0.216-0.330) +0.041 [-0.016, +0.107] |
| fine-tuned BEATs | m=4, mean of 3 sampling seeds | 0.226 (0.211-0.245) -0.060 [-0.086, -0.037] | 0.340 (0.337-0.345) +0.002 [-0.006, +0.010] | 0.070 (0.068-0.071) -0.004 [-0.008, -0.001] | 0.240 (0.234-0.244) +0.002 [-0.056, +0.054] |
| fine-tuned BEATs | m=8, mean of 3 sampling seeds | 0.254 (0.247-0.257) -0.033 [-0.064, -0.003] | 0.336 (0.335-0.338) -0.002 [-0.007, +0.003] | 0.072 (0.072-0.073) -0.001 [-0.004, +0.001] | 0.225 (0.209-0.243) -0.013 [-0.059, +0.031] |
| fine-tuned BEATs | m=16, mean of 3 sampling seeds | 0.262 (0.248-0.272) -0.025 [-0.055, +0.003] | 0.338 (0.338-0.338) -0.000 [-0.000, +0.000] | 0.073 (0.073-0.074) -0.000 [-0.002, +0.001] | 0.240 (0.234-0.244) +0.002 [-0.039, +0.047] |

## Fine-tuning seed variability (FT+C7-, default settings)

| target | AMI seed 0 (original) | AMI seed 1 | AMI seed 2 | mean | sd | min | max | frozen C7- | mean - frozen [CI] | training s (seeds 0/1/2) |
|---|---|---|---|---|---|---|---|---|---|---|
| DS | 0.286 | 0.278 | 0.286 | 0.284 | 0.005 | 0.278 | 0.286 | 0.281 | +0.003 [-0.018, +0.028] | 492.2/1588.1/785.8 |
| HMS | 0.338 | 0.339 | 0.340 | 0.339 | 0.001 | 0.338 | 0.340 | 0.329 | +0.010 [+0.001, +0.019] | 492.6/1502.1/966.5 |
| VL | 0.074 | 0.072 | 0.073 | 0.073 | 0.001 | 0.072 | 0.074 | 0.074 | -0.001 [-0.003, +0.002] | 343.0/1173.7/729.7 |
| SE | 0.238 | 0.239 | 0.236 | 0.238 | 0.002 | 0.236 | 0.239 | 0.204 | +0.034 [+0.001, +0.066] | 440.5/1662.4/927.6 |

Per fine-tuning seed minus frozen C7- [CI]:

| target | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| DS | +0.005 [-0.016, +0.033] | -0.003 [-0.028, +0.025] | +0.006 [-0.016, +0.033] |
| HMS | +0.009 [-0.002, +0.019] | +0.010 [+0.001, +0.018] | +0.011 [+0.001, +0.021] |
| VL | +0.000 [-0.002, +0.002] | -0.001 [-0.004, +0.002] | -0.001 [-0.004, +0.002] |
| SE | +0.034 [+0.001, +0.063] | +0.035 [+0.001, +0.059] | +0.032 [-0.003, +0.079] |

Training time per fine-tuning run (1500 steps): mean 925 s, min 343 s, max 1662 s over 12 runs.

