#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import urllib.request
import subprocess
# base_dir = os.path.dirname(os.path.abspath(__file__))
performance_data = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = os.path.join(performance_data, 'app')
def download_app(nums):
    try:
        if nums == 0:
            url = 'http://soft.moxiu.net/bd/vlocker/latest'
        else:
            url = 'http://soft.moxiu.net/bd/launcher/latest/A_tengxun'
        f = urllib.request.urlopen(url)
        data = f.read()
        if nums == 0:
            save_path = os.path.join(base_dir, 'default.apk')
        else:
            save_path = os.path.join(base_dir, 'tengxun.apk')
        with open(save_path, "wb") as code:
            code.write(data)
    except:
        print('下载失败')
if __name__ == "__main__":
    download_app(0)
    # download_app(1)