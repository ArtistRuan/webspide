#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: 4k_pic
@projectName pythonProject
@description: 爬取 https://pic.netbian.com/4kmeinv/ 上的图片
@author ruanshikao
@date 2021/10/18 2:15
'''


import requests
from lxml import etree
import os

def download_pic():
    url = 'https://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    page_html = requests.get(url=url,headers=headers).content
    # 实例化xpath
    tree = etree.HTML(page_html)
    # 解析数据
    li_list = tree.xpath('//div[@class="slist"]//li')
    # 创建目录来保存数据
    if not os.path.exists('./4k_web_pic'):
        os.mkdir('./4k_web_pic')
    # print(li_list)
    for li in li_list:
        img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'

        # 通用处理中文乱码的解决方案
        # img_name = img_name.encode('iso-8859-1').decode('gbk')  # 如果response.text可能会有乱码,.content一般没有乱码
        # print(img_name,img_path)
        # 对获取到的路径发起请求
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = './4k_web_pic/' + img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功!!!')

    fp.close()

def download_pics():
    # Request URL: https://pic.netbian.com/index_4.html
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    for index_num in range(2,4):
        index_num = str(index_num)
        print('第',index_num,'页数据开始获取：')
        url = 'https://pic.netbian.com/index_' + index_num + '.html'
        page_html = requests.get(url=url, headers=headers).content
        # 实例化xpath
        tree = etree.HTML(page_html)
        # 解析数据
        li_list = tree.xpath('//div[@class="slist"]//li')
        # 创建目录来保存数据
        if not os.path.exists('./4k_web_pic'):
            os.mkdir('./4k_web_pic')
        # print(li_list)
        for li in li_list:
            img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'

            # 通用处理中文乱码的解决方案
            # img_name = img_name.encode('iso-8859-1').decode('gbk')  # 如果response.text可能会有乱码,.content一般没有乱码
            # print(img_name,img_path)
            # 对获取到的路径发起请求
            img_data = requests.get(url=img_src, headers=headers).content
            img_path = './4k_web_pic/' + img_name
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功!!!')

    fp.close()


def main():
    print('第 1 页数据开始获取：')
    download_pic()
    # 第2页开始是下面的方法
    download_pics()

if __name__ == '__main__':
    main()
