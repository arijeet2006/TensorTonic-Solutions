import numpy as np
import pandas as pd


def one_hot(y: list, num_classes=None) -> np.ndarray:
    """Returns a NumPy array with shape (N, K)."""
    # Write code here
    y = np.asarray(y)
    encoded = pd.get_dummies(y, dtype=int)
    if num_classes is not None:
        encoded = encoded.reindex(columns=range(num_classes), fill_value=0)
    return encoded.values