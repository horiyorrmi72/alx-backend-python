#!/usr/bin/env python3
"""
This module defines a `task_wait_n` function using `task_wait_random`
"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_random` n times with specified max_delay and return
    the list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
