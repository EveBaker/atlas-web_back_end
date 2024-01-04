#!/usr/bin/env python3
""" Function that creates a asyncio.Task """
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates task"""
    return asyncio.create_task(wait_random(max_delay))