# -*- conding: utf-8 -*-
# @Time      :2019/8/1 16:12
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :py11.py
# s = "hello"
# print(s.find("e"))
#找到的话 返回是索引
#找不到的话 返回时-1

# if s.find("9"): #非空非零都为true
#     new_s = s.replace("o","kevin")
# print(new_s)

import logging #
# logging.debug('xiaoci今天很活跃')
# logging.info('lagom 666')
# logging.warning('kenvin')
# logging.error('Monica 马上变成大佬了')
# logging.critical("躺着舒服同学，好舒服")

#定义一个日志收集器
my_logger = logging.getLogger('python11')

#设定级别
my_logger.setLevel("DEBUG")
#设置输出格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
#收集日志
my_logger.debug("python11期1117学习logging已经懵逼")
my_logger.error("python11期1117是最棒的！坚强点")

#创建一个我们自己的输出渠道
ch = logging.StreamHandler()
ch.setLevel("ERROR")
ch.setFormatter(formatter)

fh=logging.FileHandler("py11.txt",encoding='utf-8')
fh.setLevel("DEBUG")
fh.setFormatter(formatter)
#两者对接--指定输出渠道
my_logger.addHandler(ch)
my_logger.addHandler(fh)

#收集日志
my_logger.debug("python11期1117学习logging已经懵逼")
my_logger.error("python11期1117是最棒的！坚强点")
import requests
url = "https://www.ketangpai.com/UserApi/login"
data = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
res = requests.post(url,data)
print(res.cookies)

