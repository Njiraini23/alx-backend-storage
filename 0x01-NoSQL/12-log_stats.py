#!/usr/bin/env python3
"""
A script that provides some stats about Nginx
logs stored in MongoDB with Database logs stored
in collection in nginx. First line X logs and second
line is Methods
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_logs_stats(collection, option=None):
    """
    this function shows stats for logs
    """
    if option:
        count = collection.count_documents({"method": option})
        print("\tmethod {}: {}".format(option, count))
        return

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))
    print("Methods:")
    for method in METHODS:
        get_logs_stats(collection, method)
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    """Using the MongoDB connection URL"""
    mongodb_url = 'mongodb://127.0.0.127017'
    client = MongoClient(mongodb_url)
    db = client.logs
    nginx_collection = db.nginx

    get_logs_stats(nginx_collection)
