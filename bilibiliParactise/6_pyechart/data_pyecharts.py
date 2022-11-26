#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: data_pyechart
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-26 20:24
'''
# 导入地图
from pyecharts.charts import Map, Page
# 导入地图配置信息
from pyecharts import options as opt
import pandas as pd
import numpy as np
import cpca

def process_data():

    txt_datas = pd.read_csv('datas.txt',sep='\t',header=None)
    # print(f'txt_datas={txt_datas}')

    # 获取第1和第2列的所有数据，loc参数1表示所有列，[1,2]表示索引是1和2的数据
    data_df = txt_datas.loc[:,[1,2]]
    # print(f'data={data_df}')

    # 筛选第2和3行数据不为空的 .notna 或者 .notnull()
    # 过滤空字符
    data_df = data_df.loc[data_df[2].notna()]
    data_df = data_df.loc[data_df[1].notna()]
    data_df = data_df[data_df[2] != "''"]
    print(f'原始城市data_df=\n{data_df}')
    """
    原始城市data_df=
        1      2
    0  北京  20000
    1  深圳  18000
    2  广州  17000
    3  深圳  20000
    4  深圳  15000
    5  成都  16000
    """

    # 将城市映射省份
    data_df[1] = data_df[1].map(get_prov_by_city)
    data_df[2] = data_df[2].map(get_float_data)
    print('城市名映射省份后的df=\n',data_df)

    """
    城市名映射省份后的df=
        1      2
    0  北京  20000
    1  广东  18000
    2  广东  17000
    3  广东  20000
    4  广东  15000
    5  四川  16000
    """

    """
         1        2
    0  北京  20000.0
    1  广东  18000.0
    2  广东  17000.0
    3  广东  20000.0
    4  广东  15000.0
    5  四川  16000.0
    """

    # 按第一列数据分组求每组平均数，生成df
    avg_data = data_df.groupby(1).mean()
    print(f'分组求平均后的df=\n{avg_data}')
    """
              2
    1          
    北京  20000.0
    四川  16000.0
    广东  17500.0
    """

    # 为了方便展示，将数据df重新索引
    avg_data = avg_data.reset_index()
    print(f'重新索引后的df=\n{avg_data}')
    """
        1        2
    0  北京  20000.0
    1  四川  16000.0
    2  广东  17500.0
    """

    # 拿到重置索引后对应的省份数据
    province_salary_list = avg_data.values.tolist()
    print(f'province_salary_list={province_salary_list}')
    # province_salary_list=[['北京', 20000.0], ['四川', 16000.0], ['广东', 17500.0]]

    return avg_data,province_salary_list

def show_by_echarts(avg_data,province_salary_list):
    # 创建页面
    p = Page()
    # 创建地图
    m = Map()
    # 地图的标题
    m.add("薪资",province_salary_list)
    # 设置全局配置
    """
    visualmap_opts:设置图例，滑块（最大最小值）
    """
    m.set_global_opts(visualmap_opts=opt.VisualMapOpts(max_=max(avg_data[2]),min_=min(avg_data[2])))
    # 设置是否显示每个省份信息
    m.set_series_opts(label_opts=opt.LabelOpts(is_show=True))
    # 将配置加到地图里面
    p.add(m)
    # 输出页面 html
    p.render("show.html")

def get_prov_by_city(city_str):
    # 定义列表
    cities_list = list()
    cities_list.append(city_str)

    # for city in cities_list:
    #     print(f'city={city}')

    new_city_df = cpca.transform(cities_list)
    # province = np.array(new_city_df).tolist()[0][0]
    province = np.array(new_city_df).tolist()[0][0].strip('省').strip('市')
    return province

def get_float_data(int_data):
    # 将df中整数数据整理为浮点数据，用于合并平均数
    return float(int_data)

def run():

    avg_data,province_salary_list = process_data()
    print(max(avg_data[2]),min(avg_data[2]))
    show_by_echarts(avg_data,province_salary_list)

def main():

    run()

if __name__ == '__main__':
    main()