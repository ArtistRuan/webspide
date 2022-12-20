#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

from pprint import pprint
import os
import time
import requests
import re
import json
import subprocess
import random

'''
@title: request_bilibili
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-17 23:16
'''

def correct_title(title):
    """定义特殊字符是哪些"""
    error_set = ['/', '\\', ':', '*', '?', '"', '|', '<', '>', ' ']
    for c in title:
        if c in error_set:
            title = title.replace(c, '')

    return title

def run(url):
    # referer 防盗链
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            title = re.findall('<title data-vue-meta="true">(.*?)</title>', response.text)[0]

            """纠正含有特殊字符的文件名"""
            title = correct_title(title)

            play_info = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
            json_data = json.loads(play_info)
            pprint(json_data)
            audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
            video_url = json_data['data']['dash']['video'][0]['baseUrl']
            # print(json_data)
            print(title)
            # 403 Forbidden 没有访问权限，加防盗链
            print(audio_url)
            print(video_url)

            audio_content = requests.get(url=audio_url, headers=headers).content  # 音频二进制数据
            video_content = requests.get(url=video_url, headers=headers).content  # 视频二进制数据

            # 创建专门的video目录存放视频
            if not os.path.exists('video'):
                os.mkdir('video')

            # 保存视频文件
            with open('video\\' + title + '.mp3', mode='wb') as f:
                f.write(audio_content)
            with open('video\\' + title + '.mp4', mode='wb') as f:
                f.write(video_content)

            nt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            command = f'ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental video\\{title}_{nt}output.mp4'
            subprocess.run(command, shell=True)
        else:
            print(f'输入的网址(url={url})无效，程序退出!!!')
            exit(0)
    except Exception as e:
        print(e)


def main(default_video):

    print('默认视频链接是:')
    for i in range(1,len(default_video) + 1):
        print(f'第{i}个是：{default_video[i-1]}')
    print('\n')
    print('>>>>>>注意：如果想下载随机默认视频，请直接按<<回车ENTER>>')
    input_url = input('>>>>>>注意：如果下载指定B站视频，请输入有效视频网址：\n')

    if input_url == '':
       input_url = random.choice(default_video)

    run(input_url)

if __name__ == '__main__':
    # 默认视频url清单
    default_video = [
        # 《漫步人生路》
        'https://www.bilibili.com/bangumi/play/ep671201',
        # 《简单爱》
        'https://www.bilibili.com/video/BV1dZ4y1z7yP',
        # 《稻香》
        'https://www.bilibili.com/video/BV1WS4y1F7ky',
        # 《爱的飞行日记》
        'https://www.bilibili.com/video/BV18F411x7f9',
        # 《画离弦》
        'https://www.bilibili.com/video/BV1Mh411t7gT',
        # 《谪仙》
        'https://www.bilibili.com/video/BV1fv4y1m7dM',
        # 《关山酒》
        'https://www.bilibili.com/video/BV1WG4y1n7j5'
    ]

    # 执行程序
    main(default_video)