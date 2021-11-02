#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: multiprocessing_dummy_pool
@projectName pythonProject
@description: 采用线程池的方式进行数据采集
@author ruanshikao
@date 2021/11/1 1:14
'''

import time
from multiprocessing.dummy import Pool

name_lst = ['元素1','元素2','元素3']

def get_page(str):
    print('正在操作',str)
    time.sleep(2)
    print('操作完毕',str)

def main():
    start_time = time.time()
    # 实例化Pool对象,参数为线程个数
    pool = Pool(4)
    pool.map(get_page,name_lst)
    end_time = time.time()

    print(end_time - start_time)

if __name__ == '__main__':
    main()