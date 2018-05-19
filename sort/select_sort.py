# -*- coding: utf-8 -*-

'''
选择排序

选择排序是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

@author: happyin3
@created: 2018.05.19
'''

import random


def select_sort(data):
    '''
    选择排序
    :param data: <list> 待排序数列
    :return: <list> 已排序数列
    '''
    nlen = len(data)

    for i in xrange(nlen-1):
        max_i = nlen - 1 - i
        for j in xrange(nlen-i):
            max_i = j if data[max_i] < data[j] else max_i
        if max_i != nlen-1-i:
            data[max_i], data[nlen-1-i] = data[nlen-1-i], data[max_i]

    return data


def select_sort_opt(data):
    '''
    选择排序，优化
    :param data: <list> 待排序数列
    :return: <list> 已排序数列
    '''
    nlen = len(data)

    for i in xrange(nlen-1):
        min_i, max_i = i, nlen-1-i
        for j in xrange(i, nlen-i):
            max_i = j if data[max_i] < data[j] else max_i
            min_i = j if data[min_i] > data[j] else min_i

        # 若先交换最小值，考虑最大值在最小值的位置
        # 若先交换最大值，考虑最小值在最大值的位置

        if max_i != nlen-1-i:
            data[max_i], data[nlen-1-i] = data[nlen-1-i], data[max_i]

        # 这里先交换最大值，所以考虑最小值在最大值的位置
        # 8 5 4 2
        min_i = max_i if min_i == nlen-1-i else min_i

        if min_i != i:
            data[min_i], data[i] = data[i], data[min_i]

        if i == nlen-1-i:
            break

    return data

if __name__ == '__main__':
    ori = range(1, 9)
    data = range(1, 9)

    random.shuffle(data)
    assert select_sort(data) == ori

    random.shuffle(data)
    assert select_sort_opt(data) == ori
