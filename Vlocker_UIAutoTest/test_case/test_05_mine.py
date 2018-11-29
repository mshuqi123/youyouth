# -*- coding: utf-8 -*-
import os
import sys
import unittest
from time import sleep

from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper


class MineTest(unittest.TestCase):
    "我的功能"

    def setUp(self):
        AppiumSetup().setUpClass(get_version='7.1.1', device_name='cea8dc6c')
        self.driver = AppiumSetup().driver
        self.b = BasePage.Base()
        self.h = FunctionHelper.Function()

    def test_a_mine_data(self):
        "未登录用户页面数据呈现"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath','//*[@text="我的"]')
        '校验我的页面内容呈现'
        d = self.b.find_element('xpath', '//*[@text="未登录"]', 5)
        self.assertTrue(d)
        # 消息通知
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_message"]', 5)
        self.assertTrue(d)
        # 本地主题
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_local_theme"]', 5)
        self.assertTrue(d)
        # 我的收藏
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_collection"]', 5)
        self.assertTrue(d)
        # 制作主题
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_diy_theme"]', 5)
        self.assertTrue(d)
        # 意见反馈
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_feedback"]', 5)
        self.assertTrue(d)
        # 版本升级
        d = self.b.find_element('xpath', '//*[@text="版本升级"]', 5)
        self.assertTrue(d)
        # 设置
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_setting"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    def test_b_mine_data(self):
        "本地主题内容"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath', '//*[@text="我的"]')
        '校验我的页面内容呈现'
        d = self.b.find_element('xpath', '//*[@text="未登录"]', 5)
        self.assertTrue(d)
        self.b.click_button('xpath','//*[@text="本地主题"]')
    #     校验本地主题页信息
        d = self.b.find_element('xpath', '//*[@text="视频"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@text="静态"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@text="编辑"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    def test_c_feedback(self):
        "意见反馈功能"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath', '//*[@text="我的"]')
        '校验我的页面内容呈现'
        d = self.b.find_element('xpath', '//*[@text="未登录"]', 5)
        self.assertTrue(d)
    #     点击意见反馈
        self.b.click_button('xpath', '//*[@text="意见反馈"]')
    #     校验反馈页信息
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/edit_des"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/add_image"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/edit_connect"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_commit"]', 5)
        self.assertTrue(d)
        # 输入反馈内容并提交
        self.b.send_keys('xpath', '//*[@resource-id="com.vlocker.locker:id/edit_des"]', '测试数据测试')
        self.b.send_keys('xpath', '//*[@resource-id="com.vlocker.locker:id/edit_connect"]', '123456')
        self.b.click_button('xpath', '//*[@text="提交"]')
        self.b.close_app()

    def test_d_make(self):
        "已登录用户制作主题"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath','//*[@text="我的"]')
        '校验我的页面内容呈现'
        d = self.b.find_element('xpath', '//*[@text="未登录"]', 5)
        self.assertTrue(d)
        # 消息通知
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_message"]', 5)
        self.assertTrue(d)
        # 制作主题
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_diy_theme"]', 5)
        self.assertTrue(d)
        d.click()
        # 登录页  输入用户名密码登录
        self.assertTrue(self.b.find_element('xpath', '//*[@text="登录"]', 5))
        # 输入用户名密码登录
        self.driver.find_element_by_id("com.vlocker.locker:id/edt_name").send_keys("1501149580200")
        self.driver.find_element_by_id("com.vlocker.locker:id/edt_password").send_keys("moxiutest1234")
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_login"]')
        sleep(2)
        # 登录后直接到导入视频页
        self.assertTrue(self.b.find_element('xpath', '//*[@text="导入视频"]', 5))
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_next"]')
        self.assertTrue(self.b.find_element('xpath', '//*[@text="裁剪视频"]', 5))
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_next"]')
        self.assertTrue(self.b.find_element('xpath', '//*[@text="选择封面"]', 10))
        self.b.click_button('xpath', '//*[@text="发布"]')
        # 到发布主题页选择分类后发布
        self.assertTrue(self.b.find_element('xpath', '//*[@text="主题发布"]', 10))
        self.driver.find_element_by_id("com.vlocker.locker:id/edt_theme_name").send_keys("帅哥")
        # 选择分类
        self.b.click_button('xpath', '//*[@text="选择一个分类"]')
        sleep(1)
        self.b.click_button('xpath', '//*[@text="男明星"]')
        sleep(1)
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/ll_go_labspage"]')
        # 添加标签
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/ll_labs_containt"]', 5)
        self.assertTrue(d)
        self.driver.find_element_by_id("com.vlocker.locker:id/ll_labs_containt").send_keys("帅哥")
        self.b.click_button('xpath', '//*[@text="确定"]')
        d = self.b.find_element('xpath', '//*[@text="保存到本地"]', 5)
        self.assertTrue(d)
        self.b.click_button('xpath', '//*[@text="保存到本地"]')
        d = self.b.find_element('xpath', '//*[@text="查看本地主题"]', 5)
        d = self.b.find_element('xpath', '//*[@text="应用该主题"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    def test_e_myfav(self):
        "我的收藏"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath','//*[@text="我的"]')
        # 消息通知
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_message"]', 5)
        self.assertTrue(d)
        # 点击我的收藏
        self.b.click_button('xpath', '//*[@text="我的收藏"]')
        # 校验收藏页信息
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_collect"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tool_bar_back"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    def test_f_mylike(self):
        "我的关注"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath','//*[@text="我的"]')
        # 消息通知
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_message"]', 5)
        self.assertTrue(d)
        # 点击我的关注
        self.b.click_button('xpath', '//*[@text="我的关注"]')
        # 校验关注页信息,没有关注时
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/follow_icon"]', 10)
        self.assertTrue(d)
        self.b.close_app()

    def test_g_myinfo(self):
        "我的信息"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath', '//*[@text="我的"]')
        # 消息通知
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_message"]', 5)
        self.assertTrue(d)
        # 校验我的信息
        # 头像
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/headerUserAvatar"]', 5)
        self.assertTrue(d)
        # 昵称
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_user_nickname"]', 5)
        self.assertTrue(d)
        # 签名
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_user_slogan"]', 5)
        self.assertTrue(d)
        # 点击到个人主页
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/headerUserAvatar"]')
        # 查看主页信息
        # 获赞、下载量、作品、编辑按钮
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mineHomeHeaderL1"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/theme_list_title"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tm_mine_edit_right"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    def test_h_updateinfo(self):
        "修改个人信息"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath', '//*[@text="我的"]')
        # 消息通知
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_message"]', 5)
        self.assertTrue(d)
        # 校验我的信息
        # 头像
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/headerUserAvatar"]', 5)
        self.assertTrue(d)
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/headerUserAvatar"]')
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tm_mine_edit_right"]', 5)
        self.assertTrue(d)
        d.click()
        # 修改个人资料
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_profile_cover"]', 5)
        self.assertTrue(d)
        # 修改昵称
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_profile_nickname"]')
        # self.b.send_keys('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_profile_nickname"]', 'qqqd')
        # self.driver.find_element_by_id("com.vlocker.locker:id/mine_profile_nickname").send_keys("改个昵称")
        # 保存
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_save"]')
        # 保存后返回到用户主页
        self.driver.keyevent(4)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tm_mine_edit_right"]', 5)
        self.assertTrue(d)
        # 恢复昵称
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tm_mine_edit_right"]', 5)
        self.assertTrue(d)
        d.click()
        # 修改个人资料
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_profile_cover"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    def test_i_logout(self):
        "退出登录"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        '点击我的'
        self.b.click_button('xpath', '//*[@text="我的"]')
        # 消息通知
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_message"]', 5)
        self.assertTrue(d)
        self.b.logout()
        self.b.close_app()

    def tearDown(self):
        AppiumSetup.tearDownClass()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(MineTest("test_i_logout"))
    unittest.TextTestRunner().run(suite)
