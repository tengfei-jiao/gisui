# coding=utf-8
import pytest
import time

@pytest.mark.usefixtures('start_session')
class Testlogin001:

    def test_case3(self):
        time.sleep(3)
        print('第三个用例')

    def test_case4(self):
        print('第四个用例')


if __name__ == "__main__":

    pytest.main(['-vs', 'test_1.py'])