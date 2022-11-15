#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: urllib_video
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-15 23:19
'''
import urllib.request

url_video = 'https://vd2.bdstatic.com/mda-madjt1deuj2r0n97/sc/cae_h264_nowatermark/1610607509/mda-madjt1deuj2r0n97.mp4?v_from_s=hkapp-haokan-hna&auth_key=1668527421-0-0-5a4bcc2df7afe0911f507098259e12a6&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=1220898465&vid=14194773160992083503&abtest=104959_2-105568_1&klogid=1220898465'


urllib.request.urlretrieve(url_video, 'demo.mp4')
