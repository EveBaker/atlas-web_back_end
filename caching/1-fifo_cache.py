#!/usr/bin/python3
"""
    BaseCache module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def put(self, key, item):
        """Saves item in cache, discards oldes it limit is exceded"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves item by key"""
        return self.cache_data.get(key, None)
