#!/usr/bin/python3

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def run_email():
    sender = 'm2ruan@126.com'
    receivers = ['m2ruan@126.com','1576276395@qq.com','1135965756@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header("m2ruan@126.com")
    msgRoot['To'] = Header("测试")
    subject = 'Python SMTP 邮件测试'
    msgRoot['Subject'] = Header(subject, 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.baidu.com">百度一下</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = open('we.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    try:
        # 登录邮件服务器
        smtp_obj = smtplib.SMTP_SSL("smtp.126.com")  # 发件人邮箱中的SMTP服务器，端口是25
        smtp_obj.login("m2ruan@126.com", "YVLWGFNNIJANTMDR")  # 括号中对应的是发件人邮箱账号和邮箱密码
        # smtp_obj.set_debuglevel(1)  # 显示调试信息
        smtp_obj.sendmail(sender, receivers, msgRoot.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件",e)

def main():
    run_email()

if __name__ == '__main__':
    main()