# Five frozen encoders: C7- against C2

AMI, mean of 20 k-means seeds, all units scored (the scoring used for the frozen-encoder comparison in the paper). Interval: 95% percentile interval of the dependency-group bootstrap (B=200) with both arms refit on every resample. rho is the ratio of the recording-level to the class-level variance component of the window embeddings.

| encoder | corpus | K | units | C2 | C7- | C7- minus C2 | 95% interval (refit) | rho |
|---|---|---|---|---|---|---|---|---|
| BEATs | DeepShip | 4 | 609 | 0.169 | 0.281 | +0.112 | [-0.026, +0.145] | 6.7 |
| BEATs | HearMyShip | 5 | 1149 | 0.289 | 0.330 | +0.041 | [-0.006, +0.096] | 2.9 |
| BEATs | VLIZ | 16 | 7717 | 0.061 | 0.074 | +0.013 | [+0.006, +0.028] | 18.3 |
| BEATs | ShipsEar | 5 | 90 | 0.319 | 0.204 | -0.115 | [-0.209, +0.059] | 3.2 |
| AudioMAE | DeepShip | 4 | 609 | 0.080 | 0.229 | +0.148 | [+0.071, +0.181] | 8.4 |
| AudioMAE | HearMyShip | 5 | 1149 | 0.200 | 0.330 | +0.130 | [+0.089, +0.182] | 2.7 |
| AudioMAE | VLIZ | 16 | 7717 | 0.031 | 0.066 | +0.035 | [+0.023, +0.048] | 20.3 |
| AudioMAE | ShipsEar | 5 | 90 | 0.181 | 0.271 | +0.090 | [-0.118, +0.160] | 3.2 |
| EAT | DeepShip | 4 | 609 | 0.116 | 0.213 | +0.097 | [+0.017, +0.182] | 6.6 |
| EAT | HearMyShip | 5 | 1149 | 0.262 | 0.340 | +0.078 | [+0.039, +0.150] | 2.0 |
| EAT | VLIZ | 16 | 7717 | 0.054 | 0.074 | +0.020 | [+0.008, +0.032] | 16.5 |
| EAT | ShipsEar | 5 | 90 | 0.245 | 0.221 | -0.023 | [-0.195, +0.150] | 3.9 |
| CLAP | DeepShip | 4 | 609 | 0.129 | 0.227 | +0.097 | [+0.006, +0.164] | 5.9 |
| CLAP | HearMyShip | 5 | 1149 | 0.273 | 0.356 | +0.083 | [+0.035, +0.170] | 2.2 |
| CLAP | VLIZ | 16 | 7717 | 0.052 | 0.074 | +0.023 | [+0.014, +0.038] | 14.6 |
| CLAP | ShipsEar | 5 | 90 | 0.254 | 0.208 | -0.045 | [-0.156, +0.100] | 2.9 |
| Dasheng | DeepShip | 4 | 609 | 0.168 | 0.258 | +0.089 | [-0.035, +0.140] | 5.9 |
| Dasheng | HearMyShip | 5 | 1149 | 0.305 | 0.338 | +0.034 | [-0.044, +0.060] | 3.2 |
| Dasheng | VLIZ | 16 | 7717 | 0.065 | 0.074 | +0.009 | [-0.002, +0.021] | 11.9 |
| Dasheng | ShipsEar | 5 | 90 | 0.323 | 0.206 | -0.117 | [-0.247, +0.029] | 2.8 |
