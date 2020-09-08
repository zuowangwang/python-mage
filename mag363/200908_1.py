# -*- comding:utf-8   -*-

#类的基础


class Animal:
     def __init__(self, name):
        self._name = name
     def shout(self): # 一个通用的吃方法
        print('{} shouts'.format(self.__class__.__name__))
     @property
     def name(self):
        return self._name


class Cat(Animal):
    pass
class Dog(Animal):
    pass

a = Animal('monster')
a.shout()

cat = Cat('garfield')
cat.shout()
print(cat.name)

dog = Dog('ahuang')
dog.shout()
print(dog.name)

#继承
# class Cat(Animal) 这种形式就是从父类继承，括号中写上继承的类的列表。
# 继承可以让子类从父类获取特征（属性和方法）
# 父类
# Animal就是Cat的父类，也称为基类、超类。
# 子类
# Cat就是Animal的子类，也称为派生类

#从父类继承，自己没有去父类去找











