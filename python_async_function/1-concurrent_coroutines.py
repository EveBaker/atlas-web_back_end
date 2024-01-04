#!/usr/bin/env python3
"""more async"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """float time random"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return sorted(completed_delays)
