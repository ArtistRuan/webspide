# -*- cording:utf-8 -*-

'''
发送邮件，带文本附件、图片附件、html附件、excel附件、pdf附件等等
目前已实现：文本附件、图片附件、邮件内容图片  2021-10-12 01:46
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

def send_mails_with_attchment():
    # 发件人和收件人信息
    sender = 'm2ruan@126.com'
    # receivers = ['m2ruan@126.com','liangyangruan@qq.com','1135965756@qq.com']
    receivers = ['m2ruan@126.com','liangyangruan@qq.com']

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("m2ruan@126.com")
    message['To'] = Header("测试")
    # 抄送
    message['Cc'] = ''
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject,'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是测试邮件...','plain','utf-8'))

    # 构造附件1，传送当前目录下的test.txt文件
    f = open('test.txt','rb')
    att1 = MIMEText(f.read(),'base64','utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="words文档.txt"'
    att1.add_header('Content-Disposition','attachment',filename=('utf-8','','words文档.txt'))  # 解决中文附件名乱码问题
    message.attach(att1)
    f.close()

    # 构造附件2，传送当前目录下的we.jpg文件
    with open('we.jpg','rb') as fp:
        msgImage = MIMEImage(fp.read())
        msgImage['Content-Type'] = 'application/octet-stream'
        msgImage["Content-Disposition"] = 'attachment; filename="we.jpg"'
    message.attach(msgImage)
    fp.close()

    try:
        # 登录邮件服务器
        smtp_obj = smtplib.SMTP_SSL("smtp.126.com")  # 发件人邮箱中的SMTP服务器，端口是25
        smtp_obj.login("m2ruan@126.com", "YVLWGFNNIJANTMDR")  # 括号中对应的是发件人邮箱账号和邮箱密码
        # smtp_obj.set_debuglevel(1)  # 显示调试信息
        smtp_obj.sendmail(sender,receivers,message.as_string())
        print('邮件发送成功')
        smtp_obj.quit()
    except Exception as e:
        print('邮件发送失败',e)

if __name__ == '__main__':
    send_mails_with_attchment()