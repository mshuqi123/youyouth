import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from utils.PublicEmail import get_report


def send_mail(file_new, email_list):
    # f = open(file_new, 'rb')
    #
    # mail_body = f.read()
    #
    # f.close()

    try:
        # mail_from = 'mami@moxiu.net'
        # me = 'qa<%s>' % mail_from
        # username = 'mami@moxiu.net'
        #
        # password = 'Sk3nbH3eb9XvpZfy'
        mail_from = 'qa_system@moxiu.net'
        me = 'qa<%s>' % mail_from
        username = 'qa_system@moxiu.net'

        password = 'Sk3nbH3eb9XvpZfy'

        msg = MIMEMultipart()
        html_file = open(file_new, 'rb').read()
        text = MIMEText(html_file, 'html', 'utf-8')

        text['Subject'] = Header('微锁屏功能自动化测试报告', 'utf-8')
        msg.attach(text)

        msg['Subject'] = Header(u'微锁屏功能自动化测试报告', 'utf-8')
        msg_file = MIMEText(html_file, 'html', 'utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(msg_file)

        # msg['from'] = me
        msg['from'] = me # 发送邮件的人
        msg['to'] = email_list
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.login(username, password)
        smtp.sendmail(msg['from'], msg['to'], msg.as_string())
        smtp.quit()
        print('send_mail success')

    except smtplib.SMTPException as e:
        print('send_mail failed : %s' % str(e))
        return False

if __name__ == "__main__":
    file_path = get_report()
    email_list = 'mami@moxiu.net'
    send_mail(file_path, email_list)