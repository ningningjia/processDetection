# coding=utf-8
import time
import smtplib
import psutil
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_port = 587  # 服务器端口
mail_user = "xxxx@qq.com"  # 用户名
mail_pass = "xxxx"  # 口令(QQ邮箱为授权码)
sender = "xxxx@qq.com"  # 发件人
receiver = "xxxx@foxmail.com"  # 收件人


def email_alert(alert):
    message = MIMEText(alert, 'plain', 'utf-8')
    message['From'] = Header(sender, 'utf-8')  # 发送者
    message['To'] = Header(receiver, 'utf-8')  # 接收者
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtp = smtplib.SMTP(mail_host, mail_port)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(from_addr=sender, to_addrs=receiver, msg=message.as_string())
        smtp.close()
        print "Tips: 邮件发送成功"
    except smtplib.SMTPException as e:
        print "Error: 无法发送邮件"+ str(e)


if __name__ == '__main__':
    attack_pid = 1234
    virus_pid = 1245
    spam_pid = 1241
    mali_pid = 1414
    device_pid = 1341
    while True:
        alert_content = ""
        toDo = False
        if not psutil.pid_exists(attack_pid):
            print "网络攻击进程异常终止，请检查！"
            alert_content += "pid:{}---网络攻击进程停止\n".format(str(attack_pid))
            toDo = True
        if not psutil.pid_exists(virus_pid):
            print "病毒感染进程停止，请检查！"
            alert_content += "pid:{}---病毒感染进程停止\n".format(str(virus_pid))
            toDo = True
        if not psutil.pid_exists(spam_pid):
            print "垃圾邮件进程停止，请检查！"
            alert_content += "pid:{}---垃圾邮件进程停止\n".format(str(spam_pid))
            toDo = True
        if not psutil.pid_exists(mali_pid):
            print "恶意邮件进程停止，请检查！"
            alert_content += "pid:{}---恶意邮件进程停止\n".format(str(mali_pid))
            toDo = True
        if not psutil.pid_exists(device_pid):
            print "防病毒安装进程停止，请检查！"
            alert_content += "pid:{}---防病毒安装进程停止\n".format(str(device_pid))
            toDo = True
        alert_content += "请登录上报程序所在机器进行检查"
        if toDo is True:
            email_alert(alert_content)
        time.sleep(3600)
