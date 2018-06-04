#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 479. 数组第二大数.py
    @Software: PyCharm
    @Description:
        描述
            在数组中找到第二大的数

            你可以假定至少有两个数字
        样例
            给出 [1, 3, 2, 4], 返回 3.

            给出 [1, 2], 返回 1.
"""
def secondNum(head):
    head = sorted(head)
    print head[-2]

secondNum([1, 3, 2, 4])