# coding=utf-8
import pytest
import time
from Base.base_unit import UnitBase

class Testlogin(UnitBase):

    def setUp(self):
        print('\n进入管理界面')

    def tearDown(self):
        print('退出管理界面')

    # 装饰器：标记用例执行的顺序，用的插件：pytest-ordering
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_case_01(self):
        time.sleep(3)
        print('一只小黄狗')

    @pytest.mark.product
    @pytest.mark.run(order=1)
    def test_case_02(self):
        time.sleep(3)
        print('一只小红狗')

    @pytest.mark.run(order=3)
    def test_case_04(self):
        time.sleep(3)
        print('一只小绿狗')

    @pytest.mark.run(order=4)
    def test_case4_01_ao(self):
        time.sleep(3)
        print('一只小花狗')
        assert 1==2



