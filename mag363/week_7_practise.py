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





pathlib_z()






















