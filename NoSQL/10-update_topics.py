#!/usr/bin/env python3
"""Utilities for updating school topics in MongoDB."""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """Update the topics of all school documents matching the given name.

    Args:
        mongo_collection: A PyMongo collection instance.
        name: The school name to match.
        topics: The list of topics to set for the matching documents.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})


if __name__ == "__main__":
    pass
