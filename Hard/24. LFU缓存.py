#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 24. LFU缓存.py
    @Software: PyCharm
    @Description:
        描述
            LFU是一个著名的缓存算法
            实现LFU中的set 和 get
            get(key)：返回指定key对应的value，如果指定key在cache中不存在，返回-1
            put(key, value)：设置指定key的value，如果key不存在，则插入该key-value对。如果cache空间已满，则将最少使用的key-value对移除，如果存在多个key-value对的使用次数相同，则将上次访问时间最早的key-value对移除。

        样例
            capacity = 3

            set(2,2)
            set(1,1)
            get(2)
            >> 2
            get(1)
            >> 1
            get(2)
            >> 2
            set(3,3)
            set(4,4)
            get(3)
            >> -1
            get(2)
            >> 2
            get(1)
            >> 1
            get(4)
            >> 4
"""