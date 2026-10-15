import pandas as pd
def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    s_cat = pd.Series(categories)
    s_tar = pd.Series(targets)
    return s_cat.map(s_tar.groupby(s_cat).mean()).tolist()
    pass