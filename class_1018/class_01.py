# -*- conding: utf-8 -*-
# @Time      :2019/7/8 15:37
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_01.py
class Teacher():
    name='花花'
    age = '23'

    def coding(self): #实例方法 实例调用
        print(self.name+'coding')
    def cooking(self):
        print('cooking')
    @classmethod #类方法不可以调用类变量  类名和实例均可调用
    def swimming(cls):
        print("cls swimming")
    @staticmethod#静态方法不可以调用类变量 类名和实例均可调用
    def sing():
        print("sing")
# t = Teacher()

# t.swimming()
# Teacher.swimming()
Teacher().sing()


