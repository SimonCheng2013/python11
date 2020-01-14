# -*- conding: utf-8 -*-
# @Time      :2019/7/8 15:37
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_01.py
class LemonTeacher():

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.height = 180

    def coding(self): #实例方法 实例调用
        print(self.name+'coding')
    def cooking(self):
        print(self.name+'cooking')
    @classmethod #类方法不可以调用类变量  类名和实例均可调用
    def swimming(cls):
        print("cls swimming")
    @staticmethod#静态方法不可以调用类变量 类名和实例均可调用
    def sing():
        print("static sing")
    def teacher_info(self):
        self.coding()
        print("{}老师,今年{}岁,身高{}".format(self.name,self.age,self.height))
# t = Teacher()

# t.swimming()
# Teacher.swimming()
LemonTeacher("花花",11).swimming()
LemonTeacher("猫猫",11).cooking()
LemonTeacher("狗狗",11).coding()
LemonTeacher("羊羊",11).sing()
LemonTeacher("猪猪",12).teacher_info()

print("GeT".lower())


