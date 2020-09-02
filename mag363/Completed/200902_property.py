# -*- comding:utf-8   -*-

#属性装饰器

class Person:
    def __init__(self,name,age):
        self._name = name
        self.__age = age


    def age(self):
        return  self.__age

    #也就是说，方法变属性
    @property   #装饰这个属性  getter  必须现有get 然后才有ster deleter
    def tage(self):
        return self.__age

    @tage.setter   #装饰后，可以修改这个属性
    def tage(self, value):
         self.__age = value

    @tage.deleter  # 装饰后，可以删除这个属性
    def tage(self):
        pass

tom = Person('tom',18)
print(tom._name ,tom.age())
print(tom._name ,tom.age)  #r如果没有加装饰器，<bound method Person.age of <__main__.Person object at 0x000001F3099DEC88>>

print(tom._name ,tom.tage)

tom.tage = 22
print(tom.tage)



class Person:
    def __init__(self,name,age):
        self._name = name
        self.__age = age
        self.file = open('')

    def __del__(self): #实例消亡的时候才会被调用,作为一些清理工作，关闭连接等
        print('del')
        self.file.close() #关闭，等，清理工作
print('~~~~~~~')
tom.tage = 22
print(tom.tage)




