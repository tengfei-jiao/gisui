# coding=utf-8
import pytest
from selenium import webdriver

# logger已经配置完了，待添加

# test_3模块所有的用例都执行一次 >>> autouse=True
@pytest.fixture(autouse=True)
def start_module(project_module_start):
    '''
    每个模块单独打开一次浏览器，此时 driver.quit() 需要单独加上
    :param project_module_start:  每个模块单独打开一次浏览器
    :return: driver ug
    '''
    logger.info("==========开始执行测试用例集===========")
    global driver
    driver = project_module_start
    driver.get(url)
    driver.get(GD.web_user_url)
    ug = UserPage(driver)
    yield (driver, ug)
    logger.info("==========结束执行测试用例集===========")
    driver.quit()


