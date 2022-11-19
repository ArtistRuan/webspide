#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: test
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-19 13:34
'''



url = input("请输入url\n")

if url is None:
    print("url=None")

if url == '':
    print("url = ''")
print(len(url))
print(f'url={url}')