#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `wait_n` that spawns
`wait_random` n times and returns the list of delays in ascending order.
"""

from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time using async"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
