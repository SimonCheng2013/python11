# -*- conding: utf-8 -*-
# @Time      :2019/7/30 15:09
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_http_request.py
import unittest
from tools.project_path import *
from tools.http_request import HttpRequest
from tools.get_data import GetData
from ddt import ddt,data #列表嵌套列表 或者列表嵌套字典
from tools.do_excel import DoExcel
from tools.my_log import MyLog
test_data = DoExcel.get_data(test_case_path)#执行所有用例
my_logger = MyLog()

@ddt
class TestHttpRequest_Notice(unittest.TestCase):
    def setUp(self):
        my_logger.info("开始测试")
        pass
    @data(*test_data)
    def test_api(self,item):
        # print("item is {}".format(item))
        # print("url是:{0},data是:{1},header是:{2},http_method是:{3}".format(item['url'],eval(item['data']),item["header"],item["params"],item['http_method']))
        # print("url value:{0}".format(type(item['url'])))
        # print("data value:{0}:".format(type(item['data'])))
        # print("header value:{0}:".format(type(eval(item['header']))))
        # print("params is :{}".format(item['params']))
        # print("params value:{0}:".format(type(eval(item['params']))))
        # print("http_method value:{0}:".format(type(item['http_method'])))
        if item["model"] == "login_notice":
            global  accessToken
            res_login = HttpRequest.http_request(item['url'], item['data'], eval(item["header"]), eval(item["params"]),
                                           item['http_method'], getattr(GetData, "Cookie"))
            accessToken = res_login.json()["accessToken"]
            if res_login.cookies:
                setattr(GetData, 'Cookie', res_login.cookies)
            try:
                self.assertEqual(item['excepted_code'], res_login.json()["code"])
                TestResult = 'PASS'  # 成功的
            except AssertionError as e:
                TestResult = 'Failed'  # 失败的
                my_logger.info("执行用例出错：{}".format(e))
                raise e
            finally:
                DoExcel.write_back(test_case_path,'notice',item['case_id']+1,str(res_login.json()),TestResult)
                print('获取到的结果是：{}'.format(res_login.json()))

        elif item["model"] == "notice":

            sid = accessToken
            res_notice = HttpRequest.http_request(item['url'], item['data'], eval(item["header"].replace("5EFCC60C2373B9C1FC526F64CAF24610EFA2BFC1C056AF9C92AFC48CE14EE8D8B13942D7F20742E379D7A6F89DB87D72",sid)), eval(item["params"]),
                                           item['http_method'], getattr(GetData, "Cookie"))
            if res_notice.cookies:
                setattr(GetData, 'Cookie', res_notice.cookies)
            try:
                self.assertEqual(item['excepted_code'], eval(res_notice.json()["retHead"]))
                TestResult = 'PASS'  # 成功的
            except AssertionError as e:
                TestResult = 'Failed'  # 失败的
                my_logger.info("执行用例出错：{}".format(e))
                raise e
            finally:
                DoExcel.write_back(test_case_path,'notice',item['case_id']+1,str(res_notice.json()),TestResult)
                print('获取到的结果是：{}'.format(res_notice.json()))

    def tearDown(self):
        my_logger.info("结束测试")
        pass

if __name__ == '__main__':
    '''从这里开始测试'''
    TestHttpRequest_Notice().test_api()
