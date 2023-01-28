#!/usr/bin/env python3
"""
    Simple pagination.
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        index_range
        """
        start = (page - 1) * page_size
        end = start + page_size
        return start, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get pages"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        if self.__dataset is None:
            return []
        start, end = self.index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        data = self.get_page(page, page_size)
        size_data_set = len(self.__dataset) if self.__dataset else 0
        total_pages = math.ceil(size_data_set / page_size)
        page_size = len(data) if data else None

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
