# -*- conding: utf-8 -*-
# @Time      :2019/7/4 16:31
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_for.py

# s = "hello"
# l = [1,2,3]
# d = {"age":18,"name":"hehe"}
# for item in d:
#     print(d[item])

# L = [4,6,3,7]
# sum = 0
# for i in L:
#     sum +=i
# print(sum)
# sum = 0
# for i in  range(10):
#     sex = input("请输入性别：")
#     if sex=="f":
#         age = int(input("请输入年龄:"))
#
#         if 10<=age<=12:
#             sum+=1
#             print("年龄相符，可以加入")
#         else:
#             print("年龄不符，不可以")
#     elif sex =="m":
#         print("性别不符")
#     else:
#         print('输入错误')
#
# print(sum)
# print(list(range(5)))

# L =[['w','e','r'],['t','y','u']]
# for j,i ,a in L:
#     print(j)
#     print(i)
#     print(a)

# for i in L:
#     for j in i:
#         print(j)

#打印直角三角形

# for i in range(1,6):
#     print("*"*i)

#打印等腰三角形
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(' ',end='')
#     for k in range(1,i+1):
#         print("* ",end='')
#     print()

#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(i,j,i*j),end=" ")
#     print("")

#冒泡排序法
L =[7,5,9,3,2,6]
for i in range(len(L)-1):
    for j in range(i,len(L)):
        if L[i]> L[j]:
            L[i],L[j] = L[j],L[i]
print(L)



Line = [4,1,6,5,9,2,6,2,7,1,3,9,2,9,0,3,5,9,8,6,3,4]
result=Line[1::2]
result = ""
for i in range(len(Line)):
    if i%2!=0:
        result += str(Line[i])
print("联系方式：{}".format(result))

# print("联系方式：{}".format(result))


