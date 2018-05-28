# -*- coding: utf-8 -*-

'''
调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

@author: happyin3
@created: 2018.05.28
'''

import random


def data_sort(data):
    '''
    数组排序

    :param data: <list> 待排序数列
    :return: <list> 已调整数列
    '''
    if len(data) < 2:
        return data

    left, right = 0, len(data) - 1

    while left < right:
        while left < right and data[left] & 1:
            left += 1

        while left < right and data[right] & 1 == 0:
            right -= 1

        if left < right:
            data[left], data[right] = data[right], data[left]

    return data

if __name__ == '__main__':
    data = range(10)
    random.shuffle(data)
    print data_sort(data)
