#!/usr/bin/env python3
""" Range simple helper fun """
from typing import Tuple


def index_range(page, page_size):
    """returns a tuple"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
