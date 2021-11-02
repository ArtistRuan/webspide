#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: collect_analyze_mysql
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/10/19 23:32
'''

import pymysql
import pandas as pd

#创建数据库
def create_db(host,port,user,passwd,db):
    db = pymysql.connect(host=host,port=port,user=user, password=passwd, db=db)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE db DEFAULT CHARACTER SET utf8")
    db.close()

#创建表单
def create_table():
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS yj_project_info')
    sql = 'CREATE TABLE IF NOT EXISTS yj_project_info(id VARCHAR(255), name VARCHAR(255), age INT, PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()

#insert数据到表单：
#方法1：
def insert(value):
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')
    cursor = db.cursor()
    sql = "INSERT INTO yj_project_info(id, name, age) values(%s, %s, %s)"
    try:
        cursor.execute(sql, value)
        db.commit()
        print('插入数据成功')
    except Exception as e:
        db.rollback()
        print("插入数据失败",e)
    db.close()

def get_data(sql):
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取执行结果
    result = [list(x) for x in result]  # 推导式
    col_result = cursor.description  # 获取查询结果的字段描述
    columns = [x[0] for x in col_result]
    print(columns)
    for res in result:
        print(res)

    cursor.close()
    conn.close()

def insert_mysql(host,port,user,passwd,db,sql):
    pass

def main():
    '''数据库信息'''
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = '123456'
    db = 'yj_houses'
    table_name = 'yj_project_info'
    sql = "select age,name,id from yj_project_info;"
    annex_path = 'G:/desktop/pythonProject/bilibiliParactise/3_database_related/student.xls'

    # insert_mysql(host,port,user,db,sql)
    # create_table()
    value = ['ok',',','zhang慧娴','30']
    insert(value)

    # get_data(sql)

if __name__ == '__main__':
    main()