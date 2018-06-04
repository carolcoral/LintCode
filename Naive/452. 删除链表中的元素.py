#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 452. 删除链表中的元素.py
    @Software: PyCharm
    @Description:
        描述
            删除链表中等于给定值val的所有节点。
        样例
            给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。
"""
def dellist(head,val):
    if head == "null" or head == '' or head == None:
        print "null"
    else:
        headlist = ''.join(head.split("->"))
        lenHead = len(headlist)
        for lenstr in range(0,lenHead-1):
            # print lenstr
            headlist = head.split("->")
            if headlist[lenstr] == str(val):
                head.replace("->"+str(val),'')
            else:
                print ''.join(headlist[lenstr].strip(' ')),

dellist("1->2->3->3->4->5->3",3)