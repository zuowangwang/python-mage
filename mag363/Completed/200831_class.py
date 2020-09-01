# -*- comding:utf-8   -*-

class MyClass:
    """A example class"""
    x = 'abc' # 类属性

    def foo(self): # 类属性foo，也是方法
        return ('My Class')

    def __init__(self): #对实例初始化,其他实例每次调用都会运行
        print('init')

    def test1(self):
        print('实例调用init')

print(MyClass.x)  #类变量，上例中x是类MyClass的变量
print(MyClass.foo)  #类的属性，类定义中的变量和类中定义的方法都是类的属性
print(MyClass.__doc__) #x、foo都是类的属性， __doc__ 也是类的属性
print(MyClass.test1)

s = MyClass()  #类的实例化才会调用
s.test1() #调用类的方法



#如果实例化需要传参

class MyClass:
    """A example class"""
    a = 'abc'

    def __init__(self,x:int,y:int):  # 对实例初始化,其他实例每次调用都会运行
        print('init')
        print(x + y)
        self.x = x


    def test1(self):
        print('实例调用init')
        print(self.x)


s = MyClass(5,5)  #如果初始化需要传参，那么在实例化的时候带进去，对应x,y
s.test1() #调用类的方法

#类定义，首字母大写
# __name__ 对象名
# __class__ 对象的类型
# __dict__对象的属性的字典
# __qualname__类的限定名

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符1')
# print(s.__class__.__name__)
# print(s.__class__.test1.__name__)
# print(MyClass.__name__)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符2')
# print(s.__class__.__class__)
# print(s.__class__.test1.__class__)
# print(MyClass.__class__)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符3')
print(s.__class__.__dict__.items())
print(s.__class__.__dict__['a'])
print(s.__class__.__init__.__dict__.items())
print(s.__init__.__dict__.items())
print(s.__class__.test1.__dict__.items())
print(MyClass.__dict__.items())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符4')
# print(s.__class__.__qualname__)
# print(s.__class__.test1.__qualname__)
# print(MyClass.__qualname__)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符5')

# git status  //查看当前修改的文件
# git add . //上传到本地仓库
# git commit -m  '提交的说明'
# git push || git push -u //上传远程分支
# 有文件冲突 就来取
# git pull
#
#
# git reset --hard 1b48e0b   #回退版本


print(s.__dict__)
print(s.a)
#
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符6')

print('~~~~~~~~~~解释类属性的访问顺序')
class Person:
     age = 3
     height = 170
     def __init__(self, name, age=18):
         self.name = name
         self.age = age
tom = Person('Tom') # 实例化、初始化
jerry = Person('Jerry', 20)
Person.age = 30
print(Person.age, tom.age, jerry.age) # 输出什么结果
print(Person.__dict__)
print(tom.__dict__, jerry.__dict__)


print('~~~~~~~~~~')
print(Person.height, tom.height, jerry.height) # 输出什么结果
print(Person.__dict__)
print(tom.__dict__, jerry.__dict__)


print('~~~~~~~~~~')
jerry.height = 175
print(Person.height, tom.height, jerry.height) # 输出什么结果
print(Person.__dict__)
print(tom.__dict__, jerry.__dict__)

print('~~~~~~~~~~')
tom.height += 10
print(Person.height, tom.height, jerry.height) # 输出什么结果
print(Person.__dict__)
print(tom.__dict__, jerry.__dict__)

print('~~~~~~~~~~')
Person.height += 15
print(Person.height, tom.height, jerry.height) # 输出什么结果
print(Person.__dict__)
print(tom.__dict__, jerry.__dict__)

print('~~~~~~~~~~')
Person.weight = 70
print(Person.weight, tom.weight, jerry.weight) # 输出什么结果
print(Person.__dict__)
print(tom.__dict__, jerry.__dict__)


print('~~~~~~~~~~')
tom.name = 'zww'
print(tom.name) #可以给自己添加类属性，但是本身才有
# print(Person.name, jerry.name) # 输出什么结果，因为只是给类添加了，所以其本身是没有的
print(Person.__dict__)
print(tom.__dict__, jerry.__dict__)

print('~~~~~~~~~~')
print(tom.__dict__['height'])
print(tom.weight)  #可以，因为访问的类的不是自己的
print(tom.__dict__['weight']) # 可以吗  不可以，因为本身没有，类字典才有
#指的是实例使用 .点号 来访问属性，会先找自己的 __dict__ ，如果没有，然后通过属性 __class__ 找到自己的
# 类，再去类的 __dict__ 中找
# 注意，如果实例使用 __dict__[变量名] 访问变量，将不会按照上面的查找顺序找变量了，这是指明使用字典的key
# 查找，不是属性查找。
# 一般来说，类变量可使用全大写来命名。
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符7')



