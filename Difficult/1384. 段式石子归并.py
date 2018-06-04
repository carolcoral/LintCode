#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 1384. 段式石子归并.py
    @Software: PyCharm
    @Description:
        描述
            有一个石子归并的游戏。最开始的时候，有n堆石子排成一列，目标是要将所有的石子合并成一堆。合并规则如下：

            每一次可以合并连续x堆石子，left <= x <= right
            每次合并的代价为所合并的x堆石子的重量之和
            求出最小的合并代价，如果无法完成合并返回0。

            1 <= n <= 100，2 <= left <= right <= n
            1 <= weight[i] <= 1000

        样例
            给出 n = 4, left = 3, right = 3, weight = [1,2,3,4] ,返回 0。
            解释：
            无法完成合并

            给出 n = 3, left = 2, right = 3 , weight = [1,2,3], 返回 6。
            解释：
            将1,2,3合并即可，合并代价为1+2+3=6。
"""