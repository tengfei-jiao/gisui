# coding=utf-8
import unittest
import HTMLTestRunner
import time
from Common.function import project_path


if __name__ == '__init__':
    test_dir = project_path() + 'TestCases'
    tests = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir=None)
    now = time.strftime('%Y-%m-%H-%M-%S',time.localtime(time.time()))
    filepath = project_path() + '/Reports/' + now + '.html'
    fp = open(filepath,'wb')

    # 定义测试报告的标题和描述
    # noinspection PyUnresolvedReferences
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'测试报告')
    runner.run(tests)
    fp.close()

