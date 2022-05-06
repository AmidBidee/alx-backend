#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing
    a start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters.

    Args:
        page [int]: page number
        page_size [int]: page size

    Returns:
        tuple (start_index, end_index)
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database
    of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        initializes Server
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a range of data
        based on starting and end index
        determined by the page and page_size
        """
        assert type(page) == int and type(page_size) == int
        assert (page, page_size) > (0, 0)

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if len(data) > start_index:
            return []
        return data[start_index:end_index]
