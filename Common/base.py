# --*--coding=utf-8--*--
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.log import FrameLog


class Base:
    """这里封装了操作浏览器的基础操作"""

    def __init__(self, driver, log):
        self.driver = driver
        self.log = FrameLog().log()

    def findele(self, *args):
        """
        定位元素,单星号参数代表此处接受任意多个非关键字参数
        :param args:
        :return:
        """
        return self.driver.find_element(*args)

    # 对元素click
    def click(self, *args):
        return self.findele(*args).click()

    # 发送信息
    def sendkey(self, args, value):
        self.findele(*args).send_keys(value)

    # 调用js方法
    def js(self, str):
        self.driver.execute_script(str)

    def dddd(self, *args):
        """
        检查元素是否存在于页面和可见。可见性意味着不仅显示元素,但其高度和宽度也大于0。定位器-用于查找元素,
        一旦WebElement定位并可见，返回它
        :param args:
        :return:
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located())

    def aaaaaaaa(self,*args):
        """
        检查是否有弹窗出现
        如果点击某个操作有弹框，用这个更快。
        :param args:
        :return:
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.alert_is_present())

    # 调用不要输入元组。*args已经打包了
    def dominance_clickable(self, *args):
        """
        检查元素的期望是可见的并已启用，以便您可以单击它
        点击元素之前带上这个，会更快。
        :param args:
        :return:
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(args))

    def aaa1(self,*args):
        """
        检查标题是否包含区分大小写的子字符串。title是期望的title片段,当标题匹配时返回True，否则返回False
        切换浏览器界面的title时候带上这个，会更快。
        :return:
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.title_contains(args))

    def aaaa2(self, *args):
        """
        期望检查给定帧是否可用于,切换到。 如果框架可用，则将给定的驱动程序切换到指定的帧。
        切换框架时候，用它更快。
        :param args:
        :return:
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.frame_to_be_available_and_switch_to_it(args))

    def aaaaa2(self,*args):
        """
        期望检查给定文本是否存在于指定的元素。
        如果你定位text的文本并点击它，使用它更快
        :param args:
        :return:
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element)

    def aaa(self, *args):
        """
        检查DOM上是否存在元素的期望值。一页的长度。这并不一定意味着元素是可见的。
        这个研究中
        :return:
        """
        return WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(args))

    def bbb(self, *args):
        """
        选择检查选择的期望。元素是WebElement对象
        不是很明白
        :param args:
        :return:
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_selected(args))





    def url(self):
        return self.driver.current_url

    # 后退
    def back(self):
        self.driver.back()

    # 前进
    def forward(self):
        self.driver.forward()

    # 退出
    def quit(self):
        self.driver.quit()

    # # 函数id将返回按照id属性来定位元素的语句
    # def id(element):
    #     return driver.find_element_by_id(element)
    #
    # # 函数css将返回css selector方式来定位元素的语句
    # def css(element):
    #     return driver.find_element_by_css_selector(element)
    #
    # # 函数xpath将返回xpath方式来定位元素的语句
    # def xpath(element):
    #     return driver.find_element_by_xpath(element)
    #
    # # 函数js通过selenium来执行javascript语句
    # def js(element):
    #     driver.execute_script(f"document.getElementById(f'{element}').removeAttribute('readonly')")
