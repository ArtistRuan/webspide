#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

'''
@title: json_response
@projectName pythonProject
@description: TODO
@author ruanshikao
@date 2021/10/20 22:39
'''

import requests
from lxml import etree
import time
import pymysql

def insert(value):
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')
    cursor = db.cursor()
    sql = "INSERT INTO yj_houses.yj_houses_selling_info(project_name,project_address,project_builder,project_distinct,project_total_builder_area,project_area,total_house_num,total_area,house_num,house_area,not_house_num,not_house_area,sold_house_num,sold_house_area,house_avg_price,sold_not_house_num,sold_not_house_area,not_house_avg_price,data_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql, value)
        db.commit()
        print('插入数据成功')
    except Exception as e:
        db.rollback()
        print("插入数据失败",e)
    db.close()

def parse():
    for page_num in range(1,127):
        print('正在获取第', page_num, '页10个详情页信息')
        url = 'http://219.129.189.10:9168/api/GzymApi/GetIndexSearchData?Jgid=&PageIndex=' + str(page_num) + '&PageSize=10&Ysxmmc=&Ysxkzh=&Kfsmc=&Kfxmmc='
        # ua伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
        }
        values = []
        json_response = requests.get(url=url, headers=headers).json()

        for data in json_response['Data']:
            # print(data['YSXMID'])
            # print(data['DJJG'])
            # http://219.129.189.10:9168/public/web/ysxm?ysxmid=2192CB59808D420F9E04B679DEF6934B&jgid=480de8f9-4595-490f-adfc-b5ec3eeca2bf
            new_url = 'http://219.129.189.10:9168/public/web/ysxm?ysxmid=' + data['YSXMID'] + '&jgid=' + data['DJJG']
            print('new_url是：',new_url)
            certified_detail_page = requests.get(url=new_url, headers=headers).text
            # print('certified_detail_page: ',certified_detail_page)
            print('发起跳转请求...')
            detail_tree = etree.HTML(certified_detail_page)

            # 最终需要请求的数据页url = 'http://219.129.189.10:9168/public/web/' + project_href
            project_href = detail_tree.xpath('//div[2]//tr[2]/td//tr/td[@id="PresellName"]/a/@href')

            for data_href in project_href:
                data_url = 'http://219.129.189.10:9168/public/web/' + data_href
                print('发起目标页面跳转请求...',data_url)
                # 对最终数据页面发起请求
                data_page = requests.get(url=data_url, headers=headers).content
                data_tree = etree.HTML(data_page)
                date = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))  # 获取当前时间
                print('============================解析',page_num,'表格数据============================')
                table_part_title = data_tree.xpath('//div[2]//tr[2]/td/table//td//table//text()')
                # print('目标数据表格：',table_part_title)  # 赋值即可
                print(len(table_part_title))
                target_project_name = str(table_part_title[21]).strip()  # 项目名称
                target_project_address = str(table_part_title[25]).strip()  # 项目座落
                target_project_builder = str(table_part_title[31]).strip()  # 开发商
                target_project_distinct = str(table_part_title[35]).strip()  # 所在地区
                target_project_total_builer_area = str(table_part_title[41]).strip()  # 总建筑面积
                # if str(table_part_title[45]).strip() == '㎡':
                #     target_project_area = '0 ' + str(table_part_title[45]).strip()  # 占地面积
                # else:
                #     target_project_area = str(table_part_title[45]).strip()
                target_project_area = str(table_part_title[45]).strip()
                total_house_num = str(table_part_title[63]).strip()  # 总套数
                total_area = str(table_part_title[67]).strip()  # 总面积
                house_num = str(table_part_title[73]).strip()  # 住宅套数
                house_area = str(table_part_title[77]).strip()  # 住宅面积
                not_house_num = str(table_part_title[83]).strip()  # 非住宅套数
                not_house_area = str(table_part_title[87]).strip()  # 非住宅面积
                sold_house_num = str(table_part_title[93]).strip()  # 已售住宅套数
                sold_house_area = str(table_part_title[97]).strip()  # 已售住宅面积
                house_avg_price = str(table_part_title[103]).strip()  # 住宅均价
                sold_not_house_num = str(table_part_title[111]).strip()  # 已售非住宅套数
                sold_not_house_area = str(table_part_title[115]).strip()  # 已售非住宅面积
                not_house_avg_price = str(table_part_title[121]).strip()  # 非住宅均价

                # 打印获取到是数据
                print('项目名称', target_project_name)  # 项目名称
                print('项目座落', target_project_address)  # 项目座落
                print('开发商', target_project_builder)  # 开发商
                print('所在地区', target_project_distinct)  # 所在地区
                print('总建筑面积', target_project_total_builer_area)  # 总建筑面积
                print('占地面积', target_project_area)  # 占地面积
                print('总套数', total_house_num)  # 总套数
                print('总面积', total_area)  # 总面积
                print('住宅套数', house_num)  # 住宅套数
                print('住宅面积', house_area)  # 住宅面积
                print('非住宅套数', not_house_num)  # 非住宅套数
                print('非住宅面积', not_house_area)  # 非住宅面积
                print('已售住宅套数', sold_house_num)  # 已售住宅套数
                print('已售住宅面积', sold_house_area)  # 已售住宅面积
                print('住宅均价', house_avg_price)  # 住宅均价
                print('已售非住宅套数', sold_not_house_num)  # 已售非住宅套数
                print('已售非住宅面积', sold_not_house_area)  # 已售非住宅面积
                print('非住宅均价', not_house_avg_price)  # 非住宅均价

                # 将数据加载到列表，用于存入数据库
                values.append(target_project_name)  # 项目名称
                values.append(target_project_address)  # 项目座落
                values.append(target_project_builder)  # 开发商
                values.append(target_project_distinct)  # 所在地区
                values.append(target_project_total_builer_area)  # 总建筑面积
                values.append(target_project_area)  # 占地面积
                values.append(total_house_num)  # 总套数
                values.append(total_area)  # 总面积
                values.append(house_num)  # 住宅套数
                values.append(house_area)  # 住宅面积
                values.append(not_house_num)  # 非住宅套数
                values.append(not_house_area)  # 非住宅面积
                values.append(sold_house_num)  # 已售住宅套数
                values.append(sold_house_area)  # 已售住宅面积
                values.append(house_avg_price)  # 住宅均价
                values.append(sold_not_house_num)  # 已售非住宅套数
                values.append(sold_not_house_area)  # 已售非住宅面积
                values.append(not_house_avg_price)  # 非住宅均价
                values.append(date)

                insert(values)
                print('============================解析', page_num, '表格数据============================')
                # 清空列表
                values.clear()
            # cur.execute('insert into proxy(ip, port, location, anonymity, proxy_type, speed, connect_time, validate_time) values(%s%s%s%s%s%s%s%s)',(ip, port, location, anonymity, proxy_type, speed, connect_time, validate_time))

        print('执行成功')



def main():
    parse()

if __name__ == '__main__':
    main()