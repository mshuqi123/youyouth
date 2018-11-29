#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import platform
import time
import random
import sys
class LogFile:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, 'log')
        if not os.path.isdir(directory):
            os.mkdir(directory)
        log_name = '%s%s.log' % (time.strftime("%Y%m%d%H%M%S"), random.randint(100, 999))
        sysstr = platform.system()
        if sysstr == 'Windows':
            log_file = '%s\\%s' % (directory, log_name)
        else:
            log_file = '%s/%s' % (directory, log_name)
        # if not os.path.isfile(log_file):
        #     log = open(log_file, 'w+')
        #     log.close()
        self.log_file = log_file
    @staticmethod
    def screen_shot(driver, content):
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        directory_path = os.path.join(directory, 'log\\log')
        if not os.path.isdir(directory_path):
            os.mkdir(directory_path)
        shot_name = '%s_%s.png' % (time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())), content)
        sysstr = platform.system()
        if sysstr == 'Windows':
            screen_save_path = '%s\\%s' % (directory_path, shot_name)
        else:
            screen_save_path = '%s/%s' % (directory_path, shot_name)
        driver.get_screenshot_as_file(screen_save_path)

    def info(self, content):
        LogFile.__write_log(self.log_file, "INFO", content)

    def error(self, driver, content):
        # error 情况自动截图
        LogFile.screen_shot(driver, content)
        LogFile.__write_log(self.log_file, "ERROR", content)

    def warning(self, content):
        LogFile.__write_log(self.log_file, "WARNING", content)

    @staticmethod
    def __write_log(log_file, log_type, content):
        log = open(log_file, 'a')
        log.writelines(time.strftime("%Y-%m-%d %H:%M:%S") + " " + log_type + " " + content + '\n')
        log.close()



