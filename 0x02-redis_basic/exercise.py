#!/usr/bin/env python3
"""Creates a class to store instances of the Redis
client as a private variable
"""
class Redis(object):
    def __init__(self, host='localhost', port=6379,
            db=0, password=None, socket_timeout=None)
