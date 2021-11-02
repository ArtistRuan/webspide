#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: web_domo
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/10/18 0:14
'''

from bs4 import BeautifulSoup

r = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)  30号的作业</title>
</head>
<body>
<h1>我的第一个标题</h1>
<p id="first">我的第一个段落。</p>
</body>
    <table border="1">
        <tr>
            <td>row 1, cell 1</td>
            <td>row 1, cell 2</td>
        </tr>
    </table>
</html>
'''

demo = BeautifulSoup(r, "html.parser")
print(demo.title)  # <title>菜鸟教程(runoob.com)  30号的作业</title>
print(demo.body)
'''
<body>
<h1>我的第一个标题</h1>
<p id="first">我的第一个段落。</p>
</body>
'''
print(demo.p)  # <p id="first">我的第一个段落。</p>
print(demo.string)  # None
