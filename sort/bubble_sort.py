# -*- coding: utf-8 -*-

'''
冒泡排序

1. 比较相邻的元素，如果第一个比第二个大，就交换它们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

@author: happyin3
@created: 2018.05.18
'''


def bubble_sort(data):
    '''
    冒泡排序
    :param data: <list> 待排序数列
    :return: <list> 排序后数列
    '''
    nlen = len(data)
    for i in xrange(nlen-1):
        for j in xrange(nlen-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def bubble_sort_flag(data):
    '''
    冒泡排序，增加标示量
    :param data: <list> 待排序数列
    :return: <list> 排序后数列
    '''
    nlen = len(data)

    for i in xrange(nlen-1):
        flag = False
        for j in xrange(nlen-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = True
        if not flag:
            break

    return data


def bubble_sort_index(data):
    '''
    冒泡排序，增加标示量
    :param data: <list> 待排序数列
    :return: <list> 排序后数列
    '''
    nlen = len(data)

    index = nlen - 1
    for i in xrange(nlen-1):
        temp = index
        for j in xrange(index):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                index = j
        if index == temp:
            break

    return data

if __name__ == '__main__':
    data = [4, 5, 1, 2, 6, 3, 7]
    assert bubble_sort(data) == [1, 2, 3, 4, 5, 6, 7]
    assert bubble_sort_flag(data) == [1, 2, 3, 4, 5, 6, 7]
    assert bubble_sort_index(data) == [1, 2, 3, 4, 5, 6, 7]
