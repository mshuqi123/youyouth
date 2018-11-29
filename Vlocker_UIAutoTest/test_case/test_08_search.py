# -*- coding: utf-8 -*-
import os
import sys
import unittest

from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper


class SearchTest(unittest.TestCase):
    "搜索功能"

    def setUp(self):
        AppiumSetup().setUpClass(get_version='7.1.1', device_name='cea8dc6c')
        self.driver = AppiumSetup().driver
        self.b = BasePage.Base()
        self.h = FunctionHelper.Function()

    def test_a_hot_data(self):
        "搜索热门数据加载"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        '''点击搜索框'''
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/search"]')
        '''判断搜索页数据加载'''
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/back"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tag_hot_header"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tag_hot"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    def test_b_keyword_suggest(self):
        "关键字输入联想"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        '''点击搜索框
        '''
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]')
        # 输入关键字等待，查看联想
        self.b.send_keys('xpath', '//*[@resource-id="com.vlocker.locker:id/search_edittext"]', '霍建华')
        # self.driver.find_element_by_id("com.vlocker.locker:id/search_edittext").send_keys("霍建华")
        # 校验搜索联想数据
        a=self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/suggest_content"]', 10)
        self.assertTrue(a)
        c=self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/title"]', 10)
        self.assertTrue(c)
        # 校验搜索联想内容
        d= self.driver.find_element_by_id("com.vlocker.locker:id/title").text
        self.assertEqual("霍建华", d, None)
        # 点击联想信息跳转到搜索结果页
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]')
        # 校验跳转页
        e = self.b.find_element('xpath','//*[@text="视频"]', 10)
        self.assertTrue(e)
        # 按时间
        f = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/sort_ctime"]', 10)
        self.assertTrue(f)
        # 按下载量
        f = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/sort_downnum"]', 10)
        self.assertTrue(f)
        # 视频内容存在
        f=self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/image_layout"]',10)
        self.assertTrue(f)
        self.b.close_app()

    def test_c_keyword_search(self):
        "关键字点击搜索"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        '''点击搜索框'''
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]')
        # 输入关键字搜索
        self.driver.find_element_by_id("com.vlocker.locker:id/search_edittext").send_keys("霍建华")
        self.b.click_button('xpath','//*[@text="搜索"]')
        # 校验跳转页
        e = self.b.find_element('xpath', '//*[@text="视频"]', 10)
        self.assertTrue(e)
        # 按时间
        f = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/sort_ctime"]', 10)
        self.assertTrue(f)
        # 按下载量
        f = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/sort_downnum"]', 10)
        self.assertTrue(f)
        # 视频内容存在
        f = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/image_layout"]', 10)
        self.assertTrue(f)
        self.b.close_app()

    def test_d_nokeyword_search(self):
        "非关键字点击搜索"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        '''点击搜索框到搜索页面'''
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]')
        # 输入关键字搜索
        self.driver.find_element_by_id("com.vlocker.locker:id/search_edittext").send_keys("疯狂五十的是")
        self.b.click_button('xpath', '//*[@text="搜索"]')
        # 校验跳转结果页
        a=self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/netErrAndLoad"]',10)
        self.assertTrue(a)
        b=self.b.find_element('xpath','//*[@text="一片荒芜，什么都没找到..."]', 10)
        self.assertTrue(b)
        c = self.driver.find_element_by_id("com.vlocker.locker:id/btn_post").text
        self.assertEqual("一键求视频", c)
        # 点击一键求视频
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/btn_post"]')
        # 校验已发请求后button内容
        c = self.driver.find_element_by_id("com.vlocker.locker:id/btn_post").text
        self.assertEqual("已发请求", c)
        self.b.close_app()

    def test_e_change(self):
        "热搜换一换功能"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        '''点击搜索框到搜索页面'''
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]')
        '等待页面加载'
        a = self.b.find_element('xpath', '//*[@text="搜索"]', 10)
        self.assertTrue(a)
        c = self.driver.find_element_by_id("com.vlocker.locker:id/tag_text").text
        '点击换一换'
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/btn_hot_refresh"]')
        '查看是否有变更'
        d = self.driver.find_element_by_id("com.vlocker.locker:id/tag_text").text
        self.assertNotEqual(d, c)
        self.b.close_app()

    def test_f_history(self):
        "搜索历史"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        '''点击搜索框到搜索页面'''
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]')
        '等待页面加载'
        a = self.b.find_element('xpath', '//*[@text="搜索"]', 10)
        self.assertTrue(a)
        '校验搜索历史图标'
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/icon_history"]',10))
        '校验搜索历史'
        self.assertTrue(self.b.find_element('xpath','//*[@text="搜索历史"]', 10))
        '历史记录里面第一个搜索历史内容校验'
        # 找到父节点然后找子节点，按照下标找对应的text
        d = self.driver.find_element_by_id("com.vlocker.locker:id/tag_history")
        e = d.find_elements_by_id("com.vlocker.locker:id/tag_text")

        self.assertEqual("疯狂五十的是", e[0].text)
        self.b.close_app()

    def test_g_historydel(self):
        "搜索历史删除"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        '''点击搜索框到搜索页面'''
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/search"]')
        '等待页面加载'
        a = self.b.find_element('xpath', '//*[@text="搜索"]', 10)
        self.assertTrue(a)
        # 点击删除搜索历史
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_history_clean"]')
        # 判断元素不存在
        self.b.isElement("resource-id","com.vlocker.locker:id/tag_history_header")
        self.b.close_app()

    def tearDown(self):
        AppiumSetup.tearDownClass()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(SearchTest("test_g_historydel"))
    unittest.TextTestRunner().run(suite)
