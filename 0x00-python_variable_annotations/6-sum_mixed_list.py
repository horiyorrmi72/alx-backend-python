#!/usr/bin/env python3
"""
Type-annotated function to sum a list of floats and integers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Return the sum of a list containing integers and floats as a float."""
    return sum(mxd_lst)
