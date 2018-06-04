#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 131. The Skyline Problem.py
    @Software: PyCharm
    @Description:
        描述
            水平面上有 N 座大楼，每座大楼都是矩阵的形状，可以用一个三元组表示 (start, end, height)，分别代表其在x轴上的起点，终点和高度。大楼之间从远处看可能会重叠，求出 N 座大楼的外轮廓线。

            外轮廓线的表示方法为若干三元组，每个三元组包含三个数字 (start, end, height)，代表这段轮廓的起始位置，终止位置和高度。

            请注意合并同样高度的相邻轮廓，不同的轮廓线在x轴上不能有重叠。

        样例
            给出三座大楼：

            [
              [1, 3, 3],
              [2, 4, 4],
              [5, 6, 1]
            ]
            外轮廓线为：

            [
              [1, 2, 3],
              [2, 4, 4],
              [5, 6, 1]
            ]
"""