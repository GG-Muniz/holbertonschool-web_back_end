#!/usr/bin/env python3
"""Print statistics about Nginx logs stored in MongoDB.

Database: logs
Collection: nginx
"""
from pymongo import MongoClient


def main() -> None:
    """Connect to MongoDB and print required statistics."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total = collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_check} status check")


if __name__ == "__main__":
    main()
