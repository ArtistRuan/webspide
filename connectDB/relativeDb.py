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
import os,sys

# 全局定义参数
try:
    db_host = sys.argv[1]
    db_port = int(sys.argv[2])
    db_name = sys.argv[3]
    db_user = sys.argv[4]
    db_passwd = sys.argv[5]
except Exception as e:
    print(e)
    db_host = 'localhost'
    db_port = 3306
    db_name = 'student'
    db_user = 'root'
    db_passwd = '123456'

# 从mysql获取数据
def get_data_from_mysql(sql):

    conn = pymysql.connect(host=db_host,user=db_user,passwd=db_passwd,port=db_port,db=db_name)
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
        with open(file_path, 'w',encoding='utf8') as fp:
            for row in result:
                print("每条数据是：",row)
                # line = '\27'.join('%s' %col for col in row)
                # 列表生成式中处理空数据（None）
                line = '\27'.join('%s' %col if col is not None else '\\N' for col in row)
                print("获取到的拼接内容是：")
                print(line)
                line_with_sep = '{}\n'.format(line)
                fp.write(line_with_sep)
    except Exception as e:
        print(e)


# 主方法
def main():
    try:
        sql = sys.argv[6]
    except Exception as e:
        # sql = 'select age,name,id,birthday from student'
        sql = 'select age,name from student group by age,name'
    # 执行程序
    get_data_from_mysql(sql)

if __name__ == '__main__':
    main()