# -*- conding: utf-8 -*-
# @Time      :2019/7/26 10:10
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :http_request.py
import requests
from tools.my_log import MyLog
my_logger=MyLog()
class HttpRequest:
    @staticmethod
    def http_request(url,data,http_method,cookie=None):
        try:
            if http_method=="get":
                    res = requests.get(url,data,cookies=cookie)
            elif http_method=="post":
                    res = requests.post(url, data,cookies=cookie)
            else:
                my_logger.info("输入请求方法不对")
        except Exception as e:
            my_logger.error("请求报错了：{}".format(e))
            raise e
        return res
if __name__ == '__main__':
    #注册
    register_url="https://www.ketangpai.com/UserApi/login"
    register_data={"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
    #登录
    login_url="https://www.ketangpai.com/UserApi/login"
    login_data={"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}
    #充值
    recharge_url="https://www.ketangpai.com/UserApi/login"
    recharge_data={"email": "1255811581@qq.com", "password": "huahua90!@", "remember": 0}

    login_res = HttpRequest().http_request(login_url,login_data,"get")
    recharge_res = HttpRequest().http_request(recharge_url,recharge_data,"post",login_res.cookies)
    # print("cookie的值:{}".format(login_res.cookies))
    my_logger.info("this is a rae")
    print("充值结果：{}".format(recharge_res.json()))