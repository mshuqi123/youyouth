# -*- coding: utf-8 -*-
import os
import sys
import unittest
import subprocess
from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper


class HomeTest(unittest.TestCase):
    "一级界面"
    def setUp(self):
        AppiumSetup().setUpClass(get_version='7.1.1', device_name='cea8dc6c')
        self.driver = AppiumSetup().driver
        self.b = BasePage.Base()
        self.h = FunctionHelper.Function()
    @AppiumSetup.add
    def test_a_hot_media(self):
        "视频热门数据浏览"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 5)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/image_layout"]', 10))
        self.b.close_app()

    @AppiumSetup.add
    def test_b_default_page(self):
        "锁屏app打开默认页"
        element = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]', 10)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@text="搜索视频"]', 2)
        self.assertTrue(element)
        #         com.vlocker.locker:id/title
        element = self.b.find_element('xpath', '//*[@text="最新"]', 2)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@text="分类"]', 2)
        self.assertTrue(element)
        element =self.b.find_element('xpath', '//*[@text="互动主题"]', 2)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@text="我还想要"]', 2)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@text="大事件"]', 2)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@text="热门视频锁屏"]', 2)
        self.assertTrue(element)
        self.b.close_app()

    @AppiumSetup.add
    def test_c_new_page(self):
        "最新视频页呈现"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 点击到最新
        self.b.click_button('xpath', '//*[@text="最新"]', 10)
        # 视频制作入口
        element =self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/btn_video_upload"]', 10)
        self.assertTrue(element)
        # 视频时长
        element = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/time"]', 10)
        self.assertTrue(element)
        self.b.close_app()

    @AppiumSetup.add
    def test_d_type_page(self):
        "分类页面呈现"
        d = self.b.find_element('xpath', '//*[@text="热门"]',10)
        self.assertTrue(d)
        # 点击到分类
        self.b.click_button('xpath','//*[@text="分类"]', 10)
        # tag 名称、头像、 指示箭头
        element = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tag_title"]', 10)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tag_icon"]', 10)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/icon_arrow"]', 10)
        self.assertTrue(element)
        element = self.b.find_element('xpath', '//*[@text="男明星"]', 10)
        self.assertTrue(element)
        self.b.swipe_up(2)
        self.b.close_app()
    def tearDown(self):
        AppiumSetup.tearDownClass()
if __name__ == "__main__":
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(HomeTest("test_d_type_page"))
    unittest.TextTestRunner().run(suite)
