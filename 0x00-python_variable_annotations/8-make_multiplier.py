#!/usr/bin/env python3
"""
Type-annotated function taking a float as an argument and returns a function
that multiplies a float by the multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a given float by a multiplier."""

    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
