#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Time    : 2018/6/4
    @Author  : LiuXueWen
    @Site    : 
    @File    : 454. 矩阵面积.py
    @Software: PyCharm
    @Description:
        描述
            实现一个矩阵类Rectangle，包含如下的一些成员变量与函数：

            两个共有的成员变量 width 和 height 分别代表宽度和高度。
            一个构造函数，接受2个参数 width 和 height 来设定矩阵的宽度和高度。
            一个成员函数 getArea，返回这个矩阵的面积。
        样例
            Java:
                Rectangle rec = new Rectangle(3, 4);
                rec.getArea(); // should get 12

            Python:
                rec = Rectangle(3, 4)
                rec.getArea()
"""


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        if self.width < 0 or self.height < 0:
            print "null"
        else:
            area = self.width * self.height
            print area


rec = Rectangle(0, 0)
rec.getArea()
