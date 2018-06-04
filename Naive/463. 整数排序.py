#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 463. 整数排序.py
    @Software: PyCharm
    @Description:
        描述
            给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n2) 的排序算法。
        样例
            对于数组 [3, 2, 1, 4, 5], 排序后为：[1, 2, 3, 4, 5]。
"""

def sort(arr):
    list1 = list(arr)
    res = sorted(list1)
    print res

sort("32145")