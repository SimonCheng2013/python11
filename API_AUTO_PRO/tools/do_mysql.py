# -*- conding: utf-8 -*-
# @Time      :2019/8/5 14:14
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :do_mysql.py
import pymysql
from tools import project_path
from tools.read_config import ReadConfig
class DoMysql:
    def do_mysql(self,query_sql,state=1):
        db_config = eval(ReadConfig().get_config(project_path.case_config_path,"DB","db_config"))
        cnn = pymysql.connect(**db_config)

        #游标cursor
        cursor=cnn.cursor()
        #写sql语句
        #执行语句
        cursor.execute(query_sql)
        if state==1:
            res = cursor.fetchone()  # 元组 针对一条数据
            # print(res)#获取结果，打印结果
        else:
            res=cursor.fetchall() #列表 针对多行数据 列表嵌套元组
            # print(res)

        #关闭游标
        cursor.close()
        #关闭连接
        cnn.close()
        return res
if __name__ == '__main__':
    query_sql = "select * from auth_group where id =1"
    res = DoMysql().do_mysql(query_sql)
    print(res)
