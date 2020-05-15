#-*- comding:utf-8   -*-
#80开始  95结束


#文件操作
def write1():
    #a文件存在,只写打开,追加内容文件不存在，则创建后,只写打开,追加内容
    #r是只读, wxa都是只写。wxa都可以产生新文件 , w不管文件存在与否,都会生成全新内容的文件;
    # a不管文件是否存在,都能在打开的文件尾部追加; x必须要求文件事先不存在,自己造一个新文件

    path1 = r'E:\python-mage\test.txt'

    f = open(path1)  #默认打开模式r,只读不能写
    print(f)
    print(f.read())  #读取文件
    f.close()  #关闭

    f = open(path1,'w')#打开模式写模式w--覆盖,生成新的文件
    f.write('abc')
    f.close()  #关闭文件，关闭后不允许操作

    f = open(path1,'a')#打开模式a,追加写模式，没有就创建，有就创建，一般写日志
    f.write('123abc')
    f.close()  #关闭文件，关闭后不允许操作

    f = open(path1)
    print(f.read())  #读取文件
    f.close()  #关闭

#创建小文件到目录
def te_1():
    def mkdir(path):
        import os
        path = path.strip()
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print(path + ' pass')
            return True
        else:
            print(path + ' False')
            return False


    for i in range(1000,10000):
    # F:\Downloads\文件夹
        mkpath = "F:\Downloads\文件夹\%s" % i
        print(mkpath)
        mkdir(mkpath)
        file = open(mkpath + '\\%s.txt' % i, 'w')
        file.write('hello you \n  test 10000 file')


#计算多个组合排列，然后写入文件
def writezuhe():

    a = [
        "任意的",
        "自动垂直",
        "在用户连接点上使用定位约束",
        "使用照片定位元数据进行调整",
        "使用照片定位元数据进行严格注册",
        "使用控制点进行平差",
        "使用控制点进行严格配准",
        "使用QR码调查"
    ]

    b = [
        "Notiling",
        "Regularplanargrid",
        "Regularvolumetricgrid",
        "Adaptive"
    ]

    c = [
        "24"
    ]

    d = [
        "ContexCapture3MX",
        "BentleyScalableMesh(3SM)",
        "Smart3DCantireS3C"
    ]

    e = [
        "50%组合.",
        "70%组合.",
        "90%组合.",
        "100%组合."
    ]

    from functools import reduce
    fn = lambda x, code=',': reduce(lambda x, y: [str(i) + code + str(j) for i in x for j in y], x)
    # 直接调用fn(lists, code)
    x = 1
    v = fn([a, b, c, d, e], code="+")
    path1 = r'E:\python-mage\test.txt'
    f = open(path1, 'a')  # 打开模式a,追加写模式，没有就创建，有就创建，一般写日志
    for i in v:
        f.write(i + "\n")
        x += 1
    f.write(str(x))
    f.close()


def copy_z():  #实现一个copy函数
    filename1 = r'E:\python-mage\test.txt'
    filename2 = r'E:\python-mage\test1.txt'

    def copy(src, dest):
     with open(src) as f1:
        with open(dest, 'w') as f2:
            f2.write(f1.read())

    copy(filename1, filename2)


#单词统计
def word_z():
    from collections import defaultdict
    filename = r'E:\python-mage\test.txt'
    # d = {}
    d = defaultdict(lambda :0)
    with open(filename,encoding='utf8') as f:
        for line in f:
            print(line)
            words = line.split()
            for word in map(str.lower, words):
                # d[word] = d.get(word, 0) + 1
                d[word] += 1
    print(sorted(d.items(), key=lambda item: item[1], reverse=True))




#内存中临时使用，不写入磁盘
def StringIO_z():
    from io import StringIO
    from io import BytesIO
    from sys import stdout, stderr, stdin
    with StringIO() as f:
        f.write('aaa')
        f.seek(0)
        print(f.read())
        print(f.closed)

    print(f.closed)



def os_z():
    from os import path
    # linux ，路径
    p = path.join('/E','python-mage','mag363')  #拼接linux路径
    s = path.join('E:/','python-mage','mag363') #拼接windows路径
    c = r'E:\python-mage\mag363\test.txt'
    # print(p,s)
    # print(path.exists(p))  #判断有没有这个路径,False因为这个是linux路径
    # print(path.exists(s))  #True windows路径格式正确
    #
    #
    # print(path.split(s))   #('E:/python-mage', 'mag363')切一刀
    #
    #
    # print(path.abspath('a'))  #E:\python-mage\mag363\a
    # print(path.abspath('.'))  #当前目录的绝对路径
    # print(path.abspath('..')) #上级目录的绝对路径

    # print(path.dirname(c)) #取目录是什么，E:\python-mage\mag363
    # print(path.basename(c)) #取最后文件是什么，test.txt
    # print(path.splitdrive(c)) #切除驱动器，windows,('E:', '\\python-mage\\mag363\\test.txt')

    # p1 = path.abspath(__file__) #获取自己的绝对路径，然后层层上找，所有路径
    # print(p1, path.basename(p1))
    # while p1 != path.dirname(p1):
    #     p1 = path.dirname(p1)
    #     print(p1, path.basename(p1))


