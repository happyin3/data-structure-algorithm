# -*- coding: utf-8 -*-

'''
插入排序

通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5

@author: happyin3
@created: 2018.05.19
'''

import random


def insert_sort(data):
    '''
    插入排序
    :param data: <list> 待排序数列
    :return: <list> 已排序数列
    '''
    nlen = len(data)

    for i in xrange(1, nlen):
        for j in xrange(i, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break

    return data


def insert_sort_binary(data):
    '''
    插入排序，插入位置使用二分搜索
    :param data: <list> 待排序数列
    :return: <list> 已排序数列
    '''
    nlen = len(data)

    for i in xrange(1, nlen):
        index = binary_search_index(data[:i], data[i])

        if index != i-1:
            for j in xrange(i, index, -1):
                data[j], data[j-1] = data[j-1], data[j]

    return data


def binary_search_index(data, value):
    '''
    二分查找索引位置
    :param data: <list> 有序数列
    :param value: <list> 搜索数值
    '''
    l, r = 0, len(data)-1
    while l <= r:
        mid = (l+r) / 2
        if data[mid] > value:
            r = mid - 1
        elif data[mid] < value:
            l = mid + 1
        else:
            return mid+1
    return l

if __name__ == '__main__':
    ori = range(1, 9)
    data = range(1, 9)
    random.shuffle(data)

    assert insert_sort(data) == ori
    assert insert_sort_binary(data) == ori
