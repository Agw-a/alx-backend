from typing import Tuple, List, Dict
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            Dict: _description_
        """
        data = self.get_page(page, page_size)
        dataRange = self.dataset()
        totla_pages = len(dataRange) // page_size
        if len(dataRange) % page_size:
            totla_pages += 1
        nxt_page = prv_page = None
        if page > 1:
            prv_page = page - 1
        if page < totla_pages:
            nxt_page = page + 1
        page_details = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nxt_page,
            'prev_page': prv_page,
            'total_pages': totla_pages
        }
        return page_details
