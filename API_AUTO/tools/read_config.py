# -*- conding: utf-8 -*-
# @Time      :2019/7/19 9:44
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :read_config.py

import configparser
class ReadConfig:
    def read_config(self,file_name,section,option):
        cf =configparser.ConfigParser()
        cf.read('case.config',encoding='utf-8')
        return cf.get(section,option)
if __name__ == '__main__':
    res = ReadConfig().read_config("case.config", "MODE", "mode")
    print(res)



