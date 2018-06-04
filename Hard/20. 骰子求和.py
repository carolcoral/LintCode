#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 20. 骰子求和.py
    @Software: PyCharm
    @Description:
        描述
            扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。

        样例
            给定 n = 1，返回 [ [1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]]。
"""

def Probability(n):
    max_num = 6*n
    res = 1/float(max_num)
    pro = ("%.2f" % res)
    res_list = []
    for i in range(n,max_num+1):
        pro_res = [i,pro]
        res_list.append(pro_res)
    print res_list

Probability(2)
