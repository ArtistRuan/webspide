#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: db_opr
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-09-01 20:58
'''

import pymysql

class Operation:
    def __init__(self,data,result=""):
        self.data=data
        self.res=result


    def con_db(self):
        try:
            db = pymysql.connect(host="localhost", user="root", password="123456", database="testdb", charset="utf8")
            return db
        except Exception as e:
            self.result="error"

    def sel_user(self):
        try:
            with self.con_db() as conn:
                # 写sql
                sql = f"select count(1) from users where " \
                      f"username='{self.data['username']}' and " \
                      f"pwd='{self.data['pwd']}' " \
                      f"and tel='{self.data['tel']}'"

                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    self.result = cursor.fetchall()
        except Exception as e:
            self.result="error"