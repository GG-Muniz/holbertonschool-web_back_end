#!/usr/bin/env python3
"""Basic server-side pagination utilities.

Exposes a `Server` class that loads the `Popular_Baby_Names.csv` dataset and
allows simple page retrieval via `get_page` using 1-indexed pages.
"""

from Popular_Baby_Names import csv
from typing import List, Tuple, Optional
from 0-simple_helper_function import index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset

        Returns:
            The dataset as a list of rows with header removed.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a single page of the dataset.

        Args:
            page: 1-indexed page number to retrieve.
            page_size: Number of items per page.

        Returns:
            A list of rows corresponding to the requested page. Returns an
            empty list if the computed slice is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index >= len(data):
            return []
        return data[start_index:end_index]
