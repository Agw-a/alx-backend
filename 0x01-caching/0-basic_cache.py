#!/usr/bin/python3
'''Basic caching
'''

from base_caching import BaseCaching


class BasicCache():
    '''store and get items from an id
    '''
    def put(self, key, item):
        '''insert into the cache
        '''
        if key or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''return an item
        '''
        return self.cache_data.get(key, None)
