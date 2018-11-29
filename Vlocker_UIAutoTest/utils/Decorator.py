# -*- coding: utf-8 -*-
import random
from utils.BasePage import Base


# 异常截图
def add(func):
    def warpper(self):
        try:
            func(self)
        except AssertionError:
            Base().get_img()
            print(111)
    return warpper

