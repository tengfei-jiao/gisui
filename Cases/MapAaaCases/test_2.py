import pytest, os
from selenium import webdriver
import allure


def test_login(browser):
    with allure.step("step1：打开登录首页"):
        browser.get("https://qzone.qq.com/")
    with allure.step("step2：输入账号：admin"):
        browser.find_element_by_name("u").send_keys("admin")
    with allure.step("step2：输入密码：123456"):
        browser.find_element_by_name("p").send_keys("123456")

def test_assertion():
    assert [1, 2, 3] == [1, 2, 4], "left is [1,2,3], right is [1,2,4]"


if __name__ == "__main__":

    pytest.main(['test_2.py::test_assertion'])


    # pytest.main(['--alluredir', 'D:/se_frame/Reports/allure_data', 'test_2.py::test_login'])
    # # allure转换成---html并打开测试报告
    # os.system('cd D:/se_frame/Reports/allure_data')
    # os.system('allure generate D:/se_frame/Reports/allure_data -o D:/se_frame/Reports/html --clean')