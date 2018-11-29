# -*- coding: utf-8 -*-
import os
import unittest
from appium import webdriver
from TestReport import HTMLTestRunner
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
apk_path = os.path.join(base_dir, 'Vlocker_UIAutoTest\\app')
class AppiumSetup(unittest.TestCase):
    """
    TEST mathfunc.py
    """
    @classmethod
    def setUpClass(cls, get_version=None, device_name=None):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = get_version
        desired_caps['deviceName'] = device_name
        desired_caps['appPackage'] = 'com.vlocker.locker'
        desired_caps['noReset'] = True
        desired_caps['appActivity'] = 'com.vlocker.settings.SettingsActivity'
        desired_caps['newCommandTimeout'] = '600'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # desired_caps["automationName"] = "uiautomator2"
        # desired_caps['javascriptEnabled'] = True
        # desired_caps['automationName'] = 'Selendroid'
        desired_caps['app'] = apk_path + '\\default.apk'
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True
    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)
    def cleanup(self):
        pass
    # 异常截图
    def add(func):
        def warpper(self):
            try:
                func(self)
            except AssertionError:
                self.add_img()
        return warpper
if __name__ == "__main__":
    unittest.main(verbosity=2)
