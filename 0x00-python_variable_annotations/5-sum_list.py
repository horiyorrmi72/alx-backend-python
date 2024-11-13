#!/usr/bin/env python3
"""
Module that defines a type-annotated function to sum a list of provided floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats."""
    return sum(input_list)
