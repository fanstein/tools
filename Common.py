# coding:utf8
import json


class Common(object):

    def __init__(self):
        pass

    @staticmethod
    def log(describe):
        def decorator(func):
            def wrapper(*args, **kw):
                print('call %s %s()' % (describe, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

    pass
