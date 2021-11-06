#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ruanshikao'

import demjson as demjson

'''
@title: json_response
@projectName pythonProject
@description: 网站采集
@author ruanshikao
@date 2021/10/20 22:39
'''

import requests
import pandas as pd
from lxml import etree
import time
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# from email.mime.image import MIMEImage
# import numpy  # 数据分析
import datetime
import os
import yaml

def analyze_data():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')
    cursor = conn.cursor()
    # 编写可以获取今天成交量的语句
    sql = ''
    cursor.execute(sql)
    data = cursor.fetchall()

    result = [list(x) for x in data]

    columns = []

    excel_data = pd.DataFrame(result, columns=columns)

    file_path = 'yj_house' + str(time.strftime('%Y%m%d', time.localtime(time.time()))) + '.xls'
    excel_data.to_excel(file_path, index=False)

    conn.close()
    cursor.close()

    return data


def parse_insert(proxies):
    start_time = datetime.datetime.now()
    print('开始时间：', start_time)
    # ua伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }
    # 用session对象替代requests发起请求
    session = requests.Session()
    sql = "INSERT INTO yj_houses.yj_houses_selling_info(project_name,project_address,project_builder,project_distinct,project_total_builder_area,project_area,total_house_num,total_area,house_num,house_area,not_house_num,not_house_area,sold_house_num,sold_house_area,house_avg_price,sold_not_house_num,sold_not_house_area,not_house_avg_price,data_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    ixd = 0
    a_set = set()
    b_set = set()
    values = set()
    for page_num_yj in range(1, 127):  # 获取阳江数据
        # time.sleep(2)
        print('正在获取第', page_num_yj, '页10个详情页信息')
        url_1 = 'http://219.129.189.10:9168/api/GzymApi/GetIndexSearchData?Jgid=&PageIndex=' + str(page_num_yj) + '&PageSize=10&Ysxmmc=&Ysxkzh=&Kfsmc=&Kfxmmc='
        try:
            json_response1 = session.get(url=url_1, headers=headers,proxies=proxies).json()
            print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),'json_response1:', json_response1)
            for data in json_response1['Data']:
                # print(data['YSXMID'])
                # print(data['DJJG'])
                new_url_1 = 'http://219.129.189.10:9168/public/web/ysxm?ysxmid=' + data['YSXMID'] + '&jgid=' + data['DJJG']
                a_set.add(new_url_1)
        except:
            continue

    for page_num_yd in range(1, 77):  # 获取阳东数据
        # time.sleep(2)
        print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),'正在获取第', page_num_yd, '页10个详情页信息')
        url_2 = 'http://219.129.189.10:9168/api/GzymApi/GetIndexSearchData?Jgid=d9602e29-1374-4860-8ad5-f259d239e446&PageIndex=' + str(page_num_yd) + '&PageSize=10&Ysxmmc=&Ysxkzh=&Kfsmc=&Kfxmmc='
        try:
            json_response2 = session.get(url=url_2, headers=headers,proxies=proxies).json()
        except:
            continue
        print('json_response2:', json_response2)

        try:
            for data in json_response2['Data']:
                print('YSXMID:', data['YSXMID'])
                print('DJJG:', data['DJJG'])
                new_url_2 = 'http://219.129.189.10:9168/public/web/ysxm?ysxmid=' + data['YSXMID'] + '&jgid=' + data['DJJG']
                print('new_url:', new_url_2)
                a_set.add(new_url_2)
        except:
            continue

    for new_url in a_set:
        print('获取a_set中的url信息', new_url)
        ixd += 1
        # time.sleep(1)
        certified_detail_page = session.get(url=new_url, headers=headers,proxies=proxies).text
        # print('certified_detail_page: ',certified_detail_page)
        print('解析详情页获取第', ixd, '个href...')
        detail_tree = etree.HTML(certified_detail_page)

        # 最终需要请求的数据页url = 'http://219.129.189.10:9168/public/web/' + project_href
        project_href = detail_tree.xpath('//div[2]//tr[2]/td//tr/td[@id="PresellName"]/a/@href')

        for data_href in project_href:
            data_url = 'http://219.129.189.10:9168/public/web/' + data_href
            b_set.add(data_url)

    ixd2 = 0
    for data_url in b_set:
        ixd2 += 1
        time.sleep(1)
        print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),'发起目标页面跳转请求...', data_url)
        # 对最终数据页面发起请求
        data_page = session.get(url=data_url, headers=headers,proxies=proxies).content
        data_tree = etree.HTML(data_page)
        date = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))  # 获取当前时间
        print('============================解析', ixd2, '表格数据============================')
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
        values.add((target_project_name,target_project_address,target_project_builder,target_project_distinct,target_project_total_builer_area,target_project_area,total_house_num,total_area,house_num,house_area,not_house_num,not_house_area,sold_house_num,sold_house_area,house_avg_price,sold_not_house_num,sold_not_house_area,not_house_avg_price,date))
        # values.append(target_project_name)  # 项目名称
        # values.append(target_project_address)  # 项目座落
        # values.append(target_project_builder)  # 开发商
        # values.append(target_project_distinct)  # 所在地区
        # values.append(target_project_total_builer_area)  # 总建筑面积
        # values.append(target_project_area)  # 占地面积
        # values.append(total_house_num)  # 总套数
        # values.append(total_area)  # 总面积
        # values.append(house_num)  # 住宅套数
        # values.append(house_area)  # 住宅面积
        # values.append(not_house_num)  # 非住宅套数
        # values.append(not_house_area)  # 非住宅面积
        # values.append(sold_house_num)  # 已售住宅套数
        # values.append(sold_house_area)  # 已售住宅面积
        # values.append(house_avg_price)  # 住宅均价
        # values.append(sold_not_house_num)  # 已售非住宅套数
        # values.append(sold_not_house_area)  # 已售非住宅面积
        # values.append(not_house_avg_price)  # 非住宅均价
        # values.append(date)
        print('============================解析完毕', ixd2, '表格数据============================')

    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')
    cursor = db.cursor()

    try:
        cursor.executemany(sql, values)
        db.commit()
        # values.clear()
        print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),'批量插入数据成功')
    except Exception as e:
        db.rollback()
        print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),"批量插入数据失败", e)

    db.close()
    session.close()
    end_time = datetime.datetime.now()
    t = end_time - start_time
    print('获取数据执行时长(单位：秒)', t)

