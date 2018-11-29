# -*- coding: utf-8 -*-
import os
import unittest
import time

import sys
# from eMail import send_email
from TestReport import HTMLTestRunner_cn
from eMail.send_email import *
# from test_case.test_a_home import HomeTest
# from test_case.test_c_media import MediaTest
# from test_case.test_b_search import SearchTest
# from test_case.test_d_topic import TopicTest
# from test_case.test_e_tool import ToolTest
# from test_case.test_f_mine import MineTest
# from test_case.test_g_safe import SafeTest
from utils.PublicEmail import *
from appium_setup import *
test_dir = os.path.join(os.getcwd(), 'test_case')
test_report = os.path.join(os.getcwd(), 'TestReport')
now = time.strftime("%Y-%m-%d-%H_%M_%S")
filename = test_report + "\\result" + now + ".html"

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    f = open(filename, 'wb')
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=f, title='微锁屏功能自动化测试报告', description='TestReport', verbosity=2, retry=0)
    runner.run(suite)
    # email = 'qa_d@moxiu.net'
    email = 'mashuqi@moxiu.net'
    send_mail(filename, email)