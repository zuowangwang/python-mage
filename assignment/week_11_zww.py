#-*- comding:utf-8   -*-
# P22第十一周学习安排及作业内容：
# 请同学们至少完成腾讯课堂如下学习章节：
# 【一：章节学习】
# 第33节  Python异常处理	01-习题链表容器化和property描述器实现
# 	02-异常概念、产生和捕获
# 	03-异常的继承、子句、嵌套、总结
# 第34节  Python模块化	01-slots、反向方法、生成器交互
# 	02-import和from语句使用
# 	03-模块加载搜索和主模块用途
# 	04-包
# 	05-绝对导入、相对导入
# 第35节  Python包管理与Git版本管理	01-python包管理和打包分发
# 	02-插件化开发和接口
# 	03-Gogs安装
# 	04-Git由来和基本概念操作
# 	05-Git操作增删改检出重置比较
# 	06-Git的Push和Clone
# 	07-Git分支和工作流管理
# 【二：本周作业】请同学们于下周天晚上10点前，将作业上传至GitHub；
# 1. 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
# 2. 请设计一个decorator，它可作用于任何函数上，要求可以接受一个int作为参数，如果该函数的执行时间大于int传递的时间话，请打印改函数名字和执行时间
#


#2. 请设计一个decorator，它可作用于任何函数上，要求可以接受一个int作为参数，如果该函数的执行时间大于int传递的时间话，请打印改函数名字和执行时间

from functools import update_wrapper ,wraps
import datetime

def tolog(name,took):
    print('函数 ：{} took 所用时间: {}s'.format(name, took))
    # lambda name,duration:print('{} took{}s'.format(name,duration))
def log1ger(duration,func = tolog):
    def _logger(fn):
        @wraps(fn)   #  ==  wrapper(fn)(wrapper)  柯里化参数传入
        def wrapper(*args, **kwargs):
            """装饰器文本解释器"""
            # print('前面增强')
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            # print('后面增强')
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > duration:
                func(fn.__name__, delta)
                # print('so slow 大于2s')
            else:
                pass
                # print('so fast 小于2s')
            return ret
        return wrapper
    return _logger

import time
@log1ger(1,tolog)  #loglger(3)(add1)
def add1(x,y):
    """自有函数文本解释器"""
    time.sleep(2)
    return x + y

print(add1(99,155))
print(add1.__doc__)
print(add1.__name__)


# 1. 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import datetime, functools
def log1ger(fn):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('函数 ：{} took 所用时间: {}s'.format(fn.__name__, delta))
        return ret
    # update_wrapper(wrapper,fn)
    # return wrapper
    return functools.update_wrapper(wrapper, fn)
@log1ger
def add1(x, y):
    return x + y
print(add1(99, 155))




