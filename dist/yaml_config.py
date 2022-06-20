#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: yaml_config
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2022-06-21 0:41
'''

import yaml

def get_config_info():
    with open('./db_info_config.yaml','r',encoding='utf-8') as fp:
        yaml_info = fp.read()

        yaml_dit = yaml.load(yaml_info,Loader=yaml.FullLoader)

        print(yaml_dit['prd'])
        print(yaml_dit['prd']['ip'])
        print(yaml_dit['prd']['port'])

def main():
    get_config_info()

if __name__ == '__main__':
    main()