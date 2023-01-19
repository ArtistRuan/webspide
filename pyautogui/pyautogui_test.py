#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: pyautogui_test
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2023-01-18 20:07
'''

import pyautogui
import pyperclip
from typing import Text
import time

def run_pyautogui():
    print(pyautogui.size())  # 获取屏幕分辨率 Size(width=1366, height=768)
    print(pyautogui.position())  # 获取鼠标位置 Point(x=414, y=486)
    print(pyautogui.onScreen(200,202))  # 查看位置点是否位于屏幕上

def search_current_position():
    while True:
        time.sleep(1)
        x,y = pyautogui.position()
        print(f'您当前位置坐标为：({x},{y})')

def mouse_action():
    """1 鼠标移动"""
    pyautogui.moveTo(200,202,2)  # 将鼠标在2秒内移动到指定坐标（相对原点）
    pyautogui.moveRel(200,202,2)  # 将鼠标在2秒内移动到指定坐标（相对当前位置）
    pyautogui.drag(200,202,button='left',duration=3)  # button参数指定了按键，duration指定了完成任务的时间，这个移动相对当前位置移动
    pyautogui.dragTo(100,100,button='left',duration=3)  # 具体到相对原点的坐标

    """3 鼠标点击"""
    # pyautogui.click(100,100,button='right')  # 鼠标点击指定位置
    pyautogui.click(100,100,button='left')  # 鼠标点击指定位置
    pyautogui.click(100,100,3,2,button='left')  # 鼠标点击指定位置
    pyautogui.doubleClick()

def mouse_scroll():
    """2 鼠标滚动"""
    while True:
        time.sleep(1)
        pyautogui.scroll(-200)

def button_alert():
    """alert related"""
    password_info = pyautogui.password(text='',title='',default='',mask='*')
    # pyautogui.write("hello world",interval=1)
    # pyautogui.typewrite("hello world",interval=1)
    print(password_info)

    confirm_button = pyautogui.confirm(text='',title='',buttons=['ok','6',9])
    print(confirm_button)

    alert_info = pyautogui.alert(text='程序开始了吗？',title='弹窗信息',button='OK')
    print(alert_info)

def click_and_input():

    time.sleep(2)
    input_info1 = "中文测试"
    input_info2 = 'hello world'
    pyperclip.copy(input_info1)
    pyautogui.hotkey('win','r')
    pyautogui.sleep(1)
    pyautogui.typewrite('cmd')
    # pyautogui.sleep(1)
    pyautogui.press('Enter')
    pyautogui.press('Enter')
    pyautogui.sleep(1)
    pyautogui.typewrite(input_info2)
    pyautogui.sleep(1)
    pyautogui.hotkey('ctrl','v')
    for i in range(len(input_info1) + len(input_info2)):
        # pyautogui.sleep(1)
        pyautogui.press('Backspace')
    pyautogui.typewrite('exit')
    # pyautogui.sleep(1)
    pyautogui.press('Enter')
    pyautogui.press('Enter')


def key_action():
    pyautogui.keyDown('win')
    pyautogui.keyDown('r')
    pyautogui.keyUp('win')
    pyautogui.keyUp('r')
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    # x,y = pyautogui.position()
    # pyautogui.click(x,y)
    pyautogui.sleep(2)
    # pyautogui.typewrite('exit')
    pyautogui.press('Enter')
    pyautogui.press('Enter')
    pyautogui.typewrite(r'C:\Users\Alex\AppData\Local\Google\Chrome\Application\chrome.exe')
    pyautogui.press('Enter')
    pyautogui.press('Enter')


    pyautogui.press('Enter')

def open_google():
    pass

def main():
    pyautogui.FAILSAFE = False  # 关闭自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
    # run_pyautogui()
    # search_current_position()
    # mouse_action()
    # mouse_scroll()exit
    # button_alert()
    key_action()
    # click_and_input()


    # open_google()


if __name__ == '__main__':
    main()