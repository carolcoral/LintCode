#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 484. 交换数组两个元素.py
    @Software: PyCharm
    @Description:
        描述
            给你一个数组和两个索引，交换下标为这两个索引的数字
        样例
            给出 [1,2,3,4] index1 = 2, index2 = 3. 交换之后变成 [1,2,4,3]
"""
def exchangeNum(head,index1,index2):
    """
    :param head: 目标数组
    :param index1: 需要交换的第一个下标
    :param index2: 需要交换的第二个下标
    :return: 返回交换后的新数组
    """
    exchangenum1 = head[index1]
    exchangenum2 = head[index2]
    head[index1] = exchangenum2
    head[index2] = exchangenum1
    print head

exchangeNum([1,2,3,4],1,2)