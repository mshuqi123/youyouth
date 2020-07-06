# coding:utf-8
import unittest,time,os
from TestReport import HTMLTestRunner
from TestReport import HTMLTestRunner_cn
from unittest import defaultTestLoader
import test
from tool import GeneratememoryReport
from tool import GenerateExcelReports
from eMail import send_email
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
performance_data = os.path.join(base_dir, 'youyouth_UIAutoTest')
# case_dir = r"D:\moxiu\youyang\test_case"
case_dir = ('%s\\test_case' % (performance_data))
def all_case():
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite
if __name__=="__main__":
    runner = unittest.TextTestRunner()
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    performance_data = os.path.join(base_dir, 'youyouth_UIAutoTest')
    report_path = performance_data + "\\TestReport\\result" + now + ".html"
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'清理专家APP功能UI自动化测试报告',description=u"测试设备：锤子OS105", verbosity=2, retry=0)
    runner.run(all_case())
    fp.close()
    email = send_email.Send_eMail()
    receiver = ["mashuqi@moxiu.net"]
    # receiver = ["qa_d@moxiu.net"]
    email.report_email(report_path,receiver)
    memoryhtml = GeneratememoryReport.GenerateReport()        #调用生成html的方法
    memoryhtml.get_mem_data()
    excel = GenerateExcelReports.excelReports()          #调用生成excel的方法
    excel.GenerateXls()
    email.Memory_email()                #发送内存html报告给自己的邮箱
    os.remove(('%s\\data\\memory_data.txt' % (performance_data)))











