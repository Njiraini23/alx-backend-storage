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

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """return data as a byte string when retrieved from the server"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key:str) -> Union[str, None]:
        """methods that automatically paratrize Cache.get"""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> Union[int, None]:
        """metho with Cache.get with the right conversion function"""
        return self.get(key, fn=int)

