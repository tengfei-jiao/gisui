# --*--coding=utf-8--*--
from Common.log import FrameLog
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import logging


class Base:
    """这里封装了操作浏览器的基础操作"""

    def __init__(self, driver, log):
        self.driver = driver

    def id(self, element):
        return self.driver.find_element_by_id(element)

    def findele(self, *element):
        """
        压包，和解包，示例：findele(By.Id, "xxx")
        """
        return self.driver.find_element(*element)

    def findeles(self, *element):
        """
        压包，和解包，例如findele(By.Id, "xxx"),返回是一个许多个元素
        :param element:
        :return:
        """
        return self.driver.find_elements(*element)

    def clear(self, *element):
        # 清空要输入的内容，一般用于输入前置
        return self.driver.findele(*element).clear()
        
    def click(self, *element):
        """
        点击元素，示例：click(By.Xpath, '[xxx]')
        """
        return self.driver.findele(*element).click()

    def sendkey(self, value, *element):
        """
        给输入框发送内容，示例：sendkey("tfjiao", By.Xpath, '[xxx]')
        """
        self.findele(*element).send_keys(value)

    def move_offset_click(self, canvas, *element):
        """
        移动到画布这个元素上，移动到某个位置点，并进行点击 >>> 用于画布桑画形状
        示例：move_offset_click(By.Xpath, '[xxx]', 200, 300)
        200是x坐标，300是y坐标。具体参考move_by_offset的源码
        """
        return ActionChains(self.driver).move_to_element(canvas).move_by_offset(*element).release().click().perform()

    def move_offset_click_double(self, canvas, *elenment):
        """
        移动到画布这个元素上，移动到某个位置点，并进行双击，跟move_offset_click方法类似 >>> 用于画布上双击结束绘画
        """
        return ActionChains(self.driver).move_to_element(canvas).move_by_offset(*elenment).release().double_click().perform()

    def move_element_click(self, *element):
        """
        移动到元素上，并点击。示例：move_element_click(By.Xpath, '[xxx]')
        """
        return ActionChains(self.driver).move_to_element(self.findele(*element)).release().click().perform()

    def move_element_offset_click(self, xoffset, yoffset, *element):
        """
        移动到元素的左侧位置，示例：move_element_offset_click(100, 200, By.Id, "xxx")
        """
        return ActionChains(self.driver).move_to_element(self.findele(*element), xoffset, yoffset).click().perform()

    def select_value(self, id, value):
        """
        选择下拉框的元素，id是下拉框的id值，value是下拉框元素的value属性值
        注意：下拉框有时候开发会把display设置为none,这里需要js脚本打开改变属性值，后续js脚本会说到
        """
        return Select(self.findele(By.ID, id)).select_by_value(value)

    def select_text(self, id, text):
        """
        选择下拉框的元素，id是下拉框的id,text是下拉框元素显示在页面的内容
        注意：下拉框有时候开发会把display设置为none,需要js脚本处理
        """
        return Select(self.findele(By.ID, id)).select_by_visible_text(text)

    def select_index(self, id, index):
        """
        选择下拉框的元素，id是下拉框的id,index是索引值，从0开始
        注意：下拉框有时候开发会把display设置为none,需要js脚本处理
        """
        return Select(self.findele(By.ID, id)).select_by_index(index)

    def js(self):
        """
        关于js的用法，document.querySelectorAll('css语法')基本满足了所有需要
        selenium_js定位详解：https://blog.csdn.net/weixin_45451320/article/details/115104455
        selenium_css定位详解：https://blog.csdn.net/weixin_45451320/article/details/115101192
        """
        return self.driver.execute_script('document.querySelectorAll("css语法")[1].click()')

    def js(self, str):
        return self.driver.execute_script(str)

    def click_js(self, *element):
        """
        js语法点击
        """
        return self.driver.execute_script("argument[0].click();", self.findele(*element))

    def switchframe(self, element):
        """
        切换框架
        """
        return self.driver.switch_to.frame(element)

    def wait_click(self, *element):
        """
        每0.5秒检查一次元素，元素能被点击，则执行。
        示例：wait_click(By.Xpath, '[xxx]')
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(element))

    def wait_located(self, *element):
        """
        检查元素是否存在于页面和可见。可见性意味着不仅显示元素,但其高度和宽度也大于0。定位器-用于查找元素,
        一旦WebElement定位并可见，返回它
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(element))

    def wait_alert(self,*element):
        """
        检查是否有弹窗出现
        如果点击某个操作有弹框，用这个更快。
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.alert_is_present(element))

    def wait_title(self,*element):
        """
        检查标题是否包含区分大小写的子字符串。title是期望的title片段,当标题匹配时返回True，否则返回False
        切换浏览器界面的title时候带上这个，会更快。
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.title_contains(element))

    def wait_frame(self, *element):
        """
        期望检查给定帧是否可用于,切换到。 如果框架可用，则将给定的驱动程序切换到指定的帧。
        切换框架时候，用它更快。
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.frame_to_be_available_and_switch_to_it(element))

    def wait_text_present(self,*element):
        """
        期望检查给定文本是否存在于指定的元素。
        如果你定位text的文本并点击它，使用它更快
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.text_to_be_present_in_element(element))

    def wait_visibility_located(self, *element):
        """
        检查DOM上是否存在元素的期望值。一页的长度。这并不一定意味着元素是可见的。
        """
        return WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located(element))

    def wait_selected(self, *element):
        """
        选择检查选择的期望。元素是WebElement对象
        """
        return WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_selected(element))

    def displayed(self, *element):
        """
        检查元素是否可见，可见则通过
        """
        return self.driver.findele(*element).is_displayed()

    def enabled(self, *element):
        return self.driver.findele(*element).is_enabled()

    def url(self):
        return self.driver.current_url

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def quit(self):
        self.driver.quit()
