#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/1
    @Author  : LiuXueWen
    @Site    : 
    @File    : 2. 尾部的零.py
    @Software: PyCharm
    @Description:
        描述
            设计一个算法，计算出n阶乘中尾部零的个数

            您在真实的面试中是否遇到过这个题？
            样例
            11! = 39916800，因此应该返回 2

        挑战
            O(logN)的时间复杂度
"""
import gc
"""
@param: n: An integer
@return: An integer, denote the number of trailing zeros in n!
"""
def trailingZeros(n):
    sum = 1
    for i in range(1, n + 1):
        sum = sum * i
    sum_zero = 0
    for zero in reversed(str(sum)):
        if zero == '0':
            sum_zero = sum_zero + 1
        else:
            break
    print sum_zero

trailingZeros(100000)


