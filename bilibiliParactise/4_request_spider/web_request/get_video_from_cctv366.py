#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: get_video_from_cctv366
@projectName: Request URL: https://www.cctv365.co/index.php/user/ajax_ulog/?ac=set&mid=1&id=47&sid=1&nid=23&type=4
@description: TODO
@author ruanshikao
@date 2022-11-02 21:44
'''

import requests
from tqdm import tqdm
from urllib.request import urlopen
import pandas as pd
from lxml import etree
import datetime
import time
import os
import yaml
import re

def download_video(proxies):

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    for episode in range(30,31):
        print('第',episode,'集')
        mp4_url = f'https://www.cctv365.co/vodplay/47-1-{episode}.html'
        print(f'data_url={mp4_url}')

        session = requests.Session()
        # 服务器返回视频数据
        res = session.get(mp4_url,headers=header,proxies=proxies)
        # 网页编码 请求头 服务器的链接信息
        res.encoding = res.apparent_encoding
        print(res.content)
        with open('mp4_info.mp4',mode='wb') as fp:
            fp.write(res.content)


def download_video2(proxies):
    header = {"Content-Type": "application/json;charset=UTF-8", "Referer": "125223222",
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
              }

    # ua伪装
    # header = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    # }
    # 用session对象替代requests发起请求
    session = requests.Session()
    dst = '潜行狙击.mp4'

    for episode in range(30,31):
        print('第',episode,'集')
        data_url = f'https://www.cctv365.co/vodplay/47-1-{episode}.html'
        print(f'data_url={data_url}')
        #获取文件长度
        try:
            file_size = int(urlopen(data_url).info().get('Content-Length',-1))
        except Exception as e:
            print(e)
            print(f"错误，访问url异常: {data_url} ")
            return False

        # 判断文件是否存在

        if os.path.exists(dst):
            # 获取文件大小
            first_byte = os.path.getsize(dst)
        else:
            # 初始大小为0
            first_byte = 0

        if first_byte >= file_size:
            print("文件已经存在，无需下载")
            return file_size

        pbar = tqdm(
            total=file_size, initial=first_byte,
            unit='B', unit_scale=True, desc=data_url.split('/')[-1]
        )

        # 访问url进行下载
        req = requests.get(data_url, headers=header, stream=True)
        try:
            with(open(dst, 'ab')) as f:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        pbar.update(1024)
        except Exception as e:
            print(e)
            return False

        pbar.close()
        return True


def main():
    # 开始时间
    inc_start = datetime.datetime.now()
    try:
        with open('cctv366_config.yaml',encoding='utf-8') as fp:
            config_info = fp.read()
            print('===========配置信息如下===========')
            print(config_info)
            config = yaml.load(config_info,Loader=yaml.FullLoader)
            # proxies = {"HTTP": '39.106.228.34:8080'}
            proxies = {config['prd']['proxies_method']: config['prd']['proxies_ip'] + ':' + config['prd']['proxies_port']}
            print('===========代理是===========proxies=',proxies)

            print('===========开始执行任务，获取数据===========')
            download_video(proxies)

    except Exception as e:
        print('===========执行失败，请检查代理配置文件或者网页是否变更!!!===========',e)
    inc_end = datetime.datetime.now()
    time_diff = inc_end - inc_start
    print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),' 任务耗时： ',time_diff)


if __name__ == '__main__':
    main()