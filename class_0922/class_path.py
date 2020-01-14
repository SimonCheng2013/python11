# -*- conding: utf-8 -*-
# @Time      :2019/7/8 9:52
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_path.py
import os

# os.mkdir('Alisa/Monica')
# os.mkdir('Vict/Monica')
# os.rmdir('Alisa')

#获取当前文件夹路径
# path =os.getcwd()
# print(path)

#获取当前文件路径
# path_2 = os.path.realpath(__file__)
# print(path_2)

#join
# new_path = os.path.join(os.getcwd(),'tt','ee')
# new_path = os.path.join(os.getcwd(),'tt/ee','oo')
# print(new_path)
# os.mkdir(new_path)

#判断文件还是目录
# print(os.path.isdir(os.getcwd()))
# print(os.path.isfile(os.getcwd()))

#判断文件是否存在
# print(os.path.exists('D:\PycharmProjects\python11\class_0922\class_for.py'))

#罗列出当前路径所有文件/目录
# print(os.listdir(os.getcwd()))

for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.path.join(os.getcwd(),path))
    elif os.path.isfile(path):
        print(os.path.join(os.getcwd(),path))