#!/usr/bin/env python3
"""Creates a class to store instances of the Redis
client as a private variable
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """a system that counts how many times method cache is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wraps the function and returns the wraper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs for a particular
    function wveryti e the function is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrap the decorated function and return the wrapper"""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)
        input = str(args)
        self._redis.rpush(input_key, input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def  replay(method: Callable):
    """displays the callable history of a function"""
        function_name = method.__qualname__
        input_key = "{}:inputs".format(function_name)
        output_key = "{}:outputs".format(function_name)

        inputs = cache._redis.lrange(input_key, 0, -1)
        outputs = cache._redis.lrange(output_key, 0, -1)
        print("{} was called {} times:".format(function_name, len(inputs)))
        for inp, outp in zip(inputs, outputs):
            print("{}(*{}) -> {}".format(function_name, inp.decode('utf-8'), output.decode('utf-8')))


class Cache:
    """a redis class called cache"""
    def __init__(self):
        """will store instances and flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()

   @call_history
   @count_calls
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

    def get_str(self, key: str) -> Union[str, None]:
        """methods that automatically paratrize Cache.get"""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> Union[int, None]:
        """method with Cache.get with the right conversion function"""
        return self.get(key, fn=int)
