#!/usr/bin/env python3
"""Simple helper for pagination ranges.

This module exposes a single function, `index_range`, which computes the
[start, end) slice indices corresponding to a 1-indexed page number and a
page size. It is intended to be used by pagination utilities.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute start and end indices for a paginated list slice.

    Args:
        page: 1-indexed page number.
        page_size: Number of items per page.

    Returns:
        A tuple of two integers: (start_index, end_index), suitable for use
        with list slicing semantics where end_index is exclusive.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index) 