import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    x = np.asarray(X,dtype=float)
    centred = x - np.mean(x,axis=0)
    return centred.T @ centred / (x.shape[0]-1)
    pass