#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

from pprint import pprint

'''
@title: request_bilibili
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-17 23:16
'''
import requests
import re
import json
import subprocess

def run(url):
    # referer 防盗链
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url,headers=headers)
    title = re.findall('<title data-vue-meta="true">(.*?)</title>', response.text)[0]

    play_info = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    json_data = json.loads(play_info)
    # pprint(json_data)
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    # print(json_data)
    print(title)
    # 403 Forbidden 没有访问权限，加防盗链
    print(audio_url)
    print(video_url)

    audio_content = requests.get(url=audio_url,headers=headers).content  # 音频二进制数据
    video_content = requests.get(url=video_url,headers=headers).content  # 视频二进制数据
    with open('video\\' + title +'.mp3',mode='wb') as f:
        f.write(audio_content)
    with open('video\\' + title +'.mp4',mode='wb') as f:
        f.write(video_content)

    command = f'ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental video\\{title}output.mp4'
    subprocess.run(command,shell=True)

def main():
    url = 'https://www.bilibili.com/video/BV1b24y1o7KM/'
    run(url)

if __name__ == '__main__':
    main()