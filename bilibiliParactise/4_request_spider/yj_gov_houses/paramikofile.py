#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: paramikofile
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-04-19 22:57
'''
host = "192.168.174.100"
port = 22
timeout = 30
user = "root"
password = "123456"

import paramiko

# python实现sftp:download
def sftp_download_file(server_path, local_path):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(server_path,local_path)
        t.close()
    except Exception as e:
        print(e)

# python实现sftp:upload
def sftp_upload_file(server_path, local_path):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        t.close()
    except Exception as e:
        print(e)

def sftp_exec_command(command):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, 22, user, password)
        std_in, std_out, std_err = ssh_client.exec_command(command)
        for line in std_out:
            print(line.strip("\n"))
        ssh_client.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sftp_exec_command("ls -l")
    print("============")

    # 上传文档
    # sftp_upload_file("/root/bug.txt", "F:/bug.txt")

    # 下载文档
    sftp_download_file("/root/bb.sh","F:/bb.sh")
