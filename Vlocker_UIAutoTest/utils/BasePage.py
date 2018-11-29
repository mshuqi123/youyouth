# -*- coding: utf-8 -*-
import time

import subprocess
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium_setup import AppiumSetup
from utils.PublicLog import *
from time import sleep


class Base(object):

    def __init__(self):
        self.driver = AppiumSetup().driver

    def find_element(self, item, loc, wait):
        try:
            if item == 'id':
                element = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element_by_id(loc))
            elif item == 'xpath':
                element = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element_by_xpath(loc))
            elif item == 'accessibility':
                element = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element_by_accessibility_id(loc))
        except AssertionError:
            AppiumSetup().add_img()
            LogFile().error(u"%s 页面中未能找到 %s 元素" % (self, loc))

        return element

    def find_elements(self, item, loc, wait):

        try:
            if item == 'id':
                elements = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_elements_by_id(loc))
            elif item == 'xpath':
                elements = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_elements_by_xpath(loc))
            elif item == 'accessibility':
                elements = WebDriverWait(self.driver, wait).until(lambda driver: driver.find_elements_by_accessibility_id(loc))
        except AssertionError:
            AppiumSetup().add_img()
            LogFile().error(u"%s 页面中未能找到 %s 元素" % (self, loc))

        return elements

    def send_keys(self, item, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(item, loc, wait=10).click()
            if clear_first:
                self.find_element(item, loc, wait=10).clear()
            self.find_element(item, loc, wait=10).send_keys(value)
        except AttributeError:
            LogFile().error(u"%s 页面中未能找到 %s 元素" % (self, loc))

            # 重新封装按钮点击方法

    def click_button(self, item, loc, find_first=True):
        try:
            if find_first:
                self.find_element(item, loc, wait=10)
            self.find_element(item, loc, wait=10).click()
        except AttributeError:
            LogFile().error("%s 页面未能找到 %s 按钮" % (self, loc))

    def swipe(self, st, sy, ex, ey):
        """
        滑动
        分别为:起始点x,y。结束点x,y。与滑动速度。滑动默认800
        """
        return self.driver.swipe(st, sy, ex, ey, duration=300)

    def get_window_size(self):
        """
        获取屏幕分辨率
        {u'width': 1080, u'height': 1920}
        :return: 1080,1920
        """

        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']
        return width, height

    def swipe_ratio(self, st, sy, ex, ey):
        """
        :param st: 起始点宽
        :param sy: 起始点高
        :param ex: 结束点宽
        :param ey: 结束点高
        :return: 滑动动作
        """
        width, height = self.get_window_size()
        return self.swipe(str(st * width), str(sy * height),
                          str(ex * width), str(ey * height))

    def swipe_left(self, get_num):
        """
        左滑屏幕
        """
        num = 0
        while num < get_num:

            self.swipe_ratio(0.8, 0.5, 0.2, 0.5)
            time.sleep(1)
            num += 1

    def swipe_right(self, get_num):
        """
        右滑屏幕
        """
        num = 0
        while num < get_num:
            self.swipe_ratio(0.2, 0.5, 0.8, 0.5)
            time.sleep(1)
            num += 1

    def swipe_up(self, get_num):
        """
        上滑屏幕
        """
        num = 0
        while num < get_num:
            self.swipe_ratio(0.5, 0.8, 0.5, 0.2)
            time.sleep(1)
            num += 1

    def swipe_down(self, get_num):
        """
        下滑屏幕
        """
        num = 0
        while num < get_num:
            self.swipe_ratio(0.5, 0.2, 0.5, 0.8)
            time.sleep(1)
            num += 1

    def swipe_all(self, t):
        """
        选择如何滑动屏幕
        """
        if t == 'swipe_left':
            self.swipe_left()
        elif t == 'swipe_right':
            self.swipe_right()
        elif t == 'swipe_up':
            self.swipe_up()
        elif t == 'swipe_down':
            self.swipe_down()

    def save_screenshot(self, file_path):
        """
        :param file_path:
        :return: 获取android设备截图
        """

        return self.driver.save_screenshot(file_path)

    def start_activity(self, package, activity):
        """
        启动activity
        package:包名
        activity:.activity
        """
        return self.driver.start_activity(package, activity)

    def open_notifications(self):
        """
        打开系统通知栏
        """
        return self.driver.open_notifications()

    def is_app_installed(self, package):
        """
        检查是否安装
        package:包名
        """
        return self.driver.is_app_installed(package)

    def install_app(self, path):
        """
        安装应用
        path:安装路径
        """
        return self.driver.install_app(path)

    def remove_app(self, package):
        """
        删除应用
        package:包名
        """
        return self.driver.remove_app(package)

    def shake(self, ):
        """
        摇晃设备
        """
        return self.driver.shake()

    def close_app(self, ):
        """
        关闭当前应用
        """
        return self.driver.close_app()

    def reset_app(self, ):
        """
        重置当前应用
        """
        return self.driver.reset()

    def current_activity(self, ):
        """
        当前应用的activity
        """
        return self.driver.current_activity

    def send_key_event(self, arg):
        """
        操作实体按键
 
        """
        event_list = {'entity_home': 3, 'entity_back': 4, 'entity_menu': 82, 'entity_volume_up': 24,
                      'entity_volume_down': 25, "entity_enter": 66}
        if arg in event_list:
            self.driver.keyevent(int(event_list[arg]))

    def toggle_location_services(self):
        """
        开关定位服务

        """
        return self.driver.toggle_location_services()

    def clean_app(self, package_name):

        device_name = Base.get_devices_list(self)
        for i in range(len(device_name)):
            command = 'adb -s %s shell pm clear %s' % (device_name[i], package_name)
            print(command)
            subprocess.getstatusoutput(command)

    def start_app(self,):
        device_name = Base.get_devices_list(self)
        for i in range(len(device_name)):
            command = 'adb -s %s shell am start -W -n com.haolan.infomation/.activity.SplashActivity' % device_name[i]
            print(command)
            subprocess.getstatusoutput(command)

    def get_devices_list(self, ):
        command = 'adb devices'

        out = subprocess.getstatusoutput(command)
        ss = out[1].split('\n')
        ss_list = []

        for i in range(len(ss)):
            if ss[i].__contains__('device'):
                ss_list.append(ss[i])

        devices_list = []
        dd = ss_list[1:len(ss_list)]
        for j in range(len(dd)):
            devices_list.append(str(dd[j]).replace('\tdevice', ''))

        return devices_list

    def get_version(self, device_name):

        command = 'adb -s %s shell getprop ro.build.version.release' % device_name

        out = subprocess.getstatusoutput(command)

        version_name = list(out)[1]

        return version_name

    def find_toast(self):

        try:
            if self.find_element('xpath', '//*[@class="android.widget.Toast"]', 10):
                toast_txt = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
                print(toast_txt)
            else:
                print('未找到 toast弹框')

        except AssertionError:
            AppiumSetup().add_img()
            LogFile().error('功能模块异常')

        return toast_txt

    def isElement(self, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "resource-id":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag


    def logout(self):
        " 退出登录"
        self.swipe_up(1)
        sleep(2)
        self.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_setting"]')
        self.click_button('xpath', '//*[@resource-id="com.vlocker.locker:id/mine_setting_logout"]')

    def totopic(self):
        "到主题页"
        d = self.find_element('xpath', '//*[@text="热门"]', 10)
        # 点击主题
        self.click_button('xpath', '//*[@text="主题"]')

    def get_img(self):
        self.imgs = []
        self.imgs.append(self.driver.get_screenshot_as_base64())

    def take_screenShot(self, name="takeShot"):
        '''
        method explain:获取当前屏幕的截图
        parameter explain：【name】 截图的名称
        Usage:
            device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
        '''
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        fq = "..\\screenShots\\" + day
        # fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
        tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        type = '.png'
        filename = ""
        if os.path.exists(fq):
            filename = fq + "\\" + tm + "_" + name + type
        else:
            os.makedirs(fq)
            filename = fq + "\\" + tm + "_" + name + type
        # c = os.getcwd()
        # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
        self.driver.get_screenshot_as_file(filename)






