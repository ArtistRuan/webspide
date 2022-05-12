#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: create_data_by_fake
@projectName pythonProject
@description: when you need some data,create by fake
@author ruanshikao
@date 2022-05-12 22:45
'''


from faker import Faker
from faker.providers import BaseProvider  # 用于创建自定义的Provider生成数据

# 创建自定义Provider
class CustomProvider(BaseProvider):
    def customize_type(self):
        return 'test_Faker_customize_type'

def create_datas():
    f = Faker(locale='zh_CN')
    for i in range(1,11):
        print(i,f.name(),f.phone_number(),f.address())


def main():
    create_datas()

    # 添加Provider
    fake = Faker()
    fake.add_provider(CustomProvider)
    print('打印自定义创建的内容：',fake.customize_type())

if __name__ == '__main__':
    main()