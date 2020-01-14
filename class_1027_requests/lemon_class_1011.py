# -*- conding: utf-8 -*-
# @Time      :2019/7/9 15:57
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :lemon_class_1011.py
import requests
'''
地址：http://120.78.128.25:8765/Index/login.html
参数：15928163412 sunny123456
15852445352 123abcd
13671316242 wangyan123456
13426349627 941215asd
'''
# url ="http://120.78.128.25:8765/Index/login.html"
# #get请求 不带参数
# res = requests.get(url,cookies=None)
# print(res)
# print("响应头：",res.headers)
# print("相应状态码：",res.status_code)
# print("相应正文：",res.text)

#post请求 带参数
# url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"
url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
url = "https://quant.pobo.net.cn/pobo_quant_usercenter/common/login"
data = {"mobilephone":"18688773467","pwd":"123456"}
res = requests.post(url,data)
# print(res)
print("响应头：",res.headers)
print("相应状态码：",res.status_code)
print("相应正文：",res.text)

#充值
recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
recharge_data={"mobilephone":"18688773467","amount":"1000"}
recharge_res = requests.get(recharge_url,recharge_data,cookies=res.cookies)
print("充值结果：",recharge_res.json())
print("状态码：",recharge_res.status_code)
