#!/usr/bin/env python3
"""
a python function that chnages all topics
of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of school document based on name"""
    updated_doc = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
    return updated_doc
