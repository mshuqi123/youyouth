# -*- coding: utf-8 -*-
import os
import sys
import unittest
from time import sleep
from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper


class ToolTest(unittest.TestCase):
    "工具页基础功能"
    def setUp(self):
        AppiumSetup().setUpClass(get_version='7.1.1', device_name='cea8dc6c')
        self.driver = AppiumSetup().driver
        self.b = BasePage.Base()
        self.h = FunctionHelper.Function()

    def test_a_tool_default(self):
        "工具页整体内容"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        # 点击到工具页
        self.b.click_button('xpath', '//*[@text="工具"]')
        # 页面呈现,
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tool_header_progress"]', 10))
        self.b.close_app()

    def test_b_tool_lock(self):
        "锁屏功能"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 5)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        # 点击到工具页
        self.b.click_button('xpath', '//*[@text="工具"]')
        # 页面呈现,
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tool_first_line"]', 10))
        self.b.click_button('xpath','//*[@text="锁屏功能"]')
        sleep(2)
        #锁屏功能页面
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/setting_msg_layout"]',10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/setting_music_layout"]',10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/setting_toolbox_layout"]',10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/setting_weather_item"]',10))
        self.assertTrue(
            self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/setting_music_check"]', 10))
        # self.b.swipe_up(1)
        d=self.b.find_element('xpath','//*[@text="延迟锁屏"]',10)
        self.assertTrue(d)
        self.b.close_app()

    @AppiumSetup.add
    def test_c_tool_applock(self):
        "应用锁功能校验"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        # 点击到工具页
        self.b.click_button('xpath', '//*[@text="工具"]')
        # 页面呈现,
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tool_first_line"]', 10))
        self.b.click_button('xpath','//*[@text="应用锁"]')
#         查看应用锁默认页面
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/l_app_select_count"]', 10))
        self.assertTrue(
            self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/app_selected"]', 10))
        self.assertTrue(
            self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/app_hot"]', 10))
        self.assertTrue(
            self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/app_sort_desc"]', 10))
#       点击下一步
        self.b.click_button('xpath','//*[@text="下一步"]')
        # 设置密码页查看
        self.assertTrue(
            self.b.find_element('xpath', '//*[@text="使用数字密码"]', 10))
        self.b.click_button('xpath','//*[@text="使用数字密码"]')
        self.assertTrue(
            self.b.find_element('xpath', '//*[@text="设置密码位数"]', 10))
#         点击下一步
        self.b.click_button('xpath', '//*[@text="下一步>"]')
#         密码设置com.vlocker.locker:id/locknum
        d = self.driver.find_element_by_id("com.vlocker.locker:id/locknum")
        e = d.find_elements_by_id("android.widget.TextView")
        sleep(3)
        self.b.click_button('xpath', '//*[@text="1"]')
        self.b.click_button('xpath', '//*[@text="2"]')
        self.b.click_button('xpath', '//*[@text="3"]')
        self.b.click_button('xpath', '//*[@text="4"]')
#         再次输入
        self.assertTrue(
            self.b.find_element('xpath', '//*[@text="请重复密码"]', 10))
        self.b.click_button('xpath', '//*[@text="1"]')
        self.b.click_button('xpath', '//*[@text="2"]')
        self.b.click_button('xpath', '//*[@text="3"]')
        self.b.click_button('xpath', '//*[@text="4"]')
        sleep(2)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]')
        # sleep(2)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]')
#         到密码保护页,只有首次安装app之后才会有密保输入
        self.assertTrue(
            self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_question"]', 10))
        self.b.click_button('xpath', '//*[@text="生日是?"]')
        sleep(3)
        # c = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]', 10)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]')
        # self.assertTrue(c)
        # c.click()
        os.system('adb shell input tap 228 1887')
        sleep(2)
        self.assertTrue(
            self.b.find_element('xpath', '//*[@text="应用锁"]', 10))
        sleep(2)
        self.b.click_button('xpath', '//*[@text="应用锁"]')
        self.b.click_button('xpath', '//*[@text="1"]')
        self.b.click_button('xpath', '//*[@text="2"]')
        self.b.click_button('xpath', '//*[@text="3"]')
        self.b.click_button('xpath', '//*[@text="4"]')
        self.assertTrue(
            self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/setting_enable_applock_img"]', 10))
        # 返回桌面点击图库
        # self.driver.keyevent(3)
        # sleep(3)
        # # 启动相册查看
        # cmd = "adb shell am start -W -n  com.vivo.gallery/com.android.gallery3d.vivo.GalleryTabActivity "
        # self.content = os.popen(cmd)
        # sleep(2)
        # # 校验应用锁设置生效
        # self.assertTrue(
        #     self.b.find_element('xpath', '//*[@text="输入密码"]', 10))
        self.b.close_app()

    def test_d_restartlock(self):
        "重启锁屏"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        self.b.click_button('xpath', '//*[@text="我的"]')
        d = self.b.find_element('xpath', '//*[@text="设置"]', 10)
        d.click()
        # 关闭锁屏开关
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/close_lock_check"]', 10)
        d.click()
        # 点击开启锁屏
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/start_lock"]', 10)
        d.click()
        self.b.close_app()

    @AppiumSetup.add
    def test_e_lockpassword(self):
        "锁屏密码设置应用"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        # 点击到工具页
        self.b.click_button('xpath', '//*[@text="工具"]')
        # 点击锁屏密码
        self.b.click_button('xpath', '//*[@text="锁屏密码"]')
        d = self.b.find_element('xpath', '//*[@text="密码设置"]', 5)
        self.assertTrue(d)
        # 点击设置数字密码
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/setting_enable_num_locker_img"]', 10)
        d.click()
        sleep(2)
        # 下一步
        d = self.b.find_element('xpath', '//*[@text="下一步>"]', 10)
        d.click()
        d = self.b.find_element('xpath', '//*[@text="4位密码"]', 5)
        self.assertTrue(d)
        sleep(3)
        self.b.click_button('xpath', '//*[@text="1"]')
        self.b.click_button('xpath', '//*[@text="2"]')
        self.b.click_button('xpath', '//*[@text="3"]')
        self.b.click_button('xpath', '//*[@text="4"]')
        #         再次输入
        self.assertTrue(
            self.b.find_element('xpath', '//*[@text="请重复密码"]', 10))
        self.b.click_button('xpath', '//*[@text="1"]')
        self.b.click_button('xpath', '//*[@text="2"]')
        self.b.click_button('xpath', '//*[@text="3"]')
        self.b.click_button('xpath', '//*[@text="4"]')
        # sleep(2)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_question"]')
        # sleep(2)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]')
        # # 查看密码类型
        # d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tool_bar_title"]', 10)
        # self.assertTrue(d)
        sleep(2)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]')
        # sleep(2)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]')
        #         到密码保护页,只有首次安装app之后才会有密保输入
        self.assertTrue(
            self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_question"]', 10))
        self.b.click_button('xpath', '//*[@text="生日是?"]')
        sleep(3)
        # c = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]', 10)
        # self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_question_ok"]')
        # self.assertTrue(c)
        # c.click()
        os.system('adb shell input tap 228 1887')
        sleep(2)
        # 灭屏亮屏查看锁屏应用
        self.driver.lock(1)
        # self.driver.unlock()
        # 点亮屏幕
        cmd = 'adb shell input keyevent 26'
        os.popen(cmd)
        sleep(2)
        # 右滑解锁
        self.b.swipe_right(1)
        sleep(2)
        # 当前密码锁屏页校验
        d = self.b.find_element('xpath', '//*[@text="输入密码"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@text="美化密码"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    @AppiumSetup.add
    def test_f_unlocknum(self):
        "解锁数字密码锁屏"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 5)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        # 灭屏亮屏查看锁屏应用
        self.driver.lock(1)
        # self.driver.unlock()
        cmd = 'adb shell input keyevent 26'
        os.popen(cmd)
        sleep(3)
        # 右滑解锁
        self.b.swipe_right(1)
        sleep(2)
        d = self.b.find_element('xpath', '//*[@text="美化密码"]', 5)
        self.assertTrue(d)
    #     解锁
        self.b.click_button('xpath', '//*[@text="1"]')
        self.b.click_button('xpath', '//*[@text="2"]')
        self.b.click_button('xpath', '//*[@text="3"]')
        self.b.click_button('xpath', '//*[@text="4"]')
        d = self.b.find_element('xpath', '//*[@text="互动主题"]', 5)
        self.assertTrue(d)
        self.b.close_app()

    @AppiumSetup.add
    def test_g_change_nopassword(self):
        " 密码切换无密码锁屏 "
        d = self.b.find_element('xpath', '//*[@text="热门"]', 5)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 10))
        #     点击工具
        self.b.click_button('xpath', '//*[@text="工具"]')
        # 页面呈现,
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tool_first_line"]', 10))
        # 锁屏密码页
        sleep(3)
        self.b.click_button('xpath', '//*[@text="锁屏密码"]')
        #     输入原密码
        self.assertTrue(self.b.find_element('xpath', '//*[@text="输入原密码"]', 10))
        sleep(2)
        self.b.click_button('xpath', '//*[@text="1"]')
        self.b.click_button('xpath', '//*[@text="2"]')
        self.b.click_button('xpath', '//*[@text="3"]')
        self.b.click_button('xpath', '//*[@text="4"]')
        #     到密码设置页选择无密码
        self.assertTrue(self.b.find_element('xpath', '//*[@text="密码设置"]', 10))
        # 点击无密码
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/setting_none_layout"]')
        # 校验是否已经切换到无密码
        a=self.b.isElement('text','个性设置')
        self.assertTrue(a)
        self.b.close_app()

    def tearDown(self):
        AppiumSetup.tearDownClass()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(ToolTest("test_g_change_nopassword"))
    unittest.TextTestRunner().run(suite)










