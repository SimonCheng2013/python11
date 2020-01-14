# -*- conding: utf-8 -*-
# @Time      :2019/7/5 11:30
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_function.py
#*args  多个参数 **kwargs 字典键值对
def da_lao(name='huahua'):
    print(name)
da_lao(name="dd")

def add_all_num(a,*L,**kwargs):
    print(a,L,kwargs)
add_all_num(1,2,3,4,x=1,y=2)