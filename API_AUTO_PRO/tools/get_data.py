# -*- conding: utf-8 -*-
# @Time      :2019/7/30 11:12
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :get_cookie.py
from tools import project_path
import pandas as pd

class GetData:
    Cookie=None
    NoRegTel = pd.read_excel(project_path.test_case_path,sheet_name='init').ix[0,0]


# setattr(GetCookie,"Cookie","123456")
# print(hasattr(GetCookie,"Cookie555"))
# print(getattr(GetCookie,"Cookie"))

# print(getattr(GetData,"NoRegTel"))
print(pd.read_excel(project_path.test_case_path,sheet_name='init').ix[0,0])

{
    'Content-Type': "application/json",
    'sid': "AAFF50AB129A4095E3F6530132B037D8B8019B66724379B9BD75EE1994D0D289CF1BFC75399000977240EC6143C2ABC4",
    }
