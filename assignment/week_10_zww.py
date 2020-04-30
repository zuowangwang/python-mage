#-*- comding:utf-8   -*-
# P22第十周学习安排及作业内容：
# 请同学们至少完成腾讯课堂如下学习章节：
# 【一：章节学习】
# 第30节  Python面向对象进阶(一)	01-dir的作用
# 	02-实例化、hash和equal
# 	03-bool和可视化
# 	04-运算符重载
# 	05-容器化魔术方法
# 第31节  Python面向对象进阶(二)	01-习题单双向链表实现
# 	02-可调用对象
# 	03-上下文管理
# 第32节  Python面向对象进阶(三)	01-反射基本概念
# 	02-反射的魔术方法和实例属性搜索顺序
# 	03-描述器概念
# 	04-描述器应用
# 【二：本周作业】请同学们于下周天晚上10点前，将作业上传至GitHub；
# 三：简单用函数实现一下map，reduce，fileter等函数
# map:
#  def fn():
#       return x * x
#  ret =list(map(f, [1,2,3,4,5,6,7,8,9]))
#  str1 =list(map(str, [1,2,3,4,5,6,7,8,9]))
#
# reduce:
#  def fn(x,y):
#      return x + y
#  ret = reduce(fn, [1,3,5,7,9])
#
# dilter:
#  def fn(n):
#      return  n % 2 == 1
#  ret == list(filter(fn, [1,2,4,5,6,9,10,15]))
# 提示：map，reduce，filter一般都是接受两个参数（fn，Iterable）
# 要求：
#     1.实现的函数返回结果时，可以不为惰性
#     2.检测Iterable是否为可迭代对象，如果不可迭代，抛出异常"Iterable not is Iterable"


from collections import Iterable


"""
map简单实现
"""

def my_map(func, seq):
    if isinstance(seq, Iterable):
        for i in seq:
            yield func(i)
    else:
        raise Exception("Iterable not is Iterable")

def fn(x):
    return x * x

ret = my_map(fn, [1, 2, 3, 4, 5, 6])
print(list(ret))

"""
reduce简单实现
"""

def my_reduce(func, seq):
    if isinstance(seq, Iterable):
        for i,j in enumerate(seq):
            if i == 0:
                result = j
                continue
            result = func(j,result)
        return result
    else:
        raise Exception("Iterable not is Iterable")

def fn(x,y):
    return x+y

ret = my_reduce(fn, [1, 3, 5, 7, 9])
print(ret)


"""
filter简单实现
"""

def my_filter(func, seq):
    if isinstance(seq, Iterable):
        new_list = []
        for i in seq:
            if func(i):
                new_list.append(i)
        return new_list
    else:
        raise Exception("Iterable not is Iterable")

def fn(n):
    return n % 2 == 1

ret = my_filter(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15])
print(ret)





