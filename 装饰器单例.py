#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-08-23
# @Desc


def singleton(cls, *args, **kwargs):
    _instance = {}

    def get_instance():
        if cls not in _instance:
            _instance.setdefault(cls, cls(*args, **kwargs))
        return _instance.get(cls)
    return get_instance


@singleton
class MyClass(object):pass


if __name__ == '__main__':
    var1 = MyClass()
    var2 = MyClass()
    print(id(var1))
    print(id(var2))