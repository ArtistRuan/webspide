#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: urllib_video_366
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-15 23:38
'''


import urllib.request

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

url_video = 'https://jx.wolongzywcdn.com:65/m3u8.php?url=https://wolongzywcdn.com:65/QHm5N4DU/index.m3u8'

request = urllib.request.Request(url=url_video,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)


# urllib.request.urlretrieve(url=url_video,filename='download/美丽战场第22集.mp4')
