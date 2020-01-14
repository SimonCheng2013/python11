# -*- conding: utf-8 -*-
# @Time      :2019/7/10 16:18
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_01.py
import unittest
from class_1027_unittest.class_01 import TestMathMethod
'''
方法1
一条条加载用例
'''
suite = unittest.TestSuite()

# suite.addTest(TestMathMethod("test_add_two_postive")) #用例运行次序分先后
# suite.addTest(TestMathMethod("test_add_two_zero"))
'''
方法2
'''
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
from class_1027_unittest import class_01 #具体到模块
# suite.addTest(loader.loadTestsFromModule(class_01))
'''
执行
'''
import HTMLTestRunner
with open('test_report.html','wb') as file:
    runnner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="python11期 单元测试报告",
                                            description="python11期各位大佬")#0,1,2 2最详细
    # runnner = HTMLTestRunner(stream=file,verbosity=1)#0,1,2 2最详细
    runnner.run(suite)




