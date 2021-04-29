# coding=utf-8
import os, allure, pytest, logging
from selenium import webdriver
from Common.function import project_path
from PageObject.Module_One_Page.module_one_page import Model_one_interface


@pytest.fixture(autouse=True)
def po_layer(project_start):
    """业务层代码继承了外层conftest.py的函数project_start,获取了浏览器驱动
        """
    return Model_one_interface(project_start)


@pytest.fixture(autouse=True)
def enter_interface(po_layer):
    """进入浏览器界面，po_layer继承了业务层代码、浏览器驱动，直接调用业务层封装好的方法即可。
        """
    po_layer.enter_module_one()