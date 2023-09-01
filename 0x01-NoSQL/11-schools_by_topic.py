#!/usr/bin/env python3
"""A function that returns the list of
school having specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having specific topic"""
    school_new_topic = mongo_collection.find(
            {"topics": topic})
    return list(school_new_topic)
