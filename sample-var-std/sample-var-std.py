import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    arr = np.array(x)
    mean_val = float(np.mean(x))
    n = len(arr)
    var = float(1/(n-1) * (np.sum((arr-mean_val)**2)))
    sd = float(np.sqrt(var))
    return {"variance":var,"standard_deviation":sd}
    pass