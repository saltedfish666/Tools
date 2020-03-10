#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: 红娘组
@file: test.py
@ide: PyCharm
@time: 2020-02-28 23:52:36
@author: Mr.Li
Copyright © 2020—2020 Mr.Li. All rights reserved.
"""

if __name__ == '__main__':
    choose = [[0 for i in range(6)] for i in range(3)]
    print(choose)
    choose[1][5] = '1'
    print(choose)