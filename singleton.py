# -*- coding:utf-8 -*-

# A class that only has one instance.
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwards):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwards)
        return cls._instance
