#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: 红娘组
@file: be_choose.py
@ide: PyCharm
@time: 2020-02-29 20:23:31
@author: Mr.Li
Copyright © 2020—2020 Mr.Li. All rights reserved.
"""

import xlrd

if __name__ == '__main__':
    # 获得名字和序号的对照字典
    data = xlrd.open_workbook('选择表.xlsx')
    sheet1 = data.sheet_by_name('Sheet1')
    dic_name_id = {}
    dic_id_name = {}
    id_list = []
    for i in list(range(1, sheet1.nrows)):
        dic_id_name[int(sheet1.row_values(i)[1])] = sheet1.row_values(i)[0]
        dic_name_id[sheet1.row_values(i)[0]] = int(sheet1.row_values(i)[1])
        id_list.append(int(sheet1.row_values(i)[1]))
    #给id_list排序
    for i in range(len(id_list)):
        for j in range(len(id_list)):
            n = 0
            if id_list[i] < id_list[j]:
                n = id_list[i]
                id_list[i] = id_list[j]
                id_list[j] = n
    #print(id_list)
    # 获得选择的二维数组
    choose = [[0 for i in range(10)] for i in range(sheet1.nrows)]  # 行数和列数已+1，按实际的坐标
    for i in list(range(0, sheet1.nrows)):
        j = 0
        for temp in sheet1.row_values(i, 2, 12):
            if isinstance(temp, float):
                choose[i][j] = int(temp)
            else:
                choose[i][j] = temp
            j += 1
    for i in list(range(1, sheet1.nrows)):
        for j in list(range(10)):
            if choose[i][j]:
                choose[i][j] = int(choose[i][j])
    #print(choose)    #有包括第一行心动1心动2

    for id in id_list:    #遍历所有人
        name = dic_id_name[id]
        print('选了' + name + '（' + str(id) + '）的人：')
        for j in list(range(1, len(choose))):    #遍历全表，找选了TA的人
            for k in list(range(10)):    #遍历每个人的选择
                if id == choose[j][k]:
                    print(sheet1.row_values(j)[0] + '(' + str(sheet1.row_values(j)[1]) + ')', end=',')
                    break
        print('\n')