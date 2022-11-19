#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: replace_erro_file_name
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-11-19 11:46
'''
import time
import datetime

def correct_title(title):
    """定义特殊字符是哪些"""
    error_set = ['/', '\\', ':', '*', '?', '"', '|', '<', '>', ' ']
    for c in title:
        if c in error_set:
            title = title.replace(c, '')

    return title


def run(title):
    start_time = datetime.datetime.now()

    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print(f'now_time={now_time}')

    print(f"start={start_time}")
    print(f'original_title={title}')
    title = correct_title(title)
    print(f'correct_title={title}')
    end_time = datetime.datetime.now()
    print(f'time={end_time}')
    print(end_time-start_time)

def main():
    title = '也许是B站最好的 Markdown 科普教程 | 15  款顶级笔记软件测评推荐_哔哩哔哩_bilibili.mp3'
    run(title)

if __name__ == '__main__':
    main()