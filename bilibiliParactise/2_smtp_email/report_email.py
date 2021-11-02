import pymysql
import pandas as pd
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
import schedule, time


def create_report(host, port, user, passwd, db, sql, annex_path):
    '从数据库读取报表数据,以excel形式将报表存到本地'
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取执行结果
    result = [list(x) for x in result]
    col_result = cursor.description  # 获取查询结果的字段描述
    columns = [x[0] for x in col_result]
    data = pd.DataFrame(result, columns=columns)
    data.to_excel(annex_path, index=False)
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接


def send_email(file_name, annex_path):
    '#创建报表和发送邮件'
    try:
        file_name_new = str(datetime.datetime.now().date()) + file_name  # 根据当前日期拼接附件名称
        annex_path_new = annex_path + '/' + file_name_new  # 拼接报表存储完整路径
        create_report(host, port, user, passwd, db, sql, annex_path_new)  # 创建报表

        # 传入邮件发送者、接受者、抄送者邮箱以及主题
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ','.join(receiver)
        message['Cc'] = ";".join(Cc_receiver)
        message['Subject'] = Header(str(datetime.datetime.now().date()) + title, 'utf-8')

        # 添加邮件内容
        text_content = MIMEText(content)
        message.attach(text_content)

        # 添加附件
        annex = MIMEApplication(open(annex_path_new, 'rb').read())  # 打开附件
        annex.add_header('Content-Disposition', 'attachment', filename=file_name_new)
        message.attach(annex)

        # image_path = 'C:/Users/yang/Desktop/1.png'
        # image = MIMEImage(open(image_path , 'rb').read(), imageFile.split('.')[-1])
        # image.add_header('Content-Disposition', 'attachment', filename=image_path.split('/')[-1])
        # message.attach(image)

        # 登入邮箱发送报表
        server = smtplib.SMTP(smtp_ip)  # 端口默认是25,所以不用指定
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        print('success!', datetime.datetime.now())

    except smtplib.SMTPException as e:
        print('error:', e, datetime.datetime.now())  # 打印错误


if __name__ == '__main__':
    # 参数设置
    # 数据库参数设置
    host = 'localhost'  # 数据库ip地址
    port = 3306  # 端口
    user = 'root'  # 账户
    passwd = '123456'  # 密码
    db = 'student'  # 数据库名称
    sql = "SELECT age,name,id,birthday FROM student;"  # 报表查询语句

    # 发送邮件参数设置
    sender = 'm2ruan@126.com'  # 发送者邮箱
    password = 'YVLWGFNNIJANTMDR'  # 发送者邮箱授权码
    smtp_ip = 'smtp.126.com'  # smtp服务器ip,根据发送者邮箱而定
    receiver = ['1576276395@qq.com', 'm2ruan@126.com']  # 接收者邮箱
    Cc_receiver = ['ruanshikao@outlook.com', 'ruanshikao@126.com']  # 抄送者邮箱
    title = '订单日报'  # 邮件主题
    content = 'hello,这是今天的订单日报！'  # 邮件内容
    file_name = '订单日报.xlsx'  # 报表名称
    annex_path = 'bilibiliParactise/2_smtp_email/2019年广东省县级以上机关和珠三角地区乡镇机关招录公务员职位表sazx.xls'  # 报表存储路径，也是附件路径
    ts = '23:19'  # 发送邮件的定时设置,每天ts时刻运行

    # 自动创建报表并发送邮件
    print('邮件定时发送任务启动中.......')
    schedule.every().day.at(ts).do(send_email, file_name, annex_path)  # 每天某时刻运行
    while True:
        schedule.run_pending()  # 运行所有可运行的任务
        time.sleep(43200)  # 因为每次发送邮件的间隔时间是一天左右，所以休眠时间可以设长些