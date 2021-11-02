#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: bs4_BeautifulSoup
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/10/17 16:08
'''

'''
下载方法是：
    pip install bs4
        (bs4在使用时候需要第三方库，可以同时安装一下 pip install lxml)
    pip install BeautifulSoup
        BeautifulSoup实例化的方法：
        soup = BeautifulSoup(页源码或者html文档,'lxml')
        1、html文件：
            with open('./web.html','r',encoding='utf-8') as fp:
                soup = BeautifulSoup(fp,'lxml')
        2、页源码
            page_html = response.text
            soup = BeautifulSoup(page_html,'lxml')
如果还是下载不了，需要更换pip数据源为国内源，如阿里源、豆瓣源、网易源等：
    - windows
    1、打开文件管理器（文件夹地址栏中）
    2、地址栏上输入 %appdata%
    3、在这里新建一个文件夹 pip
    4、在pip文件夹里面新建一个文件叫做 pip.ini ,内容为如下
        [global]
        timeout = 6000
        index-url = https://mirrors.aliyun.com/pypi/simple/
        trusted-host = mirrors.aliyun.com
    - linux
    1、cd ~
    2、mkdir ~/.pip
    3、vim ~/.pip/pip.conf
    4、编辑内容，和windows一模一样
'''
'''
数据解析的3种方法：
    1、正则解析
    2、bs4
    3、xpath
2、soup提供的用于数据解析的方法和属性：
    - soup.tagName:返回的是文档中第一次出现的tagName对应的标签
    - soup.find():
        - find('tagName'):等同于soup.div(即，soup.标签类型)
        - 属性定位:
            - soup.find('div',class_/id/attr='song')
    -soup.find_all('tagName'):返回复合要求的所有标签（列表）
- select:
    - select('某种选择器(id,class,标签...选择器)'),返回的是一个列表
    - 层级选择器:
        - soup.select('.tang > ul > li > a')  # > 表示的是一个层级
        - soup.select('.tang > ul a')  # 空格表示的是多个层级
- 获取标签之间的文本数据
    soup.a.string  # 只获取a标签直系的文本内容
    soup.a.text/get_string()  # 获取a标签下所有的文本内容
- 获取标签中的属性值:
    soup.a['href']  # 获取a标签下href属性值
3、xpath
- xpath解析原理（最常用建议用的方法）：
    - 1.实例化一个etree对象，且需要将被解析的页面源码数据加载到该对象
    - 2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获
- 环境安装：
    - pip install lxml
- 如何实例化一个etrr对象：from lxml import etree
    - 1.将本地的html文档中的源码数据加载到etree对象中：
        etree.parse(filePath)
    - 2.可以将从互联网上获取的源码数据加载到该对象中
        etree.HTML('page_text')
    - 3.xpath('xpath表达式') 
        - /:表示的是从根节点开始定位。表示的是一个层级。
        - //:表示的是多个层级。可以表示从任意位置开始定位。
        - 属性定位：tag[@attrName="attrValue"] ，如 //div[@class="song"]
        - 索引定位：//div[@class="song"]/p[3]，索引是从1开始的。
        - 取文本：
            - /text() 获取的是标签中直系的文本内容
            - //text() 标签中非直系的文本内容（所有文本内容）
        - 取属性：
            /@attrName，如img/@src
            
