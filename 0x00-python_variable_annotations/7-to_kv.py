#!/usr/bin/env python3
"""
type-annotatedd function that takes a string and an int OR float 
as  arguments and returns a tuple.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This returns a tuple"""
    return (k, float(v ** 2))
