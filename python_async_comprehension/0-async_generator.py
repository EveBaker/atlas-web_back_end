#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random


async def async_generator():
    """returns time random"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
