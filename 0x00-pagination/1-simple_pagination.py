#!/usr/bin/env python3
'''Implement a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
If the arguments are out of range for the dataset, an empty list is returned.
'''
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """determine index range from a page and page size

    Args:
        page (int): page number 1-indexed
        page_size (int): range

    Returns:
        Tuple[int, int]: start index and end index
    """
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    '''Server class to paginate a DB of popular babt names
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """list of retreived data

        Args:
            page (int, optional):  Defaults to 1.
            page_size (int, optional):  Defaults to 10.

        Returns:
            List[List]: list with data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        paginateRange = index_range(page, page_size)
        data = self.dataset()
        res = []
        if paginateRange[0] > len(data):
            pass
        elif paginateRange[1] > len(data):
            res = data[paginateRange[0]:]
        else:
            res = data[paginateRange[0]:paginateRange[1]]
        return res
