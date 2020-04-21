#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: 红娘组
@file: one_table.py
@ide: PyCharm
@time: 2020-02-29 18:29:54
@author: Mr.Li
Copyright © 2020—2020 Mr.Li. All rights reserved.
"""

import xlrd

if __name__ == '__main__':
    #获得名字和序号的对照字典
    data = xlrd.open_workbook('E:\Project\一些小工具\红娘组资料\互选表16改成35.xlsx')
    sheet1 = data.sheet_by_name('Sheet1')
    dic_name_id = {}
    dic_id_name = {}
    id_list = []
    for i in list(range(sheet1.nrows)):
        dic_id_name[int(sheet1.row_values(i)[1])] = sheet1.row_values(i)[0]
        dic_name_id[sheet1.row_values(i)[0]] = int(sheet1.row_values(i)[1])
        id_list.append(int(sheet1.row_values(i)[1]))
        #print(dic_name_id[sheet1.row_values(i)[0]])
    # 给id_list排序
    for i in range(len(id_list)):
        for j in range(len(id_list)):
            n = 0
            if id_list[i] < id_list[j]:
                n = id_list[i]
                id_list[i] = id_list[j]
                id_list[j] = n
    #获得选择的二维数组
    choose = [[0 for i in range(sheet1.ncols - 2)] for i in range(sheet1.nrows)]
    for i in list(range(sheet1.nrows)):
        j = 0
        for temp in sheet1.row_values(i, 2, sheet1.ncols):
            if isinstance(temp, float):
                choose[i][j] = int(temp)
            else:
                choose[i][j] = temp
            j += 1
        #print(choose[i])
    '''for i in list(range(sheet1.nrows)):
        for j in list(range(5)):
            if choose[i][j]:
                choose[i][j] = int(choose[i][j])'''

    for i in list(range(len(choose))):    #遍历所有人
        name = sheet1.row_values(i)[0]
        id = int(sheet1.row_values(i)[1])
        for j in list(range(sheet1.ncols - 2)):    #遍历男生所选的ID
            select_id = choose[i][j]
            flag = 0
            for k in list(range(i, len(choose))):    #确定男生所选的选择表的位置
                if select_id == int(sheet1.row_values(k)[1]):
                    flag = 1    #列表往下有成功互选的
                    break
            if flag:
                for l in list(range(sheet1.ncols - 2)):    #遍历男生所选女生的选择
                    if id == choose[k][l]:
                        print('恭喜' + name + '（' + str(id) + '）和' + dic_id_name[select_id] + '（' + str(select_id) + '）配对成功')
