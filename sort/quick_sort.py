# -*- coding: utf-8 -*-

'''
快速排序

快速排序使用分治法策略来把一个序列分为两个子序列。
步骤：
1. 从数列中挑出一个元素，称为基准
2. 重新排列序列，所有比基准小的元素摆放在基准前面，所有比基
   准大的元素摆放在基准后面。在这个分割结束后，该基准就处于
   数列的中间位置。
3. 递归地把小于基准值元素的子序列和大于基准值的子序列排序。

@author: happyin3
@created: 2018.05.18
'''

import random


def partition(data, low, high):
    p_index = low
    p_data = data[p_index]

    for i in xrange(low+1, high+1):
        if data[i] < p_data:
            for j in xrange(i, p_index, -1):
                data[j], data[j-1] = data[j-1], data[j]
            p_index += 1

    return p_index


def quick_sort(data, low, high):
    '''
    快速排序
    :param data: <list> 待排序数列
    :param low: <int> 数列开始位置
    :param high: <int> 数列结束位置
    :return: <list> 已排序数列
    '''
    if low > high:
        return data

    mid = partition(data, low, high)
    quick_sort(data, low, mid-1)
    quick_sort(data, mid+1, high)

    return data

if __name__ == '__main__':
    ori = range(1, 9)
    data = range(1, 9)

    random.shuffle(data)
    assert quick_sort(data, 0, len(data)-1) == ori
