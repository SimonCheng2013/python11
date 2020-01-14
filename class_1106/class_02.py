# -*- conding: utf-8 -*-
# @Time      :2019/7/19 10:56
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_01.py
import requests
class HttpRequest:
    a = 666
    def __init__(self,url,data):
        self.url=url
        self.data=data

    def get_request(self,url,data):
        res=requests.get(url,data)
        print("返回结果是{}".format(res))

    @staticmethod
    def get_post_request(self):
        res = requests.post(self.url,self.data)
        print("返回结果是{}".format(res))

    def post_request(self):#实例方法 只能通过实例来调用
        res = requests.post(self.url,self.data)
        print("返回结果是{}".format(res))

    @classmethod
    def add(cls,a,b):
        print("class")
        return a+b

    @staticmethod
    def print_msg(a,b):
        print(a+b)
        print("python11")

#类方法 静态方法 可以直接类名，方法名调用 他也可以通过实例调用
HttpRequest.add()
HttpRequest.print_msg()
HttpRequest(1,2).print_msg()
#实例方法 必须要创造实例来调用 类名
url = "https://www.ketangpai.com/UserApi/login"
data = {"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
# HttpRequest(1,2).post_request()
print(HttpRequest.a)

#类方法 静态方法
