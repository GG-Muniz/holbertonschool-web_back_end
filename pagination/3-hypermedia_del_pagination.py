#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination

Implements a `Server` class that provides an indexed dataset and a
`get_hyper_index` method which is resilient to deletions between requests.
"""
import csv
from typing import Dict, List, Optional, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute start and end indices for a paginated list slice."""
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # Keep the full dataset indexed to match the 
            provided main script behavior
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, object]:
        """Return a deletion-resilient hypermedia page starting from index.

        Args:
            index: Starting index for the page (0-based). Must be within range
                   of the current indexed dataset keys.
            page_size: Number of items to return.

        Returns:
            A dictionary with keys: index, next_index, page_size, data.
        """
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        max_index = max(indexed.keys()) if indexed else -1

        if index is None:
            index = 0
        assert isinstance(index, int) and 0 <= index <= max_index + 1

        data: List[List[str]] = []
        current = index
        # Collect up to page_size existing items, skipping missing indices
        while len(data) < page_size and current <= max_index:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        next_index = current if current <= max_index else current

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
