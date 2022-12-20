#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: bubbleAlgorithm
    1 冒泡算法
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-12-20 23:04
'''
import time

def r_bubble(lst):

    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                time.sleep(5)
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
                print(lst)


def main():
    original_list = [1, 4, 5, 3, 2, 9, 8, 6, 7]
    print(f'原数组是：{original_list}')
    r_bubble(original_list)



if __name__ == '__main__':
    main()