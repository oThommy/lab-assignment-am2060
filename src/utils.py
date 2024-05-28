from typing import Optional
import numpy as np

def is_divisible_by(dividend: float, divisor: float, tol: float = 1e-9) -> bool:
    if divisor == 0:
        raise ValueError('The divisor cannot be zero.')
    quotient = dividend / divisor
    return np.abs(quotient - round(quotient)) < tol

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
        raise ValueError(f'The number must be positive, got {x} instead.')
    else:
        raise ValueError(f'The variable {variable_name} must be positive, got {x} instead.')

