# coding=utf-8
import pytest

# test_3模块所有的用例都执行一次 >>> autouse=True
@pytest.fixture(autouse=True)
def fixture_mokuai2():
    print('\n进入建筑物管理界面')
    yield
    print('\n退出建筑物管理界面')
