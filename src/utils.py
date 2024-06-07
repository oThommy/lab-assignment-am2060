import pandas as pd
from IPython.display import display
from typing import Optional
import numpy as np
import warnings
from pathlib import Path
import os
import sys

def is_divisible_by(dividend: float, divisor: float, tolerance: float = 1e-9) -> bool:
    if divisor == 0:
        raise ValueError('The divisor cannot be zero.')
    quotient = dividend / divisor
    return np.abs(quotient - round(quotient)) < tolerance

def assert_is_positive(x: float, /, variable_name: Optional[str] = None) -> None:
    if x > 0:
        return
    if variable_name is None:
        raise ValueError(f'The number must be positive, got {x} instead.')
    else:
        raise ValueError(f'The variable {variable_name} must be positive, got {x} instead.')
    
def assert_is_nonnegative(x: float, /, variable_name: Optional[str] = None) -> None:
    if x >= 0:
        return
    if variable_name is None:
        raise ValueError(f'The number must be nonnegative, got {x} instead.')
    else:
        raise ValueError(f'The variable {variable_name} must be nonnegative, got {x} instead.')

def display_df(df: pd.DataFrame) -> None:
    '''
    Pretty print a pandas DataFrame without the index column in a Jupyter notebook.

    Raises:
    Warning: If the function is not called from within a Jupyter notebook.
    '''
    is_in_notebook = 'ipykernel' in sys.modules
    if not is_in_notebook:
        warnings.warn('display_df is designed to be used in Jupyter notebooks only.', UserWarning)

    df_styled = df.style.hide(axis='index')
    display(df_styled)

def ensure_dir_exists(dir: Path) -> None:
    '''Ensures directory exists by creating the directory recursively if it doesn't exist yet'''
    if not dir.exists():
        os.makedirs(dir)