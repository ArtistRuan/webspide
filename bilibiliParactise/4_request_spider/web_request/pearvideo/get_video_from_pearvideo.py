#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

import re
import requests
import yaml

'''
@title: get_video_from_pearvideo
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-10 21:22
'''

def get_video_from_pearvideo(url):

    with open('pearvideo.yaml',encoding='utf-8') as fp:
        config_data = fp.read()
        config = yaml.load(config_data,Loader=yaml.FullLoader)
        proxies = {config['prd']['proxies_method']:config['prd']['proxies_ip']+':'+config['prd']['proxies_port']}
        print(proxies)


    # 加上请求头，伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    session = requests.Session()

    res = session.get(url=url,headers=headers,proxies=proxies)

    # 正则表达式模块 内建模块 本身自带
    # alt .*? 匹配想要的东西  -> https://video.pearvideo.com/mp4/short/20170818/cont-1135255-10772797-hd.mp4
    # mp4_url = re.findall('<video webkit-playsinline="" playsinline="" x-webkit-airplay="" autoplay="autoplay" src="(.*?)"',res.text)

    # 对于可以在html页面看到的内容，可以直接正则匹配获取 .*?
    mp4_name = re.findall(r'<title>(.*?)</title>',res.text)[0]

    # 专访局座张召忠：谁能忽悠得过我
    mp4_name = mp4_name.split('?')[0]
    print(mp4_name)

    # response = requests.get(mp4_url,headers)
    response = session.get(url='https://video.pearvideo.com/mp4/short/20170818/cont-1135255-10772797-hd.mp4',headers=headers,proxies=proxies)

    # 保存视频
    with open(f'{mp4_name}.mp4',mode='wb') as fp:
        fp.write(response.content)

def run():
    # url
    url = 'https://www.pearvideo.com/video_1135255'
    get_video_from_pearvideo(url)

def main():
    run()

if __name__ == '__main__':
    main()