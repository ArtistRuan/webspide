#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: faker_data_into_db
@projectName pythonProject
@description: faker造批量数据写入数据库
@author ruanshikao
@date 2023-01-14 15:28
'''

"""
-- mysql数据库建表:
create table csr_info(
id int not null auto_increment primary key comment '主键id',
name varchar(50) comment '姓名',
phone_number varchar(50) comment '电话',
address varchar(512) comment '地址',
commpany varchar(512) comment '公司名',
company_email varchar(50) comment '公司邮箱',
update_date timestamp default current_timestamp comment '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- postgresql数据库建表：
CREATE TABLE if not exists public.csr_info
(
  id serial NOT NULL,
  name varchar(50),
	phone_number varchar(50),
	address varchar(512),
	company varchar(512),
	company_email varchar(50),
	update_date timestamp default current_timestamp,
  CONSTRAINT student2_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.csr_info OWNER TO postgres;
COMMENT ON TABLE public.csr_info IS '客户信息表';
COMMENT ON COLUMN public.csr_info.id IS '主键id';
COMMENT ON COLUMN public.csr_info.name IS '姓名';
COMMENT ON COLUMN public.csr_info.phone_number IS '电话';
COMMENT ON COLUMN public.csr_info.address IS '地址';
COMMENT ON COLUMN public.csr_info.company IS '公司名';
COMMENT ON COLUMN public.csr_info.company_email IS '公司邮箱';
COMMENT ON COLUMN public.csr_info.update_date IS '更新时间';
"""

from faker import Faker
from faker.providers import BaseProvider  # 用于创建自定义的Provider生成数据
import pymysql
import psycopg2


# 创建自定义Provider
class CustomProvider(BaseProvider):
    """faker创建自定义Provider"""
    def customize_type(self):
        return 'test_Faker_customize_type'

def create_datas(faker_data_quantity):
    """造数据"""
    lst = list()
    f = Faker(locale='zh_CN')
    for i in range(1, faker_data_quantity + 1):
        name = f.name()
        phone_number = f.phone_number()
        address = f.address()
        company = f.company()
        company_email = f.company_email()
        if i < 11:
            print(i,name,phone_number,address,company,company_email)
        lst.append((i,name,phone_number,address,company,company_email))

    return lst

def connect_mysql_db(host, port, user, passwd, db):
    """连接到mysql数据库"""
    try:
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)  # 连接mysql
        cursor = conn.cursor()  # 创建游标
        # cursor.execute(sql)  # 执行sql语句
        # result = cursor.fetchall()  # 获取执行结果
        print("数据库连接成功")
        return cursor,conn

    except Exception as e:
        print("数据库连接失败")
        print(e)

def connect_postgresql_db(host,port,user,passwd,db):
    """连接到postgresql数据库"""
    try:

        # conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")
        # print("Opened database successfully")

        conn = psycopg2.connect(host=host, port=port, user=user, password=passwd, database=db)  # 连接postgresql
        cursor = conn.cursor()  # 创建游标
        # cursor.execute(sql)  # 执行sql语句
        # result = cursor.fetchall()  # 获取执行结果
        print("数据库连接成功")
        return cursor,conn

    except Exception as e:
        print("数据库连接失败")
        print(e)

def insert_db(cursor,conn,lst,sql):
    """将列表数据插入数据库"""
    cursor.executemany(sql,lst)
    conn.commit()


def main():
    """主程序"""

    flag = True
    while flag:
        print("请输入数据要插入的数据库类型表示的数字：")
        print("postgresql请输入*** 1 ***")
        print("mysql请输入*** 2 ***")
        db_type = input()
        print("请输入造数据的条数:")
        faker_data_quantity = input()

        if faker_data_quantity.isdigit() and (db_type == "1" or db_type == "2"):
            flag = False

    """
    造数据条数:faker_data_quantity
    插入数据库sql:sql
    """
    # faker_data_quantity = 100000
    sql = "insert into csr_info(id,name,phone_number,address,company,company_email) values (%s,%s,%s,%s,%s,%s)"

    """造数据程序"""
    lst = create_datas(int(faker_data_quantity))

    """连接数据库"""
    if db_type == "1":
        """postgresql数据库信息"""
        host = "192.168.175.128"
        port = 5432
        user = "postgres"
        passwd = "123456"
        db = "flink"
        cursor, conn = connect_postgresql_db(host, port, user, passwd, db)
    elif db_type == "2":
        """mysql数据库信息"""
        host = "192.168.175.128"
        port = 3306
        user = "root"
        passwd = "123456"
        db = "test"
        cursor, conn = connect_mysql_db(host, port, user, passwd, db)
    else:
        print("暂无开发的数据库，请联系主任继续开发逻辑")
        exit(-1)


    """将lst数据批量插入数据库"""
    insert_db(cursor=cursor,conn=conn,lst=lst,sql=sql)
    print(f"成功插入 {faker_data_quantity} 条数据")

    # 查看数据情况
    # for i in lst:
    #     print(i)

    # 添加Provider
    fake = Faker()
    fake.add_provider(CustomProvider)
    print('打印自定义创建的内容：', fake.customize_type())

    print("Faker库的内容：", dir(fake))


if __name__ == '__main__':
    main()