def pathlib_z():
    from pathlib import Path
    p = Path()
    p = Path('/etc','asd','vvvv')
    # print(p) #\etc\asd\vvvv  linux路径
    # print(p.absolute()) #E:\etc\asd\vvvv windows路径


    # print(p / 'nn') #\etc\asd\vvvv\nn
    # print(p.absolute() / 'cc') #E:\etc\asd\vvvv\cc
    # print('pp' / p)  #不行，变成了字符串除法

    # p1 =  p / 'nnc'
    # print(p / p1)  #两个路径可以组合，去重组合


    # print(p.parts) #拆解路径#('\\', 'etc', 'asd', 'vvvv')


    # print(p.joinpath('x','c')) #当前路径上增加路径
    #
    # print(p.parent) #返回父路径
    #
    # print(p.parents) #返回一个可迭代对象，获得所有迭代父路径
    # for i in p.parents:
    #     print(i)

    # p2 = p / 'ccccc.tar.gz'
    # print(p2.name)  #获取文件名，最后一个
    # print(p2.stem)  #去除扩展名
    # print(p2.suffix) #获取后缀
    # print(p2.suffixes) #获取所有后缀名
    #
    #
    # print(p2.with_name('asad')) #替换最后一个名称
    # print(p2.with_suffix('.py')) #替换文件后缀

    # print(p.cwd())#当前文件路径
    # print(p.home())#当前用户家目录

    ## Path('E:/asdasd/asdasd/asdas').rmdir()#删除空目录
    ## Path('E:/asdasd/asdasd/asdas').touch()#创建文件
    ## Path('E:/asdasd/asdasd/asdas').mkdir()#创建目录  #默认不创建父目录
    #mkdir(parents = True) #创建父目录，默认创建一层父目录
    #mkdir(exist_ok=True) #如果存在不用提醒，默认提示存在的目录 3.5版本才有


    c = Path()
    # for i in c.iterdir(): #迭代当前目录中所有内容
    #     print(i)


    # for i in p.parents: #迭代当前所有目录
    #     print(i)

    # print(p.parents[len(p.parents) - 1]) #找到顶层父路径

    # for x in p.parents[len(p.parents) - 1].iterdir(): #递归找到顶层目录中所有文件
    #     # print(x, end='\t')
    #     # print(x)
    #     if x.is_dir():
    #         print(x,'这是一个文件夹')
    #         pass
    #     elif x.is_file():
    #         print(x,'这个是一个文件')
    #         pass



    #递归查找文件
    p = Path().absolute() #当前路径
    #
    # # print((p.parents[len(p.parents) - 1])) #顶层路径windows
    # # p = p.parents[len(p.parents) - 1]
    #
    # print(p)
    #
    # # for i in list(p.glob('*.py')): #当前目录打印所有Py结尾的文件
    # #     print(i)
    # #week* 或者以这个开通的
    # # for i in list(p.glob('**/*.py')): #递归当前往下所有目录Py结尾的文件
    # #     print(i)
    #
    # for i in list(p.rglob('*.py')): #所有目录打印所有Py结尾的文件
    #     print(i)

    # print(p) #匹配路径
    # print(p.match('week_10_practise.py'))
    # print(p.match('mag363'))
    # print(p.match('*/mag363'))
    # print(p.match('python-mage\mag363'))
    # print(p.match('python-mage\*'))



    p = Path().absolute()  # 当前路径
    p = Path('ttest1.py').absolute()
    # print(p.stat()) #链接本身的文件信息
    # # os.stat_result(st_mode=33206,
    # # st_ino=562949953577999, st_dev=3637338224,
    # # st_nlink=1, st_uid=0, st_gid=0, st_size=413,
    # # st_atime=1588235735, st_mtime=1588235735, st_ctime=1588235735)
    # print(hex(33206))
    # print(bin(33206))
    # print(p.lstat())

    # l = Path('E:/python-mage/test.txt') #临时编写插入一下
    # l.open()
    # l.write_text('cccc')
    # print(l.read_text())
    # l.write_bytes(b'xyztab')
    # print(l.read_bytes())

    # with l.open() as f:
    #     print(f.read(3))


def sys_os():
    import sys,os
    print(sys.platform)  #查看操作系统
    print(os.name)     #windows是nt , linux是posix，查看当前系统是什么系统
    print(os.listdir()) #查看当前目录有什么文件
    # os.chmod('test',0o777) #注意用的时候权限问题
    # os.chown(path,uid,gid) #修改文件的属主，组，但是需要足够的权限


def shutil_z():
    import shutil,os
    path1 = r'E:\python-mage\test.txt'
    path2 = r'E:\python-mage\test1.txt'
    # shutil.copy(path1,path2)  #拷贝A内容到B里面,拷贝文件和权限都进行copy
    # shutil.rmtree('目标目录')#可以递归删除目录下的目录及文件。
    # shutil.move('源文件','指定路径')#递归移动一个文件。
    # shutil.copytree('源目录必须存在','目标目录必须不存在')#可以递归copy多个目录到指定目录下。
    # print(os.stat(path1)) #查看文件状态，权限相关
    # shutil.copyfile(path1, 'test3.txt')#复制成一个新文件












