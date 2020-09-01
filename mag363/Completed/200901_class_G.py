# # -*- comding:utf-8   -*-
#
#
# # def add_name(cls, name= 'jerry'):
# #     cls.NAME = name
# #     return cls
#
# def add_name(name= 'jerry'):  #
#     def wrapper(cls):
#         cls.NAME = name
#         return cls
#     return wrapper
#
# @add_name('tom')
# class Person:   #Person =wrapper(Person)
#     AGE = 20
#
#     def __init__(self):
#         self.name = 'tom'
#     def method(self):
#         print(123)
#         print('abc123')
#         return 55
#
#     @classmethod
#     def class_method(self):
#         print(999)
#         return 000
#     @staticmethod
#     def static(self):
#         print(999)
#         return 111
#
# #装饰一个类，给类增加一个属性
#
# print(Person.__dict__)
# print(Person.__dict__['NAME'])
#
#
# print(Person().method())
#

# class Person:
#      def normal_method():
#         print('normal')
#         return 'normal_method'
#
#      def method(self):
#         print("{}'s method".format(self))
#         return 'method'
#
#      @classmethod
#      def class_method(cls): # cls是什么
#         print('class = {0.__name__} ({0})'.format(cls))
#         cls.HEIGHT = 170
#         return 'class_method'
#
#      @staticmethod
#      def static_methd():
#         print(Person.HEIGHT)
#         return 'static_methd'
#
#
# print('~~~~类访问')
# print(1, Person.normal_method()) # 可以吗
# print(2, Person.method(1)) # 可以吗
# print(3, Person.class_method()) # 可以吗
# print(4, Person.static_methd()) # 可以吗
# print(Person.__dict__)
#
# print('\n')
# print('~~~~实例访问')
# print('tom----')
# tom = Person()
# # print(1, tom.normal_method()) # 可以吗
# print(2, tom.method()) # 可以吗
# print(3, tom.class_method()) # 可以吗？
# print(4, tom.static_methd()) # 可以吗
# print(5, tom.__dict__)
#
# print('\n')
# print('jerry----')
# jerry = Person()
# # print(1, jerry.normal_method()) # 可以吗
# print(2, jerry.method()) # 可以吗
# print(3, jerry.class_method()) # 可以吗？
# print(4, jerry.static_methd()) # 可以吗
# print(5, jerry.__dict__)





class Person:
    @staticmethod  #静态方法，如果使用只能直接调用了
    def normal_method(): # 可以吗？
        print('normal')
        # print(Person.normal_method())
# 如何调用
Person.normal_method() # 可以吗？
Person().normal_method() # 可以吗？
print(Person.__dict__)

print('\n')

class Person:
     @classmethod   #可以操作类的属性，但是不能操作类的方法
     def class_method(cls): # cls是什么
         print('class = {0.__name__} ({0})'.format(cls))
         cls.HEIGHT = 170
Person.class_method()
print(Person.__dict__)



































