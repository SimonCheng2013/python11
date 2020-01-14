# -*- conding: utf-8 -*-
# @Time      :2019/7/25 14:24
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_suite.py
import unittest
from class_1106.test_http_request import TestHttpRequest

#收集用例TestSuite
my_suite = unittest.TestSuite()

#加载用例
#方法一：测试类里面一个实例 就是一个测试用例
url = "https://www.ketangpai.com/UserApi/login"
data_normal = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
data_err_pwd = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}

test_data=[{"url":"https://www.ketangpai.com/UserApi/login",
            "data":{"email": "1255811581@qq.com","password": "huahua90!@", "remember": 0},
            "http_method":"get","title":"正常登录"},
           {"url": "https://www.ketangpai.com/UserApi/login",
            "data": {"email": "1255811581@qq.com", "password": "huahua90!@2", "remember": 0},
            "http_method": "post", "title": "输入错误的密码登录"}
           ]
for item in test_data:
    print("正在执行的用例是：{}".format(item['title']))
    my_suite.addTest(TestHttpRequest(item["url"],item['data'],item["http_method"],"test_login"))

#方法二：TestLoader
# loader = unittest.TestLoader()
#loadTestsFromTestCase 一次性加载测试类中的所有测试用例
# my_suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
#loadTestsFromModule一次性加载模块下所有的测试类
# from class_1106 import test_http_request
# my_suite.addTest(loader.loadTestsFromModule(test_http_request))
#执行用例
runner= unittest.TextTestRunner()
runner.run(my_suite)