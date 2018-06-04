#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 6. 合并排序数组 II.py
    @Software: PyCharm
    @Description:
        描述
            合并两个排序的整数数组A和B变成一个新的数组。

        样例
            给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

        挑战
            你能否优化你的算法，如果其中一个数组很大而另一个数组很小？
"""
def combainList(lista,listb):
    lista.extend(listb)
    new_list = sorted(lista)
    print new_list

combainList([1,2,3,4],[2,4,5,6])