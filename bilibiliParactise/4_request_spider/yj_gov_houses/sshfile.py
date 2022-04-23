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
import subprocess

#直接系统命令（执行超时）
def system_command():
    # 为支持重跑，检查是否存在
    ssh_command = """
        ssh 192.168.174.100 <<EOF
        if [ -d /export/shell_python/20220423 ] && [ -f /export/shell_python/20220423/data.dat ];then
            rm -rf /export/shell_python/20220423
            echo "ok"
        else
            echo -e "\e[1;41mno ok file\e[0m\e[1;31m contact the supplier\e[0m `date +"%Y-%m-%d %H%M%S"`"
            exit 1
        fi
        >>EOF
    """
    scp_command = "scp -r /export/shell_python/20220423/ root@192.168.174.100:/export/shell_python/"
    os.system(ssh_command)
    os.system(scp_command)

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