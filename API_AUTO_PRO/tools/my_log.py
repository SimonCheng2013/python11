# -*- conding: utf-8 -*-
# @Time      :2019/8/2 17:34
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :my_log.py
import logging #
class MyLog:
    def my_log(self,msg,level):
        #定义一个日志收集器
        # my_logger = logging.getLogger('python11')
        my_logger = logging.getLogger(__name__)

        #设定级别
        my_logger.setLevel("DEBUG")
        #设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        #收集日志
        # my_logger.debug("python11期1117学习logging已经懵逼")
        # my_logger.error("python11期1117是最棒的！坚强点")

        #创建一个我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel("INFO")
        ch.setFormatter(formatter)

        # fh=logging.FileHandler("py11.txt",encoding='utf-8')
        # fh.setLevel("DEBUG")
        # fh.setFormatter(formatter)
        #两者对接--指定输出渠道
        my_logger.addHandler(ch)
        # my_logger.addHandler(fh)

        #收集日志
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)
        #关闭渠道
        my_logger.removeHandler(ch)
        # my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')
    def info(self,msg):
        self.my_log(msg,'INFO')
    def error(self,msg):
        self.my_log(msg,'ERROR')
if __name__ == '__main__':
    my_logger = MyLog()
    # my_logger.debug("可不可以这样？？")
    my_logger.info("可行吗")
    # my_logger.error("执行用例出错：{}".format("rrrrr"))
    # my_logger.debug("执行用例出错：{}".format("ddd"))
    # my_logger.my_log("qqq","ERROR")


    # MyLog().my_log('stone 今天萌萌哒',"ERROR")
    # MyLog().my_log('MIT 今天萌萌哒',"ERROR")
    # MyLog().my_log('巴拉巴拉今天萌萌哒',"ERROR")
