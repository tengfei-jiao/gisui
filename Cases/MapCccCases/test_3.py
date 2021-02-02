# coding=utf-8
import pytest
import time


# 部分用例的前后置
@pytest.fixture()
def eat():
    print('\n这是test03、test04的前置方法')
    yield
    print('\n这里是test03、test04的后置方法')
#
# # test_3模块所有的用例都执行一次 >>> autouse=True
# @pytest.fixture(autouse=True)
# def heshui():
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

class Testlogin1():

    # (1) 在该类所有用例执行开始前，要干的事，只干一次。
    def setup_class(self):
        print('\n进入到***界面,连接***数据库,创建接口请求对象')

    def teardown_class(self):
        print('日志开始销毁')

    # (2) 每个用例执行性都会执行setup方法
    def setup(self):
        print('\n进入管理界面')

    def teardown(self):
        print('退出管理界面')

    def test_case_01(self):
        time.sleep(3)
        print('一只小黄狗')

    def test_case_02(self, eat):
        print('一只小黑狗')

    def test_case_03(self, eat):
        print('一只小野狗')

    def test_case_04(self, benpao):
        print(f'{benpao}在奔跑')

if __name__ == "__main__":

    pytest.main(['-vs','test_3.py'])