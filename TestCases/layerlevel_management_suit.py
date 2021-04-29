# coding=utf-8
import pytest, allure, os


def report(case):
    """执行模块1用例，并生成allure测试报告
        """
    path = "../OutPuts/Reports/allure_data"
    pytest.main(['--alluredir', 'path', 'case'])
    os.system(f"cd {path}")
    os.system(f"allure generate {path} -o {path}/html --clean")


if __name__ == '__main__':

    report("./testModuleOneCases/test_module_one_cases.py::Test_layerlevel_management")  # 执行类
    # report("./testModuleOneCases/test_module_one_cases.py::Test_layerlevel_management::test_xxx1")  # 执行某个用例