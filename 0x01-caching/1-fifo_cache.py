#!/usr/bin/env python3
from base_caching import BaseCaching
'''FIFO cache module
'''


class FIFOCache(BaseCaching):
    '''Represents FIFO rempving mechanism
    '''
    def __init__(self):
        '''call parent cache init
        '''
        super().__init__()
        self.data = []

    def put(self, key, item):
        '''insert into the cache
        '''
        if key is None or item is None:
            return

        if len(self.cac) >= self.MAX_ITEMS:
            discard = self.data.pop(0)
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]

        self.data.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''get an item by key value
        '''
        return self.cache_data.get(key, None)
