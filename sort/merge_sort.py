# -*- coding: utf-8 -*-

'''
归并排序

归并排序是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的。然后再把有序子序列合并为整体有序序列。

算法步骤：
1. 把n个记录看成n个长度为1的有序子表；
2. 进行两两归并使记录关键字有序，得到n/2个长度为2的有序子表；
3. 重复第2步直到所有记录归并成一个长度为n的有序表为止。

@author: happyin3
@created: 2018.05.19
'''

import random


def merge_sort(data):
    '''
    归并排序
    :param data: <list> 待排序数列
    :return: <list> 已排序数列
    '''
    def merge(sort_data, low, mid, high):
        '''
        合并两个有序数列
        :param sort_data: <list> 待合并数列
        :param low: <int> 数列开始位置
        :param mid: <int> 两个数列分隔位置
        :param high: <int> 数列结束位置
        :return: <None> None
        '''
        left = sort_data[low:mid]
        right = sort_data[mid:high]

        j, k = 0, 0
        result = []

        llen, rlen = len(left), len(right)
        while j < llen and k < rlen:
            if left[j] <= right[k]:
                result.append(left[j])
                j += 1
            else:
                result.append(right[k])
                k += 1

        result.extend(left[j:])
        result.extend(right[k:])

        sort_data[low:high] = result

    nlen = len(data)
    i = 1
    while i < nlen:
        low = 0
        while low < nlen:
            mid = low + i
            high = min(low + 2 * i, nlen)
            if mid < high:
                merge(data, low, mid, high)
            low += 2 * i
        i *= 2

    return data

if __name__ == '__main__':
    ori = range(1, 9)
    data = range(1, 9)

    random.shuffle(data)
    assert merge_sort(data) == ori
