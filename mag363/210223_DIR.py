# -*- comding:utf-8   -*-

#124


# class A:pass
#
# class B(A):pass
#
# class C(B):
#     def __init__ (self):
#         self.x = 100
#     def __dir__(self):
#         return {'a':200,'b':300}
# print(C.__dict__)
#
# print(dir(C))
# print('_'*30)
#
# c = C()
# print(dir(c), type(c))
# print('_'*30)
#
# print(dir()) #当前所有对象属性


#如果没有定义则收集所有实例，如果定义了则返回当前定义的内容


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# __init__  创建
# __del__  销毁



# class A:pass
#
# class B(A):pass
#
# class C(B):
#     # def __new__(cls, *args, **kwargs):  #拦截信息，进行修改，只有修改以后才会云init
#     #     print(cls)
#     #     print(*args)
#     #     print(**kwargs)
#     #     # return super().__new__(cls)
#     #     # return 1
#     #     return super().__new__(cls)
#
#     def __hash__(self):
#         return 1
#
#     def __eq__(self, other):
#         return True
#
#     def __init__(self, name):
#         self.name = name
#         print('~~~~~~~~~~~~~~~~~~~')
#
#     def __repr__(self):
#         return self.name
# #new
# # a = C('tom')
# # print(a.__dict__)
# # print(dir(a))
#
#
# a = C('tom')
# b = C('ccc')
# print(a.__dict__)
#
# print(hash(a))
# print(hash(b))
# print('-'*30)
# print({a,b})
# print((a,b))
# print([a,b])

#设计二维坐标类Point，使其成为可hash类型，并比较2个坐标的实例是否相等？
# from collections import Hashable
# class Point:
#      def __init__(self, x, y):
#          self.x = x
#          self.y = y
#      def __hash__(self):
#         return hash((self.x, self.y))
#      def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
# p1 = Point(4, 5)
# p2 = Point(4, 5)
# print(p1, p2)
# print(hash(p1))
# print(hash(p2))
# print(p1 is p2)
# print(p1 == p2) # True 使用__eq__
# print(hex(id(p1)), hex(id(p2)))
# print(set((p1, p2)))
# print(isinstance(p1, Hashable))


#布尔值内建函数bool()，或者对象放在逻辑表达式的位置，调用这个函数返回布尔值。
# 没有定义 __bool__ ()，就找 __len__ ()返回长度，非0为真。
# 如果 __len__ ()也没有定义，那么所有实例都返回真
# class A :pass
#
# if A:
#     print(1, 'True')
#
# if A():
#     print(2, 'True')
#
#
# print(bool(A), bool(A()))
# print(dir(A))
#
#
# print('~'*30)
#
# class B:
#     def __bool__(self):
#         return False
#
# if B:
#     print(1, 'True')
#
# if B():
#     print(2, 'True')
# else:
#     print(-2, 'False')
#
#
# print(bool(B), bool(B()))
# print(dir(B))
#


#内建函数repr()对一个对象获取字符串表达。
# 调用 __repr__ 方法返回字符串表达，如果 __repr__ 也没有定义，就直接返回object的定义
# 就是显示内存地址信息
#
#
#
# str()函数、format()函数、print()函数调用，需要返回对象的字符串表达。如果没有定义，就
# 去调用 __repr__ 方法返回字符串表达，如果 __repr__ 没有定义，就直接返回对象的内存地
# 址信息
#
#
#
#
# bytes()函数调用，返回一个对象的bytes表达，即返回bytes对象





class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'repr: {},{}'.format(self.name, self.age)

    def __str__(self):
        return 'str: {},{}'.format(self.name, self.age)

    def __bytes__(self):
        # return "{} is {}".format(self.name, self.age).encode()
        import json
        return json.dumps(self.__dict__).encode()



#三种方式默认调用str,A()，format函数，str(A())，[]使用__str__，
#如果使用reor(A()),才会调用repr函数
#
# print(A('tom'))  # print函数使用__str__
# print([A('tom')])  # []使用__str__，但其内部使用__repr__
# print([str(A('tom'))])  # []使用__str__，其中的元素使用str()函数也调用__str__
# print('str:a,1')  # 字符串直接输出没有引号
# s = '1'
# print(s)
# s1 = 'a'
# print(s1)
# print([s1], (s,))  # 字符串在基本数据类型内部输出有引号
# print({s, 'a'})
# print(bytes(A('tom')))
#




# @functools.total_ordering 装饰器
# __lt__ , __le__ , __eq__ , __gt__ , __ge__ 是比较大小必须实现的方法，但是全部写完太麻烦，使用
# @functools.total_ordering 装饰器就可以大大简化代码。
# 但是要求 __eq__ 必须实现，其它方法 __lt__ , __le__ , __gt__ , __ge__ 实现其一

# from functools import total_ordering
# @total_ordering
# class Person:
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
#      def __eq__(self, other):
#         return self.age == other.age
#      def __gt__(self, other):
#          return self.age > other.age
#
# tom = Person('tom', 20)
# jerry = Person('jerry', 16)
# print(tom > jerry)
# print(tom < jerry)
# print(tom >= jerry) #
# print(tom <= jerry)


#字典或其子类使用 __getitem__() 调用时，key不存在执行该方法
# class A(dict):
#      def __missing__(self, key):
#          print('Missing key : ', key)
#          return 0
#
# a = A()
# print(a['k'])


print(1)





























