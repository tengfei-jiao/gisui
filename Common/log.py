# coding=utf-8
import time
import logging
from Common.function import project_path

# 这里是日志配置文件的应用
# # coding=utf-8
# import logging
# import logging.config
# logging.config.fileConfig('log.conf')
# logs = logging.getLogger('error')
# logs.error('errorsssss')


# 【注意】后面调成日志的配置文件
# 单词：formatter格式器、handler处理程序、FileHandler文件内容处理程序
class FrameLog:
    """这里定义了日志输出的基本格式
        """
    def __init__(self, name=None):
        # 调用Framelog，user默认root、日志级别默认debug
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # handler定义了将日志发送到哪里，如：pycharm控制器、日志文件、邮件、短信等，

        # 创建一个处理程序（handler）,它将日志发送到日志路径下的_log.log文件，并规定了日志内容的格式、级别等
        self.log_name = f"{project_path()}/OutPuts/Logs/" + time.strftime("%Y_%m_%d") + "_log.log" # 日志的路径及命名格式
        file = logging.FileHandler(self.log_name, "a", "utf-8")
        formatter = logging.Formatter('[%(asctime)s] %(filename)s-> %(funcName)s line:%(lineno)d [%(levelname)s]%(''message)s')
        file.setFormatter(formatter)
        file.setLevel(logging.DEBUG)

        # 创建一个处理程序（handler），StreamHandler将日志发送到pycharm的下面，你运行代码的时候，这里可以显示你定义的日志
        console = logging.StreamHandler(stream=None)
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)

        # 你还可以创建一个handler，去输出到其他地方


        # 将2个处理器加入到logger中，不但向控制器输出、还向文件中输出你定义的日志。
        self.logger.addHandler(file)
        self.logger.addHandler(console)

    def log(self):
        return self.logger


if __name__ == '__main__':
    # xxx模块，打印xxx-server模块的日志
    log = FrameLog('xxx-server').log()
    try:
        print(2/0)
    except ZeroDivisionError:
        print('这里打印在控制台')
        # 下面的message输入到日志
        log.error('这是一个框架性的错误11111111')
        log.debug('这是业务代码里的错误1111111111')
        log.info('这是业务代码里info级别的错误11111111111')
        log.critical('这是系统性的错误1111111')

    # yyy模块，打印yyy - server模块的日志
    log = FrameLog('yyy-server').log()
    try:
        print(2/0)
    except ZeroDivisionError:
        print('这里打印在控制台')
        # 下面的message输入到日志
        log.error('这是一个框架性的错误22222')
        log.debug('这是业务代码里的错误22')
        log.info('这是业务代码里info级别的错误2222')
        log.critical('这是系统性的错误222')



