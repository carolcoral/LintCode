#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 13. Implement strStr().py
    @Software: PyCharm
    @Description:
        描述
            对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

        说明
            在面试中我是否需要实现KMP算法？

            不需要，当这种问题出现在面试中时，面试官很可能只是想要测试一下你的基础应用能力。当然你需要先跟面试官确认清楚要怎么实现这个题。
        样例
            如果 source = "source" 和 target = "target"，返回 -1。

            如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

        挑战
            O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP）
"""
def strStr(source,target):
    source_list = []
    target_list = []
    for sources in source:
        source_list.append(sources)
    for targets in target:
        target_list.append(targets)
    for i in range(len(source)):
        for j in range(len(target)):
            if source_list[i] == target_list[0]:
                k = i
                if source_list[k+j] == target_list[j]:
                    print k
                else:
                    print -1

strStr("abcdabcdefg","bcd")