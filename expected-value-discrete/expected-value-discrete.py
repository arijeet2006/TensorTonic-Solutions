import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    a = np.array(x)
    b = np.array(p)
    p = float(np.dot(a,b))
    return p
    pass