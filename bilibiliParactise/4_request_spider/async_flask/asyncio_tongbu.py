#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: asyncio_tongbu
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/11/4 0:59
'''
import requests
import asyncio
import time

async def get_page(url):
    print('正在下载',url)
    # requests.get是基于同步，必须使用基于异步的网络请求模块进行指定的url的请求发送
    # aiohttp是基于异步的网络请求模块
    response = requests.get(url)
    print('下载完毕',response.text)

def main():
    start = time.time()
    urls = [
        'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
    ]
    tasks = []
    for url in urls:
        c = get_page(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('总耗时： ',end - start)  # 总耗时：  6.075148105621338

if __name__ == '__main__':
    main()