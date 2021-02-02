import time
from selenium.webdriver.common.by import By
from Common.basepage import Base
from Common.log import FrameLog

# 这里对页面进行分析，提取出来要封装的函数
class BookPage(Base):
    log = FrameLog('map_management').log()

    def book(self):
        try:
            return self.findele(By.XPATH, '')
        except:
            self.log.error('卧槽，点击预订失败了，开发定位下吧')

    def book_type(self):
        return self.findele(By.CSS_SELECTOR, '')

    def book_btn(self):
        try:
            time.sleep(7)
            self.book_type().click()
            time.sleep(2)
            self.book().click()
        # 如果try没执行同，则执行except并返回url
        except:
            self.log.error('车次查询失败')
        return self.url()

