import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    prob = []
    for i in range(k+1):
        res = math.comb(n,i) * p ** i * (1.0-p)**(n-i)
        prob.append(res)
    return {"pmf":prob[k], "cdf":sum(prob)}
    pass