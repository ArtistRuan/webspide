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

import random

url = input("请输入url\n")

if url is None:
    print("url=None")

if url == '':
    print("url = ''")
print(len(url))
print(f'url={url}')


default_video = [
        'https://www.bilibili.com/bangumi/play/ep671201',
        'https://www.bilibili.com/video/BV1dZ4y1z7yP/',
        'https://www.bilibili.com/video/BV1M14y1L7oe'
    ]

print(random.choice(default_video))