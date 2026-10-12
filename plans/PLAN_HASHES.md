# Digests of the sealed analysis plans

Each analysis plan was written and its SHA-256 digest recorded before the corresponding computation started.
The digests below are those recorded at sealing time. Times are in Japan Standard Time (UTC+9).

| plan | what it fixes | sealed | SHA-256 |
|---|---|---|---|
| Nested nuisance model, real-data predictions | The 14 predictions checked on real data: connectedness of the class-session graph, invariance of the within-recording covariance under the equalizer, smoothness of the session layer, fall of the session AMI after the equalizer. | 2026-10-09 10:54 | `273f20e79d7f7269cda1511ecc71a5d72f56304f0b53570c4adc692379eea086` |
| Optional fine-tuning | Layers tuned, loss, positives, optional gradient-reversal discriminator, selection of its weight by leave-one-source-out validation inside the source corpora, shuffled-label control, evaluation. | 2026-10-09 15:04 | `8454d3d78400c5b755ba835456f942d397f919fb94118be2d59c48ad175e78db` |
| External methods, common conditions | Encoder, inputs, K, seeds, metrics and bootstrap shared by all external methods; the LEACE and ComBat arms. | 2026-10-10 00:43 | `5aea87234d5822b8acb37ad05ba8f8248a2508a1ee720ed23b25b61c36b037a1` |
| External methods, amendment 1 | Definition of the input Z, hyper-parameter procedure for PET-TURTLE, handling of the violated SPLINCE premise. | 2026-10-10 | `c631dd3ab477dd358b6ec96885f9058d52c7483b86834ec217e0688a93523693` |
| Matched comparison | Crossing of the three inputs with the clustering heads, tuning budget by leave-one-source-out validation, grouping by source-label use. | 2026-10-10 12:21 | `795663e3cadcc87e50c7a80d4c28a5c87bb6186bbe76ad8d79c8dec1b554a6c6` |
| Matched comparison, amendment 1 | Rescaling of the whitened inputs for TURTLE and PET-TURTLE, PET-TURTLE grid and training loop, SPLINCE fallback. | 2026-10-10 | `74c37518fa4dd6c767271ab1f0c0f4de8131a8097101bb2723cbb02a71d7c16a` |
| Matched comparison, amendment 2 | Final scoring: units of classes with fewer than five units are not scored. | 2026-10-10 13:46 | `57dfb5906e75a49c6f286333930c931bbd15e1566fbc0f2972cc200d7bea4737` |
| Sensitivity analyses (post hoc) | Settings of the post hoc sensitivity analyses, run after the main results. | 2026-10-11 20:13 | `3666db756306805caeeaff3901c47a15b83e1799ffc4ab202cbd04e5f04f4e9d` |
| Sensitivity analyses, amendment 1 | Implementation details fixed before launch (covariance estimators, scoring, what the fine-tuning seed controls). | 2026-10-11 | `7392808c6b416bf5bc27db64e83a358166f7eabceab18f5f8d12ee85c37f0f73` |

The sensitivity analyses are post hoc: their plan was sealed before they were run, but after the main results were known.
The ShipsEar part of the graph prediction in the first plan was made after the class-by-date table of ShipsEar had been seen.
