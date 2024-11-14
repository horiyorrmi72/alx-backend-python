#!/usr/bin/env python3
"""
Takes a list of sequences and returns a list of tuples, each containing a
sequence and its length.
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of sequences and returns a list of tuples, each containing a
    sequence and its length.
    """
    return [(i, len(i)) for i in lst]
