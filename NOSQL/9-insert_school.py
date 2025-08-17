#!/usr/bin/env python3
"""Utilities for inserting documents into a MongoDB collection."""
from typing import Any


def insert_school(mongo_collection, **kwargs: Any) -> Any:
    """Insert a new document into the collection using provided kwargs.

    Args:
        mongo_collection: A PyMongo collection instance.
        **kwargs: Arbitrary keyword arguments to form the document.

    Returns:
        The `_id` of the inserted document.
    """
    result = mongo_collection.insert_one(dict(kwargs))
    return result.inserted_id


if __name__ == "__main__":
    pass
