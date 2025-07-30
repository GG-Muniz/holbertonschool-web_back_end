#!/usr/bin/env python3
"""Module for creating key-value tuples with type annotations."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with string key and squared numeric value.
    
    Args:
        k: String key
        v: Numeric value (int or float) to be squared
        
    Returns:
        Tuple containing the string key and squared value as float
    """
    return (k, v ** 2)
