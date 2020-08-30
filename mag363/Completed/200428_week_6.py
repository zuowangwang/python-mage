#-*- comding:utf-8   -*-
#71开始79结束

#高阶函数1
def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc

#高阶函数2
def k16():
    def inc(base,step=1):
        base += step
        return base
    def counter(base):
        return inc
    fn1 = counter(5)
    fn2 = counter(5)
    #fn1 == fn2 #false
    #fn1 is fn2 #false

#创建文件夹函数
def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


    # # 定义要创建的目录
    # mkpath = "d:\\qttc\\web\\"
    # # 调用函数
    # mkdir(mkpath)

    # for i in range(2): #创建并在其中创建一个文件夹
    #     mkpath = "E:\\%s"%i
    #     mkdir(mkpath)
    #     file = open(mkpath+'\\%s.txt'%i, 'w')
    #     file.write('你好，\n  测试1万文件使用')

#创建1W文件并写入小文件,创建文件
def python2_mkdir():
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

    for i in range(1):
        mkpath = "E:\\%s" % i
        mkdir(mkpath)
        file = open(mkpath + '\\%s.txt' % i, 'w')
        file.write('hello you \n  test 10000 file')

##########################################
def compare(a,b):
    return a>b

# def  sort(iterable, reverse=False,key= lambda a,b: a>):
def  sort(iterable, reverse=False,key=compare):
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):
            # print(i,y,'注释')
            flag = key(x,y) if reverse else not key(x,y)
            if flag:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    print(sort([5, 2, 6, 7]))
    return newlist

def  sort1(iterable, reverse=False,key=str.lower):
    newlist = []
    for x in iterable:
        for i,y in enumerate(newlist):
            # print(i,y,'注释')
            flag = key(x) > key(y) if  reverse else key(x) < key(y)
            if flag:
                newlist.insert(i,x)
                break
        else:
            newlist.append(x)
    print(sort1(['a', 'A', 'b']))
    return newlist


#迭代器，去掉不需要的值，然后生成迭代器,过滤函数
def filter_map_sorted():
    print(sorted([5,6,3,8,9],key = str))

    for x in filter(lambda  x: x % 2 ==0 , range(10)):
        print(x)  #0 2 4 6 8


    for x in filter(lambda  x: x - 2 == 2, range(10)):
        print(x)   #4


    for x in map(lambda  x: x+1, range(5)): #迭代增加函数，迭代器
        print(x)

    print({x for x in map(lambda  x: x+1, range(5))})#{1, 2, 3, 4, 5}
    print(set(map(lambda  x: x+1, range(5))))#{1, 2, 3, 4, 5}
    print(dict(map(lambda x: (x%5,x), range(500))))#{0: 495, 1: 496, 2: 497, 3: 498, 4: 499}

#把每个进程，统计，然后打印出来，tv_w32.exe:1
def windowsjincheng():
    import os
    file = os.popen('tasklist|sort')
    list = []
    c = 0
    for x in file.readlines():
        s = x.split(' ')[0]
        c = c + 1
        if c > 2:
            list.append(s)
    result = {}
    for i in set(list):
        result[i] = list.count(i)
    for key,value in result.items():
        print('{key}:{value}'.format(key=key, value=value))  #tv_w32.exe:1

#高级函数柯里化
def kelihua():
    def add(x,y):
        return x + y

    print(add(4,5))
    def add(x):
        def fn(y):
            return x + y
        return fn

    print(add(4)(5))  #柯里化第一个必须要是函数，第一个要调用第二个

#装饰器，不影响原本函数的原有功能的情况下，进行可移植性，让需要增加一些功能的函数，但是不影响起原有作用

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def b(m, n, *args, x, y, **kwargs):
    pass

# def logger(fn, x, y):
#     print('call function : {} x={}, y={}'.format(fn.__name__, x, y))
#     ret = fn(x, y)
#     return  ret
# print('result = {}'.format(logger(add, 4,5)))
# print('result = {}'.format(logger(sub, 4,5)))

