import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    list = []
    q = 1.0 - p
    for i in range (len(x)):
        if x[i] == 0:
            list.append(q)
        else:
            list.append(p)
    mean = p * 1.0
    var = p*q
    pmf = np.array(list)
    return {"pmf":pmf,"mean":mean,"variance":var}
    pass