#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 37. 反转一个3位整数.py
    @Software: PyCharm
    @Description:
        描述
            反转一个只有3位数的整数。

            你可以假设输入一定是一个只有三位数的整数，这个整数大于等于100，小于1000。

            您在真实的面试中是否遇到过这个题？
        样例
            123 反转之后是 321。
            900 反转之后是 9。
"""

def reverse():
    input_num = raw_input("请输入一个三位数的整数:")
    output_num =  ''.join(reversed(str(input_num)))
    print int(output_num)

reverse()