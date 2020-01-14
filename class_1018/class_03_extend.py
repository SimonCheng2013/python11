# -*- conding: utf-8 -*-
# @Time      :2019/7/8 16:50
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_03_extend.py
class RobotOne():
    # def __init__(self,year,name):
    #     self.year=year
    #     self.name = name
    def walking_on_group(self):
        print(self.name+"只能在平地行走,有障碍就摔倒")
    def robot_info(self):
        print("{}年产生的机器人{},是中国研发的".format(self.year,self.name))
# class RobotTwo(RobotOne):
#     def walking_on_group(self): #重写
#         print(self.name+"可以在平地平稳行走")
#     def walking_avoid_block(self): #拓展
#         print(self.name+"可以避开障碍")

class RobotTwo():
    # def __init__(self,year,name):
    #     self.year = year
    #     self.name = name
    def walking_on_group(self):  # 重写
        print(self.name + "可以在平地平稳行走")

    def walking_avoid_block(self):  # 拓展
        print(self.name + "可以避开障碍")
# r2 = RobotTwo("1990","小王")
# r2.robot_info()
# r2.walking_avoid_block()
# r2.walking_on_group()
#
# r1 = RobotOne('1998','小明')
# r1.walking_on_group()
# r1.robot_info()
class RobotThree(RobotTwo,RobotOne):#复写 谁在前调用谁的复写方法,初始化方法也是
    def __init__(self,year,name):
        self.year=year
        self.name = name
    def jump(self):
        print(self.name+"可以单膝跳跃")
r3 = RobotThree('2000','大王')
r3.jump()
r3.walking_on_group()


