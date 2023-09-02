#!/usr/bin/env python3
"""Creates a class to store instances of the Redis
client as a private variable
"""

import redis
import uuid
from typing import Union

class Cache:
    """a redis class called cache"""
    def __init__(self):
        """will store instances and flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        A store method that takes in data and returns a string.
        The method generates a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
