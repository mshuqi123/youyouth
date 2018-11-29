# -*- coding: utf-8 -*-
import os
import random
import time


class LogFile:
    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(base_dir, 'logfile')
        if not os.path.isdir(directory):
            os.mkdir(directory)

        log_name = '%s.log' % (time.strftime("%Y-%m-%d %H:%M:%S"))
        log_file = '%s/%s' % (directory, log_name)

        if not os.path.isfile(log_file):
            log = open(log_file, 'w+')
            log.close()

        self.log_file = log_file

    def info(self, content):
        LogFile.__write_log(self.log_file, "INFO", content)

    def error(self, content):

        LogFile.__write_log(self.log_file, "ERROR", content)

    def warning(self, content):
        LogFile.__write_log(self.log_file, "WARNING", content)

    @staticmethod
    def __write_log(log_file, log_type, content):
        log = open(log_file, 'a')
        log.writelines(time.strftime("%Y-%m-%d %H:%M:%S") + " " + log_type + " " + content + '\n')
        log.close()


