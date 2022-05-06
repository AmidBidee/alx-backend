#!/usr/bin/python3
"""
a simple pagination helper function
"""


def index_range(page, page_size):
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
