# -*- conding: utf-8 -*-
# @Time      :2019/7/10 16:18
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_01.py
import unittest
from class_1027_unittest.math_method import MathMethod
class TestMathMethod(unittest.TestCase):
    def setUp(self):
        print("开始执行测试用例")
    def test_add_two_postive(self):
        res = MathMethod(1,1).add()
        print('1+1结果是：',res)
        try:
            self.assertEqual(2,res)
        except AssertionError as e:
            print("出错了，断言的错误是{}".format(e))
            raise e
    def test_add_two_zero(self):
        res = MathMethod(0,0).add()
        print('0+0结果是：',res)
        try:
            self.assertEqual(2,res,"this erro")
        except AssertionError as e:
            print("出错了，断言错误是{0}".format(e))
            raise e
    def test_add_two_negative(self):
        res = MathMethod(-1,-2).add()
        print("-1+-2的结果是：",res)
        try:
            self.assertEqual(-3,res,"this erro")
        except AssertionError as e:
            print("出错了，断言错误是{0}".format(e))
            raise e
class TestMulti(unittest.TestCase):
    def test_multi_two_postive(self):
        res = MathMethod(1,1).multi()
        print('1*1结果是：',res)
    def test_multi_two_zero(self):
        res = MathMethod(0,0).add()
        print('0*0结果是：',res)
    def test_multi_two_negative(self):
        res = MathMethod(-1,-2).add()
        print("-1*-2的结果是：",res)
    def tearDown(self):
        print("我已执行完测试用例")
if __name__ == '__main__':
    unittest.main()


