#-*- comding:utf-8   -*-
import random
#random 随机数应用 ASCII 所有
def k4():
    i = 0
    charlist = []
    for _ in range(255):
        char1 = (random.choice(chr(random.randint(i, i))))
        i  +=1
        charlist.append(char1)
        #ASCII =['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98', '\x99', '\x9a', '\x9b', '\x9c', '\x9d', '\x9e', '\x9f', '\xa0', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '\xad', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ']
    print(charlist)
        # char1 = (random.choice([chr(random.randint(65,90)), str(random.randint(0,9))]))

    list1 = bytes(range(97, 123)).decode()  # 生成所有字母
    list2 = random.choices(list1, k=10)  # choices 可以指定取出随机多少个随机字符
    list3 = chr(random.randint(97, 122))  # 所有小写字母，随机一个
    list4 = chr(random.randint(65, 90))  # 所有大写字母，随机一个

#函数,一定要注释，缺省值,callable判断是不是函数
def add(x = 4,y = 5):
    print(callable(add))  # 判断这个是不是函数，能不能调用，能则True
    return x + y

#登录函数,默认缺省值
def login(host = '127.0.0.1',port = '8080', username = 'admin', password = '123456'):
    print('{}:{}@{}/{}'.format(host,port,username,password))

def add1(a=1,*nums):
    print(a)
    sum = 0
    for x in nums:
        sum += x
    return sum
#add1('a',2,3)#*nums ,代表全部归为一个元组，作为迭代对象,a作为一个可变位置参数，不能放到*可变位置参数后面

