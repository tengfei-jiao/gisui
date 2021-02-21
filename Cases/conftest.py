# coding=utf-8
import pytest, os, allure
from selenium import webdriver


@pytest.fixture(autouse=True)
def project_session_start():
    driver = webdriver.Chrome()
    print('\n启动浏览器')
    yield
    driver.quit()
    print('\n退出浏览器')

# 将失败用例的截图加到allure报告里面【待整理】

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         if hasattr(project_session_start, "get_screenshot_as_png"):
#             with allure.step('添加失败截图...'):
#                 allure.attach(project_session_start.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)