# def logger(fn, *args, **kwargs):
#     print('call function : {} x={}, y={}'.format(fn.__name__, *args))
#     ret = fn(*args, **kwargs)
#     return  ret
# print('result = {}'.format(logger(add, 4,5)))
# print('result = {}'.format(logger(sub, 4,5)))
# print('result = {}'.format(logger(b, 4,5,6,7,x=10,y=11)))
def copy_properties(src):
    def _copy(dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest
    return _copy

#现在是两个函数的模块name  doc 要改，如果有几十个怎么改
from functools import update_wrapper ,wraps

#柯里化
def logger(fn):
    """装饰器文本字符串，解释fn ==  变量喊出"""
    # @copy_properties
    # #如果这样 inner = copy_properties(inner)  但是我们想要的是 inner = copy_properties(fn)(inner)
    @copy_properties(fn)
    #如果这样，inner = _copy(inner)  ,所以要返回dest  要加上return dest，这样重新停用返回
    #
    def inner(*args, **kwargs):
        print('call function : {} x={}, y={}'.format(fn.__name__, *args))
        ret = fn(*args, **kwargs)
        return  ret
    # copy_properties(fn)(inner)#调用的方式
    # inner.__name__ = fn.__name__
    # inner.__doc__ = fn.__doc__  #强转换，改变了自己的函数解释，显示了被调用的函数
    return inner
# print('result = {}'.format(logger(add)(4,5)))
# print('result = {}'.format(logger(b)(4,5,6,7,x=10,y=11)))

# add = logger(add)#为什么能够执行成功，因为logger里面的fn记录着之前的add变量
# ret = add(4,5)
# print(ret)

@logger  #装饰器，等价为add = logger(add) 无参装饰器
def add(x,y):
    """函数自己的解释文本，x=数字 y=数字"""
    return x + y
# print(add(4,5))
# call function : add x=4, y=5
# 9

#编写一个能够检测函数运行时长的函数
def k180():
    import datetime,functools
    def log1ger(fn):
        def wrapper(*args, **kwargs):
            # print('前面增强')
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            # print('后面增强')
            delta = (datetime.datetime.now() - start).total_seconds()
            print('函数 ：{} took 所用时间: {}s'.format(fn.__name__,delta))
            if delta > 5:
                print('so slow')
            else:
                print('so fast')
            return ret
        # update_wrapper(wrapper,fn)
        # return wrapper
        return functools.update_wrapper(wrapper,fn)

    import time
    @log1ger
    def add1(x,y):
        time.sleep(6)
        return x + y

    print(add1(99,155))



#文档字符串
def k228():
    print(add(4,5))
    print(add.__name__)
    print(add.__doc__)
#要求放在函数名称下面的第一行，"""三引号，如果有装饰器，会显示装饰器定义转换的内容，
 # 1.如何改变，在装饰器函数内，加上  对应的inner.__neme =  fn.__name__
 # 2.用函数调用copy_properties(fn)(inner)#调用的方式
 # 3.用装饰器@copy_properties(fn)
 # 4.用自有函数 from functools import update_wrapper ,wraps   1)update_wrapper(wrapper,fn)  替换函数   2）装饰器wraps

pass

#2. 请设计一个decorator，它可作用于任何函数上，要求可以接受一个int作为参数，如果该函数的执行时间大于int传递的时间话，请打印改函数名字和执行时间
def k240():
    from functools import update_wrapper ,wraps
    import datetime

    def tolog(name,took):
        print('函数 ：{} took 所用时间: {}s'.format(name, took))
        # lambda name,duration:print('{} took{}s'.format(name,duration))
    def log1ger(duration,func = tolog):
        def _logger(fn):
            @wraps(fn)   #  ==  wrapper(fn)(wrapper)  柯里化参数传入
            def wrapper(*args, **kwargs):
                """装饰器文本解释器"""
                # print('前面增强')
                start = datetime.datetime.now()
                ret = fn(*args, **kwargs)
                # print('后面增强')
                delta = (datetime.datetime.now() - start).total_seconds()
                if delta > duration:
                    func(fn.__name__, delta)
                    # print('so slow 大于2s')
                else:
                    pass
                    # print('so fast 小于2s')
                return ret
            return wrapper
        return _logger

    import time
    @log1ger(1,tolog)  #loglger(3)(add1)
    def add1(x,y):
        """自有函数文本解释器"""
        time.sleep(2)
        return x + y

    print(add1(99,155))
    print(add1.__doc__)
    print(add1.__name__)


# 1. 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def k283():
    import datetime, functools
    def log1ger(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print('函数 ：{} took 所用时间: {}s'.format(fn.__name__, delta))
            return ret
        # update_wrapper(wrapper,fn)
        # return wrapper
        return functools.update_wrapper(wrapper, fn)
    @log1ger
    def add1(x, y):
        '''自己函数解释'''
        return x + y
    print(add1(99, 155))
    print(add1.__name__)
    print(add1.__doc__)


# 给定一个包含多个元素的list，让你查找其中出现次数最多的元素，你会怎么做？在下图中，我们介绍了两种方法，其中第一种是利用max()函数的key参数，第二种则是使用Counter。
def k332():
    a=[1,2,3,4,4,3,1,1,1,2,3]
    print(max(set(a),key=a.count))
    from collections import Counter
    cnt = Counter(a)
    print(cnt.most_common(1))

#正则匹配指定一个字符串，取其中的一个或者任意字符
def k341():
    import re
    s = "师资力量学校现有教职工近4000余人，其中专任教师1800余人，教授、副教授1100余人，中国科学院院士3名，中国工程院院士3名，" \
        "双聘两院院士2名，加拿大工程院院士1名，发展中国家科学院院士1名，“千人计划”53人，“万人计划”学者13人、“长江学者”eee15人，" \
        "国家杰出青年基金获得者21人，国务院学位委员会学科评议组成员6人，入选国家百千万人才工程（“百千万人才工程”一二层次人选、" \
        "新世纪百千万人才工程国家级人选）23人、国家创新人才推进计划中青年创新领军人才2人，教育部新世纪优秀人才支持计划入选者134人，" \
        "湖南省“百人计划”学者64人，湖南省“芙蓉学者奖励计划”特聘教授、讲座教授17人，享受政府特殊津贴专家201人，国家教学名师4人，" \
        "国家自然科学基金创新研究群体3个，教育部“长江学者与创新团队发展计划”创新团队8个，湖南省自然科学基金创新研究群体11个" \
        "。（数据截止日期：2017年01月） [31] "  # 由于字符串过长，在编译器中会要求换行，字符“\”为换行后自动添加的，不影响字符串本身

    n = re.findall(r"长江学者(.+?)人", s)  # 正则表达式匹配长江学者人数  提取“长江学者”和其后的“人”之间的字符，返回一个列表
    print(n)
    num = re.findall('\d+', str(n))  # 正则表达式提取数字，返回一个列表
    print(num)
    num = '长江学者:' + num[0] + '人'  # 重新构建一个字符串
    print(num)

#类型注解,注解不强制，提示信息
def k359():
    def add(x:int,y:int) -> int:  #参数的注解类型，后面的注解是指定返回类型，如果不对会有其他提示
        """

        :param x:
        :param y:
        :return:
        """
        print(x,y)
        return x + y
    add(4,5)
    add('asd','asdas')
    print(add.__annotations__) #打印对应参数的注解

    def add(x:list = [1]) ->list:  #函数注解可以设定，下面的直接引用方式，直接作为一个列表参数作为使用
        """

        :param x:
        :return:
        """
        a = x.append(5)
        return a

    a:int = 5
    print(a)
    #3.6python 可以使用变量注解 ，这样可以在运行之前发现更多的错误

    import inspect
    print(inspect.isgenerator(add))

    #获取签名
    sig = inspect.signature(add)
    print(sig)  #  (x:list)  函数的声明及定义

    params = sig.parameters  #打印函数里面的参数的声明
    print(params)
    print('ok')

    for i,(k,param) in enumerate(params.items()):
    #Parameter 内建函数，可以通过这个指定，然后查看这个函数的各种注解
    # from inspect  import Parameter
        a = param
        print(a)
        print(type(a))
        # a:Parameter = 1
        print(a.name ,'|分隔|' ,a.default ,'|分隔|', a.annotation,'|分隔|', a.kind)


#signature(callable) ,获取签名(函数签名包含了一个函数的信息，包括函数名、它的参数类型、它所在的类和名称空间及其他信息)

def k408():
   import  inspect
   def  add(x:int ,y :int,*args ,**kwargs)->int:
       return x + y
   sig = inspect.signature(add)
   print(sig, type(sig))  # 函数签名
   print('params: ',sig.parameters) # OrderedDict
   print('return: ',sig.return_annotation)
   print(sig.parameters['y'],type(sig.parameters['y']))
   print(sig.parameters['x'].annotation)
   print(sig.parameters['args'])
   print(sig.parameters['args'].annotation)
   print(sig.parameters['kwargs'])
   print(sig.parameters['kwargs'].annotation)

   print(inspect.isfunction(add)) #是否是函数
   print(inspect.ismethod(add)) #是否是类的方法
   print(inspect.isgenerator(add)) #是否是生成器对象
   print(inspect.isgeneratorfunction(add)) #是否是生成器函数
   print(inspect.isclass(add)) #是否是类
   print(inspect.ismodule(inspect)) #是否是模块
   print(inspect.isbuiltin(print)) #是否是内建对象
   #还有很多is函数，需要的时候查阅inspect模块帮助



def k434():
    import  inspect
    import inspect
    def add(x, y: int = 7, *args, z, t=10, **kwargs) -> int:
        return(x + y)

    sig = inspect.signature(add)
    print(sig)
    print('params:',sig.parameters)  # 有序字典
    print('return:',sig.return_annotation)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for i, item in enumerate(sig.parameters.items()):
        name, param = item
    print(i + 1,name ,param.annotation, param.kind, param.default)
    print(param.default is param.empty, end='\n\n')


#请检查用户输入是否附和参数注解的要求？  装饰器
import  inspect
from inspect import Parameter
from functools import update_wrapper,wraps
def k457():
    def check(fn):
        @wraps(fn) #复制全部属性和函数：
        def wrappor(*args, **kwargs):
            sig = inspect.signature(fn)#拿到签名
            # print(sig)
            params = sig.parameters#有序字典
            # print(params) #所有参数的注解

            values = list(params.values())
            # print(values)#[<Parameter "x:int">, <Parameter "y:int=6">]
            flag = True
            for i,x in enumerate(args):
                param:Parameter = values[i]
                # print(param.annotation) #打印函数的注解，如果没有注解则为inspect._empty，有则为对应的类型int
                # print(inspect._empty)#函数注解没有为空的字段inspect._empty
                # print(param,i,x)#显示第一个参数注解，enumerate，把参数变为键值对，分别取出，第0位，值为4
                if param.annotation  !=   inspect._empty and not isinstance(x,param.annotation):
                    # 判断为不为空，不为空则判断类型是否相同，如果相同则打印
                    print(x, 'not')
                    flag = False
                    break
                else:
                    print(x, 'ok')
            for k,v in kwargs.items():
                param: Parameter = params[k]
                if param.annotation  !=   inspect._empty and not isinstance(v,param.annotation):
                    print(v, 'not!')
                    flag = False
                    break
                else:
                    print(v, 'ok!')
            if not flag:
                raise TypeError('这个位置错误')
            ret = fn(*args, **kwargs)
            return ret
        return wrappor
    @check
    def add(x:int, y:int=6 ) ->int:
        '''测试各种函数，注解'''
        return x + y
    add(  4 ,y = 5) #运行
    print(add.__name__)  #函数的名字
    print(add.__doc__)   #函数的注释，解释


from functools import update_wrapper,wraps,reduce
#累加reduce 函数
def k505():
    print(reduce(lambda value,x: value + x,range(5),10))  #累加，前面加后面的累加 20
    print(reduce(lambda value,x: value + x,[2],3)) #列表，相加，累加
    print(reduce(lambda value,x: value + x,range(1,5)))  #range(1,5) = 1,2,3,4  累加结果10


#偏函数partial方法，偏函数,把函数部分的参数固定下来,相当于为部分的参数添加了一个固定的默认值, 形成一个新的函数并返回从partial生成的新函数,是对原函数的封装
from functools import partial
def k513():
    def add(x,y,z=6):
        return x + y + z

    newadd = partial(add, z=4, y=1) #重新复制这个函数，然后传入部分参数，作为默认参数，后续调用
    print(inspect.signature(newadd))
    print(newadd(6))#举例，本来需要3个参数，没有默认值，然后传入默认值两个，然后这样只用传入一个参数
    print(newadd(6,y=6))#如果有默认值，则需要制定传参改变。没有则使用默认值
    newadd = partial(add, z=2, y=2)  #可以重复覆盖默认值
    print(inspect.signature(newadd))

#验证码，激活码
def ckod():
    import string,random

    class ITer_:
        def __init__(self):
            self.chars = string.ascii_letters + string.digits

        def __iter__(self):
            for _ in range(200):
                codes =[]
                codes.append("".join(random.choices(self.chars, k=5)))
                random.shuffle(codes)
                yield "-".join(codes)


    for x in ITer_():
        print(x)

#验证码，激活码
def ckod1():
    import random
    import re
    '''
    格式：xxxxx-xxxxx-xxxxx-xxxxx
    '''

    def get_code1():
        chars = [str(n) for n in range(11)] + [chr(c) for c in range(65,91)]
        ret = list()
        for _ in range(4):
            ret.append(''.join(random.choices(chars, k=5)))
        yield '-'.join(ret)

    def get_code2():
        chars = [str(n) for n in range(11)] + [chr(c) for c in range(65,91)]
        random.shuffle(chars)
        chars = ''.join(chars)
        regex = re.compile(r'.{5}', re.S)
        ret = regex.findall(chars)
        yield '-'.join(ret[:4])

    for _ in range(20):
        print(next(get_code2()))

#缓存函数
def cache():
    from functools import lru_cache
    import time
    #什么叫缓存，就是说第一次调用的时候需要等待3秒，第二次调用的时候，因为在缓存中，不需要在启动这个方法，所以可以直接得到结果
    @lru_cache()
    def add(x=3):
        time.sleep(3)
        # print(x)
        return x

    print(add(4))
    print(add(5))  #第一次运行的时候没有缓存，所以需要等待3秒
    print(add(4))
    print(add(5))  #第二次运行的时候有缓存，所以可以直接从缓存中读取数据，直接得到结果

#表格操作
def xlrd_cz():
    import xlrd
    data  = xlrd.open_workbook('F:/Downloads/quxiantu1.xls')
    # print(data.sheet_names())
    teb1 = data.sheet_by_name('test')
    # print(teb1.ncols) #列 查询有几列
    # print(teb1.nrows) #行 查询有几行
    # print(teb1.row_values(0))  #返回由该行中所有单元格的数据组成的列表
    # print(teb1.row_values(0)[1])
    fig = 0
    for s in range(teb1.nrows): #根据表有多少行，然后读取多少遍
        print(fig)
        fig += 1
        for i in range(teb1.ncols):#根据表有多少列，然后循环取出里面所有列，
            print(teb1.row_values(s)[i],end=',  ')
        print()
    # print(teb1.row_len(2) )#返回该列的有效单元格长度


#把渲染任务的所有帧运行时间打印出来，存进表中，制作曲线图
def tasktimeopen():
    import xlrd,requests
    from xlutils.copy import copy

    def read_excel(sheet,row,col):
        '''读取excel表公共方法'''
        a = xlrd.open_workbook('F:/Downloads/quxiantu1.xls')   #打开excel文件，apiTestCase3.xls是正式环境文件，apiTestCase2.xls是测试环境文件
        b = a.sheet_by_name(sheet)   #获取sheet表
        c = b.cell_value(row,col)   #获取sheet表里面的行，列（序号0开始）
        return c    #返回行/列号

    def write_excel(list,row,col,data):
        '''写入excel表公共方法'''
        file = r"F:/Downloads/quxiantu1.xls"              #定义变量file
        rb = xlrd.open_workbook(file, formatting_info=True)       #打开Excel
        wb = copy(rb)    #将rb复制到wb,原因是因为“修改文件内容，依赖于xlutils(xlrd和xlwt)提供修改文件功能，xlutils.copy模块的copy()实现了这个功能”
        ws = wb.get_sheet(list)   #获取sheet，list 第几章表0开始，row几行, col几列, data写入的数据
        ws.write(row, col, data)  #根据行/列/数据，写入Excel
        wb.save(file)   #保存

    def frameslist(rendertask,testcol,testrow):
            '''访问帧作业列表'''
            url = "https://admin.renderbus.com/api/rendering/admin/task/rendering/getTaskFrameRenderList"
            parameter = {"nodeName":"","nodeIp":"","pageNum":1,"pageSize":200,"taskId":rendertask,"searchKeyword":"","defaultFlag":1}
            headers = {'channel': '5', 'platform': '6', 'signature': 'rayvision2017', 'version': '1.0.0', 'x-auth-token': '1e1d63bd-aef0-4d45-b0ab-ef8b25ecdb1d', 'Content-Type': 'application/json', 'languageFlag': '0'}
            baseUrl = requests.post(url, json=parameter, headers=headers,verify=False)  #接口URL
            result = baseUrl.json()  #读取的帧作业列表操作
            # print(result)
            # testrow = 0
            write_excel(testSheet, testrow, testcol, rendertask)
            for s in result['data']['items']:
                # print(s['frameExecuteTime'])
                write_excel(testSheet, testrow, testcol, int(s['frameExecuteTime']))
                testrow = testrow + 1

    testSheet = "test"
    rendertaskSheet = 'taskid'
    testcol =0
    testrow =0

    for s in [11416811,	11416809, 11416807, 11416805,
              11419537, 11419535, 11419533,	11419531,
              11426101, 11426105, 11426099,	11426091,
              11435185, 11435183, 11435179,	11435177,
              11470841, 11470839, 11470837,	11470835]:
        print(s)
        frameslist(int(s),testcol,testrow)
        testcol +=1


# 输入一个字符串：判断该字符串是否可以作为密码。可作为密码的条件:必须是包含大小写字母和数字的组合，不能使用特殊字符,长度在8-10之间。
def passwdfd():
    a = "1qaz2QAZed"
    if 8 <= len(a) <= 10 and a.isalnum():
        print("OK")
    else:
        print("Fail")

    a = "1qaz!QAZ"
    if 8 <= len(a) <= 10 and a.isalnum():
        if sum(map(str.islower, a)) > 0 and sum(map(str.isupper, a)) > 0 and sum(map(str.isdecimal, a)) > 0:
            print("{} valid for password".format(a))
        else:
            print("{} invalid for password".format(a))
    else:
        print("{} invalid for password".format(a))

import re
def checkpassword(password):
    return print(True) if re.search("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,10}$", password)  else print(False)


def checjpasswd(passwd:str) -> bool:
    if not 8 <= len(passwd) <=10:
        print("Fx")
        return False
    upper_regex = re.compile(r"[A-Z]+",re.S)
    lower_regex = re.compile(r"[a-z]+",re.S)
    num_regex = re.compile(r"\d+",re.S)
    print(upper_regex.findall(passwd))#查询有有没有大写字母
    print(lower_regex.findall(passwd))#查询有有没有小写字母
    print(num_regex.findall(passwd))#查询有有没有数字
    if upper_regex.findall(passwd) and lower_regex.findall(passwd) and num_regex.findall(passwd):
        print("OK")
        return True
    else:
        print("FX")
        return False

    # checjpasswd("123asdasd")

#字典使用
def testdict():
    src = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

    print(src['a']['b'])#1 字典打印
    print(src['d']['f']['g'])#4 字典打印

    src['r'] = 'cc'#如果没有这个ky对，则添加此kr
    print(src)

    for k,v in src.items():
        print(k,v)

    prefix = ''
    for k,v in src.items():
        prefix = prefix + k + '.'
        print(prefix)


#字典扁平化
src = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
def flatmap(src:dict):
    target = {}
    def _flatmap(src:dict,prefix=''):
        for k, v in src.items():
            if isinstance(v,(dict,)):#判断V是字典，否则
                prefix = prefix + k + '.'
                _flatmap(v,prefix)
            else:
                target[prefix + k] = v
    _flatmap(src)
    return target

    # print(flatmap(src))


#base64编码实现
import base64
#print(base64.b64encode('a'.encode()))


#求最大公共子串
s1 = 'defa'
s2 = 'defabcd1'
def findit(str1:str,str2:str):

    if len(str2) < len(str1):
        str1, str2 = str2, str1

    length1 = len(str1) #拿到最短的字符串
    length2 = len(str2)

    matrix = [ [0]*length1 for i in range(length2) ]
    # print(matrix)

    xmax = 0
    xindex =0

    for i,x in enumerate(str2):
        for j,y in enumerate(str1):
            if x != y:
                pass
            else:
                if i== 0 or j == 0:
                    matrix[i][j] =1
                else:
                    matrix[i][j] = matrix[i-1][j-1]+1
                if matrix[i][j] > xmax:
                    xmax = matrix[i][j]
                    xindex = j
    # print(matrix,xmax,xindex)
    start = xindex + 1 - xmax
    end = xindex + 1
    return str1[start:end]

# print(findit(s1,s2))

def findit1(str1,str2):
    if len(str2) < len(str1):
        str1, str2 = str2, str1

    length = len(str1)

    for sublen in range(length, 0, -1):
        for start in range(0, length - sublen + 1):

            substr = str1[start:start+sublen]

            print(substr)
            if str2.find(substr) > -1 :
                return substr

    # print(findit1(s1,s2))

#字符串查找find，如果在里面返回0，如果里面没有返回-1
# print(s2.find('t'))


#实现一个cache装饰器，过期清除的功能,打印运行时间
def cache_z():
    from functools import wraps
    import inspect
    import time
    import datetime


    def logger(fn):
        @wraps(fn)  # ==  wrapper(fn)(wrapper)  柯里化参数传入
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print(fn.__name__,delta)
            return ret
        return wrapper

    def mag_cache(duration = 5):
        def _mag_cache(fn):
            local_cache = {}  #对不同函数名是不同的cache
            @wraps(fn)
            def wrapper(*args, **kwargs):
                def _clear_expire():
                    expire_keys = [ ]
                    for k ,(_, stamp) in local_cache.items():
                        if datetime.datetime.now().timestamp() - stamp > duration :
                            expire_keys.append(k)
                    for k in expire_keys:
                        local_cache.pop(k)

                def _make_key(args, kwargs):
                    # 参数处理，构建Key
                    sig = inspect.signature(fn)
                    params = sig.parameters  # 有序字典
                    params_dict = {}
                    # 位置和关键字传参
                    params_dict.update(zip(params.keys(), args))
                    params_dict.update(kwargs)
                    for k, v in params.items():  # 定义的所有参数
                        if k not in params_dict:
                            params_dict[k] = v.default
                    key = tuple(sorted(params_dict.items()))
                    print(key)
                    return key

                _clear_expire()

                key = _make_key(args, kwargs)

                if key not in local_cache.keys():
                    local_cache[key] = fn(*args, **kwargs), datetime.datetime.now().timestamp()

                return local_cache[key]
            return wrapper
        return _mag_cache


    @logger#打印函数运行时间
    @mag_cache(6)#加入缓存，然后运行
    def add(x=4,y=5):
        time.sleep(3)
        return x + y


    add()
    print('~' * 30 )
    add(4,5)
    print('~' * 30 )
    add(y=5,x=4)


#命令分发器实现
def k873():#实现1
    commands = { }

    def reg(cmd):
        def _reg(fn):
            commands[cmd] = fn
            return fn
        return _reg

    def defaultfn():
        print('Unknown command')

    @reg('mag') #foo1 = reg ('mag')(foo1)   #reg('py',foo1)  -   @reg('py')  本来执行，变成了执行后然后，装饰器必定先运行才会给方法加上装饰器功能
    def foo1():
        print('magedu')
        print('123')

    @reg('py')
    def foo2():
        print('python')
        print('456')

    def dispatcher():
        while True:
            cmd = input('>>>'.strip())
            if cmd == '':
                print('bye')
                return
            commands.get(cmd, defaultfn)()

    dispatcher()

# 命令分发器实现
def k906():#实现2
    def cmds_dispatcher(defaultfn=lambda:print('Unknown command')):
        commands = { }
        def reg(cmd):
            def _reg(fn):
                commands[cmd] = fn
                return fn
            return _reg

        def dispatcher():
            while True:
                cmd = input('>>>'.strip())
                if cmd == '':
                    print('bye')
                    return
                commands.get(cmd, defaultfn)()
        return reg,dispatcher
    reg,run = cmds_dispatcher()  #全局变量解构

    @reg('mag') #foo1 = reg ('mag')(foo1)   #reg('py',foo1)  -   @reg('py')  本来执行，变成了执行后然后，装饰器必定先运行才会给方法加上装饰器功能
    def foo1():
        print('magedu')
        print('123')
    @reg('py')
    def foo2():
        print('python')
        print('456')
    run()  #解构之后运行，请看第一行运行解构变量



















#公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱。
def lianxiti():
    for i in range(1, 20): #公鸡
        for j in range(1, 33):  #母鸡
            for k in range(1, 300):  #小鸡
                if (5*i + 3*j + k/3) == 100 and i+j+k == 100:
                    print(i, j, k)

    for x in range(5, 100, 5):
        for y in range(3, 100 - x , 3):
            z = 100 - x - y
            if  x // 5 + y // 3 + z * 3 == 100:
                print("公鸡{}只，母鸡{}只，小鸡{}只".format(x // 5, y // 3, z * 3))




