def send_email():
    # 发件人和收件人信息
    sender = 'm2ruan@126.com'
    receivers = ['m2ruan@126.com','1135965756@qq.com']
    # receivers = ['m2ruan@126.com', 'liangyangruan@qq.com']
    mail_content = '''
    尊敬的夫人：
        请查收今日数据。

    '''

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("m2ruan@126.com")
    message['To'] = Header("老婆")
    # 抄送
    message['Cc'] = 'liangyangruan@qq.com'
    subject = '本日量网签数据（含阳江江城及阳东）'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的test.txt文件
    # file_name = 'yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    file_path = './yj_house_all/yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.xlsx'
    f = open(file_path, 'rb')
    att1 = MIMEText(f.read(), 'xlsx', 'utf-8')
    # att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=%s' % (file_path)  # 这句会影响附件的后缀名，多个attachment，导致手机打不开
    # att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', file_path))  # 解决中文附件名乱码问题
    att1.add_header('Content-Disposition', 'attachment', filename=file_path)  # 解决中文附件名乱码问题
    message.attach(att1)
    f.close()

    # 构造excel附件2，传送当前目录下的test.txt文件
    # file_name = 'yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    file_path2 = './yj_house_day/yj_house_day_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.xlsx'
    f2 = open(file_path2, 'rb')
    att2 = MIMEText(f2.read(), 'xlsx', 'utf-8')
    # att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att2['Content-Type'] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=%s' % (file_path)
    att2.add_header('Content-Disposition', 'attachment', filename=file_path2)  # 解决中文附件名乱码问题
    message.attach(att2)
    f2.close()

    # 构造excel附件3，传送当前目录下的test.txt文件
    # file_name = 'yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    file_path3 = './yj_house_week/yj_house_week_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.xlsx'
    f3 = open(file_path3, 'rb')
    att3 = MIMEText(f3.read(), 'xlsx', 'utf-8')
    # att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att3['Content-Type'] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=%s' % (file_path)
    att3.add_header('Content-Disposition', 'attachment', filename=file_path3)  # 解决中文附件名乱码问题
    message.attach(att3)
    f3.close()

    # # 构造附件2，传送当前目录下的we.jpg文件
    # with open('we.jpg', 'rb') as fp:
    #     msgImage = MIMEImage(fp.read())
    #     msgImage['Content-Type'] = 'application/octet-stream'
    #     msgImage["Content-Disposition"] = 'attachment; filename="we.jpg"'
    # message.attach(msgImage)
    # fp.close()

    try:
        # 登录邮件服务器
        smtp_obj = smtplib.SMTP_SSL("smtp.126.com")  # 发件人邮箱中的SMTP服务器，端口是25
        smtp_obj.login("m2ruan@126.com", "YVLWGFNNIJANTMDR")  # 括号中对应的是发件人邮箱账号和邮箱密码
        # smtp_obj.set_debuglevel(1)  # 显示调试信息
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print('邮件发送成功')
        smtp_obj.quit()
    except Exception as e:
        print('邮件发送失败', e)

