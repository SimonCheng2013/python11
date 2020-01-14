# -*- conding: utf-8 -*-
# @Time      :2019/7/17 15:03
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :try001.py
import unittest
class Extend(unittest.TestCase):
    def big(self):
        self.assertEqual(1,3)
Extend().big()