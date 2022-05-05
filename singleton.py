#-*- coding:utf-8 -*-

class Singleton(object):
    ''' This class and it's derived class will only have one implement. '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
