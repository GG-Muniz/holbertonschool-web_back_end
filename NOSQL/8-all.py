#!/usr/bin/env python3
"""Utilities for listing all documents in a MongoDB collection."""
from typing import List


def list_all(mongo_collection) -> List[dict]:
    """List all documents in the provided MongoDB collection.

    Args:
        mongo_collection: A PyMongo collection instance.

    Returns:
        A list of all documents in the collection. Returns an empty list if
        the collection contains no documents.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())


if __name__ == "__main__":
    pass
