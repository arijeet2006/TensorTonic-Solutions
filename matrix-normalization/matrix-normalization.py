import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix, normalized according to norm_type.
    """
    matrix = np.asarray(matrix, dtype=float)

    if norm_type == "l1":
        denominator = np.sum(np.abs(matrix), axis=axis, keepdims=True)
    elif norm_type == "l2":
        denominator = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
    elif norm_type == "max":
        denominator = np.max(np.abs(matrix), axis=axis, keepdims=True)
    else:
        raise ValueError(f"Unsupported norm_type: {norm_type}")

    # Handle division by zero where denominator is 0
    return np.where(denominator == 0, matrix, matrix / denominator)