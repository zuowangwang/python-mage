#-*- comding:utf-8   -*-
# 136-150


def foo():
    print(1/0) #除零异常

def test1():
    try:
        foo()
        print('pass')
    except:   #https://www.runoob.com/python/python-exceptions.html
        print('error')

def test2():
    try:
        fh = open("testfile.txt", "r")
        #w打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
        #r以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
        fh.write("这是一个测试文件，用于测试异常!!")
    except IOError:#一般用于每个文件没有读写权限
        print ("Error: 没有找到文件或读取文件失败")
    else:
        print ("内容写入文件成功")
        fh.close()


class Zerror(Exception):#自定义异常，一般写到最后，自定义退出异常
    pass
def test3():
    try:
        raise  Zerror
    except Zerror :
        print('Zerror')


def test4():
    try:
        1/0
        # print(lst[1])
    except  ArithmeticError:
        print('ArithmeticError')
    except LookupError:
        print('LookupError')
    except Exception:#一般情况下，子类异常在上面，父类异常在下，因为子类异常是你需要关注的，异常一旦捕获所以不会再继续捕获了,如果没有捕获到那么直接崩溃了
        print('Exception')



class Werror(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message
def test5():
    try:
        # raise 1/0
        # print(lst[1])
        raise  Werror(100 , '我指定的的异常信息')
    except Werror as e:
        print('Zerror',e)
        print(e.code , e.message)

    except Exception as e:
        print('Exception',e)
        print(dir(e))
        #dir()函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
        print(e) #打印具体异常对象是什么

    print('捕获异常后，继续执行')



def test6():
    try:
        foo()
        print('pass')
        # return 3
    except ZeroDivisionError as e:   #打印具体异常对象是什么
        print(1, 'ZeroDivisionError',e)
        # return 4
    finally:
        #不管异常有没有捕获都会执行
        print("finally , 必须执行")
        # return 5
        #  就算有return也会执行，如果内部包含多个return，只会返回最后一个return


def test7():
    f = None
    try:
        f = open('test1.test')
        print(f)
    except FileNotFoundError as e:
        print('{} , {} , {}'.format(e.__class__,e.errno,e.strerror))
        raise#如果没有，就抛出最后一个异常
    finally:
        print('清理工作')
        # if f:
        #     f.close()
        try:
            f.close()
        except Exception as e:
            print('Exception' , e)
        # return 1
        # finally 里面一般不会写return,会压制异常


def test8():
    try:
        # 1/0
        print(1)
    except ArithmeticError as e:
        print('如果有异常返回error')
    else:
        print('如果没有异常执行这个')
    finally:
        print('总会执行')

# try:
#  <语句> #运行别的代码
# except <异常类>：
#  <语句> # 捕获某种类型的异常
# except <异常类> as <变量名>:
#  <语句> # 捕获某种类型的异常并获得对象
# else:
#  <语句> #如果没有异常发生
# finally:
#  <语句> #退出try时总会执行



def test9():#立即修改异常
    def parse_int(s):
        try:
            x = int(s)
        except:
            x = 0
        return x


#__slots__的使用
class A:
    X = 1

    __slots__ = 'y z a'.split()
    # __slots__ = tuple('y z a'.split())#只要是可迭代对象就可以，一般使用列表，节约内存用元组

    def __init__(self):
        self.y = 5
        self.z = 7

# print(A.__class__)
# a = A()
#
# # print(a.__dict__) #定义了__slots__之后就没有了
# print(a.X)
# print(a.y)
# # print(a.a)
# #使用需要构建在数百万以上对象，且内存容量较为紧张，实例的属性简单、固定且不用动态增加的场景。





import os  #导入
# print(dir())#检查当前模块有什么

# import os.path
# print(os.path)
# print(type(os.path))#打印这是一个什么，这个是一个模块
# print(dir(os))

# from time import  time as titi  #别名




# 1. 模块名就是文件名
# 2. 模块名必须符合标识符的要求，是非数字开头的字母数字和下划线的组合。test-module.py这样的文件名不
# 能作为模块名
# 3. 不要使用系统模块名来避免冲突，除非你明确知道这个模块名的用途
# 4. 通常模块名为全小写，下划线来分割#######

#使用 sys.path 查看搜索顺序
# import sys
# for p in sys.path:
#    print(p)
# 显示结果为，python模块的路径搜索顺序
# 当加载一个模块的时候，需要从这些搜索路径中从前到后依次查找，并不搜索这些目录的子目录。
# 搜索到模块就加载，搜索不到就抛异常
# 路径也可以为字典、zip文件、egg文件。
# .egg文件，由setuptools库创建的包，第三方库常用的格式。添加了元数据（版本号、依赖项等）信息的zip文件
# 路径顺序为
# 程序主目录，程序运行的主程序脚本所在的目录
# PYTHONPATH目录，环境变量PYTHONPATH设置的目录也是搜索模块的路径
# 标准库目录，Python自带的库模块所在目录
# sys.path可以被修改，增加新的目录


# print(sys.modules)  #所有加载的模块都会记录在sys.modules中，sys.modules是存储已经加载过的所有模块的字典


#__name__ == '__main__的使用方法
# class zuo():  #其他模块代码
#     def zuo1(self):
#         print(11111111)
#
# #这是一个运行模块
# if __name__ == '__main__':
#     print('in main ,主模块时候运行这里的代码','我的模块名字',__name__)
#     zuo().zuo1()
# else:
#     print('其他模块调用时候运行这里','我的模块名字',__name__)

#如果一个模块进行调用
# import ttest1
# ttest1


# 包目录中 __init__.py
# 是在包第一次导入的时候就会执行，内容可以为空，也可以是用于该包初始化工作的代码
# 或者执行每次需要导入其他模块的变量

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 相对导入
# 只能在包内使用，且只能用在from语句中
# 使用.点号，表示当前目录内 from .ttest1 import zuo
# ..表示上一级目录  from ..ttest1 import zuo
# 不要在顶层模块中使用相对导入


# import  ttest1
# print(ttest1.__dict__.keys())  #打印当前导入模块中，对象情况

# from  ttest1 import z as wz,_z as w_zs
# print(wz,w_zs)#打印别名变量内容
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ##路径问题
# print(os.path.dirname(__file__))  #打印当前路径，E:/python-mage/mag363
# print(__file__)#打印当前执行文件   #E:/python-mage/mag363/week_11_practise.py
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. 如果模块没有 __all__ ， from xyz import * 只导入非下划线开头的该模块的变量。如果是包，子模块也不
# 会导入，除非在 __all__ 中设置，或 __init__.py 中导入它们
# 2. 如果模块有 __all__ ， from xyz import * 只导入 __all__ 列表中指定的名称，哪怕这个名词是下划线开头
# 的，或者是子模块
# 3. from xyz import * 方式导入，使用简单，但是其副作用是导入大量不需要使用的变量，甚至有可能造成名
# 称的冲突。而 __all__ 可以控制被导入模块在这种导入方式下能够提供的变量名称，就是为了阻止from xyz
# import *导入过多的模块变量，从而避免冲突。因此，编写模块时，应该尽量加入 __all__


#all的使用，导入一个模块的时候，如果用*会导入非常多无用模块，而且不能导入_z等格式的模块
#但是用了all之后，会固定导入编写完成的模块，不会导入其他大量无用模块
# __all__ = ['z','_z']
# from ttest1 import *
# print(z)
# print(dir())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ##如何打包，以及安装
# from distutils.core import  setup
# from setuptools import setup #兼容上面的
#
# setup(name = 'Completed',  #包名字
#       version ='0.1.0',    #版本
#       description = 'Completed Utilities',  #打包什么工具
#       author = 'zuo' , #你的名字
#       author_email = 'zuo@qq.com',  #你的邮箱
#       url = 'http://www.baidu.com',  #网址-github
#       packages = ['mag363','mag363.Completed'], #需要打包的内容，精确到文件夹
#       )
#  python setup.py build  #build命令，编译
#  python setup.py sdist  #E:\python-mage\dist\Completed-0.1.0.tar.gz
#  在其他地方解压缩这个文件，里面有setup.py，
#  就可以使用 python setup.py install 安装了
#  也可以 $ pip install Completed-0.1.0.zip 直接使用pip安装这个压缩包
#  python setup.py bdist_rpm # 打包成rpm
#  pip list  #查看当前安装列表，然后安装，查看就可以了



# #插件化开发
# zuo.zuo1
# class zuo():
#     def zuo1(self):
#         print(11111111)
#
#
# # 主程序模块test.py
# import importlib
# def plugin_load(plugin_name:str, sep=":"):
#      m, _, c = plugin_name.partition(sep)
#      mod = importlib.import_module(m)
#      cls = getattr(mod, c)
#      return cls()
#
# if __name__ == '__main__':
#     # 装载插件
#     a = plugin_load('ttest1:zuo')  #现在可以动态加载模块类对象
#     a.zuo1()




#虚拟环境
# pip freeze > requirements.txt   导出当前环境库
# pip install -r requirements.txt  安装文件中所有库


#git

#git  config --global user.email '752491485@qq.com'
#git config --global use.name 'zuowangwang'

#初始化
#git init

#添加文件进行管理
#git add .
#git add  新文件.txt



#查看文件状态
#git status
#git status -s  查看新文件
#追踪的Tracked，已经加入版本库的文件
#未追踪的Untracked，未加入到版本库的未被管理的文件
#忽略的Ignored，git不再关注的文件

#提交版本，进行备注
#git commit -m "备注"


#已经跟踪的文件
#Git commit -a -m '新增修改1'


#git commit --amend -m '备注'

#git log

# 重置内容到上一次
# git reset
# git reset --hard
# git reset --hard   a75007d  #指定



# git remote add origin  https://github.com/zuowangwang/python-mage.git

#  git push origin master # 指定推送到的远程主机和分支
#  git push origin # 指定当前分支推送到的主机和对应分支
#  git push -u origin master # 指定远程默认主机和分支
#  git push



#git add.
#git commit -m "备注"
#git commit -a -m '新增修改1'
#git push origin zuowangwang

#git push -f origin zuowangwang  #强制提交