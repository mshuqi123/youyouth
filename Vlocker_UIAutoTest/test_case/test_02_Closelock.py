# -*- coding: utf-8 -*-
import os,time
import sys
import unittest
from time import sleep
from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper
class SafeTest(unittest.TestCase):
    "修复功能"
    def setUp(self):
        AppiumSetup().setUpClass(get_version='7.1.1', device_name='cea8dc6c')
        self.driver = AppiumSetup().driver
        self.b = BasePage.Base()
        self.h = FunctionHelper.Function()
    def test_a_close_syslock(self):
        "关闭系统锁屏"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        # 点击到工具页
        self.b.click_button('xpath', '//*[@text="工具"]')
        # 点击存在隐患
        os.system('adb shell input tap 541 1229')
        os.system('adb shell input tap 541 1229')
        os.system('adb shell input tap 541 1229')
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/tool_header_progress"]')
        #点击去解决
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/task_item_action"]')
        time.sleep(2)
        e = self.b.find_element('xpath', '//*[@text="100"]', 10)
        self.assertTrue(e)
        self.b.close_app()
    def tearDown(self):
        AppiumSetup.tearDownClass()
if __name__ == "__main__":
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(SafeTest("test_a_repair"))
    unittest.TextTestRunner().run(suite)