def config(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print('{}={}'.format(k,v))
# config(host='127.0.0.01',port='80')#关键字参数，可以是一个可变关键字，生成一个字典

def config1(c,*args,houst,a,**kwargs):#c,a 代表的是keyword-only参数，必须要指定，如果不指定就会被*args搜集走
    print(c,a,houst,args,kwargs)
    for k,v in kwargs.items():
        print('{}={}'.format(k,v))
#config1(2,3,4,5,6,houst=22,a=11,host ='127.0.0.01',port='80')#一定要注意这些参数的定义，*元组，**字典。

def fn(x,y,z=3,*arg,m=4,n,**kwargs): #一半定义时
    pass

def connect2(**kwargs):
    print(type(kwargs))
    print(kwargs.items())
    print(kwargs.keys())
    print(kwargs['db'])
    connect2(db='cmdb')

#海外注册刷接口
def abroadRegister():
    import requests
    a = 450
    for _  in range(1000):
        url = "https://task-pre.foxrenderfarm.com/api/rendering/user/abroadRegister"
        payload = '{"userName":"a132456798%s","password":"2edf692c26918cc7d11def6ab41bbdffdbecce52","email":"a132456798%s@qq.com","phone":"","agentId":null,"shareId":"93100001"}'%(a,a)
        # print(payload)
        headers = {
            'content-type': "application/json",
            'signature': "rayvision2017",
            'platform': "0",
            'channel': "2",
            'version': "1.0.0",
            'cache-control': "no-cache",
            'postman-token': "8db844e2-d1cb-d250-2361-94c3a9b02279"
        }
        response = requests.request("POST", url, data=payload, headers=headers, verify=False)
        a += 1

def add3(x,y):
    print(x + y)
    # return x + y
    # add3(*range(100,102))
    print(2)
    # add3(*{'x':100,'y':200,})
    print(3)
    # add3(**{'x':100,'y':200,})
    print(4)
    # add3(*{'x':100,'b':200,})
    print(5)
    # add3(**{'x':100,'b':200,})

#编写一个函数最少接受两个值，返回最大最小
def instmaxmin(*xx):
    print (min(xx),max(xx))
    # for i in z:

#编写一个函数，接受一个参数n，n为正整数，左右两种打印方式。要求数字必须对齐
def triangie_print(n):#先创建一个最多的列表，然后每次循环打印，切片打印，倒着打印，每次打印一次增加2位，这样就是每次增加1
    tail = ' '.join(str(i) for i in range(n, 0, -1))
    width = len(tail)
    start = -1
    step =2
    points = {10*i for i  in range(1, 3)}
    for i in range(1, n+1):
        print('{:>{}}'.format(tail[start:], width))
        if i+1 in points:
            step += 1
        start = start - step
#                          1
#                        2 1
#                      3 2 1
#                    4 3 2 1
#                  5 4 3 2 1
#                6 5 4 3 2 1
#              7 6 5 4 3 2 1
#            8 7 6 5 4 3 2 1
#          9 8 7 6 5 4 3 2 1
#       10 9 8 7 6 5 4 3 2 1
#    11 10 9 8 7 6 5 4 3 2 1
# 12 11 10 9 8 7 6 5 4 3 2 1

def showtail(n):#反打
    tail = ' '.join([str(i) for i in range(n, 0, -1)])
    print(tail)
    for i in range(len(tail)):
        if tail[i] == ' ':
            print(' '*i,tail[i+1:])

def triangie_print1(n):#正打
    tail = ' '.join([str(i) for i in range(n, 0, -1)])
    for i in range(len(tail)-2,0,-1):
        if tail[i] == ' ':
            print(' '*(i-1),tail[-(len(tail)-i):])
    print(tail)

#插入排序算法，哨兵
def interposition():
    origin = [1,9,8,5,6]
    nums = [0] + origin
    length =len(nums)
    for i in range(2, length):
        nums[0] = nums[i] #哨兵
        j = i -1
        if nums[j] > nums[0]:
            print(i,j,nums[j],nums[0],'看看',nums)
            while nums[j] > nums[0]:
                nums[j+1] = nums[j]
                print('开始',nums)
                j -= 1
            nums[j+1] = nums[0]

    print(nums)

#字符设定颜色
def k155():
    string = (1,2,3,4,5,6)
    color_str = ''
    color_id = random.sample((range(31, 38)), 6)
    for i in range(6):
        color_str += "\033[0;{c};40m{s}\033[0m".format(c = color_id[i], s = string[i])
        print(color_str)

#函数的返回值，只要函数中有return执行了，后面的都不会被执行，很重要额一个结束标志,只要遇到了就会结束函数,如果返回的值需要多个，那么会返回一个元组
def k164(x):
    if x < 3:
        return  2
    c = x+1
    # return [c,x]
    return 1,2
    #一般情况下函数里面都有一个return，如果没写，默认为 return None
    #返回值只有一个，多个自动封装成一个元组
    #或者指定封装成一个列表
    #可以通过解构来获取元组里面的参数，x,y = k164(5)

#函数的作业域,内部函数不能再外部使用。可见范围才能调用，在函数内部
def outer():
    def inner():
        print(1)
    print(2)
    inner()
    #outer可以作为使用，但是inner这个函数在outer里面，不可使用，所以不可单纯使用Inner()来使用

#赋值重新定义

def show():
    s = 5
    print(s)   #只要内部重新定义了，外部的s的作用域同样没有用了
    s = s + 1   #当内部重新定义后，外面的s的变量就不能用了，所以外部和内部不能使用，内部重新定义的值，会让外部定义的值，内部取不了
    print(s)   #这样是不对的，重新定义这样是不可用的
    #重新定义，造成后面的定义取不到定义，所以不能成功

#全局变量globals(),
def k192():
    globals() #在函数内部操作外部变量
    x = 6
    def foo():
        global x
        x += 1
        print(x)
    print(x)
    foo()#因为函数内部定义了全局变量，所以变化之后，变量也会跟着变
    print(x)

#全局变量如果在多重函数中的时候,并且使用全局的时候，必要要有一个全局变量定义
def foo1():
    z = 1  #因为global是定义全局变量，如果外面没有定义，那么就算函数内部定义了，也不生效
    def foo():
        z = 2
        def bar():
            global z  #如果定义全局变量，必须要声明这个是要用全局变量的，要不然会用局部变量作用域，相当于重新定义会报错
            z = z*100
            # print(z)
        print(1,z)
        bar()
        # print(2,z)
    foo()
    print(z)

#闭包，也就是说，父子结构的函数类型，内层函数用到外层函数的局部变量，就称为闭包（子函数用户到父函数里面的变量，就叫做闭包）（内层函数用到外部函数的局部变量就叫做闭包）
def foo2():
    z = [100]
    # z = 100
    def foo3():
        z[0] += 1
        # z += 1
        print(z)   #内部函数用到了外层函数的变量，称为自由变量
    print(z)
    return foo3()
    # foo3() #执行foo2()则能够成功打印   ,为什么可以，因为闭包的数据变量，但是不能用z = 100


def counter():#因为c = [0] 不是普通变量，产生了闭包，所以可以使用这一的流程
    c = [0]
    def inc():
        c[0] += 1
        return c[0]
    return inc

    # counter()
    # foo4 = counter()
    # print(foo4(),foo4())
    # c = 100    #为什么执行这个的时候没有生效，因为此时执行的还是之前的定义函数内部有定义
    # print(foo4())

#nonlocal 的使用，globals是全局的变量，所以使用nonlocal,他定义是把外部作用域作为内部作用域使用，但是这个外部作用域变量不能是全局作用域。
def foo4():  #普通变量不能产生闭包，怎么产生闭包，全局变量，但是能不用就不要用，所以使用nonlocal，对普通变量闭包
    z = 100
    def foo5():
        nonlocal z  #去外层的局部作业域中找一个对应的定义，作为内部的局部定义，只在局部作为使用，获取局部变量
        z += 1
        print(z)
    print(z)
    return foo5()
    #foo4() #如果没有nonlocal，那么此时不能执行的，因为c找不到，但是使用后，就可以吧外部作用域作为内部作业域使用，相当于闭包内部使用

#默认值的本质 本质
def k257():
    def bar(xyz = [1]):
        xyz += [1]
        print(xyz)

    def foo(xyz = 1):
        xyz += 1
        print(xyz)
    bar()
    bar()
    bar([3])
    bar()
    print(bar.__defaults__) #打印的是元组缺省值，函数的缺省值也会改变，跟着函数的变量而变量，调用三次之后缺省值变成([1, 1, 1, 1],)，一个元组
    print(bar.__kwdefaults__)#打印的是字典或者缺省值

    def foo2(a = [10,11]):
        a = a[:]   #影子拷贝，这样就不会改变缺省值，导致缺省值每次都跟着改变。但是这样每次都是一个全新的所以还是有问题
        a.append(1)
        print(a)

    def foo3(a = None):
        if a is None:  #这样样子就是定义一个缺省值，每次判断是否是空的，然后来使用
            a = []
        a.append(1)
        print(a)
        return a
        # foo2影子拷贝，永远不能修改传入参数的
        # foo3创建或者修改传入对象口这种方式灵活，应用广泛，很多函数的定义，都可以看到使用None这个不可变的值作为默认参数，可以说这是一种惯用法

        #del a   #删除函数变量


#递归的几种方式,直接或者间接的调用自己，一定要有边界条件，fib1的是最快的，其他的是超级慢的
def fib1(n):
    a = 0
    b = 0
    for i in range(n):
        a, b = b, a+b
    print(a)

def fib(n):
    if n == 0:
        # print(0)
        return 0
    elif n < 3:
        # print(1)
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    return 1 if n<3 else  fib(n-1) + fib(n-2)

def fib3(n,a=0,b=1):#最后总结，总结了这个。
    if n < 3:
        return a+b
    else:
        print(a,b,'a1')
        a,b = b,a+b
        print(a,b,'a2')
        return fib3(n-1,a,b)

def fib4(n,a=0,b=1):
    a, b = b, a + b
    if n == 0:
        return a
    # print(a,b)
    return fib4(n-1,a,b)

#递归练习题N的阶乘
def fib5(n):
    # if n == 1:
    #     return 1
    # return n * fib5(n-1)
    return 1 if n == 1 else n * fib5(n-1)

def fib6(n,fac=1):
    if n ==1:
        return fac
    fac = fac * n
    return fib6(n-1,fac)

#递归数字排序，倒序，将一个数逆序放入列表中，例如1234=>【4，3，2，1】
data = str(1234)
def revert(x):#递归
    print(x)
    if x == -1:
        return []
    return [data[x]] + revert(x-1)

    #print(revert(len(data)-1))

def revert1(x,target=[]):#切片递归
    if x:
        target.append(x[-1])
        revert1(x[:-1])
    return target

    # print(revert1('1234'))

def revert2(x,targer=None):#数字取模递归
    if targer == None:
        targer = []
    x , y  = divmod(x,10)
    targer.append(y)

    if x ==0:
        return targer
    return revert2(x,targer)

    #print(revert2(123045))

#递归猴子吃桃,猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想吃时，只剩下一个桃子了。求第一天共摘多少个桃子。
def peach(days=10):
    if days == 1 :
        return 1
    return (peach(days-1)+1)*2

#取模
def k367():
    x = 123456
    print(divmod(x, 10))
    x, y = divmod(x, 10)
    print(x, y)
    #整除取余数

#匿名函数 lambda，只接受一行，单行函数
def labada1():
    print((lambda  x : x ** 2)(4))

    fn = lambda x : x ** 2  #不推荐

    def fn(x):
        return x ** 2

    print((lambda x,*,y=30:x+y)(5,y=30)) #35
    print((lambda *args : (x for x in args))(*range(5)))  #返回迭代器
    print((lambda *args : {x for x in args})(*range(5)))  #{0, 1, 2, 3, 4}
    print((lambda *args : [x for x in args])(*range(5)))  #[0, 1, 2, 3, 4]
    print([x for x in (lambda  *args : map(lambda x: x+1 ,args))(*range(5))])  #[1, 2, 3, 4, 5]
    print([x for x in (lambda  *args: map(lambda x: (x+1,args),args))(*range(5))])

#生成器函数，必须包含yield语句，惰性求值，不着急的慢慢算，极力推广
def fn():
    for i in range(5):
        yield i

    print(type(fn())) #<class 'generator'> 生成器对象
    print(type(fn))  #<class 'function'>   函数
    print(next(fn()))
    for i in fn():
        print(i)

def gen():
    print('1')
    yield 2
    print('3')
    yield 4
    print('5')
    return 6  #return 会终止，返回stopiteration异常
#生成器可以把无线循环作为迭代使用
def k418():
    def counter():
        i = 0
        while True:
            i += 1
            yield i
    def inc(c):
        return next(c)

    c = counter()  #这样相当于计数
    print(inc(c))
    print(inc(c))
    #d第二种方法
    def inc():  #这样每次都是重置
        c = counter()
        return next(c)

    print(inc())
    print(inc())
    print(inc())

def k419():#优化
    def inc():
        def counter():
            i = 0
            while True:
                i += 1
                yield i
    c = counter()

    def _inc():
        return next(c)

    return _inc #返回的是一个函数

    g = inc() #变量等于这个函数
    print(g())  #调用函数，然后执行
    print(g())

#yield from
def inc():
    yield from range(5)

    # for i in inc():
    #     print(i)

























