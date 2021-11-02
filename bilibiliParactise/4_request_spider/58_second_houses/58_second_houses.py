#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: 58_second_houses
@projectName pythonProject
@description: 爬取58二手房的房源名称
@author ruanshikao
@date 2021/10/18 1:21
'''

import requests
from lxml import etree

def get_houses_info():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    url = 'https://sz.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text
    # 实例化xpath对象
    # tree = etree.xpath(page_text)  # 这个方法适合本地的html文档
    tree = etree.HTML(page_text)
    # 解析数据
    section_list = tree.xpath('//section[@class="list"]/div')
    # print(section_list)
    # 将数据保存到文档或者列表中
    fp = open('58houses.txt','w',encoding='utf-8')
    for div in section_list:
        title = div.xpath('.//h3/@title')[0]
        # print(title)
        fp.write(title+'\n')
    fp.close()


def main():
    get_houses_info()

if __name__ == '__main__':
    main()