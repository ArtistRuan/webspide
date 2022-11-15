#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: urllib_pic
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-15 23:12
'''
import urllib.request

url_img = 'https://img0.baidu.com/it/u=1309359181,3567527426&fm=253&fmt=auto&app=138&f=JPEG?w=281&h=499'

urllib.request.urlretrieve(url=url_img, filename='lisa.jpg')