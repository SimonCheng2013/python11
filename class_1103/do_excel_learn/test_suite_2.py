# -*- conding: utf-8 -*-
# @Time      :2019/7/12 14:14
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :test_suite.py
import unittest
import HTMLTestRunner
from class_1103.test_http import TestHttp #类名
from class_1103.do_excel_2 import DoExcel

t=DoExcel("xh.xlsx","python")
suite = unittest.TestSuite()
for i in range(1,t.max_row+1):
    suite.addTest(TestHttp("test_api",t.get_data(i,1),t.get_data(i,2),eval(t.get_data(i,3)),str(t.get_data(i,4))))

# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_http))

with open("test_summer.html","wb") as file:
    runnner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="python11期 单元测试报告",
                                            description="python11期各位大佬")  # 0,1,2 2最详细
    runnner.run(suite)
