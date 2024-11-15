#!/usr/bin/env python3
"""
This module provides a utility function to safely retrieve a value
from a dictionary by a specified key, returning a default value if
the key is not found.
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary by key,
    returning a default value if the key is not found.

    Arguments:
        dct (Mapping): A dictionary-like mapping from which retrieve the value
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return
            if the key is not found. Defaults to None.

    Returns:
       Union[Any, T]: The value corresponding to the key, or the default value
    """
    if key in dct:
        return dct[key]
    return default
