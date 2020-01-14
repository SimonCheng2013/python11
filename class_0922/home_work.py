# -*- conding: utf-8 -*-
# @Time      :2019/7/4 15:38
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :home_work.py
# a=int(input("请问价格："))
# if a<50:
#     print("没有折扣券")
#     print("您需要支付：{}".format(a))
# elif 50<=a<=100:
#     print("折扣是：10%")
#     print("支付价格：{}".format(a*0.9))
# elif a>100:
#     print("折扣是：20%")
#     print("支付价格：{}".format(a * 0.8))

import random
b = random.randint(1,9) #前包后包[]
num_2 = int(input("我猜："))
print("b是：%d"%b)

if num_2>b:
    print("big")
elif num_2<b:
    print('less')
else:
    print('equal')

