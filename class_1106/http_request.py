# -*- conding: utf-8 -*-
# @Time      :2019/7/25 9:22
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_request.py
import requests
class HttpRequest:
    # def __init__(self,url,data):
    #     self.url=url
    #     self.data=data
    #     print("此处省去一万行代码")
    def get_post_request(self):
        res = requests.post(self.url, self.data)
        print("get返回结果是{}".format(res))


    def post_request(self):  # 实例方法 只能通过实例来调用
        res = requests.post(self.url, self.data)
        print("post返回结果是{}".format(res))
    def http_request(self,url,data,method):
        if method=='get':
            res = requests.get(url,data)
        else:
            res = requests.post(url,data)
        return res
