#!/usr/bin/env python3
"""Duck-typed Module that safely retrieves the first element
from a sequence, returning None if the sequence is empty"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely retrieve the first element of a sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
