# -*- conding: utf-8 -*-
# @Time      :2019/8/8 11:05
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :pobo_tongyi.py
import requests
import unittest
import hashlib

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()
info = str(90000003111111)
password = md5(info).upper()
# print(md5(info))

# class Notice():
#     def md5(self,str):
#         m = hashlib.md5()
#         m.update(str.encode("utf-8"))
#         return m.hexdigest()
#     def login(self):
#         info = str(90000003111111)
#         password = self.md5(info).upper()
#         print(password)
#         '''密码是md5(userCode+密码)再转大写'''
#         login_url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token?authType=password"
#         login_data =str({"rand":"4e24eefa-1298-4601-8dfd-b5e63f742a43",
#         	"clientCode":"pbsso",
#             "orgCode":"0000",
#             "userCode":"90000003",
#             "password":password,
#             "kaptchaCode":"7165"})
#         header = {
#   "Content-Type": "application/json",
#         }
#         login_res = requests.post(login_url,data=login_data,headers=header)
#         print(login_res.json())
#     def test_send_notice(self):
#         url = "http://192.168.6.119:8080/NoticeService/webservice"
#         data = {"func":"2003","uid":"474","brokerid":"0000","data":[{"pagecount":"1000","currentindex":"1"}]}
#         header = {"Content-Type":"application/json",
#                   "sid":"A0F3A9862287A502B94F30EEDDE98CC6BEAE0DE3068079CE4E027BA92C16A8C1063F58521A4928A43EC11A7E84326874"}
#         res = requests.post(url,data,headers=header)
#         print(res.json())
#         pass
# if __name__ == '__main__':
#     Notice().login()

import requests

url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token"

querystring = {"authType":"password"}

# payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\"," \
#           "\n\t\"clientCode\":\"pbsso\"," \
#           "\n\t\"orgCode\":\"0000\"," \
#           "\n\t\"userCode\":\"90000003\"," \
#           "\n\t\"password\":\"9418375E1760BFEAA4D016E9F92FFF1F\"," \
#           "\n\t\"kaptchaCode\":\"7165\"}"
payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\"," \
          "\n\t\"clientCode\":\"pbsso\"," \
          "\n\t\"orgCode\":\"0000\"," \
          "\n\t\"userCode\":\"90000003\"," \
          "\n\t\"password\":\"password_value\"," \
          "\n\t\"kaptchaCode\":\"7165\"}".replace("password_value",password)
# payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\",\"clientCode\":\"pbsso\",\"orgCode\":\"0000\",\"userCode\":\"90000003\",\"password\":\"9418375E1760BFEAA4D016E9F92FFF1F\",\"kaptchaCode\":\"7165\"}"
# a = {"rand":"4e24eefa-1298-4601-8dfd-b5e63f742a43","clientCode":"pbsso","orgCode":"0000","userCode":"90000003","password":"9418375E1760BFEAA4D016E9F92FFF1F","kaptchaCode":"7165"}
# payload = str(a)
# print(payload)
# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "38ec01c4-ae99-43b7-b202-756e7edfc56f"
#     }
headers = {
    "Content-Type": "application/json"
    }

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
# response = requests.post(url, data=payload, headers=headers, params=querystring)
response = requests.post(url, data=payload, headers=headers, params=querystring)

sid = response.json()["accessToken"]
print(sid)
# def test_send_notice():
#     url = "http://192.168.6.119:8080/NoticeService/webservice"
#     data = {"func":"2003","uid":"474","brokerid":"0000","data":[{"pagecount":"1000","currentindex":"1"}]}
#     header = {"Content-Type":"application/json",
#               "sid":"{}".format(sid)}
#     res = requests.post(url,data,headers=header)
#     print(res.json())
#     pass
def test_send_notice2():
    url = "http://192.168.6.119:8080/NoticeService/webservice"
    payload = "{\"func\":\"2003\",\"uid\":\"474\",\"brokerid\":\"0000\",\"data\":[{\"pagecount\":\"1000\",\"currentindex\":\"1\"}]}"
    # headers = {
    #     'Content-Type': "application/json",
    #     'sid': sid
    #     }
    headers = {
        'Content-Type': "application/json",
        'sid': sid
        }
    # response = requests.request("POST", url, data=payload, headers=headers)
    response = requests.post( url, data=payload, headers=headers)
    print(response.json())
# if __name__ == '__main__':
#
#     test_send_notice2()

class Notice(unittest.TestCase):
    info = str(90000003111111)
    def setUp(self):

        pass

    def password_md5(self,str):
        m = hashlib.md5()
        m.update(str.encode("utf-8"))
        hexdigest=m.hexdigest()
        password = hexdigest.upper()
        return password
    def get_sid_value(self,info):
        url = "http://192.168.6.119:8080/pbsso-server/v1.0.0/pc/auth/token"
        querystring = {"authType": "password"}
        payload = "{\"rand\":\"4e24eefa-1298-4601-8dfd-b5e63f742a43\"," \
                  "\n\t\"clientCode\":\"pbsso\"," \
                  "\n\t\"orgCode\":\"0000\"," \
                  "\n\t\"userCode\":\"90000003\"," \
                  "\n\t\"password\":\"password_value\"," \
                  "\n\t\"kaptchaCode\":\"7165\"}".replace("password_value", self.password_md5(str(info)))
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=payload, headers=headers, params=querystring)
        sid = response.json()["accessToken"]
        return sid

    def test_send_notice(self,info_password):
        url = "http://192.168.6.119:8080/NoticeService/webservice"
        payload = "{\"func\":\"2003\",\"uid\":\"474\",\"brokerid\":\"0000\",\"data\":[{\"pagecount\":\"1000\",\"currentindex\":\"1\"}]}"
        headers = {
            'Content-Type': "application/json",
            'sid': self.get_sid_value(info_password)
        }
        response = requests.post(url, data=payload, headers=headers)
        print(response.json())

if __name__ == '__main__':
    info_password = 90000003111111
    Notice().password_md5(info_password)

    Notice().test_send_notice(info_password)