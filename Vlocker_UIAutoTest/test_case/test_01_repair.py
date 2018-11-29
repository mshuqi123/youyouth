# -*-coding:utf-8-*-
from appium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import sys
import unittest
import subprocess
from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper
import time
from utils import version_crawler
class OnekeyRepair (unittest.TestCase):
    "一键修复"
    @classmethod
    def setUpClass(cls):
        cmd = 'adb shell input keyevent 26'
        os.popen(cmd)
        time.sleep(2)
        # 右滑解锁
        os.system('adb shell input swipe 210 1080 680 1080 500 ')
        time.sleep(2)
        os.popen('adb uninstall com.vlocker.locker')
        # version_crawler.download_app(0)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        performance_data = os.path.join(base_dir, 'app')
        # command = 'adb install -r D:\moxiu\Vlocker_UIAutoTest\\app\\default.apk'
        command = 'adb install -r {}\\default.apk'.format(performance_data)
        subprocess.getstatusoutput(command)
    def setUp(self):
        # 启动APP
        os.system('adb shell am start -W -n com.vlocker.locker/com.vlocker.settings.SettingsActivity')
    def tearDown(self):
        time.sleep(30)
        os.system('adb shell input tap 541 1229')
        os.system('adb shell input keyevent 3')
    def test_Coldboot(self):
        '''首次启动锁屏APP进行一键修复'''
        time.sleep(3)
        os.system('adb shell input tap 541 1229')
        time.sleep(15)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/repair_now"]')
        os.system('adb shell input tap 227 1661')
        time.sleep(2)
        os.system('adb shell input tap 541 1229')
        time.sleep(2)
        os.system('adb shell input tap 541 1229')
        time.sleep(3)
        os.system('adb shell input swipe 540 1620 540 540 500 ')
        time.sleep(3)
        os.system('adb shell input tap 75 1625')
        time.sleep(3)
        os.system('adb shell input tap 849 221')
        time.sleep(3)
        os.system('adb shell input tap 541 1228')
        os.system('adb shell input tap 541 1229')
        # d = self.b.find_element('xpath', '//*[@text="热门"]', 60)
        # self.assertTrue(d)
if __name__=='__main__':
    unittest.main(warnings="ignore")
