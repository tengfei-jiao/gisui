# coding=utf-8
import os, sys, time, logging, allure, pytest
from selenium import webdriver
from logging import config
from Common.function import *
from Common.base import Base

driver = None

# 用例执行失败后，会把失败截图放到allure报告中
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """获取常规钩子方法的调用结果,返回一个result对象
　　:param item:测试用例对象
　　:param call:测试用例的测试步骤
　　         执行完常规钩子函数返回的report报告有个属性叫report.when
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        mode = "a" if os.path.exists("failures") else "w"  # 就是判断括号里的文件是否存在的意思，括号内的可以是文件路径。
        with open("failures", mode) as f:  # 打开这个文件
            if "tmpir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
                f.write(report.nodeid + extra + "\n")
            with allure.step('添加失败截图...'):  # 添加1个测试测试步骤为了防截图
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)  # 插入截图的详细信息


@pytest.fixture(autouse=True)
def project_start():
    """每个用例都会自动执行登录操作
        """
    global driver
    driver = webdriver.Chrome()  # 打开浏览器
    driver.get(config_url())  # 打卡网址
    driver.maximize_window()  # 浏览器最大化
    driver.implicitly_wait(30)  # 最多等待10秒，10秒后继续执行
    # 跳过红色安全警告
    driver.find_element_by_id("xxx")
    driver.find_element_by_id("xxx")
    # 开始登录
    driver.find_element_by_id("username").send_keys(config_urer())
    driver.find_element_by_id("password").send_keys(config_password())
    logging.info("----------成功登录环境----------")
    yield driver
    driver.quit()
    logging.info("----------成功退出环境----------")


if __name__ == '__main__':
    project_start()