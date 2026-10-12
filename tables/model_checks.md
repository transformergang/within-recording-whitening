# Checks of the nested nuisance model

## Real data (255-bin log spectra; equalizer: projection onto the first 16 discrete-cosine-transform components)

The 14 predictions below were sealed before computing on real data (plan hash in `plans/PLAN_HASHES.md`). The ShipsEar part of the graph prediction was made after its class-by-date table had been seen (post hoc).

| quantity | DS | SE | HMS | VL |
|---|---|---|---|---|
| connected components of the class-session graph | 1 | 2 | 1 | 1 |
| sessions | 363 | 8 | 26 | 5 |
| relative change of Sigma_e under the equalizer | 3.6e-16 | 5.6e-16 | 2.3e-16 | 4.3e-16 |
| phi_h (smooth fraction of the session layer) | 0.96 | 0.98 | 0.88 | 1.00 |
| phi_c (smooth fraction of the class contrast; descriptive) | 0.98 | 0.99 | 0.99 | 1.00 |
| session AMI of C7-, before the equalizer | 0.01 | 0.36 | 0.00 | 0.39 |
| session AMI of C7-, after the equalizer | 0.00 | 0.34 | 0.00 | 0.08 |
| class AMI of C7-, before the equalizer (descriptive) | 0.18 | 0.06 | 0.20 | 0.05 |
| class AMI of C7-, after the equalizer (descriptive) | 0.03 | 0.04 | 0.06 | 0.02 |

| sealed prediction | held |
|---|---|
| class graph connected, DS | yes |
| class graph connected, HMS | yes |
| class graph connected, VL | yes |
| class graph not connected on SE, class E alone (post hoc for SE) | yes |
| Sigma_e unchanged by the equalizer (relative change < 1e-8), DS | yes |
| Sigma_e unchanged by the equalizer, SE | yes |
| Sigma_e unchanged by the equalizer, HMS | yes |
| Sigma_e unchanged by the equalizer, VL | yes |
| phi_h >= 0.7, DS | yes |
| phi_h >= 0.7, SE | yes |
| phi_h >= 0.7, HMS | yes |
| phi_h >= 0.7, VL | yes |
| session AMI of C7- falls after the equalizer, SE | yes |
| session AMI of C7- falls after the equalizer, VL | yes |

Eight of the 14 are identity or assumption checks (the four Sigma_e rows and the four phi_h rows).

## ShipsEar: recordings per class and recording date

| class | 2012-10-04 | 2013-07-10 | 2013-07-18 | 2013-07-19 | 2013-07-23 | 2013-09-25 | 2013-09-27 | 2014-03-06 |
|---|---|---|---|---|---|---|---|---|
| A | 1 | 1 | 0 | 2 | 9 | 0 | 0 | 4 |
| B | 0 | 0 | 1 | 8 | 10 | 0 | 0 | 0 |
| C | 0 | 10 | 0 | 9 | 11 | 0 | 0 | 0 |
| D | 0 | 1 | 3 | 4 | 4 | 0 | 0 | 0 |
| E | 0 | 0 | 0 | 0 | 0 | 9 | 3 | 0 |

Classes A-D share recording dates (six dates); class E (background noise) occupies two dates of its own. AMI between class and recording date: 0.32 on ShipsEar, 0.06 on DeepShip.

## Synthetic checks of the propositions (14 of 14 passed)

| check (identifier in the analysis script) | passed |
|---|---|
| `a_identity` | yes |
| `d1_W_invariant_shift` | yes |
| `a_EW_equals_Sigma_w` | yes |
| `b_EB_formula` | yes |
| `c_EH_design1_equal_proportions` | yes |
| `c_EH_design2_unequal_proportions` | yes |
| `c_Smq_zero_iff_equal_proportions` | yes |
| `d2_identity_B_projected` | yes |
| `d2_expectation_no_h_c_when_in_range_S` | yes |
| `d2_negative_control_h_leaks_when_not_smooth` | yes |
| `P2_distribution_equivalence` | yes |
| `P2prime_named_designs` | yes |
| `P2prime_ShipsEar_actual` | yes |
| `P2prime_exhaustive_up_to_3x4` | yes |
