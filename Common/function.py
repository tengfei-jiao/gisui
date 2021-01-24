# coding=utf-8
import configparser
import os
'''
os 模块：获取操作系统级别的目录、文件夹、文件的读取和写入等
configparser 模块：读取配置文件
'''


'''
os.path.split() 将文件路径转化为元组：('C:\\Users\\Administrator\\PycharmProjects\\pythonProject3\\test\\日常练习', 'test.py')
os.path.realpath(__file__)获取你正在打开的脚本的绝对路径
split() 拆分字符串返回列表。本来返回D:\se_frame\Common，从大写C切开，只返回前面的路径也就是项目路径
'''
def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]


# 返回config.ini文件中testUrl
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + "config.ini")
    return config.get('testUrl', 'url')


if __name__ == '__main__':
    print('项目路径为：' + project_path())
    print('被测系统URL为：' + config_url())
