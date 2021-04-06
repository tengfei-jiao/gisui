# coding=utf-8
import pytest
import allure
import os

@pytest.fixture()
def test_case_3():
    print('---3号用例完成---')

@pytest.fixture()
def test_case_4():
    print('---4号用例完成---')

@pytest.fixture()
def test_case_5():
    print('---5号用例完成---')

@pytest.fixture()
def test_case_6():
    print('---6号用例完成---')

@pytest.fixture()
def test_case_7():
    print('---7号用例完成---')

@pytest.fixture()
def test_case_8():
    print('---8号用例完成---')

# （1）这里按照【从下到上的顺序】，执行优先级是3、4、5
@pytest.mark.usefixtures('test_case_5')
@pytest.mark.usefixtures('test_case_4')
@pytest.mark.usefixtures('test_case_3')
class Testlogin001:

    @allure.feature('这里是1级特性')
    @allure.story('这里是2级特性')
    @allure.title('这里是用例标题1')
    @allure.description('这里是用例描述1')
    @allure.severity('blocker')
    @allure.issue('添加缺陷对应链接：https://www.baidu.com/')
    @allure.testcase('测试用例链接，比如：https://www.baidu.com/')
    # 被pytest.fixture()装饰的函数，函数名可以作为变量传递给测试用例，最终在执行测试用例之前执行这个装饰过的函数
    def test_case_1(self, test_case_8):
        print('---1号用例完成---')
        with allure.step('测试步骤：'):
            allure.attach('测试步骤1')
            allure.attach('测试步骤2')

    @allure.feature('这里是1级特性')
    @allure.story('这里是2级特性')
    @allure.title('这里是用例标题2')
    @allure.description('这里是用例描述2')
    @allure.severity('critical')
    # （2）这里按照调用了前面的函数test_case_6，局部的调用，执行优先级是最高的。
    @pytest.mark.usefixtures('test_case_7')
    @pytest.mark.usefixtures('test_case_6')
    def test_case_2(self):
        print('---2号用例完成---')
        allure.attach('用例的一些test body信息')

    # 单参数单值
    @pytest.mark.parametrize('arg', [1])
    def test_case_9(self, arg):
        print("传入的值为：{}".format(arg))
        assert arg == 1

    # 单参数多值
    @pytest.mark.parametrize('arg',['abc',1,{'a':1,'b':3},(4,5)])
    def test_case_10(self, arg):
        print(f"传入的值为：{arg}")

    # 多参数多值
    @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("5-2", 3), ("5*2", 10)])
    def test_case_11(self, test_input, expected):
        print(f"原值：{test_input} 期望值{expected}")
        assert eval(test_input) == expected

    @pytest.mark.xfail(condition=1<3, reason='该功能尚未完善,还在调测中')
    def test_case_12(self):
        print('---12号用例完成---')

    @pytest.mark.skipif(reason='test_case_13用例还在调测中')
    def test_case_13(self):
        print('---13号用例完成---')


@pytest.mark.skipif(1>3, reason='Testlogin2模块还在调测中')
class Testlogin2:

    def test_case_14(self, start_module):
        print('---14号用例完成---')
        allure.attach(start_module.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
        # allure.attach.file()

if __name__ == "__main__":

    # pytest.main(['test_1.py'])

    # 生成测试报告---json格式
    pytest.main(['--alluredir', 'D:/se_frame/Reports/allure_data', 'test_1.py::Testlogin001::test_case_1'])
    # allure转换成---html并打开测试报告
    os.system('cd D:/se_frame/Reports/allure_data')
    os.system('allure generate D:/se_frame/Reports/allure_data -o D:/se_frame/Reports/html --clean')
    os.system('allure serve D:/se_frame/Reports/allure_data')




# @pytest.fixture(scope='package')
# @pytest.yield_fixture()
# @pytest.mark.parametrize
# @pytest.mark.usefixtures()
# @pytest.mark.xfail()
# @pytest.mark.skipif
# @pytest.main()

