#!/usr/bin/env python3
"""
lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """returns empty list if no document"""
    documents = mongo_collection.find()
    return list(documents)
