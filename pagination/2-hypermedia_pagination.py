#!/usr/bin/env python3
"""Hypermedia pagination utilities.

Exposes a `Server` class that supports both page retrieval and a hypermedia
response describing pagination state.
"""
import csv
import math
from typing import Dict, List, Optional, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute start and end indices for a paginated list slice.

    Args:
        page: 1-indexed page number.
        page_size: Number of items per page.

    Returns:
        A tuple of two integers: (start_index, end_index),
        suitable for use
        with list slicing semantics where end_index is exclusive.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a single page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index >= len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, object]:
        """Return hypermedia pagination details for a page request.

        The returned dictionary contains:
        - page_size: length of the returned data page
        - page: current page number
        - data: list of rows for the page
        - next_page: next page number or None
        - prev_page: previous page number or None
        - total_pages: total number of pages in the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if page_size else 0

        next_page: Optional[int] = page + 1 if page < total_pages else None
        prev_page: Optional[int] = page - 1 if page > 1 else None

        result: Dict[str, object] = {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
        return result
