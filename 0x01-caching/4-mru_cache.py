#!/usr/bin/python3
"""MRU Caching policy
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Inherits from BaseCaching class
    """

    def __init__(self):
        """Inherit attribute from BaseCaching
        """
        super().__init__()
        self.data = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        an item value for the key.
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            Discard = self.data.pop()
            print("DISCARD: {}".format(Discard))
            del self.cache_data[Discard]

        self.data.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to a key
        """

        if key is None or key not in self.cache_data:
            return None

        self.data.remove(key)
        self.data.append(key)

        return self.cache_data[key]
