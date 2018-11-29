# -*- coding: utf-8 -*-
import random
from utils.BasePage import Base
from appium_setup import AppiumSetup
from utils.PublicLog import LogFile


class Function(object):

    def __init__(self):
        self.driver = AppiumSetup().driver
        self.b = Base()

    def login(self):

        try:
            dict_list = [{'17778060392': 'a123456789'}, {'18511071948': 'moxiutest'}, {'16602297370': 'a123456789'}]
            num_list = dict_list[random.randint(0, 2)]
            account_num = list(num_list.keys())[0]
            password_num = list(num_list.values())[0]
            account = self.b.find_element('xpath', '//*[@text="请输入手机号/邮箱"]', 10)
            account.send_keys('%s' % account_num)
            password = self.b.find_element('xpath', '//*[@resource-id="com.haolan.infomation:id/edt_password"]', 10)
            password.send_keys('%s' % password_num)
            self.b.find_element('xpath', '//*[@text="登录"]', 10).click()

        except AssertionError:
            AppiumSetup().add_img()
            LogFile().error('登陆 异常')

    def logout(self):

        try:
            self.b.find_element('xpath', '//*[@text="我的"]', 10).click()
            d = self.b.find_element('xpath', '//*[@text="设置"]', 10)
            tmp = ''
            while tmp == '':
                if d:
                    d.click()
                    break
                else:
                    self.b.swipe_up(1)
            self.b.find_element('xpath', '//*[@text="退出登录"]', 10).click()

        except AssertionError:
            AppiumSetup().add_img()
            LogFile().error('退出登录 异常')