# -*- conding: utf-8 -*-
# @Time      :2019/7/9 17:25
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_requests.py
import requests
class HttpRequest:
    def http_request(self,url,data,method,cookie=None):
        if method.lower() =='get':
            res = requests.get(url,data,cookies=cookie,verify=False)
        else:
            res = requests.post(url, data,cookies=cookie,verify=False)
        return res


if __name__ == '__main__':
    # url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    # data = {"mobilephone": "18688773467", "pwd": "123456"}
    # res = HttpRequest().http_request(url,data,"post")
    # print("登录的结果是：",res.json())

    # 充值
    # recharge_url = "http://119.23.241.154:8080/futureloan/mvc/api/member/recharge"
    # recharge_data = {"mobilephone": "18688773467", "amount": "1000"}
    # recharge_res = HttpRequest().http_request(recharge_url,recharge_data,"get",res.cookies)
    # print("充值结果是：",recharge_res.json())

    login_url="https://www.ketangpai.com/UserApi/login"
    data={"email":"1255811581@qq.com","password":"huahua90!@","remember":0}
    res = HttpRequest().http_request(login_url,data,"post")
    print("课堂派登录结果：{}".format(res.json()))
    print("课堂派登录结果：{}".format(res.cookies))
    print("课堂派登录cookies：{}".format(res.cookies["PHPSESSID"]))

    #查看个人的考勤情况
