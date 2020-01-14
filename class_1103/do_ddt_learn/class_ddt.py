# -*- conding: utf-8 -*-
# @Time      :2019/7/17 17:38
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_ddt.py

#ddt  ddt + unittest进行数据处理 第三方库
#装饰器 会在函数运行之前运行
import unittest
from ddt import ddt,data,unpack

test_data=[{"no":1,"name":"稳当"},{"no":2,"name":"小黄"}]

@ddt#装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data)#装饰测试方法 拿到几个数据 就执行几条用例
    # @unpack #如果unpack后的参数 少于5个 推荐用unpack
    #要注意参数不对等的情况，提供对应个数的参数来接受变量

    #如果你要对字典进行unpack的，参数与字典key对应
    def test_print_data(self,no,name):#测试用例
        print("no",no)
        print("name",name)





