#!/usr/bin/env python3
"""Module for duck typing with iterables and sequences."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples with elements and their lengths.

    Args:
        lst: Iterable of sequences

    Returns:
        List of tuples where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
