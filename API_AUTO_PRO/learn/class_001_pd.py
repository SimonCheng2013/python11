# -*- conding: utf-8 -*-
# @Time      :2019/7/30 13:49
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :class_001_pd.py
#导入pasdas from

import pandas as pd

df = pd.read_excel('test_data.xlsx',sheet_name='recharge')
# print(df.values)
# print(df.ix[1,3])#第二列
# df.ix[1,["url","data"]].to_dict()
test_data=[]
for i in df.index.values:
    row_data=df.ix[i,['url','data','title','case_id','http_method']].to_dict()
    test_data.append(row_data)
print(test_data)