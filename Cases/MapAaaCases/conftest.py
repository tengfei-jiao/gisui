# coding=utf-8
import pytest
from selenium import webdriver
import logging

logger = logging.getLogger()

@pytest.fixture(autouse=True)
def start_module(project_session_start):
    print('---进入要执行模块的的界面---')


