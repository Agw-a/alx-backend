#!/usr/bin/python3
'''LRU Cache replacement
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Represents LRU cachind policy
    '''

    def __init__(self):
        '''Intilizes the oject
        '''
        super().__init__()
        self.data = []

    def put(self, key, item):
        '''get item using LRU
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            Discard = self.data.pop(0)
            print('DISCARD: {}'.format(Discard))
            del self.cache_data[Discard]

        self.data.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Returns data linked to a key
        '''

        if key is None or key not in self.cache_data:
            return None

        self.data.remove(key)
        self.data.append(key)

        return self.cache_data[key]
