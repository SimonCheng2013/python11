# -*- conding: utf-8 -*-
# @Time      :2019/7/12 13:59
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_http.py
import unittest
from ddt import ddt,data
from class_1103.http_requests import HttpRequest
from class_1103.get_data import GetData
from class_1103.do_excel import DoExcel
#列表里面嵌套字典

test_data=[]
t = DoExcel("xh.xlsx","python").get_data()
for i in range(len(t)):
    if i%2==0:
        test_data.append(t[i])

@ddt
class TestHttp(unittest.TestCase):
    def setUp(self):
        print("开始测试")
        pass
    @data(*test_data)
    def test_api(self,item):#接口用例
            res = HttpRequest().http_request(item['url'], eval(item["data"]), item["method"],getattr(GetData,"Cookie"))
            if res.cookies:#如果cookie有的话，更新cookie
                setattr(GetData,"Cookie",res.cookies)
            try:
                self.assertEqual(str(item["status"]),res.json()['status'])
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
