# -*- coding: utf-8 -*-

'''
希尔排序

希尔排序是插入排序一种更高效的改进版本。

希尔排序是基于插入排序的以下两点性质而提出改进方法的：
* 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
* 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

希尔排序通过将比较的全部元素分为几个区域来提升插入排序的性能。这样可以让一个元素可以一次性地朝最终位置前进一大步。然后算法再取越来越小的步长进行>排序，算法的最后一步就是普通的插入排序，但是到了这步，需排序的数据几乎是已排好的了（此时插入排序较快）。

1. 先取一个正整数 d1(d1 < n)，把全部记录分成 d1 个组，所有距离为 d1 的倍数的记录看成一组，然后在各组内进行插入排序
2. 然后取 d2(d2 < d1)
3. 重复上述分组和排序操作；直到取 di = 1(i >= 1) 位置，即所有记录成为一个组，最后对这个组进行插入排序。一般选 d1 约为 n/2，d2 为 d1 /2， d3 为 d2/2 ，…， di = 1。

@author: happyin3
@created: 2018.05.20
'''

import random


def shell_sort(data):
    '''
    希尔排序
    :param data: <list> 待排序数列
    :return: <list> 已排序数列
    '''
    nlen = len(data)

    gap = nlen / 2
    while gap > 0:
        for i in range(gap, nlen):
            # 插入排序
            for j in range(i, 0, -gap):
                if data[j] < data[j-gap]:
                    data[j], data[j-gap] = data[j-gap], data[j]
                else:
                    break
        gap = gap / 2

    return data


def shell_sort_opt(data):
    nlen = len(data)

    gap = nlen / 2
    while gap > 0:
        for i in range(gap, nlen):
            temp = data[i]
            j = i
            while j >= gap and data[j-gap] > temp:
                data[j] = data[j-gap]
                j -= gap
            data[j] = temp
        gap = gap / 2

    return data

if __name__ == '__main__':
    ori = range(1, 9)
    data = range(1, 9)

    random.shuffle(data)
    assert shell_sort(data) == ori

    random.shuffle(data)
    assert shell_sort_opt(data) == ori
