#!/usr/bin/env python3
""" Module for BasicCache class """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A simple caching system. It stores
    data in a dictionary with no limit."""


def put(self, key, item):
    """
    Save an item to the cache
    If the key or item is None, nothing happens.
    """
    if key is not None and item is not none:
        self.cache_data[key] = item


def get(self, key):
    """
    Get an item by its key.
    Returns None if the key is none or doesn't exist.
    """
    return self.cache_data.get(key, None)
