# coding=utf-8
import pytest

# 测试用例执行方式1：Terminal栏目输入:pytest -vs test_2.py

# 测试用例执行方式2：这里的执行跟你在哪个文件执行这个代码没有毛关系
if __name__ == '__main__':

    # # 执行测试用例目录（TestCase）下，所有test开头的.py文件
    # pytest.main(['-vs'])
    # pytest.main()

    # 执行测试用例目录（TestCase）下test_1.py的文件,这个文件跟test_2在一层
    pytest.main(['-vs','./MapAaaCases/test_1.py'])

    # 执行interface_testcase目录下面的test开头的用例
    # pytest.main(['-vs', 'D:\\se_frame\\其他'])

    # # 失败的用例再跑2次，运用插件：pytest_rerunfailures
    # pytest.main(['-vs', 'test_2.py', '--reruns=2'])

    # # 执行下test_2.py下的testlogin类下的test_case1方法
    # pytest.main(['-vs', 'test_2.py::Testlogin::test_004'])

    # 分布式运行，执行2个用例。运用插件：pytest-xdist
    # pytest.main(['-vs', 'test_2.py', '-n=2'])

    # # 根据用例的部分字符串指定测试用例,ao是用例的方法名内容
    # pytest.main(['-vs', 'test_2.py', '-k=ao'])
    # pytest -vs test_2.py -k "ao"

    """
    分布式结果是这样的：
    test_2.py::Testlogin::test_case1 
    test_2.py::Testlogin::test_case2 
    [gw1] PASSED test_2.py::Testlogin::test_case2 
    [gw0] PASSED test_2.py::Testlogin::test_case1 
    test_2.py::Testlogin::test_case4 
    test_2.py::Testlogin::test_case3 
    [gw0] PASSED test_2.py::Testlogin::test_case3 
    [gw1] FAILED test_2.py::Testlogin::test_case4 
    """

    """
    pytest参数详解：
    -s 表示输出陶氏信息,包括print打印的信息
    -v 表示更相信的信息
    -vs 一般一起用
    -n 支持分布式运行测试用例
    -k 根据用例的部分字符串指定测试用例
    --html 路径 生成测试报告
    """

# 测试用例执行方式3：通过pytest.ini运行，核心配置文件，
    # 位置：项目根目录,
    # 编码格式：ANSI编码（notepad++转格式）
    # 运行规则：主函数、命令行执行用例都会读取配置文件
    # 文件内容：干掉标注，转成ANSI格式
    """
    [pytest]
    # pytest执行用例的参数，空格分开,这里加了-vs，你用pytest执行用例，就不用加了
    addopts = -vs --html ./report/report.html
    # 测试用例文件夹，可以自己配置
    testpaths = D:\se_frame\TestCases
    # 配置测试搜索的测试类名
    python_classes = Test*
    # 配置测试搜索的测试函数名
    python_functions = test
    # 分模块执行用例
    markers = 
        smoke:冒烟用例
        usermange:用户管理模块
        product:产品模块
    """

# 执行用例的顺序是：
    # 按照@pytest.mark.run(order=2)这个order的值来排序

# 如何执行冒烟用例？分模块执行？分接口？分web？>>>配置文件
    # （1）用例上加标记 @pytest.mark.xxx  例如冒烟用例：@pytest.mark.smoke
    # （2）配置文件进行配置
    # # 执行了冒烟用例、product模块
    # pytest.main(['-vs', 'test_2.py', '-m= smoke or product'])

# pytest跳过用例执行？
    # 无条件跳过>>>@pytest.mark.skip(reason="这个是大数据量的，暂时跳过")
    # 有条件跳过>>>@pytest.mark.skip(age>18,'年龄大于18则跳过')

# 生成测试报告？
    # 第一种报告：pytest.ini加--html 路径。运行用例即可生成测试报告，举例如下：
    """
    [pytest]
    addopts = -vs --html D:\\se_frame\\Reports\\report.html
    testpaths = D:\se_frame\TestCases
    python_classes = Test*
    python_functions = test
    markers =
        smoke:冒烟用例
        usermange:用户管理模块
        product:产品模块
    """
    # 第二种报告：
    # allure-pytest 待补充输出>>>1月27






