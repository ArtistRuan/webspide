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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    for episode in range(30,31):
        print('第',episode,'集')
        # // *[ @ id = "mo-play-iframe"]
        # /html/body/div[3]/div/div[1]/div[1]/iframe
        home_url = f'https://www.cctv365.co/vodplay/47-1-{episode}.html'
        print(f'home_url={home_url}')

        session = requests.Session()
        # 服务器返回视频数据
        home_res = session.get(home_url,headers=headers,proxies=proxies)
        # 对响应数据进行编码，避免乱码
        home_res.encoding = 'utf-8'
        # 网页编码 请求头 服务器的链接信息
        # res_page.encoding = res_page.apparent_encoding
        # print(res)
        page_etree = etree.HTML(home_res.text)
        # mp4_url = page_etree.xpath('//*[@id="mo-play-iframe"]/@src')
        # mp4_url = 'https://jx.xhswglobal.com/dplayer/?url=https://new.qqaku.com/20220219/9WK5lypO/index.m3u8'
        mp4_url = page_etree.xpath('/html/body/div[3]/div/div[1]/div[1]/iframe/@src')
        # mp4_url = page_etree.xpath('//iframe[@class="mo-play-iframe"]/@src')

        print(f'mp4_url={mp4_url}')
        mp4_res = session.get(url=r'https://jx.xhswglobal.com/dplayer/?url=https://new.qqaku.com/20220219/9WK5lypO/index.m3u8',
                              headers=headers, proxies=proxies)

        with open('潜行狙击第30集.mp4',mode='wb') as fp:
            fp.write(mp4_res.content)


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

def get_proxies_config():

    try:
        with open('cctv366_config.yaml', encoding='utf-8') as fp:
            config_info = fp.read()
            print('===========打印配置信息===========')
            print(config_info)
            config = yaml.load(config_info,Loader=yaml.FullLoader)
            # proxies = {"HTTP": '39.106.228.34:8080'}
            proxies = {config['prd']['proxies_method']: config['prd']['proxies_ip'] + ':' + config['prd']['proxies_port']}
            print('===========打印代理信息============')
            print(f'proxies={proxies}')

    except Exception as e:
        print('===========获取配置文件中代理信息时发生异常!!!===========')
        print(e)

    return proxies

def get_target_response(url,proxies):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    session = requests.Session()
    print(f'请求的url={url}')

    res = session.get(url, headers=header, proxies=proxies)
    # 对响应数据进行编码，避免乱码
    res.encoding = 'utf-8'
    # 网页编码 请求头 服务器的链接信息
    res.encoding = res.apparent_encoding

    return res

def parse_serve_response(res,href_path,name_path,src_path):
    tree = etree.HTML(res.text)

    try:
        content_href = tree.xpath(href_path)
    except Exception as e:
        print(e)
        print('没有解析到对象href，对象href为空')
        content_href = href_path

    try:
        content_name = tree.xpath(name_path)
    except Exception as e:
        print(e)
        print('没有解析到对象名称，对象名称为空')
        content_name = 'defaul_name'

    try:
        content_src = tree.xpath(src_path)
    except Exception as e:
        print(e)
        print('没有解析到对象src，对象src为空')
        content_src = 'defaul_src'

    return content_href,content_name,content_src

def parse_local_html(res):

    tree = etree.parse(res)

def download_resource(url, proxies,out_path):
    res = get_target_response(url, proxies)

    with open(out_path,'wb') as fp:
        fp.write(res.content)

    print('下载完成')

def main():
    # 开始时间
    inc_start = datetime.datetime.now()

    name_path = '//*[@id="main"]/div[3]/ul/li[7]/a/img/@alt'
    href_path = 'https://pic.netbian.com'
    src_path = '//*[@id="main"]/div[3]/ul/li[7]/a/img/@src'

    """调用方法，获取代理配置"""
    proxies = get_proxies_config()

    # url = f'https://www.cctv365.co/vodplay/47-1-{episode}.html'
    url = f'https://pic.netbian.com/4kmeinv/index_3.html'

    """调用方法，获取响应html"""
    res = get_target_response(url=url,proxies=proxies)

    """调用方法，解析出爬取内容的名称和src"""
    content_href,content_name,content_src = parse_serve_response(res=res,href_path=href_path,name_path=name_path,src_path=src_path)
    print(f'content_name={content_name}')
    print(f'content_href={content_href}')
    print(f'content_src={content_src[0]}')

    """创建下载目录位置"""
    if not os.path.exists('download'):
        os.mkdir('download')

    try:
        type = content_src[0].split('.')[1]
    except Exception as e:
        print(e)
        type = 'jpg'
    """调用方法，进行目标内容下载"""
    download_resource(url=f'{content_href}{content_src[0]}', proxies=proxies, out_path=f'download/{content_name}.{type}')


    # download_video(proxies)

    inc_end = datetime.datetime.now()
    time_diff = inc_end - inc_start
    print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),' 任务耗时： ',time_diff)

if __name__ == '__main__':

    # main()
    download_video(get_proxies_config())