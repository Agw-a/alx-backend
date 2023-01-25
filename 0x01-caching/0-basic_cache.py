#!/usr/bin/env python3
'''Basic caching
'''
from base_caching import BaseCaching


class BasicCache():
    '''inherits from BaseCaching
    '''
    def put(self, key, item):
        if key or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data linked to key.
        '''
        return self.cache_data.get(key, None)
