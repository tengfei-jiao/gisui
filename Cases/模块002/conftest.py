# coding=utf-8
import pytest

# test_3模块所有的用例都执行一次 >>> autouse=True
@pytest.fixture(autouse=True)
def fixture_mokuai2():
    print('\n模块1的用例开始前，都要进入模块2的界面')
    yield
    print('\n每个用例执行完退出模块2的界面')
