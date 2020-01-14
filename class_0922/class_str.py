# -*- conding: utf-8 -*-
# @Time      :2019/7/4 8:58
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_str.py
s='666hello!666'
#[:]切片
# print(s[::-1])
#切除
# print(s.split(" "))
# print(s.split('e'))
# print(s.split('l'))#['he','lo!'] ['he','lo!']['he',]

#去除 1.默认去掉两端空格 2.只能去掉头和尾的指定字符(包含重复)
# new = s.strip('!')
# print(len(s))
# print(s)
# new = s.strip()
# print(new)
# print(len(new))
new =s.strip("6")
print(new)

#字符串拼接 左右两边变量值类型相同才可拼接
# s_1 = 'hello'
# s_2 = 'word'
# s_3 = 666
# print(s_1+s_2+str(s_3))

#字符串格式化输出 % format
age = 18
name = 'jack'
#format
print('我是{},今年{}'.format(age,name))
# %
print('我是%s,今年%s'%(age,name))
