#!/usr/bin/env python3
"""
Module for Cache class.
"""

import redis
import uuid
from typing import Union, Callable

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

    def get(self, key: str, fn: Callable = None):
        """stores cache"""
        value = self._redis.get(key)
        if value is not None and fn:
            return fn(value)
        return value
    
    def get_str(self, key: str) -> str:
        """gets str"""
        return self._redis.get(key).decode("utf-8") 
    
    def get_int(self, key:str) -> int:
        """Parametrized get int"""
        return self.get(key, fn=int)