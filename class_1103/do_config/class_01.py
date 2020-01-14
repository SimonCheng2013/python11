# -*- conding: utf-8 -*-
# @Time      :2019/7/19 8:33
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_01.py

#配置文件
import configparser

cf =configparser.ConfigParser()
cf.read('case.config',encoding='utf-8')

#读取配置文件数据
# print(cf.sections())
# print(cf.items('PYTHON11'))
# res_1=cf.get('MODE','mode')
# print(res_1)

#数据类型讨论---都是字符串--eval转换我们的数据类型
print(type(cf.get('PYTHON11','num')))
print(type(cf.get('PYTHON11','name')))


