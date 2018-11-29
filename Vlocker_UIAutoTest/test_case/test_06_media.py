# -*- coding: utf-8 -*-
import os
import sys
import unittest

from appium_setup import AppiumSetup
from utils import BasePage, FunctionHelper
from time import sleep


class MediaTest(unittest.TestCase):
    "视频页内容验证"

    def setUp(self):
        AppiumSetup().setUpClass(get_version='7.1.1', device_name='cea8dc6c')
        self.driver = AppiumSetup().driver
        self.b = BasePage.Base()
        self.h = FunctionHelper.Function()

    def test_a_active_media(self):
        "互动主题页功能"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 5)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 5))
        '点击互动主题'
        self.b.click_button('xpath','//*[@text="互动主题"]')
        '互动主题页信息校验'
        self.assertTrue(self.b.find_element('xpath', '//*[@text="动态主题"]', 5))
        self.assertTrue(self.b.find_element('xpath','//*[@class="android.widget.ImageButton"]', 5))
        '上滑主题列表'
        self.b.swipe_up(5)
        '校验元素不存在'
        self.b.isElement("name", "陈立农唱歌给你听")
        '点击到主题详情页'
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/iv_spine_list_item"]', 10)
        '校验详情页内容'
        # 主题名称
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/tv_theme_title"]', 5))
        # 主题星级下载量
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/rb_theme"]', 5))
        self.assertTrue(self.b.find_element('xpath', '//*[@text="下载量:"]', 10))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_theme_download_num"]', 5))
        # 主题描述
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/tv_theme_desc"]', 10))
        '下载后应用'
        a = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/video_progress_down"]', 5)
        self.assertTrue(a)
        a.click()
        sleep(15)
        # 加判断，是否已经下载， 如果已经下载，则点击直接应用，如果没下载的，还需要再点击一次
        if self.b.isElement("resource-id", "com.vlocker.locker:id/video_progress_down"):
            a = self.driver.find_element_by_id("com.vlocker.locker:id/video_progress_down")
            a.click()
        else:
            print("已经下载，直接应用到桌面了")
            sleep(3)
        # a = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/video_progress_down"]', 5)
        # self.assertTrue(a)
        # a.click()
        # self.assertTrue(a)
        self.b.swipe_up(1)
        self.b.close_app()

    def test_b_rank(self):
        "排行榜功能"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 5)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 5))
        '点击排行榜'
        self.b.click_button('xpath','//*[@text="排行榜"]')
        #查看排行榜页面内容
        d=self.b.find_element('xpath','//*[@text="下载排行榜真香→_→"]',10)
        self.assertTrue(d)
    #     上传视频入口
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/btn_video_upload"]', 10)
        self.assertTrue(d)
        self.b.close_app()

    def test_c_like(self):
        "普通视频壁纸点赞"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 5))
        '点击视频点赞'
        # 点击热门第一个视频
        # 找到父节点然后找子节点，按照下标找对应的text
        d = self.driver.find_element_by_id("com.vlocker.locker:id/mainView")
        e = d.find_elements_by_class_name("android.widget.FrameLayout")
        sleep(2)
        e[1].click()
        '校验视频页信息'
        d = self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/app_down"]', 5)
        self.assertTrue(d)
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/video_progress_down"]', 5)
        self.assertTrue(d)
        # 用户头像
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/video_img_user"]', 5)
        self.assertTrue(d)
        # 视频名称
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/video_text_title"]', 5)
        self.assertTrue(d)
        # 视频标签内容
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/video_layout_tag"]', 5)
        self.assertTrue(d)
        # 视频时长
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/desc_time"]', 5)
        self.assertTrue(d)
        # 视频大小
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/video_layout_tag"]', 5)
        self.assertTrue(d)
        # 视频有声
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/desc_sound"]', 5)
        self.assertTrue(d)
        # 视频大小
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/desc_size"]', 5)
        self.assertTrue(d)
        # 视频下载次数
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/desc_down"]', 5)
        self.assertTrue(d)
        '点赞视频-跳转登录'
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/video_img_like"]')
        # 登录页  输入用户名密码登录
        self.assertTrue(self.b.find_element('xpath','//*[@text="登录"]',10))
        # 输入用户名密码登录
        self.driver.find_element_by_id("com.vlocker.locker:id/edt_name").send_keys("1501149580200")
        self.driver.find_element_by_id("com.vlocker.locker:id/edt_password").send_keys("moxiutest1234")
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/btn_login"]', 2)
        # 登录成功后跳转到视频页
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/fab_share"]', 5))
        # 点赞状态
        d = self.driver.find_element_by_id("com.vlocker.locker:id/video_img_like")
        #d = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.vlocker.locker:id/video_img_like")')
        d = d.is_selected()
        # if self.assertFalse(d):
            # 点赞
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/video_img_like"]')
        # else :
        #     print("已经点赞过，查看是否状态为已点赞")
        # 校验点赞成功
        d = self.driver.find_element_by_id("com.vlocker.locker:id/video_img_like")
        d=d.is_selected()
        self.assertTrue(d)
        self.b.close_app()

    def test_d_fav(self):
        "普通视频壁纸收藏"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 5))
        # 点击热门第一个视频
        # 找到父节点然后找子节点，按照下标找对应的text
        d = self.driver.find_element_by_id("com.vlocker.locker:id/mainView")
        e = d.find_elements_by_class_name("android.widget.FrameLayout")
        e[1].click()
        '校验视频页信息'
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/app_down"]', 5)
        self.assertTrue(d)
        # 判断收藏状态是否已收藏
        d = self.driver.find_element_by_id("com.vlocker.locker:id/video_img_collection")
        d = d.is_selected()
        # if self.assertFalse(d):
        #     # 点赞
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/video_img_collection"]')
        # else:
        #     print("已经点赞过，查看是否状态为已点赞")
        # 校验点赞成功
        # d=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.vlocker.locker:id/video_img_like")')
        # self.assertTrue(d)
        sleep(3)
        d = self.driver.find_element_by_id("com.vlocker.locker:id/video_img_collection")
        d = d.is_selected()
        self.assertTrue(d)
        self.b.close_app()

    def test_e_usevlocker(self):
        "视频锁屏应用"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 5))
        # 上滑后点击视频
        # 找到父节点然后找子节点，按照下标找对应的text
        self.b.swipe_up(4)
        d = self.driver.find_element_by_id("com.vlocker.locker:id/mainView")
        e = d.find_elements_by_class_name("android.widget.FrameLayout")
        e[1].click()
        '校验视频页信息'
        d = self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/app_down"]', 5)
        self.assertTrue(d)
        '应用到锁屏'
        d = self.driver.find_element_by_id("com.vlocker.locker:id/video_progress_down")
        d.click()
        sleep(20)
        # 加判断，是否已经下载， 如果已经下载，则点击直接应用，如果没下载的，还需要再点击一次
        if self.b.isElement("resource-id","com.vlocker.locker:id/video_progress_down"):
            e = self.driver.find_element_by_id("com.vlocker.locker:id/video_progress_down")
            e.click()
        else:
            print("已经下载，直接应用到桌面")
            sleep(3)
        '判断是否应用到锁屏'
        self.assertTrue(self.b.find_element('xpath', '//*[@text="滑动以解锁"]', 10))
        self.b.swipe_right(1)
        self.b.close_app()

    def test_f_typefollow(self):
        "视频分类关注"
        d = self.b.find_element('xpath', '//*[@text="热门"]',10)
        self.assertTrue(d)
        d =self.b.find_element('xpath','//*[@text="分类"]',2)
        d.click()
        # 点击某个分类到详情页
        self.b.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/tag_icon"]')
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/like_btn"]', 5))
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/layout_title"]', 5))
        '点击关注'
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/like_btn"]', 10)
        '关注后关注按钮变成取消关注'
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/like_btn_cancel"]', 5))
        '返回我的关注查看'
        self.driver.keyevent(4)
        self.b.click_button('xpath','//*[@text="我的"]')
        '点击我的关注查看'
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/mine_follow"]')
    #     我的关注有信息
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/follow_btn_follow"]',5))
    #     点击已关注按钮取消关注
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/follow_btn_follow"]')
        sleep(2)
        e = self.driver.find_element_by_id("com.vlocker.locker:id/follow_btn_unfollow").text
        self.assertEqual(e,"关注")
        self.driver.keyevent(4)
        self.b.close_app()

    def test_g_sharemedia(self):
        "视频分享"
        d = self.b.find_element('xpath', '//*[@text="热门"]', 10)
        self.assertTrue(d)
        # 判断数据加载
        self.assertTrue(self.b.find_element('xpath', '//*[@resource-id="com.vlocker.locker:id/title"]', 5))
        # 找到父节点然后找子节点，按照下标找对应的text
        d = self.driver.find_element_by_id("com.vlocker.locker:id/mainView")
        e = d.find_elements_by_class_name("android.widget.FrameLayout")
        e[1].click()
        '点击分享'
        self.b.click_button('xpath','//*[@resource-id="com.vlocker.locker:id/fab_share"]')
    #     分享路径
        self.assertTrue(self.b.find_element('xpath','//*[@resource-id="com.vlocker.locker:id/mx_share_layout"]', 6))
    #     点击分享到qq
        self.b.click_button('xpath','//*[@text="QQ"]')
        sleep(2)
        # 发送
        self.b.click_button('xpath','//*[@text="魔秀大树"]')
        d=self.b.find_element('xpath','//*[@resource-id="com.tencent.mobileqq:id/dialogRightBtn"]',10)
        d.click()
    #     成功后点击回到微锁屏
    #     self.assertTrue(self.b.find_element('xpath','//*[@text="已发送"]',10))
        sleep(3)
        self.b.click_button('xpath','//*[@text="返回微锁屏"]')
        self.driver.keyevent(4)
        self.b.close_app()

    def tearDown(self):
        AppiumSetup.tearDownClass()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(MediaTest("test_g_sharemedia"))
    unittest.TextTestRunner().run(suite)
