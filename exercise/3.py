# -*- coding: utf-8 -*-

'''
链表中倒数第k个节点

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本地从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

@author: happyin3
@created: 2018.05.28
'''

import random


class Node(object):
    '''
    节点
    '''
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class NodeList(object):
    '''
    链表
    '''
    def __init__(self):
        self.head = None
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        res_list = []

        p = self.head
        while p is not None:
            res_list.append(str(p.data))
            p = p.next

        return ' '.join(res_list)

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            self.head, node.next = node, self.head

        self.len += 1


def find_kth_to_tail(data, k_index):
    '''
    链表中倒数第k个节点

    :param data: <NodeList> 链表
    :param k: <int> 查找索引
    :return: <> 查找节点值
    '''
    # 链表为空，k_index为0
    if data is None or k_index <= 0:
        return None

    p1, p2 = data.head, data.head
    step = 0
    while p1.next is not None:
        p1 = p1.next

        if step < k_index-1:
            step += 1
        else:
            p2 = p2.next

    # 间距小于k_index
    if step < k_index-1:
        return None

    return p2.data

if __name__ == '__main__':
    data = range(10)
    random.shuffle(data)

    node_list = NodeList()
    for i in data:
        node_list.append(i)
    print node_list

    print find_kth_to_tail(node_list, 1)
    print find_kth_to_tail(node_list, 2)
    print find_kth_to_tail(node_list, 5)