'''
# bs4
from bs4 import BeautifulSoup

# xpath
from lxml import etree

def bs4_demo():
    with open('text.html','r',encoding='utf-8') as fp:
        soup = BeautifulSoup(fp,'lxml')
        # （1）通过标签名查找
        print('1 ',soup.select('title'))  # [<title>The Dormouse story</title>]
        print('1 ',soup.select('title')[0].text)  # The Dormouse story
        print('1@ ',soup.select('p',class_='title'))
        '''
        [<p>html = """
        </p>, <p class="title" name="dromouse"><b>The Dormouse's story</b></p>, <p class="story">Once upon a time there were three little sisters; and their names were
        <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
        <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
        <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>, <p class="story">...</p>]
        '''
        print('1* ',soup.select('.title'))  # [<p class="title" name="dromouse"><b>The Dormouse's story</b></p>]
        print('1^ ',soup.select('.title')[0].text)  # The Dormouse's story
        print('1^ ',soup.select('.title name'))  # []
        '''
        [<p>html = """
        </p>, <p class="title" name="dromouse"><b>The Dormouse's story</b></p>, <p class="story">Once upon a time there were three little sisters; and their names were
        <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
        <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
        <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>, <p class="story">...</p>]
        '''
        print('2 ',soup.select('a'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        print('2% ',soup.find('a'))  # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
        print('2+ ',soup.find_all('a'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        print('2- ',soup.find_all('body > p > a'))  # []
        print('3 ',soup.select('b'))  # [<b>The Dormouse's story</b>]
        print('3) ',soup.find('b').text)  # The Dormouse's story
        print('3- ',soup.find('p',class_='story').text)
        '''
        Once upon a time there were three little sisters; and their names were
        ,
        Lacie and
        Tillie;
        and they lived at the bottom of a well.
        '''
        print('3% ',soup.find('a',class_='sister'))  # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
        print('3+ ',soup.find_all('a',class_='sister'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        print('3++ ',soup.find_all('a',class_='sister',id='link3'))  # [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

        # （2）通过类名查找
        print('4 ',soup.select('.sister'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        print('4+ ',soup.select('.title'))  # [<p class="title" name="dromouse"><b>The Dormouse's story</b></p>]

        # （3）通过 id 名查找 #不能少
        print('5 ',soup.select('#link1'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
        print('5- ',soup.select('link1'))  # []
        print('5= ',soup.select('#link2'))  # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
        print('5= ',soup.select('#link2')[0]['id'])  # link2
        print('5) ',soup.select('p[name]'))  # [<p class="title" name="dromouse"><b>The Dormouse's story</b></p>]
        print('5) ',soup.select('p')[1])  # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        print('5) ',soup.select('p')[1]['name'])  # dromouse

        # （4）1 组合查找
        #       组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，
        #       例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
        print('6 ',soup.select('p #link1'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

        # （4）2 直接子标签查找
        print('7 ',soup.select("head > title"))   # 理想效果：[<title>The Dormouse story</title>] 但是[]
        print('7 ',soup.find('head > title'))   # 理想效果：[<title>The Dormouse story</title>] 但是[]
        print('7+ ',soup.select('head #title'))   # 理想效果：[<title>The Dormouse story</title>] 但是[]
        print('7+ ',soup.select('.head title'))   # 理想效果：[<title>The Dormouse story</title>] 但是[]
        print('7+1 ',soup.select('p a'))   # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
        print('7+2 ',soup.find('title'))   # <title>The Dormouse story</title>
        print('7+3 ',soup.find_all('title'))   # [<title>The Dormouse story</title>]

        # （5）1 属性查找  查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
        print('8 ',soup.select("head title"))  # 理想效果：[<title>The Dormouse's story</title>] 但是[]
        # （5）2 属性查找
        print('9 ',soup.select('a[href="http://example.com/elsie"]'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
        # （5） 3 属性查找 同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
        print('10 ',soup.select('p a[href="http://example.com/elsie"]'))  # [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]


    # 关闭文件io
    fp.close()

def xpath_demo():
    # 实例化一个etree对象，且将被解析的源码加载到该对象中
    tree = etree.parse('test.html')
    # r = tree.xpath('/html/body/div')  # 定位到div
    # r = tree.xpath('/html//div')  # 定位到div
    # r = tree.xpath('//div')  # 定位到div
    # r = tree.xpath('//div[@class="song"]')  # 定位到class为song的div
    # r = tree.xpath('//div[@class="song"]/p')  # 有4个p标签
    # r = tree.xpath('//div[@class="song"]/p[3]')  # 有4个p标签,定位到第3个p标签
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')  # 获取tang下面第5个li标签下a标签的文本，返回列表
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]  # 获取该列表第一个元素
    # r = tree.xpath('//li[7]//text()')  # 第7个li下所有的文本内容
    # r = tree.xpath('//div[@class="tang"]//text()')  # tang下所有的文本内容
    r = tree.xpath('//div[@class="song"]//img/@src')  # ['http://www.baidu.com/meinv.jpb']   img下src的属性值

    print(r)

if __name__ == '__main__':
    # bs4_demo()
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    xpath_demo()