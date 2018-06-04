#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 8. 旋转字符串.py
    @Software: PyCharm
    @Description:
        描述
            给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

        样例
            对于字符串 "abcdefg".

            offset=0 => "abcdefg"
            offset=1 => "gabcdef"
            offset=2 => "fgabcde"
            offset=3 => "efgabcd"
        挑战
            在数组上原地旋转，使用O(1)的额外空间
"""
def offsetStr(str,offset):
    list_num = []
    str_list = []
    for istr in str:
        list_num.append(istr)
    if offset > 0:
        offset = offset%len(str)
        for i in range(1,offset+1):
            str_list.append(list_num[-i])
        for res in str_list:
            list_num.remove(res)
        rever = reversed(str_list)
        list_rever = list(rever)
        list_rever.extend(list_num)
        res = ''
        for i in range(len(list_rever)):
            res = res+ list_rever[i]
        print res


offsetStr("abcdefg",3)