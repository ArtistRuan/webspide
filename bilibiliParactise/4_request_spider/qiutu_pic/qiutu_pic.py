#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: qiutu_pic
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/10/17 13:48
'''

import requests
import re
import os

def get_pic():
    # 创建保存图片的目录
    folder_name = './homepage_pic'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    # url = 'https://www.qiushibaike.com/imgrank/'
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    # 分页爬取，https://www.qiushibaike.com/imgrank/page/1/
    page_total = 13 + 1
    for page_num in range(1,page_total):  # 共13页
        new_url = format(url%page_num)

        page_text = requests.get(url=new_url,headers=headers).text

        #将页面保存下来
        with open('./quitu.html','w',encoding='utf-8') as fp:
            fp.write(page_text)

        """
        需求获取的图片在这里，需要正则匹配出来
        <div class="thumb">
        <a href="/article/124825991" target="_blank">
        <img src="//pic.qiushibaike.com/system/pictures/12482/124825991/medium/OC3OEXR7AGPAW3JB.jpg" alt="糗事#124825991" class="illustration" width="100%" height="auto">
        </a>
        </div>
        """
        # 正则匹配规则
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        #re.S是单行匹配，re.M是多行匹配
        img_src_list = re.findall(ex,page_text,re.S)
        # print(img_src_list)
        # print(len(img_src_list))
        # 循环获取图片数据
        for src in img_src_list:
            src_url = 'https:' + src
            # print(src_url)
            # 将获取到的url作为新的内容发起请求,获取图片的二进制数据
            img_data = requests.get(url=src_url,headers=headers).content
            # 获取图片名称  src_url = https://pic.qiushibaike.com/system/pictures/12482/124826383/medium/G5F7P6F4EGVZMMRR.jpg
            img_name = src_url.split('/')[-1]
            img_path = folder_name + '/' + img_name
            # print(img_name)
            # print(img_list)
            # 保存到当前目录
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print('第',page_num,'页：',img_name,'下载成功!!!')


def main():
    get_pic()

if __name__ == '__main__':
    main()