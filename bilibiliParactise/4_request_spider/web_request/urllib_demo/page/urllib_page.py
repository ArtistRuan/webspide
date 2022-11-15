#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: urllib_page
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-15 23:05
'''

import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

"""
2个参数：
参数1：url，表示下载的url
参数2：filename，表示文件名
"""
urllib.request.urlretrieve(url_page, 'baidu.html')