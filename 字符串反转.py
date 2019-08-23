#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-08-23
# @Desc


# 反转字符串 1
def foo(data):
    """
    1. 字符串为不可变类型
    :param data:
    :return:
    """
    data = list(data)  # 字符串为不可变类型，需先转为list
    for i in range(len(data) // 2):
        data[i], data[len(data) - i - 1] = data[len(data) - i - 1], data[i]
    return ''.join(data)
    # 列表转为字符串返回


if __name__ == '__main__':
    s = 'abcdef'
    print(s)
    # 切片反转
    print(s[::-1])
    # 函数反转,list强转,join连接
    print(''.join(list(reversed(s))))
    print(foo(s))
