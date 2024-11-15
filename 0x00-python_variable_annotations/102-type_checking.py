#!/usr/bin/env python3
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on an array by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int, optional): The repetition factor. Defaults to 2.

    Returns:
        List[int]: A list with each element of the tuple repeated.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
