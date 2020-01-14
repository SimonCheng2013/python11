# -*- conding: utf-8 -*-
# @Time      :2019/7/12 13:59
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_http.py
import unittest
from class_1101.http_requests import HttpRequest
from class_1101.get_data import GetData
#列表里面嵌套字典
# test_data =ail": "1255811581@qq.com", "password": "huahua90!@2", "remember": -1},"status":1,"method":"post"}]
class TestHttp(unittest.TestCase):
    def setUp(self):
        print("开始测试")
        pass
    def __init__(self,methodName,url,data,method,status):#通过初始化函数传参
        super(TestHttp,self).__init__(methodName)#父类的方法保留了
        self.url=url
        self.data = data
        self.method = method
        self.status = status
    def test_api(self):#接口用例
            res = HttpRequest().http_request(self.url, self.data, self.method,getattr(GetData,"Cookie"))
            if res.cookies:#如果cookie有的话，更新cookie
                setattr(GetData,"Cookie",res.cookies)
            try:
                self.assertEqual(self.status,res.json()['status'])
            except AssertionError as e:
                print("test_login_normal's error is {}".format(e))
                raise e
            print(res.cookies)
            pass
    # def test_login_wrong_pwd(self):#输入错误密码
    #     res = HttpRequest().http_request(self.login_url, data, "post")
    #     try:
    #         self.assertEqual(0,res.json()["status"])
    #     except AssertionError as e:
    #         print("test_login_wrong_pwd's error is {}".format(e))
    #         raise e
    #     print(res.json())
    #     pass
    # def test_recharge_normal(self):#正常充值
    #     '''set up传cookie'''
    #     # res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",self.cookies)
    #     '''全局传cookie'''
    #     res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",getattr(GetData,"Cookie"))
    #
    #
    #     try:
    #         self.assertEqual("1",res.json()["status"])
    #     except AssertionError as e:
    #         print("test_recharge_normal erro is{}".format(e))
    #         raise e
    #     pass
    # def test_recharge_negative(self):#充值为负数
    #     # res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",self.cookies)
    #     res = HttpRequest().http_request(self.recharge_url, recharge_data, "post",getattr(GetData,"Cookie"))
    #     try:
    #         self.assertEqual("1",res.json()["status"])
    #     except AssertionError as e:
    #         print("test_recharge_negative erro is{}".format(e))
    #         raise e
    #     print(res.json())
    def tearDown(self):
        pass

# TestHttp().test_login_normal()
if __name__ == '__main__':
    TestHttp().test_login_normal()