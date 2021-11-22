#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import pyhive
import sasl
from hive_service import ThriftHive
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

__author__ = 'ruanshikao'

'''
@title: hiveDB
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/11/22 11:04
'''

def connect_hive(sql):
    transport = TSocket.TSocket('192.168.174.100',10000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # client = ThriftHive.Client(protocol)
    client =pyhive.Client(protocol)
    client.execute(sql)
    resultSets = client.fetchAll()
    for j in range(len(resultSets)):
        print(resultSets[j])
    transport.close()

def main():
    sql = "select count(1) from yj_houses.yj_houses_selling_info"
    connect_hive(sql)

if __name__ == '__main__':
    main()