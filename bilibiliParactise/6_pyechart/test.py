#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: test
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-26 22:08
'''
import cpca
import pandas as pd
import numpy as np

def deal_data():
    csv_datas = pd.read_csv('datas.csv',header=None)
    txt_datas = pd.read_csv('datas.txt',sep='\t',header=None)

    # print(f'csv_datas={csv_datas}')
    print(f'txt_datas={txt_datas}')

    # 获取第1和第2列的所有数据，loc参数1表示所有列，[1,2]表示索引是1和2的数据
    data = txt_datas.loc[:,[1,2]]
    print(f'data={data}')

    # 筛选第3行数据不为空的 .notna 或者 .notnull()
    data = data.loc[data[2].notna()]
    # data1 = data.loc[data[2].notnull()]
    print(f'data={data}')
    # print(f'data1={data1}')

    # 将城市映射省份
    # data[1] = data[1].map(get_prov_by_city)

def test_cpca():
    txt_datas = pd.read_csv('datas.txt', sep='\t', header=None)
    data = txt_datas.loc[:,[1]]
    data = data.loc[data[1].notnull()]
    # print(data)
    # print(type(data))
    # print(type(list(data)))

    # 将dataframe转为list，必须先转为数组，再转列表
    city_data = np.array(data)
    city_list = city_data.tolist()

    # for i in city_list:
    #     print('i=',i)

    for city in city_list:
        city_df = cpca.transform(city)
        # print(f'city={city_df}')
        # print(type(city_df))

        # 将df转为列表，取值
        province = np.array(city_df).tolist()[0][0].strip('省').strip('市')
        print(f'province={province}')

    # location_str = ["深圳市宝安区汉庭酒店"]
    # df = cpca.transform(location_str)
    # print(f'df={df}')

def main():
    # deal_data()
    test_cpca()


if __name__ == '__main__':
    main()