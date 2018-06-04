#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 54. String to Integer (atoi).py
    @Software: PyCharm
    @Description:
        描述
            实现atoi这个函数，将一个字符串转换为整数。如果没有合法的整数，返回0。如果整数超出了32位整数的范围，如果是正整数返回INT_MAX(2147483647)，如果是负整数或者INT_MIN(-2147483648)。

        样例
            "10" =>10

            "-1" => -1

            "123123123123123" => 2147483647

            "1.0" => 1
"""
def aToi(str):
    res_str = str.split('.')
    if res_str[1] > "5":
        res_num = int(res_str[0])+1
        ifnum(res_num)
    else:
        ifnum(int(res_str[0]))


def ifnum(intn):
    if intn>2147483647:
        print "INT_MAX(2147483647)"
    elif intn < -2147483648:
        print "INT_MIN(-2147483648)"
    elif intn > -2147483648 and intn <2147483647:
        print intn
    else:
        print 0

aToi("2.0")