def send_email2():
    # 发件人和收件人信息
    sender = 'm2ruan@126.com'
    # receivers = ['m2ruan@126.com','1135965756@qq.com']
    receivers = ['m2ruan@126.com', 'liangyangruan@qq.com']
    mail_content = '''
    尊敬的夫人：
        请查收今日数据。
    '''

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("m2ruan@126.com")
    message['To'] = Header("老婆")
    # 抄送
    message['Cc'] = 'liangyangruan@qq.com'
    subject = '本日网签数据（含阳江江城及阳东）'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的test.txt文件
    # file_name = 'yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    file_path = './yj_house_all/yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.xlsx'
    f = open(file_path, 'rb')
    att1 = MIMEText(f.read(), 'xlsx', 'utf-8')
    # att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=%s' % (file_path)
    att1.add_header('Content-Disposition', 'attachment', filename=file_path)  # 解决中文附件名乱码问题
    message.attach(att1)
    f.close()

    # 构造excel附件2，传送当前目录下的test.txt文件
    # file_name = 'yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    file_path2 = './yj_house_day/yj_house_day_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.xlsx'
    f2 = open(file_path2, 'rb')
    att2 = MIMEText(f2.read(), 'xlsx', 'utf-8')
    # att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att2['Content-Type'] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=%s' % (file_path)
    att2.add_header('Content-Disposition', 'attachment', filename=file_path2)  # 解决中文附件名乱码问题
    message.attach(att2)
    f2.close()

    # 构造excel附件3，传送当前目录下的test.txt文件
    # file_name = 'yj_house_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    file_path3 = './yj_house_week/yj_house_week_' + str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + '.xlsx'
    f3 = open(file_path3, 'rb')
    att3 = MIMEText(f3.read(), 'xlsx', 'utf-8')
    # att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att3['Content-Type'] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename=%s' % (file_path)
    att3.add_header('Content-Disposition', 'attachment', filename=file_path3)  # 解决中文附件名乱码问题
    message.attach(att3)
    f3.close()

    # # 构造附件2，传送当前目录下的we.jpg文件
    # with open('we.jpg', 'rb') as fp:
    #     msgImage = MIMEImage(fp.read())
    #     msgImage['Content-Type'] = 'application/octet-stream'
    #     msgImage["Content-Disposition"] = 'attachment; filename="we.jpg"'
    # message.attach(msgImage)
    # fp.close()

    try:
        # 登录邮件服务器
        smtp_obj = smtplib.SMTP_SSL("smtp.126.com")  # 发件人邮箱中的SMTP服务器，端口是25
        smtp_obj.login("m2ruan@126.com", "YVLWGFNNIJANTMDR")  # 括号中对应的是发件人邮箱账号和邮箱密码
        # smtp_obj.set_debuglevel(1)  # 显示调试信息
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print('邮件发送成功')
        smtp_obj.quit()
    except Exception as e:
        print('邮件发送失败', e)

# 保存每天全量数据
def db_save_excel_days():
    if not os.path.exists('./yj_house_all/'):
        os.mkdir('./yj_house_all/')
    data_date_str = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    annex_path = './yj_house_all/yj_house_' + data_date_str + '.xlsx'
    # sql = "select distinct project_name,project_address,project_builder,project_distinct,project_total_builder_area,project_area,total_house_num,total_area,house_num,house_area,not_house_num,not_house_area,sold_house_num,sold_house_area,house_avg_price,sold_not_house_num,sold_not_house_area,not_house_avg_price,current_date() from yj_houses.yj_houses_selling_info where data_date = '%s'" % (data_date_str)
    sql = """
    select distinct
        project_name
        ,project_address
        ,project_builder
        ,project_distinct
        ,project_total_builder_area
        ,project_area
        ,total_house_num
        ,total_area
        ,house_num
        ,house_area
        ,not_house_num
        ,not_house_area
        ,sold_house_num
        ,sold_house_area
        ,house_avg_price
        ,sold_not_house_num
        ,sold_not_house_area
        ,not_house_avg_price
        ,current_date()
    from yj_houses.yj_houses_selling_info where data_date = '%s' order by project_distinct desc""" % (data_date_str)
    # print('日期是：',data_date_str)
    # print('执行的语句是：',sql)
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取执行结果
    # result = [list(x) for x in result]  # 推导式
    col_result = cursor.description  # 获取查询结果的字段描述
    # columns = [x[0] for x in col_result]
    # 定义表头
    columns = ['项目名称','项目座落','开发商','所在地区','总建筑面积','占地面积','总套数','总面积','住宅套数','住宅面积','非住宅套数','非住宅面积','已售住宅套数','已售住宅面积','住宅均价','已售非住宅套数','已售非住宅面积','非住宅均价','数据批次（日期）']
    data = pd.DataFrame(result, columns=columns)
    print('日采集落excel数据量：',len(data))
    data.to_excel(annex_path, index=False)  # 将数据库数据保存到excel中

    cursor.close()
    conn.close()

