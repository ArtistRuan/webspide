#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 需求：实现网页采集器

"""
UA:User-Agent(请求载体的身份标识)
UA检测：门户网站的服务器会检查对应的请求的载体身份标识，如果检测到请求的载体身份标识位某一款浏览器
        说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标识不是某款浏览器的，则标识该
        为异常的请求（爬虫）。则服务器就很有可能拒绝该次请求。

应对UA检测的反反爬方式就是[UA伪装]
UA伪装：让爬虫对应的请求载体身份标识伪装为某款浏览器

为了爬虫的安全不触犯法律，吃局饭，就得在评估阶段查看“君子协议”。
君子协议：规定了网站中哪些数据可以被爬虫爬取，哪些数据不可以被爬取，且爬取的同时，不能造成对方网站崩溃。
方式：在网站网址末加上robots.txt，即可查看“君子协议”的内容。
"""

import requests
def run_web_collection():
    # UA伪装，将对应的User-Agent封装到一个字典中
    headers = {
        # 通过在页面中右键【检查】，然后找到【Network】，接着在【web?...】中找到User-Agent信息
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    # 指定url，如https://www.sogou.com/web?query=波晓张
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a keyword：')
    param = {
        'query':kw
    }
    # 对指定的url发起请求并获取响应，携带的参数为输入的动态关键字和ua
    response = requests.get(url=url,params=param,headers=headers)
    # 通过响应对应获取数据
    page_text = response.text
    # 将获取到的数据保存到文件中，定义文件名
    file_name = kw + '.html'
    with open(file_name,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(file_name,'保存成功!!!')

def main():
    run_web_collection()

if __name__ == '__main__':
    main()