#!/usr/bin/env python3
"""Module for summing mixed lists with type annotations."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all numbers in a mixed int/float list.

    Args:
        mxd_lst: List of integers and floats to sum

    Returns:
        Sum of all numbers in the list as a float
    """
    return sum(mxd_lst)
