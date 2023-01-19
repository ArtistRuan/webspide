#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: selenium_demo
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2023-01-19 21:36
'''

from selenium import webdriver

def run_selenium():

    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")

    driver.quit()

def main():
    run_selenium()

if __name__ == '__main__':
    main()