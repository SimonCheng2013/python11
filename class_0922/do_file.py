# -*- conding: utf-8 -*-
# @Time      :2019/7/5 16:26
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :do_file.py
from time import sleep
#read 读取全部
# with open("python11.txt",'r+') as file:
#     a = file.read()
#     file.write('8') #追加到末尾
#     sleep(3)
#     print(a)

# with open("python11.txt",'a') as file:
#
#     file.write('8') #w w+覆盖写入
#
#     # a = file.read()
#     sleep(3)
#     # print(a)

# with open("python11.txt",'r') as file:
#     r = file.readline()
#     print(r)
#     r = file.readline()
#     print(r)
#     r = file.readline()
#     print(r)

with open("python11.txt",'a') as file:
    # r = file.readlines()#按照列表返回
    # print(r)
    w = file.writelines(['777\n','888'])



