#!/usr/bin/env python3
import asyncio
import random

"""basic await"""


async def wait_random(max_delay: int = 10) -> float:
    """returns random float time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
