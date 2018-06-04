#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 9. Fizz Buzz 问题.py
    @Software: PyCharm
    @Description:
        描述
            给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

            如果这个数被 3 整除，打印fizz.
            如果这个数被 5 整除，打印buzz.
            如果这个数能同时被3和5整除，打印fizz buzz.
        样例
            比如 n = 15, 返回一个字符串数组：

            [
              "1", "2", "fizz",
              "4", "buzz", "fizz",
              "7", "8", "fizz",
              "buzz", "11", "fizz",
              "13", "14", "fizz buzz"
            ]
        挑战
            Can you do it with only one if statement?
"""
def choiseNum(n):
    list_num = []
    for i in range(0,n):
        i = i+1
        if i%3 == 0 and i%5 !=0:
            list_num.append('fizz')
        elif i%5 == 0 and i%3 !=0:
            list_num.append('buzz')
        elif i%3 ==0 and i%5 == 0:
            list_num.append('fizz buzz')
        else:
            list_num.append(str(i))
    print list_num

choiseNum(15)