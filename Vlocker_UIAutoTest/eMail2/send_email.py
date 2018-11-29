# coding:utf-8
import unittest,time,os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.mime.text import MIMEText
import smtplib
class Send_eMail(object):
    def report_email(self,report_path,receiver):
        a = open(report_path, "rb")
        mail_body = a.read()
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = u"有样APP功能UI自动化测试报告"
        msg["from"] = "mashuqi@moxiu.net"
        msg["to"] = ";".join(receiver)
        msg.attach(body)
        att = MIMEText(mail_body,'base64', _charset='utf-8')
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="youyang_ui_baogao.html"'
        msg.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect("smtp.exmail.qq.com")
        smtp.login("mashuqi@moxiu.net", "Msq130722")
        smtp.sendmail("mashuqi@moxiu.net", receiver, msg.as_string())
        smtp.quit()
    def Memory_email(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        performance_data = os.path.join(base_dir, 'data')
        report_path = ('%s\\memory_report.html' % (performance_data))
        receiver = ["mashuqi@moxiu.net"]
        a = open(report_path, "rb")
        mail_body = a.read()
        msg = MIMEMultipart()
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = u"有样短视频APP性能测试内存报表"
        msg["from"] = "mashuqi@moxiu.net"
        msg["to"] = ";".join(receiver)
        msg.attach(body)
        att = MIMEText(mail_body, 'base64', _charset='utf-8')
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="youyangAPP_xnbg.html"'
        msg.attach(att)
        smtp = smtplib.SMTP()
        smtp.connect("smtp.exmail.qq.com")
        smtp.login("mashuqi@moxiu.net", "Msq130722")
        smtp.sendmail("mashuqi@moxiu.net", receiver, msg.as_string())
        smtp.quit()
if __name__=="__main__":
    a = Send_eMail()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    performance_data = os.path.join(base_dir)
    report_path = performance_data + "\\TestReport\\result2018-11-07 12_19_08.html"
    receiver = ["mashuqi@moxiu.net"]
    # # receiver = ["qa_d@moxiu.net"]
    a.report_email(report_path,receiver)
    # Memory_email()                #发送内存html报告给自己的邮箱













