import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the KL divergence D_KL(P || Q) as a float.
    """
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    p_safe = np.clip(p, eps, None)
    q_safe = np.clip(q, eps, None)

    return float(np.sum(p * np.log(p_safe / q_safe)))