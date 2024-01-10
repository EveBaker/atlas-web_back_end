#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """ Range of the page, returns tuple
        with the range start and end size page """
    start_index = (page - 1) * page_size
    end_index = start_index = page_size
    return start_index, end_index


class server:
    """server class for paginating a database of baby names"""
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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.__dataset):
            return []
        return self.__dataset[start_index:end_index]
