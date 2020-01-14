# -*- conding: utf-8 -*-
# @Time      :2019/7/25 13:37
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_http_request.py
import unittest
from class_1106.http_request import HttpRequest
class TestHttpRequest(unittest.TestCase):
    def __init__(self,url,data,http_method,methodName):
        super(TestHttpRequest,self).__init__(methodName)
        self.url = url
        self.data = data
        self.http_method=http_method
    def setUp(self):
        print('我要开始测试了')
    def test_login(self):
        res = HttpRequest().http_request(self.url,self.data,self.http_method)
        print("测试请求的结果是：{}".format(res))
    def test_norma_login(self):
        res = HttpRequest().http_request(self.url,self.data,self.http_method)
        print("测试请求的结果是：{}".format(res))

    # def test_err_pwd_login(self):
    #     url = "https://www.ketangpai.com/UserApi/login"
    #     data = {"email": "1255811581@qq.com", "password": "huahua90!@2", "remember": 0}
    #     res = HttpRequest().http_request(self.url,self.data,self.http_method)
    #     print("测试请求的结果是：{}".format(res))
    def tearDown(self):
        print('我已经结束测试了')
class TestMath(unittest.TestCase):
    def test_add(self):
        print("a+b=",10)
    def test_sub(self):
        print("a-b",20)

# if __name__ == '__main__':
#     TestHttpRequest().test_norma_login()
