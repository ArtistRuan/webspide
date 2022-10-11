#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: create_data_into_excel
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-10-11 20:35
'''

from faker import Faker
from xpinyin import Pinyin
import random
import pandas as pd
import os
import shutil
import sys
import datetime

# 获取传入的参数
if sys.argv[0].isdigit():
    total_rows = sys.argv[0]
else:
    print("参数1传的不是表示创建数据条数的数字，用默认条数total_rows=20")
    total_rows = 20

def create_data():


    data_folder = './data/'
    annex_path = data_folder + 'create_data.xlsx'

    print("造数据的条数=" + str(total_rows))
    # f = Faker()
    f = Faker(locale='zh_CN')
    p = Pinyin()
    values = list()

    # 判断文件在不在
    if os.path.exists(data_folder):
        shutil.rmtree(data_folder)
        # os.rmdir(data_folder)
    os.mkdir(data_folder)

    # 循环获取若干条数据
    for row in range(1,total_rows + 1):
        # 获取名字的音频
        cn_name = f.name()

        en_name_arr = p.get_pinyin(cn_name).split('-')
        # print(s)
        result1 = ''
        for i in range(0, len(en_name_arr)):
            # result1 = result1 + s[i].capitalize()
            result1 = result1 + en_name_arr[i]
        # um上加数字
        r = random.randint(1, 1000)
        if r < 10:
            um = result1 + '00' + str(r)
        elif r < 100:
            um = result1 + '0' + str(r)
        else:
            um = result1 + str(r)

        print(row,cn_name, um)
        values.append((cn_name,um))

    columns = ['姓名','um号']
    data = pd.DataFrame(values,columns=columns)
    data.to_excel(annex_path,index=False)


def main():
    start_time = datetime.datetime.now()

    create_data()


    end_time = datetime.datetime.now()
    print('开始时间=', start_time)
    print('结束时间=', end_time)
    t = end_time - start_time
    print('获取数据执行时长(单位：秒)', t)

if __name__ == '__main__':
    main()