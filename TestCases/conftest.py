# coding=utf-8
import pytest, os, allure
from selenium import webdriver
import xlrd


# 对于给定的测试用例(item)和调用步骤(call)，返回一个测试报告对象(_pytest.runner.TestReport)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
　　每个测试用例执行后，制作测试报告
　　:param item:测试用例对象
　　:param call:测试用例的测试步骤
　　         执行完常规钩子函数返回的report报告有个属性叫report.when
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
    :return:
    """
    # 获取常规钩子方法的调用结果,返回一个result对象
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:

        # 就是判断括号里的文件是否存在的意思，括号内的可以是文件路径。
        mode = "a" if os.path.exists("failures") else "w"
        # 打开这个文件
        with open("failures", mode) as f:
            if "tmpir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
                f.write(report.nodeid + extra + "\n")

            # 添加1个测试测试步骤为了防截图
            with allure.step('添加失败截图...'):
                # 插入截图的详细信息
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope='session', autouse=True)
def browser():

    global driver
    driver = webdriver.Chrome()
    return driver
