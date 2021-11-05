#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: selenium_demo
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/11/4 1:36
'''

"""
selenium是什么？
    - 基于浏览器自动化的一个模块。
    
selenium使用流程：
    - 环境安装：pip install selenium
    - 下载一个浏览器的驱动程序（谷歌浏览器如下）
        - 下载路径：http://chromedriver.storage.googleapis.com/index.html
        - 驱动程序和浏览器的映射关系：http://blog.csdn.net/huilan_same/article/details/51896672
    - 实例化一个selenium对象
    - 编写基于浏览器自动化的操作代码
"""
from selenium import webdriver
from lxml import  etree
import time

def main():
    # 实例化一个selenium对象
    brow = webdriver.Chrome(executable_path='./chromedriver')
    # 让浏览器对指定的url发起请求
    brow.get('http://scxk.nmpa.gov.cn:81/xk/')

    # page_source获取浏览器当前页面的页面源码数据
    page_text = brow.page_source

    # 用xpath解析企业名称
    tree = etree.HTML(page_text)
    # lst = tree.xpath('//*[@id="gzlist"]/li')
    lst = tree.xpath('//ul[@id="gzlist"]/li')

    for li in lst:
        name = li.xpath('./dl/@title')[0]
        print(name)

    time.sleep(8)  # 因为最新版会自动关闭，需要设置操作才能看到页面
    brow.quit()

if __name__ == '__main__':
    main()