# -*- conding: utf-8 -*-
# @Time      :2019/7/9 11:13
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_04_supper.py
# class A:
#     def add(self,x):
#         y = x+1
#         print(y)
#     def sub(self):
#         print("A sub")
# class B(A):
#     def add(self,x):
#         super().add(x)
# b=B()
# b.add(2)

# class FooParent():
#     def __init__(self):
#         self.parent = 'I am the parent'
#         print('Parent')
#     def bar(self,message):
#         print("%s from Parent" %message)
# class FooChild(FooParent):
#     def __init__(self):
#         super(FooChild,self).__init__()
#         print('Chlid')
#     def bar(self,message):
#         super(FooChild,self).bar(message)
#         print('Child bar function')
#         print(self.parent)
# if __name__ =="__main__":
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')

# class A:
#     def __init__(self):
#         print("a init")
#     def m(self):
#         print('A')
#     def n(self):
#         print('A n')

# class B:
#     def __init__(self):
#         print("b init")
#     def m(self):
#         print('B')
# class C(A):
#     def __init__(self):
#         print("c init")
#     def m(self):
#         print('C')
#         # super().m()
#         self.n()
# C().m()

class MathMethod():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("我是父类的add方法：",self.a+self.b)

    def sub(self):
        return self.a+self.b
class MathMethod_1(MathMethod):
    def divide(self):
        return self.a/self.b
    def add(self): #重写 想用父类方法 又不想重新写
        super(MathMethod_1,self).add()
        print("我是子类的加法：",self.a+self.b+10)

MathMethod_1(5,6).add()
