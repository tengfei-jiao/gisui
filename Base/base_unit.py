# coding=utf-8
import unittest
from selenium import webdriver
from Common.function import config_url


# 区分类和方法：首字母大小写
class UnitBase(unittest.TestCase):

    def setup_method(cls, method):
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)


    def teardown_method(cls, method):
        cls.driver.quit()


# 接下来的设置，是为了多线程的测试
class ParaCase(unittest.TestCase):
    # unittest增加参数化
    def __init__(self,methodName='Tests',param=None):
        """
        :param methodName:
        :param param:
        """
        super(ParaCase, self).__init__(methodName)
        self.driver = param


    def setUp(self):
        self.driver.maximize_window()


    @staticmethod
    # 创建测试套件，此套件可以再被继承子类中调用，并在子类中设置需要运行的方法，通过param参数进行设置即可
    def parametrize(testcase, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase(name,param=param))
        return suite



