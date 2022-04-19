#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: sshfile
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-04-19 23:13
'''
host = "192.168.174.100"
port = 22
timeout = 30
user = "root"
password = "123456"

import paramiko
import os

#直接系统命令（执行超时）
def system_command():
    command = "ssh root@192.168.174.100 mkdir -p /test"
    os.system(command)

# 免密ssh（报错，没有密钥）
def ssh_con_without_key():
    private_key = paramiko.RSAKey.from_private_key_file('id_rsa96')  # 使用目标的私钥来登录

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname='192.168.174.100', port=22, username='root', pkey=private_key)

    cmd = 'ps'
    stdin, stdout, stderr = ssh.exec_command(cmd)

    result = stdout.read()

    if not result:
        result = stderr.read()
    ssh.close()

    print(result.decode())

# python实现ssh
def ssh_conn():
    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname='192.168.174.100', port=22, username='root', password='123456')

    # cmd = 'ps'
    # cmd = 'ls /'
    # cmd = 'mkdir -p /test'
    # cmd = 'rm -rf /test'
    cmd = 'ls -l;ifconfig'       #多个命令用;隔开
    stdin, stdout, stderr = ssh.exec_command(cmd)

    result = stdout.read()

    if not result:
        result = stderr.read()
    ssh.close()

    print(result.decode())

if __name__ == '__main__':
    # ssh_conn()
    # ssh_con_without_key()
    system_command()