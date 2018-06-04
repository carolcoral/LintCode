#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 466. 链表节点计数.py
    @Software: PyCharm
    @Description:
        描述
            计算链表中有多少个节点.
        样例
            给出 1->3->5, 返回 3.
"""
def sumList(head):
    sum = 0
    list = str(head).split('->')
    for i in list:
        if i == 'null'or i == None:
            pass
        else:
            sum = sum+1
    print sum

sumList("1->3->5->6->null")