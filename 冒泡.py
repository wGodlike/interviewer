#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by wGodlike at 2019-08-23
# @Desc


def foo(data):
    for i in range(len(data)):
        flag = False
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
        if not flag:
            break
    return data


def bubble_sort(data):
    """
    最坏情况 时间复杂度 O(n**2)
    最好情况 时间复杂度 O(n)
    稳定排序法
    空间复杂度最佳     只需要一个额外空间
    适用于数据量小或有部分数据已经排过序的情况
    :param data:
    :return:
    """
    # i 倒序循环列表排序
    for i in range(len(data)-1, -1, -1):
        flag = False                        # flag判断是否执行了交换操作
        # i 为倒序循环，所以j的最大值即是i 0～i
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True                # 执行过交换操作，把flag致为True
        if not flag:
            break
            # 执行完一次扫描后，判断是否执行过交换操作，如果没有交换过数据，就表示此时数组已完成排序，故直接跳出循环
        print('第{0}次排序: {1}'.format(len(data)-i, data))
    return data


if __name__ == '__main__':
    a = [3, 5, 4, 2, 6, 8, 1, 9, 7]
    print(a)
    print(foo(a))
