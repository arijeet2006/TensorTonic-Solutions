import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    x = np.asarray(X, dtype=float)
    n = len(x)
    d = x.shape[1]

    corr = np.empty((d, d))

    for i in range(d):
        for j in range(i, d):
            x_val = x[:, i]
            y_val = x[:, j]
            x_bar = np.sum(x_val) / n
            y_bar = np.sum(y_val) / n

            dx = x_val - x_bar
            dy = y_val - y_bar

            sigma_x = np.sqrt(np.sum(dx**2) / (n - 1))
            sigma_y = np.sqrt(np.sum(dy**2) / (n - 1))

            cov = np.sum(dx * dy) / (n - 1)

            if sigma_x * sigma_y == 0:
                r = np.nan
            elif i == j:
                r = 1.0
            else:
                r = cov / (sigma_x * sigma_y)

            corr[i, j] = r
            corr[j, i] = r

    return corr