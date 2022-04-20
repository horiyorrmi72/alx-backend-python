import asyncio
import random

async def wait_random(max_delay = 10)-> float:
    y = random.uniform(0, max_delay)
    await asyncio.sleep(y)
    return y

