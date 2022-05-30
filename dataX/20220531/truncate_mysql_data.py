#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: truncate_mysql_data
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-05-31 0:15
'''

import pymysql
import sys

# 全局定义参数
try:
    db_host = sys.argv[1]
    db_port = int(sys.argv[2])
    db_name = sys.argv[3]
    db_user = sys.argv[4]
    db_passwd = sys.argv[5]
except Exception as e:
    print("参数获取异常：",e)
    db_host = '192.168.174.100'
    db_port = 3306
    db_name = 'datax'
    db_user = 'root'
    db_passwd = '123456'

def truncate_mysql_data():
    try:
        conn = pymysql.connect(host=db_host, user=db_user, passwd=db_passwd, port=db_port, db=db_name)
        print("数据库连接成功!!!")
    except Exception as e:
        print("数据库连接失败")
        print(e)
    # 获取游标
    cursor = conn.cursor()
    sql = "truncate table hive_partition_source"
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print("执行清空表操作失败")
        print(e)

    cursor.close()
    conn.close()

def main():
    truncate_mysql_data()

if __name__ == '__main__':
    main()