#!/usr/bin/python
# -*- coding: utf-8 -*
import os
import time


def get_report():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_report = os.path.join(base_dir, 'report')
    dirs = os.listdir(test_report)
    dirs.sort()
    new_report = dirs[-1]
    print('The new report name: {0}'.format(new_report))
    file_new = os.path.join(test_report, new_report)

    return file_new

