# -*- conding: utf-8 -*-
# @Time      :2019/7/5 11:30
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_function.py
#*args  多个参数 **kwargs 字典键值对
a = 1
def add(b):
    global a
    a = 5
    print(a+b)

add(10)
print(a)
