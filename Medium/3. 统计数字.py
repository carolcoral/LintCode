#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 3. 统计数字.py
    @Software: PyCharm
    @Description:
        描述
            计算数字k在0到n中的出现的次数，k可能是0~9的一个值

        样例
            例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)
"""
def countNum(n,k):
    list_num = []
    sum = 0
    for i in range(n+1):
        list_num.append(str(i))
    res_num =  ''.join(list_num)
    for j in res_num:
        if j == str(k):
            sum = sum+1
    print sum

countNum(12,1)