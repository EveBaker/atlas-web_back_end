#!/usr/bin/python3
"""
    BaseCache module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that discards
    the last item added when full."""

    def __init__(self):
        """Initalizes LIFOCache"""
        super().__init__()
        self.last_key_added = None

    def put(self, key, item):
        """
        Saves an item in the cache.
        Discards the last added item if the limit is exceeded.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key_added:
                    del self.cache_data[self.last_key_added]
                    print("DISCARD:", self.last_key_added)
                    self.cache_data[key] = item
                    self.last_key_added = key

    def get(self, key):
        """Retrieves item by key"""
        return self.cache_data.get(key, None)
