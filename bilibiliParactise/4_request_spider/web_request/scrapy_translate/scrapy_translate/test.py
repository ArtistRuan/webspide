#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: test
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-14 23:01
'''

import time
times=time.time()
local_time=time.localtime(times)
local_f_time=time.strftime('%Y%m%d%H%M%S',local_time)

print(local_time)
print(local_f_time)