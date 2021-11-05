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

import aiohttp
import requests
import asyncio
import time

async def get_page(url):
    # 使用异步的session发起请求
    async with aiohttp.ClientSession() as session:
        # 与aiohttp与requests发起请求的方法一样，都是get()、post()
        # headers进行ua伪装，params/data适用参数的携带，代理的设置不一样，是proxy='http://ip:port'
        async with await session.get(url) as response:
            # 不同于requests方式，这里只有如下3中获取数据方式
            # text() 返回字符串形式的响应数据
            # read() 返回二进制形式的响应数据
            # json() 返回的是json对象
            # 注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)

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
    print('总耗时： ',end - start)  # 总耗时：  2.0403761863708496

if __name__ == '__main__':
    main()