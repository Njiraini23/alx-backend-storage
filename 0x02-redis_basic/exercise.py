#!/usr/bin/env python3
"""Creates a class to store instances of the Redis
client as a private variable
"""
class Cache:
    """a redis class called cache"""
    def __init__(self):
        """will store instances and flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()
