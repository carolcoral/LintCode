#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 366. 斐波纳契数列.py
    @Software: PyCharm
    @Description:
        描述
            查找斐波纳契数列中第 N 个数。

            所谓的斐波纳契数列是指：

            前2个数是 0 和 1 。
            第 i 个数是第 i-1 个数和第i-2 个数的和。
            斐波纳契数列的前10个数字是：

            0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

        样例
            给定 1，返回 0

            给定 2，返回 1

            给定 10，返回 34
"""

def Fibolache(j):
    n = j-1
    if n == 1 or n == 2:
        return 1
    # 用迭代进行计算
    nPre = 1
    nLast = 1
    nResult = 0
    i = 2
    while i < n:
        nResult = nPre + nLast
        nPre = nLast
        nLast = nResult
        i += 1

    print  nResult

Fibolache(100)