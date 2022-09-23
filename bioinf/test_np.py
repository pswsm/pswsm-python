import numpy as np
import pandas as pd

def test_nan() -> pd.Series:
    return pd.Series([1, 2, 3, np.NAN, 4])

def test_custom_idx() -> pd.Series:
    idx_temp: list = ['jan', 'feb', 'mar', 'apr']
    month_tmp_serie: pd.Series = pd.Series(data=idx_temp, dtype='string')
    return month_tmp_serie

print(test_nan())
print(test_custom_idx())
