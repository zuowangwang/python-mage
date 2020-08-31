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
print(s.__class__.__name__)
print(s.__class__.test1.__name__)
print(MyClass.__name__)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符2')
print(s.__class__.__class__)
print(s.__class__.test1.__class__)
print(MyClass.__class__)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符3')
print(s.__class__.__dict__)
print(s.__class__.test1.__dict__)
print(MyClass.__dict__)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符4')
print(s.__class__.__qualname__)
print(s.__class__.test1.__qualname__)
print(MyClass.__qualname__)
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



print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符6')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符7')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符8')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符9')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符10')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符11')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符12')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符13')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符14')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符15')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符16')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符17')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符18')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~分隔符19')


