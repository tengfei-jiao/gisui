import time, os, sys, logging, allure
import logging.config
from selenium.webdriver.common.by import By
from Common.base import Base
from Common.function import project_path

logging.config.fileConfig(f"f{project_path()}/logging.ini")
logger = logging.getLogger("testUser")


# 这里定义了模块1中的所有的页面相关操作
@allure.feature("模块1中的业务功能点")
class Model_one_interface(Base):

    def enter_module_one(self):
        """从登陆后的界面，进入模块1
            """
        try:
            with allure.step("点击菜单栏"):
                self.click(By.ID, "xxx")
            with allure.step("点击信息管理"):
                self.click(By.XPATH, '//*[text()="信息管理"]')
            with allure.step("点击模块1"):
                self.click(By.XPATH, '//*[text()="模块1"]')
            with allure.step("切换frame,进入模块1界面"):
                self.switchframe("centerFramexxxxxx")
            logger.info("----------没有进入模块1界面-----------")
        except:
            logger.error("----------没有进入模块1界面-----------")

    def layer_hide(self):
        """隐藏、显示图层的显示级别
            """
        try:
            self.wait_visibility_located(By.CSS_SELECTOR, '[id="xxx"][class="xxx"]')
            self.wait_click(By.CSS_SELECTOR, '[id="xxx"][class="xxx"]')
            self.findele(By.CSS_SELECTOR, '[id=""]')
            self.click(By.CSS_SELECTOR, '[value="xxx"]')
            logger.info("the layer was successfully hidden")
            self.wait_click(By.CSS_SELECTOR, '[id="xxx"][class="xxx"]')
            logger.info("the loyer appears successful")
        except Exception as e:
            # 输出异常的内容，一般都是直接看最后两行
            logger.error(e)

    def layer_resert(self):
        """点击重置，图层返回初始状态
            """
        try:
            self.click(By.CSS_SELECTOR, '[value="确定"][class="xxx"]')
            self.wait_click(By.CSS_SELECTOR, '[class="xxx"][value="xxx"]')
            logger.info("the resert layer was successful")
        except:
            logger.error("重置失败")

    def layer_edit_min(self):
        """编辑图层等级，最小级别全部加1，点击确定，进行保存
            """
        try:
            self.wait_click(By.CSS_SELECTOR, '[class="xxx"][value="xxx"]')
            self.click(By.CSS_SELECTOR, '[value="确定"][class="xxx"]')
            self.select_text("xxx", "3_min_level")
            self.select_text("xxx", "5_min_level")
            self.select_text("xxx", "2_min_level")
            self.click(By.CSS_SELECTOR, '[value="确定"]')
            logger.info("all maximum visible levels have been increased by one level")
        except:
            logger.error("加1失败")


if __name__ == '__main__':
    pass