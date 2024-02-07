#!/usr/bin/env python3
"""
Module for Cache class.
"""

import redis
import uuid
from typing import Union

class Cache:
    """Cache class for redis storage"""
    def __init__(self):
        """initializes the cache class for redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key