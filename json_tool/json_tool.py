# coding:utf8

import json


def getFromJson():
    print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])


getFromJson()