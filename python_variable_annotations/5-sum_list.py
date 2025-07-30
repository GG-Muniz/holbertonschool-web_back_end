#!/usr/bin/env python3
"""Module for summing a list of floats with type annotations."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum all floats in a list.

    Args:
        input_list: List of float numbers to sum

    Returns:
        Sum of all floats in the list
    """
    return sum(input_list)
