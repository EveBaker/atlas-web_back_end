#!/usr/bin/env python3
""" Hypermedia pagination """
import csv
from math import ceil
from typing import List, Tuple, Dict


def index_range(page, page_size):
    """returns tuple with the range start and end size page"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
                return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the page, returns List of the pagination done"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.__dataset):
            return[]
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Range of the page"""
        total_pages = ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
