# -*- coding: utf-8 -*-
import os
import sys
import unittest

from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper
from time import sleep

class TopicTest(unittest.TestCase):
    "主题页功能验证"

    def setUp(self):
        AppiumSetup().setUpClass(get_version='7.1.1', device_name='cea8dc6c')
        self.driver = AppiumSetup().driver
        self.b = BasePage.Base()
        self.h = FunctionHelper.Function()

    def test_a_topictype(self):
        self.b.totopic()
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/cardItemContainer"]', 10))
        # 点击全部分类
        self.b.click_button('xpath','//*[@text="全部分类"]')
        # 完整分类页内容呈现
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/tagsContainer"]',10))
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/subTagsContainer"]',10))
        # 找到父节点然后找子节点，按照下标找对应的text
        # 点击分类的第n个类别
        d = self.driver.find_element_by_id("com.vlocker.locker:id/tagsContainer")
        e = d.find_elements_by_id("com.vlocker.locker:id/tagName")
        e[4].click()
        # 再点击第一个子类
        f=self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/tagIcon"]',10)
        f.click()
        #查看分类详情页
        self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/listContainer"]',10)
        # 页面点击第9张主题图
        d=self.driver.find_elements_by_id("com.vlocker.locker:id/cardImagebg")
        d[8].click()
        self.b.close_app()

    def test_b_topicdetails(self):
        "主题详情页"
        self.b.totopic()
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/cardItemContainer"]', 10))
    #     点击分类中某一个进去到主题详情
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/imageView"]')
        d=self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/cardImagebg"]',10)
        d.click()
        # 查看详情页信息
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/rv_theme_preview"]',10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_title"]', 10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/view_theme_tag"]', 10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_download_count"]', 10))
        self.b.close_app()

    def test_c_topic_apply(self):
        "主题应用"
        self.b.totopic()
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/cardItemContainer"]', 10))
        #     点击分类中某一个进去到主题详情
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/imageView"]')
        d = self.b.find_elements('xpath', '//*[@resource-id="com.vlocker.locker:id/cardImagebg"]', 10)
        d[2].click()
        # 查看详情页信息
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/rv_theme_preview"]', 10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_title"]', 10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/view_theme_tag"]', 10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_download_count"]', 10))
        # 点击下载按钮
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/theme_progress_down"]')
        sleep(3)
        # 点击应用
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/theme_progress_down"]')
    #     校验是否已应用锁屏
        self.assertTrue(self.b.isElement('text','滑动以解锁'))
        self.b.close_app()

    def test_d_topic_search(self):
        "主题搜索"
        self.b.totopic()
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/cardItemContainer"]', 10))
        # 搜索框输入主题关键字搜索
        '''点击搜索框到搜索页面'''
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]')
        '等待页面加载'
        a = self.b.find_element('xpath', '//*[@text="搜索"]', 10)
        self.assertTrue(a)
        # 输入关键字搜索
        self.driver.find_element_by_id("com.vlocker.locker:id/search_edittext").send_keys("霍建华")
        self.b.click_button('xpath', '//*[@text="搜索"]')
        # 校验跳转页是主题搜索页
        e = self.b.find_element('xpath', '//*[@text="综合"]', 10)
        self.assertTrue(e)
        # 点击第一个主题图
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/image_layout"]')
        self.b.close_app()

    def test_e_topic_share(self):
        "主题分享"
        self.b.totopic()
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/cardItemContainer"]', 10))
        #     点击分类中某一个进去到主题详情
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/imageView"]')
        d = self.b.find_elements('xpath', '//*[@resource-id="com.vlocker.locker:id/cardImagebg"]', 10)
        d[2].click()
        # 查看详情页信息
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/rv_theme_preview"]', 10))
        '点击分享'
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/fab_share"]')
        #     分享路径
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mx_share_layout"]', 6))
        #     点击分享到qq
        self.b.click_button('xpath', '//*[@text="QQ"]')
        sleep(2)
        # 发送
        self.b.click_button('xpath', '//*[@text="魔秀大树"]')
        d = self.b.find_element('xpath', '//*[@resource-id="com.tencent.mobileqq:id/dialogRightBtn"]', 10)
        d.click()
        #     成功后点击回到微锁屏
        # self.assertTrue(self.b.find_element('xpath', '//*[@text="已发送"]', 10))
        sleep(3)
        self.b.click_button('xpath', '//*[@text="返回微锁屏"]')
        self.driver.keyevent(4)
        sleep(1)
        self.driver.keyevent(4)
        sleep(2)
        self.b.click_button('xpath','//*[@text="我的"]')
        '在当前类最后一个用例后退出登录'
        '退出登录'
        # self.b.logout()
        self.b.close_app()

    def tearDown(self):
        AppiumSetup.tearDownClass()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(TopicTest("test_e_topic_share"))
    unittest.TextTestRunner().run(suite)

