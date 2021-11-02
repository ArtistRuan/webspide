# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText  # 邮件正文
from email.header import Header  # 邮件头


def send_email():
    # 登录邮件服务器
    smtp_obj = smtplib.SMTP_SSL("smtp.126.com")  # 发件人邮箱中的SMTP服务器，端口是25
    smtp_obj.login("m2ruan@126.com","YVLWGFNNIJANTMDR")  # 括号中对应的是发件人邮箱账号和邮箱密码
    # smtp_obj.set_debuglevel(1)  # 显示调试信息

    # 设置邮件头信息
    msg = MIMEText("请查看邮件内容","plain","utf-8")
    msg["From"] = Header("m2ruan@126.com")  # 发送者
    # msg['From'] = 'm2ruan@126.com'
    msg['To'] = 'you'   # 接收者
    # msg['from'] = 'm2ruan@126.com'
    # msg['to'] = 'you'  # 接收者
    msg["Subject"] = Header("python_demo","utf-8")  # 主题

    #  发送
    smtp_obj.sendmail("m2ruan@126.com",["m2ruan@126.com","ruanshikao@outlook.com","liangyangruan@qq.com"],msg.as_string())

if __name__ == '__main__':
    try:
        send_email()
    except Exception as e:
        print('邮件发送失败',e)