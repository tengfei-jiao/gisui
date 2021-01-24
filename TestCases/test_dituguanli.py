import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.base import Base
from Base.base_unit import UnitBase
from Common.function import config_url

class Dituguanli(UnitBase,Base):

    # 如何确保是Base类中的self.find_element()跟unittest中的是一类。
    def test_dianjixinwen(self):
        self.findele(By.XPATH,"//*[text()='新闻']")
        print('跑通了')


if __name__ == '__init__':
    test = Dituguanli()
    test.test_dianjixinwen()