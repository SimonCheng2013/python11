# -*- conding: utf-8 -*-
# @Time      :2019/7/5 10:00
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_wile.py

i = 10
count =0
while True:
    sex = input('请输入性别：')
    if sex =="f":

        age =int(input('请输入年龄：'))
        if 10<=age<=12:
            print('恭喜请加入')
            i -= 1
            count+=1
        else:
            print('年龄不符')
            i -= 1
    elif sex =='m':
        print('性别不符')
        i -= 1
    if i==0:
        print("已结束")
        break
print('入选{}人'.format(count))



