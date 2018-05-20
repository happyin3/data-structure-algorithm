# -*- coding: utf-8 -*-

'''
二分搜索

二分搜索是一种在有序数组中查找某一特定元素的搜索演算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。

@author: happyin3
@created: 2018.05.20
'''


def binary_search(data, value):
    '''
    二分搜索
    :param data: <list> 有序数列
    :param value: <int> 搜索值
    :return: <int> 存在：索引值；不存在：-1
    '''
    nlen = len(data)

    low, high = 0, nlen-1
    while low <= high:
        mid = (low+high) / 2
        if data[mid] > value:
            high = mid - 1
        elif data[mid] < value:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    data = range(1, 9)

    assert binary_search(data, 8) == 7
    assert binary_search(data, 9) == -1
