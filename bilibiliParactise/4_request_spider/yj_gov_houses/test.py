#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

from fabric2 import Connection
import os
import fabric2


def deploy():
    # 如果服务器配置了ssh免密码登录，就不需要 connect_kwargs 来指定密码
    conn = Connection("root@192.168.174.120", connect_kwargs={"password": "123456"})
    # conn = Connection("root@192.168.174.120")
    conn.run("ls")

    with conn.cd('/home'):
        # result = conn.client.exec_command('[ -f testdir ] && echo ok')
        # if result == 'ok':
        #     print("testdir exists",result)
        conn.run("rm -rf testdir")
        conn.run("mkdir testdir",encoding='utf-8')
    with conn.cd('/home/testdir'):
        conn.run('mkdir aaa')
        conn.put('config.yaml', '/home/testdir')  # 上传文件


if __name__ == '__main__':
    deploy()