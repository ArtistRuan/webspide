
from win32com.client.gencache import EnsureDispatch
import win32com.client as win32

def send_email():
    outlook = EnsureDispatch('outlook.application')
    mail = outlook.CreateItem(0)  # 获取发送邮件功能的对象

    mail.To = "m2ruan@126.com;ruanshikao@outlook.com;liangyangruan@qq.com"  # 收件人，多个用分号隔开
    mail.Cc = "ruanshikao@126.com;ruanshikao@gmail.com"  # 抄送，多个用分号隔开
    mail.Subject = 'test Subject'  # 邮件标题
    mail.Body = 'test Body'  # 邮件内容
    mail.Attachments.add('we.jpg')  # 设置附件
    mail.Send()

def main():
    send_email()

if __name__ == '__main__':
    main()