#!/usr/bin/env python3
"""Module for creating multiplier functions with type annotations."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.
    
    Args:
        multiplier: The multiplier value
        
    Returns:
        A function that takes a float and returns it multiplied by multiplier
    """
    def multiply(n: float) -> float:
        """Multiply n by the multiplier.
        
        Args:
            n: Float to multiply
            
        Returns:
            n multiplied by multiplier
        """
        return n * multiplier
    return multiply