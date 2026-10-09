from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))
    mode_val = float(Counter(x).most_common(1)[0][0])
    return {"mean":mean_val,"median":median_val,"mode":mode_val}
    
    pass