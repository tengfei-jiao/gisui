# coding=utf-8
import logging
import time
from Common.function import project_path

# 单词：formatter格式器、handler处理程序、FileHandler文件内容处理程序
class FrameLog:
    """
    这里定义了日志输出的基本格式
    """
    def __init__(self, name=None):
        # 调用Framelog，user默认root、日志级别默认debug
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # handler定义了将日志发送到哪里，如：pycharm控制器、日志文件、邮件、短信等，
        # 创建一个handler,定义了将日志发送到文件，并设置了日志内容的格式、级别、
        self.log_name = f"{project_path()}/logs/" + time.strftime("%Y_%m_%d") + "_log.log"
        file = logging.FileHandler(self.log_name, "a", "utf-8")
        formatter = logging.Formatter('[%(asctime)s] %(filename)s-> %(funcName)s line:%(lineno)d [%(levelname)s]%(''message)s')
        file.setFormatter(formatter)
        file.setLevel(logging.DEBUG)

        # 再次创建一个handler，将日志发送到控制器
        console = logging.StreamHandler(stream=None)
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)

        # 将2个处理器加入到logger中，不但向控制器输出、还想文件输出。
        self.logger.addHandler(file)
        self.logger.addHandler(console)

    def log(self):
        return self.logger


if __name__ == '__main__':
    # cgis模块，打印cgis-server模块的日志
    log = FrameLog('cgis-server').log()
    try:
        print(2/0)
    except ZeroDivisionError:
        print('这里打印在控制台')
        # 下面的message输入到日志
        log.error('这是一个框架性的错误11111111')
        log.debug('这是业务代码里的错误1111111111')
        log.info('这是业务代码里info级别的错误11111111111')
        log.critical('这是系统性的错误1111111')

    # fgis模块，打印fgis - server模块的日志
    log = FrameLog('fgis-server').log()
    try:
        print(2/0)
    except ZeroDivisionError:
        print('这里打印在控制台')
        # 下面的message输入到日志
        log.error('这是一个框架性的错误22222')
        log.debug('这是业务代码里的错误22')
        log.info('这是业务代码里info级别的错误2222')
        log.critical('这是系统性的错误222')


# coding=utf-8
import logging
import logging.config
logging.config.fileConfig('log.conf')

logs = logging.getLogger('error')
logs.error('errorsssss')
