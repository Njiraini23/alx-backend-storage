#!/usr/bin/env python3
"""
a python function that inserts a new document
in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    new_id = mongo_collection.insert_one(kwargs)
    return new_id.inserted_id
