#!/usr/bin/python3
"""
    BaseCache module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that discards
    the last item added when full."""

    def __int__(self):
        """Initalizes LIFOCache"""
        super().__int__()

    def put(self, key, item):
        """
        Saves an item in the cache.
        Discards the last added item if the limit is exceeded.
        """
        if key or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self_last_key_added:
                    del self.cache_data[self_last_key_added]
                    print("DISCARD:", self_last_key_added)
                    self.cache_data[key] = item
                    self_last_key_added = key

    def get(self, key):
        """Retrieves item by key"""
        return self.cache_data.get(key, None)
