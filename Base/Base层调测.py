# coding=utf-8
from behave import given, when, then, step

@given("we have behave install")
def step_impl(context):
    pass

# 数字类型number奖状换成整数类型
# 以下函数功能是获取在苍井文件中设置的数字5，然后做出判断等操作
@when('we implement{number:d} tests')
def step_impl(context, number):
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0


git config --global user.name "tfjiao"
git config --global user.email "jiaotengfei1016@163com"






# import logging
#
# # set up logging to file - see previous section for more details
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt='%m-%d %H:%M',
#                     filename='D:\se_frame\Logs\2021_01_23_log.log',
#                     filemode='w')
# # define a Handler which writes INFO messages or higher to the sys.stderr
# #
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# # set a format which is simpler for console use
# #设置格式
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# # tell the handler to use this format
# #告诉handler使用这个格式
# console.setFormatter(formatter)
# # add the handler to the root logger
# #为root logger添加handler
# logging.getLogger('').addHandler(console)
#
# # Now, we can log to the root logger, or any other logger. First the root...
# #默认使用的是root logger
# logging.info('Jackdaws love my big sphinx of quartz.')
#
# # Now, define a couple of other loggers which might represent areas in your
# # application:
#
# logger1 = logging.getLogger('myapp.area1')
# logger2 = logging.getLogger('myapp.area2')
#
# logger1.debug('Quick zephyrs blow, vexing daft Jim.')
# logger1.info('How quickly daft jumping zebras vex.')
# logger2.warning('Jail zesty vixen who grabbed pay from quack.')
# logger2.error('The five boxing wizards jump quickly.')





#
# # 定义元素的基本操作
# # class Base:
# #
# #     def findele(self, *args):                      # 方法中的*args，是将多余的参数，打包成元组。
# #             return self.driver.find_element(*args) # 返回中的*args,是将打的包解开。
# #
# #     # 点击
# #     def click(self, *args):                        # 调用后是self.click(By.XPATH,"//*[text()='新闻']"),传入的参数打包成元组发送给findele最终拆包，才能用
# #         return self.findele(*args).click()
# #
# #     # 发送内容
# #     def sendkey(self, args, value):               # 调用send((By.XPATH,"//*[text()='新闻']"),'发送'),元组一个参数、value一个参数，findele的*args拆包。
# #         self.findele(*args).send_keys(value)
# #
# #     def implicitly_wait(self):
#
#
# # def myprint(name,*args, **kwargs):
# #     print(args)
# #     print(args) # 未拆包，除了第一个和关键字参数，其他输出是元组类型
# #     print(*args) # 进行拆包，不拆包怎么用，看上面的业务代码。
# #     print(kwargs)
# #     print(kwargs)# 未拆包，输出是字典类型
# #     print(*kwargs)# 进行拆包(**kwargs无法打印)
# #
# # # 1、*args：用于接受多余的未命名的参数（？），元组类型；
# # # 2、 ** kwargs：用于接受形参的命名参数（关键字参数），字典类型；
# # myprint(1, 2, 3, 4, 8, a= 5, c=7)
# #
# # '''
# # args
# # (1, 2, 3, 4, 8)
# # 1 2 3 4 8
# # kwargs
# # {'a': 5, 'c': 7}
# # a c
# # '''
# #
# #
# # '''
# # findele*(self,*args)
# #     return  return self.driver.find_element(*args)
# #
# #     def click(self, *args):
# #         return self.findele(*args).click()
# # '''
#
#
# # class Dog():
# #     '''一次模拟小狗的简单尝试'''
# #
# #     # '属性'
# #     def __init__(self,name,age):
# #         '''初始化dog的属性'''
# #         self.name = name
# #         self.age = age
# #         self.a = 0
# #
# #     # '方法'
# #     def sit(self):
# #         '''模拟小狗蹲下'''
# #         print(self.name.title() + "is now sitting.")
# #
# #     def roll_over(self):
# #         '''模拟小狗打滚'''
# #         print(self.name.title()+'rolled over!')
# #
# #     def man_bu(self):
# #         '''小狗漫步'''
# #         print('小狗向前走了' + str(self.a) + '步')
# #
# #     def update_man_bu(self,b):
# #         self.a += b
# #
# # class huangsegougou(Dog):
# #     '''这是黄色狗狗'''
# #
# #     # 这两行代码中的，super函数让黄色狗狗继承了父类dog的所有属性
# #     def __init__(self,name,age):
# #         super(huangsegougou, self).__init__(name,age)
# #         # 将下面的wangcai类的实例直接放在这,只要我调用黄色色狗狗这个类，我的旺财就会“吼一声”
# #         self.wangcai = Wangcai()
# #
# #     # 通过覆盖方法名，直接重写了父类的方法。
# #     def man_bu(self):
# #         print('黄色狗狗走了' + str(self.a) + '步')
# #
# # class Wangcai:
# #
# #     def __init__(self):
# #         print('旺财吼了一声，声如雷！')
# #
#
# # # （1）类化为对象，访问属性
# # a = Dog('habagou1',6).name
# # b = Dog('habagou2',6).age
# # print(a,b)
# # # （2）类化为对象，调用方法
# # a1 = Dog('habagou3',6).sit()
# # b1 = Dog('habagou3',6).roll_over()
# # print(a1)
#
# # 修改类的默认属性值,且属性值递增
# # a = Dog('habago4u',6)
# # print(a.man_bu())
# #
# # a.update_man_bu(5)
# # a.update_man_bu(5)
# # a.update_man_bu(5)
# # print(a.man_bu())
#
#
# 业务代码应用：
# ```python
#
#
# class Base:
#
#     def findele(self, *args):  # 方法中的*args，是将多余的参数，打包成元组。
#         return self.driver.find_element(*args)  # 返回中的*args,是将打的包解开。
#
#     # 点击
#     def click(self, *args):
#         return self.findele(*args).click()
#
#     # 调用后是self.click(By.XPATH,"//*[text()='新闻']"),传入的参数打包成元组发送给findele最终拆包，才能用
#     # 你问click里面为什么要打包，不打包的话你传入是多个参数呀
#
#     # 发送内容
#     def sendkey(self, args, value):
#         self.findele(*args).send_keys(value)
#     # 调用send((By.XPATH,"//*[text()='新闻']"),'发送'),元组一个参数、value一个参数，findele的*args拆包。
#
#
# ```
# 非业务验证：
#
# ```python
#
#
# def myprint(name, *args, **kwargs):
#     print(args)
#     print(args)  # 未拆包，除了第一个和关键字参数，其他输出是元组类型
#     print(*args)  # 进行拆包，不拆包怎么用，看上面的业务代码。
#     print(kwargs)
#     print(kwargs)  # 未拆包，输出是字典类型
#     print(*kwargs)  # 进行拆包(**kwargs无法打印)
#
#
# # 1、*args：用于接受多余的未命名的参数（？），元组类型；
# # 2、 ** kwargs：用于接受形参的命名参数（关键字参数），字典类型；
# myprint(1, 2, 3, 4, 8, a=5, c=7)
#
# '''
# args
# (1, 2, 3, 4, 8)
# 1 2 3 4 8
# kwargs
# {'a': 5, 'c': 7}
# a c
# '''
# ```