# 保存每天统计的天数据
def db_save_excel_calc_day():
    if not os.path.exists('./yj_house_day/'):
        os.mkdir('./yj_house_day/')
    data_date_str = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    annex_path = './yj_house_day/yj_house_day_' + data_date_str + '.xlsx'
    sql = """
    select
        project_name
        ,project_distinct
        ,total_house_num
        ,sold_house_num
        ,today_sold_house_num
        ,house_avg_price
        ,sold_not_house_num
        ,today_sold_not_house_num
        ,not_house_avg_price
        ,data_date
    from yj_houses_selling_info_day WHERE data_date = CURRENT_DATE()"""
    # from yj_houses_selling_info_day WHERE data_date = CURRENT_DATE()"""
    # print('日期是：',data_date_str)
    # print('执行的语句是：',sql)
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取执行结果
    # result = [list(x) for x in result]  # 推导式
    col_result = cursor.description  # 获取查询结果的字段描述
    # columns = [x[0] for x in col_result]
    # 定义表头
    columns=['项目名称','所在地区','总套数','已售住宅套数','本日已售住宅套数','住宅均价','已售非住宅套数','本日已售非住宅套数','非住宅均价','数据时间']
    data = pd.DataFrame(result, columns=columns)
    print('日采集落excel日表数据量：',len(data))
    data.to_excel(annex_path, index=False)  # 将数据库数据保存到excel中

    cursor.close()
    conn.close()

# 保存每天统计的周数据
def db_save_excel_calc_week():
    if not os.path.exists('./yj_house_week/'):
        os.mkdir('./yj_house_week/')
    data_date_str = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    annex_path = './yj_house_week/yj_house_week_' + data_date_str + '.xlsx'
    sql = """
    select
        project_name
        ,project_distinct
        ,total_house_num
        ,sold_house_num
        ,week_sold_house_num
        ,house_avg_price
        ,sold_not_house_num
        ,week_sold_not_house_num
        ,not_house_avg_price
        ,data_date
    from yj_houses_selling_info_week WHERE data_date = CURRENT_DATE()"""
    # from yj_houses_selling_info_day WHERE data_date = CURRENT_DATE()"""
    # print('日期是：',data_date_str)
    # print('执行的语句是：',sql)
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取执行结果
    # result = [list(x) for x in result]  # 推导式
    col_result = cursor.description  # 获取查询结果的字段描述
    # columns = [x[0] for x in col_result]
    # 定义表头
    columns=['项目名称','所在地区','总套数','已售住宅套数','本周已售住宅套数','住宅均价','已售非住宅套数','本周已售非住宅套数','非住宅均价','数据时间']
    data = pd.DataFrame(result, columns=columns)
    print('日采集落excel周表数据量：',len(data))
    data.to_excel(annex_path, index=False)  # 将数据库数据保存到excel中

    cursor.close()
    conn.close()

def data_insert_day_table():
    conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='yj_houses')
    cursor = conn.cursor()
    sql_day = 'call yj_houses_selling_info_day_calc;'
    sql_wekk = 'call yj_houses_selling_info_week_calc;'
    cursor.execute(sql_day)
    cursor.execute(sql_wekk)
    cursor.close()
    conn.close()
    print('存储过程执行完毕。')

def main():
    inc_time = datetime.datetime.now()
    # # analyze_data()
    try:
        with open('config.yaml', encoding='utf-8') as fp:
            yml_data = fp.read()
            print(yml_data)
            print('-------------')
            data = yaml.load(yml_data, Loader=yaml.FullLoader)
            # print(data['prd']['proxies_method'])
            # print(data['prd']['proxies_ip'])
            # print(data['prd']['proxies_port'])

            proxies = {data['prd']['proxies_method']: data['prd']['proxies_ip'] + ':' + data['prd']['proxies_port']}
            print('代理是：', proxies)
            # proxies = {"HTTP": '27.42.168.46:55481'}

            parse_insert(proxies)
            data_insert_day_table()
            db_save_excel_days()
            db_save_excel_calc_day()
            db_save_excel_calc_week()
            send_email()
            # send_email2()

            print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime((time.time())))), '今日任务执行完毕!!!')
    except:
        print('执行失败，请检查代理配置文件或者网页是否变更!!!')
    end_time = datetime.datetime.now()
    time_diff = end_time - inc_time
    print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime((time.time())))),' 任务执行用时： ',time_diff)

if __name__ == '__main__':
    main()

