# coding=utf-8
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def project_session_start():
    print('\n启动浏览器')
    yield
    print('\n退出浏览器')