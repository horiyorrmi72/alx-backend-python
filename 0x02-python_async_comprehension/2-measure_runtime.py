#!/usr/bin/env python3
"""
This module defines the `measure_runtime` coroutine
which executes `async_comprehension` 4 times concurrently
and measures the total runtime.
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of 4 parallel executions of async_comprehension.
    Return the total time it took to execute the 4 calls.
    """

    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()

    return end_time - start_time
