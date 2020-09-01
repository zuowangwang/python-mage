# -*- comding:utf-8   -*-



class Person:
     def __init__(self, name, age=18):
         self.name = name
         self.__age = age
     def growup(self, i=1):
        if i > 0 and i < 150: # 控制逻辑
            self.__age += i  #私有属性

     def getage(self):
        print(self.name)
        return self.__age

tom = Person('tom')

print(tom.getage())
print(tom.__dict__)

tom.__age = 1000 #私有属性是不能更改的，这个相当于新增了一个属性
print(tom.getage())
print(tom.__dict__)

tom._Person__age =2000 #私有属性更改，修改了实际属性名
print(tom.getage())
print(tom.__dict__)

#属性中 _ 一个下划线叫保护属性， __两个下划线叫私有属性，建议不要更改
#方法同理

