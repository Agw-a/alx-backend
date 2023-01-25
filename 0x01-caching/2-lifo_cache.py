#!/usr/bin/env python3
'''LIFO cache module
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Represents an object inherited from BaseCaching
    '''

    def __init__(self):
        '''Initilize object'''
        super().__init__()
        self.data = []

    def put(self, key, item):
        '''Insert cache data using the LIFO policy
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            Discard = self.data.pop()
            print('DISCARD: {}'.format(Discard))
            del self.cache_data[Discard]

        self.data.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''returns data linked to the key
        '''

        if key is None or key not in self.cache_data:
            return

        return self.cache_data[key]
