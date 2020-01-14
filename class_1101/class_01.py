# -*- conding: utf-8 -*-
# @Time      :2019/7/15 9:50
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_01.py
'''反射reflex'''
class GetData:
    Cookie = "小郭"
print(GetData.Cookie)
setattr(GetData,"Cookie","小黄")
print(GetData.Cookie)
print(hasattr(GetData,"Cookie"))
print(getattr(GetData,"Cookie"))
print(GetData.Cookie)