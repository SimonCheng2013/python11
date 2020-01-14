# -*- conding: utf-8 -*-
# @Time      :2019/7/25 8:54
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_03.py
from class_1106.http_request import HttpRequest

class PythonHttpRequest(HttpRequest):#继承
    def __init__(self,method):#超继承
        self.method = method
        super(PythonHttpRequest, self).__init__(url,data)#调用父类里面的方法
        # super(子类名，self)父类跟这个子类函数同名的方法（参数）

    def print_msg(self):
        print('我是一个没用的函数，我在这里要调用父类函数')
        if self.method=='get':
            self.get_post_request()
        elif self.method=='post':
            self.post_request()
    def add(self):
        print("a+b=",self.a+self.b)

#继承的时候 子类要不要传初始化参数 看父类
url="https://www.ketangpai.com/UserApi/login"
data={"email":"1255811581@qq.com","password":"huahua90!@","remember":0}
PythonHttpRequest("get",url,data).print_msg()

