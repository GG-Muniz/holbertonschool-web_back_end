#!/usr/bin/env python3
"""Query utilities for schools by topic."""
from typing import List, Dict, Any


def schools_by_topic(mongo_collection, topic: str) -> List[Dict[str, Any]]:
    """Return list of schools having the specified topic.

    Args:
        mongo_collection: A PyMongo collection instance.
        topic: The topic to search within the "topics" array field.

    Returns:
        A list of matching school documents.
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    pass 