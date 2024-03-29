#!/usr/bin/env python3
"""
Module for Cache class.
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """counts calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        method_name = method.__qualname__
        self._redis.incr(method_name) #increments call count
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """calls the history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper method"""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        
        return result
    return wrapper


class Cache:
    """Cache class for redis storage"""
    def __init__(self):
        """initializes the cache class for redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    

    @call_history
    @count_calls
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