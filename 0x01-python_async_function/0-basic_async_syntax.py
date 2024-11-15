#!/usr/bin/env python3
"""
This module defines an asynchronous`wait_random` that waits for a
random delay and returns the delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ returns random float numbers betweewn 0 and max_delay

max_delay: the maximum delay time to return

Returns:
    random float between 0 and max_delay
"""
    y = random.uniform(0, max_delay)
    await asyncio.sleep(y)
    return y
