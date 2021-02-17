# coding=utf-8
import pytest

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

    # 被pytest.fixture()装饰的函数，函数名可以作为变量传递给测试用例，最终在执行测试用例之前执行这个装饰过的函数
    def test_case_1(self, test_case_8):
        print('---1号用例完成---')

    # （2）这里按照调用了前面的函数test_case_6，局部的调用，执行优先级是最高的。
    @pytest.mark.usefixtures('test_case_7')
    @pytest.mark.usefixtures('test_case_6')
    def test_case_2(self):
        print('---2号用例完成---')

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


if __name__ == "__main__":
    pytest.main(['-vs', 'test_1.py'])





# @pytest.fixture(scope='package')
# @pytest.yield_fixture()
# @pytest.mark.parametrize
# @pytest.mark.usefixtures()
# @pytest.mark.xfail()
# @pytest.mark.skipif
# @pytest.main()

