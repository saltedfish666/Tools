#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: 红娘组
@file: work.py
@ide: PyCharm
@time: 2020-02-28 22:36:29
@author: Mr.Li
Copyright © 2020—2020 Mr.Li. All rights reserved.
"""

import xlrd

def get_list(list_name):
    data = xlrd.open_workbook(list_name)
    sheet1 = data.sheet_by_name('Sheet1')
    dic_name_id = {}
    dic_id_name = {}
    for i in list(range(1, sheet1.nrows)):
        dic_name_id[sheet1.row_values(i)[1]] = int(sheet1.row_values(i)[0])
        dic_id_name[int(sheet1.row_values(i)[0])] = sheet1.row_values(i)[1]
    return dic_name_id, dic_id_name

def get_choose(choose_name):
    data = xlrd.open_workbook(choose_name)
    sheet1 = data.sheet_by_name('Sheet1')
    choose = [[0 for i in range(6)] for i in range(sheet1.nrows)]    #行数和列数已+1，按实际的坐标
    for i in list(range(1, sheet1.nrows)):
        j = 0
        for temp in sheet1.row_values(i):
            if isinstance(temp, float):
                choose[i][j] = int(temp)
            else:
                choose[i][j] = temp
            j += 1
    return choose

'''例如想要男生选女生的数据，则运行select(男生，女生)'''
#def select(c_a, c_b):

if __name__ == '__main__':
    dict_boy_name_id, dict_boy_id_name = get_list('男生列表.xlsx')
    dict_girl_name_id, dict_girl_id_name = get_list('女生列表.xlsx')
    choose_boy = get_choose('男生选择.xlsx')
    choose_girl = get_choose('女生选择.xlsx')
    for i in list(range(1, len(choose_boy))):    #遍历男生
        name_boy = choose_boy[i][0]
        id_boy = dict_boy_name_id[name_boy]
        for j in list(range(1, 6)):    #遍历男生所选女生
            boy_select_girl_id = choose_boy[i][j]
            boy_select_girl_name = dict_girl_id_name[boy_select_girl_id]
            for k in list(range(1, len(choose_girl))):    #确定男生所选女生在女生选择表的位置
                if boy_select_girl_name == choose_girl[k][0]:
                    break
            for l in list(range(1, 6)):    #遍历男生所选女生的选择
                if id_boy == choose_girl[k][l]:
                    print('恭喜' + name_boy + '和' + boy_select_girl_name + '配对成功')