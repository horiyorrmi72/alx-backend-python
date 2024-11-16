#!/usr/bin/env python3
"""
This module defines a `measure_time` function to measure the
runtime of `wait_n` with concurrency.
"""

import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime of wait_n and return the average time per call,
    return the result in float
    """
    begins_at = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - begins_at

    return total_time / n
