#!/usr/bin/python3
"""  Basic cache """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class that inherits from BaseCaching """
    def put(self, key, item):
        """ Assign to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the linked value """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
