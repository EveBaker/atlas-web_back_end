#!/usr/bin/python3
"""
    BaseCache module
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Initializes LRUCache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Saves item in cache, discards least used"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_order.reverse(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru = self.usage_order.pop(0)
                del self.cache_data[lru]
                print("DISCARD:", lru)

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """Retrieves item by key, updates to most recent"""
        if key is not None and key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
