# -*- conding: utf-8 -*-
# @Time      :2019/7/26 10:10
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_request.py
import requests

register_url="https://www.ketangpai.com/UserApi/login"
register_data={"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
res = requests.post(register_url,register_data)
# print(res.text)
# print(res.json())

login_url="https://www.ketangpai.com/UserApi/login"
login_data={"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
# login_res = requests.post(login_url,login_data)
# print(login_res.text)
# print(login_res.json())
# print(login_res.cookies)

recharge_url="https://www.ketangpai.com/UserApi/login"
recharge_data={"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
# header = {"User-Agent":"Mozilla/5.0"}
# recharge_res = requests.get(recharge_url,recharge_data,cookies=login_res.cookies,headers=header)
# print(recharge_res.text)
# print(recharge_res.json())

#拓展点
s = requests.session()
login_res = s.get(login_url,params=login_data)
recharge_res = s.post(recharge_url,recharge_data)
print(recharge_res.json())
