#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: relativeDb
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-04-12 22:16
'''
import pymysql
import os

# 从mysql获取数据
def get_data_from_mysql(sql):
    mysql_host='localhost'
    mysql_port=3306
    mysql_database='student'
    mysql_user='root'
    mysql_passwd='123456'
    conn = pymysql.connect(host=mysql_host,user=mysql_user,passwd=mysql_passwd,port=mysql_port,db=mysql_database)
    # 获取游标
    cursor = conn.cursor()
    # 执行的sql
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print("结果集是：")
        print(result)
        if not os.path.exists('./mysql_data/'):
            os.mkdir('./mysql_data/')
        file_path = './mysql_data/student.txt'
        with open(file_path, 'w') as fp:
            for row in result:
                print("每条数据是：",row)
                line = '\27'.join('%s' %col for col in row)
                print("获取到的拼接内容是：")
                print(line)
                line_with_sep = '{}\n'.format(line)
                fp.write(line_with_sep)
    except Exception as e:
        print(e)


# 主方法
def main():
    sql = 'select * from student'
    get_data_from_mysql(sql)

if __name__ == '__main__':
    main()