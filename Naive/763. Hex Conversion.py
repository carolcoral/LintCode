#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 763. Hex Conversion.py
    @Software: PyCharm
    @Description:
        进制转换：输入一个十进制的数n，根据输入的k值转换，例如k=16，n=10，即为把10 转换成16进制的数
        描述
            Given a decimal number n and an integer k, Convert decimal number n to base-k.

            1.0<=n<=2^31-1, 2<=k<=16
            2.Each letter over 9 is indicated in uppercase
        样例
            Example 1:
            Given n = 5, k = 2
            return "101"

            Example 2:
            Given n = 30, k = 16
            return "1E"
"""

def decimalToNBaseByNormal(decimalVar, base):
    """
    :param decimalVar: 任意十进制的数字
    :param base: 需要转换的进制单位
    :return: 转换后的对应进制表示的数字
    """
    tempList = []
    temp = decimalVar
    i = 0
    if temp == 0 :
        print 0
    while (temp > 0):
        ord = temp % base
        # 如果余数大于9，则以字母的形式表示
        if (ord > 9):
            # 把数字转换成字符
            ord = chr(65 + (ord - 10))
        tempList.append(ord)
        temp = int(temp / base)
        i = i + 1
    tempList.reverse()
    binary = ""
    for j in range(len(tempList)):
        binary = binary + str(tempList[j])
    print(binary)

decimalToNBaseByNormal(0,16)