#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: data_from_file_to_mysql
@projectName pythonProject
@description: 将文本数据写入数据库，数据量为485000多
                程序执行日志：
                参数获取异常： list index out of range
                执行时间： 0.02740856909751892
@author ruanshikao
@date 2022-04-28 1:04
'''

import pymysql
import sys
import time

# 全局定义参数
try:
    db_host = sys.argv[1]
    db_port = int(sys.argv[2])
    db_name = sys.argv[3]
    db_user = sys.argv[4]
    db_passwd = sys.argv[5]
except Exception as e:
    print("参数获取异常：",e)
    # db_host = 'localhost'  # 写入本地
    db_host = '192.168.174.100'  # 写到虚拟机node1
    db_port = 3306
    db_name = 'flink'
    db_user = 'root'
    db_passwd = '123456'

def data_etl():
    conn = pymysql.connect(host=db_host, user=db_user, passwd=db_passwd, port=db_port, db=db_name)
    # 获取游标
    cursor = conn.cursor()
    # 执行的sql
    sql = "insert into webview_from_py values(%s,%s,%s,%s,%s)"

    each_row_list = list()
    values_list = list()

    with open('UserBehavior.csv','r',encoding='utf-8') as fp:
        # lines = fp.readlines()
        # for line in lines:
        for line in fp.readlines():
            web_id = line.split(",")[0]
            city_id = line.split(",")[1]
            user_id = line.split(",")[2]
            action_name = line.split(",")[3]
            action_time = line.split(",")[4]
            values_list.append((web_id,city_id,user_id,action_name,action_time))

    try:
        cursor.executemany(sql, values_list)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("发生异常：",e)

    conn.close()
    cursor.close()

def main():
    start_time = time.time()
    data_etl()
    end_time = time.time()
    execute_time = (end_time - start_time) / 1000
    print("执行时间：",execute_time)

if __name__ == '__main__':
    main()
