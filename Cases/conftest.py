# coding=utf-8
import pytest
from selenium import webdriver

# 日志以配好

# test_3模块所有的用例都执行一次 >>> autouse=True
@pytest.fixture(autouse=True)
def project_session_start():
    logger.info("==========进入 地图管理界面===========")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    logger.info("==========退出 地图管理界面===========")
# # 部分用例的前后置
# @pytest.fixture()
# def eat():
#     print('\n这是test03、test04的前置方法')
#     yield
#     print('\n这里是test03、test04的后置方法')

#
# # test_3模块里的每个类执行一次
# @pytest.fixture(scope='class')
# def houyisheng():
#     print('\n这是test03、test04的前置方法')
#     yield
#     print('\n这里是test03、test04的后置方法')
#
# # test_3模块只执行一次
# @pytest.fixture(scope='module')
# def yaoweiba():
#     print('\n这是test03、test04的前置方法')
#     yield
#     print('\n这里是test03、test04的后置方法')
#
# # 引入benpao的用例，因为入参为3，执行了3次。
# @pytest.fixture(params=['小黄', '小黑', '小红'])
# def benpao(request):
#     print('\n这是前置方法')
#     yield request.param   # 跟return request.param一样，但yield后可接代码
#     print('\n这是后置方法')