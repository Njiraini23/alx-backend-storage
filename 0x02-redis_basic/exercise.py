#!/usr/bin/env python3
"""module with a cache class"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrap decorated function and return the wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """"wrap decorated function and return the wrapper"""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)
        input = str(args)
        self._redis.rpush(input_key, input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def replay(method: Callable):
    """function to display the history of calls of a particular function"""
    function_name = method.__qualname__
    input_key = "{}:inputs".format(function_name)
    output_key = "{}:outputs".format(function_name)

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)
    print("{} was called {} times:".format(function_name, len(inputs)))
    for inp, outp in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(function_name, inp.decode('utf-8'),
                                     outp.decode('utf-8')))


class Cache:
    """a cache redis class"""
    def __init__(self):
        """store an instance then flush"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data argument and returns a string.
        method generates a random key store the input data in Redis using
        the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """convert the data back to the desired format."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Union[str, None]:
        """ parametrize Cache.get with correct conversion function"""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> Union[int, None]:
        """parametrize Cache.get with the correct conversion function"""
        return self.get(key, fn=int)
