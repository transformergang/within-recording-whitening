"""Reference implementation of within-recording whitening (C7-) and of the standardized baseline (C2).

This file is self-contained (NumPy only) and follows the formulas of the paper:

    Sigma_e  pooled covariance of the window vectors around their own recording mean, scaled to unit trace
    Sigma~ = (1 - gamma) * Sigma_e + gamma * tr(Sigma_e) * I / d          (gamma = 0.1)
    S_B      covariance of the recording means
    W      = Sigma~^(-1/2) U,  U = top 2K eigenvectors of Sigma~^(-1/2) S_B Sigma~^(-1/2)
    embedding of recording i = W^T m_i, clustered by k-means (k-means++, 20 restarts)

No label of any corpus is used by `c7_minus`. `c2_baseline` uses no label either; it needs the recording
means of the other corpora for the per-dimension z-score.

Input convention used for the results in the paper: a window vector is the mean over tokens of the encoder
output for a 2 s window, L2-normalized; a recording mean m_i is the plain mean of its window vectors.

Run `python c7minus.py` for a small synthetic demonstration.
"""
import numpy as np


def inv_sqrt(S):
    """Symmetric inverse square root with an eigenvalue floor of 1e-12 times the largest eigenvalue."""
    w, V = np.linalg.eigh(S)
    w = np.maximum(w, 1e-12 * w.max())
    return (V / np.sqrt(w)) @ V.T


def recording_means(X, rec, n_rec=None):
    """Mean window vector of every recording. X: (n_windows, d). rec: (n_windows,) integers in 0..n_rec-1."""
    n_rec = int(rec.max()) + 1 if n_rec is None else n_rec
    cnt = np.bincount(rec, minlength=n_rec)
    M = np.zeros((n_rec, X.shape[1]))
    np.add.at(M, rec, X.astype(np.float64))
    return M / cnt[:, None], cnt


def within_recording_covariance(X, rec, n_rec=None):
    """Pooled within-recording window covariance, scaled to unit trace, and the recording means.

    Recordings with a single window contribute to the means only. The divisor is the sum of (n_i - 1)
    over recordings with at least two windows.
    """
    M, cnt = recording_means(X, rec, n_rec)
    ok = cnt[rec] >= 2
    R = X[ok].astype(np.float64) - M[rec[ok]]
    S = R.T @ R / max(1, int((cnt[cnt >= 2] - 1).sum()))
    return S / np.trace(S), M


def shrink(S, gamma=0.1):
    d = S.shape[0]
    return (1.0 - gamma) * S + gamma * np.trace(S) / d * np.eye(d)


def c7_minus(X, rec, K, gamma=0.1, n_dirs=None, n_rec=None):
    """Within-recording whitening followed by the leading generalized eigendirections.

    X: (n_windows, d) window vectors of the target corpus; rec: recording index of every window;
    K: number of classes; n_dirs: number of retained directions (default 2K).
    Returns (E, W): E = M @ W are the recording embeddings to be clustered, W is the (d, n_dirs) map.
    """
    Se, M = within_recording_covariance(X, rec, n_rec)
    Ni = inv_sqrt(shrink(Se, gamma))
    Sb = np.cov(M.T)
    lam, U = np.linalg.eigh(Ni @ Sb @ Ni)
    order = np.argsort(-lam)[: (2 * K if n_dirs is None else n_dirs)]
    W = Ni @ U[:, order]
    return M @ W, W


def l2(X):
    return X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-12)


def c2_baseline(M_target, M_sources):
    """Baseline C2: recording means are L2-normalized, z-scored per dimension with the mean and standard
    deviation of the (L2-normalized) recording means of the other corpora, and L2-normalized again."""
    V_t, V_s = l2(M_target), l2(M_sources)
    mu, sd = V_s.mean(0), V_s.std(0) + 1e-8
    return l2((V_t - mu) / sd)


def kmeans(E, K, seed, n_init=20, max_iter=300, tol=1e-4):
    """k-means with k-means++ seeding and n_init restarts; returns the labels of the restart with the lowest inertia."""
    rng = np.random.default_rng(seed)
    best, best_in = None, np.inf
    E = E.astype(np.float64)
    sq = (E ** 2).sum(1)
    for _ in range(n_init):
        C = [E[rng.integers(len(E))]]
        d = sq - 2 * E @ C[0] + (C[0] ** 2).sum()
        for _k in range(1, K):
            p = np.maximum(d, 0)
            p = p / p.sum() if p.sum() > 0 else np.full(len(E), 1 / len(E))
            C.append(E[rng.choice(len(E), p=p)])
            d = np.minimum(d, sq - 2 * E @ C[-1] + (C[-1] ** 2).sum())
        C = np.stack(C)
        for _it in range(max_iter):
            D = sq[:, None] - 2 * E @ C.T + (C ** 2).sum(1)[None]
            lab = D.argmin(1)
            Cn = np.stack([E[lab == k].mean(0) if (lab == k).any() else C[k] for k in range(K)])
            shift = ((Cn - C) ** 2).sum()
            C = Cn
            if shift < tol:
                break
        inertia = D[np.arange(len(E)), lab].sum()
        if inertia < best_in:
            best_in, best = inertia, lab
    return best


def _demo():
    """Synthetic data from the nested model: class mean + recording offset + within-recording part.
    The within-recording part is large along directions that carry no class information."""
    rng = np.random.default_rng(0)
    d, K, n_rec, n_win = 32, 3, 300, 6
    y = rng.integers(K, size=n_rec)
    mu = np.zeros((K, d)); mu[:, :2] = np.array([[1.0, 0.0], [-0.5, 0.87], [-0.5, -0.87]])   # class means in dimensions 0-1
    scale_w = np.r_[0.5 * np.ones(2), 3.0 * np.ones(8), 0.5 * np.ones(d - 10)]  # window layer: large in dimensions 2-9
    c = 0.2 * rng.normal(size=(n_rec, d))                                   # recording-level offset
    rec = np.repeat(np.arange(n_rec), n_win)
    X = mu[y][rec] + c[rec] + rng.normal(size=(n_rec * n_win, d)) * scale_w

    def agreement(lab):                                                     # purity, for the demo only
        return sum(np.bincount(y[lab == k], minlength=K).max() for k in range(K)) / n_rec

    M, _ = recording_means(X, rec)
    E, _ = c7_minus(X, rec, K)
    print("purity, k-means on recording means : %.3f" % agreement(kmeans(M, K, 0)))
    print("purity, k-means after C7-          : %.3f" % agreement(kmeans(E, K, 0)))


if __name__ == "__main__":
    _demo()
