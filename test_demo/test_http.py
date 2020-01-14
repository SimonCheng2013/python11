# -*- conding: utf-8 -*-
# @Time      :2019/7/12 13:59
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_http.py
import unittest
from test_demo.http_requests import HttpRequest
from test_demo.get_data import GetData
# COOKIE = None #全局变量
class TestHttp(unittest.TestCase):
    def setUp(self):
        #登录
        self.login_url = "https://www.ketangpai.com/UserApi/login"
        self.login_data = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
        #充值的URL
        self.recharge_url = "https://www.ketangpai.com/UserApi/login"
        #获取登录后的URL
        self.cookies= HttpRequest().http_request(self.login_url,self.login_data,"post").cookies
        print("setup函数里登录的cookies是：{}".format(self.cookies))
    def test_login_normal(self):#正常登录
        global COOKIE#声明全局变量
        data = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
        res = HttpRequest().http_request(self.login_url, data, "post")
        if res.cookies:#如果cookie有的话，更新cookie
            # COOKIE=res.cookies
            setattr(GetData,"Cookie",res.cookies)
        try:
            self.assertEqual(1,res.json()['status'])
        except AssertionError as e:
            print("test_login_normal's error is {}".format(e))
            raise e
        print(res.cookies)
        pass
    def test_login_wrong_pwd(self):#输入错误密码
        data = {"email": "1255811581@qq.com", "password": "huahua90!@000", "remember": 0}
        res = HttpRequest().http_request(self.login_url, data, "post")
        try:
            self.assertEqual('1',res.json()["status"])
        except AssertionError as e:
            print("test_login_wrong_pwd's error is {}".format(e))
            raise e
        print(res.json())
        pass
    def test_recharge_normal(self):#正常充值
        # global COOKIE
        recharge_data = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
        '''set up传cookie'''
        # res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",self.cookies)
        '''全局传cookie'''
        res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",getattr(GetData,"Cookie"))


        try:
            self.assertEqual("1",res.json()["status"])
        except AssertionError as e:
            print("test_recharge_normal erro is{}".format(e))
            raise e
        pass
    def test_recharge_negative(self):#充值为负数
        # global COOKIE
        recharge_data = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": -1}
        # res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",self.cookies)
        res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",getattr(GetData,"Cookie"))
        try:
            self.assertEqual("1",res.json()["status"])
        except AssertionError as e:
            print("test_recharge_negative erro is{}".format(e))
            raise e
        print(res.json())
    def tearDown(self):
        pass

# TestHttp().test_login_normal()
if __name__ == '__main__':
    TestHttp().test_login_normal()