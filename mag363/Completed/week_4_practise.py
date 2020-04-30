#-*- comding:utf-8   -*-
#杨辉三角解法
def k3():
  m = 3
  k = 4
  oldline = []
  for i in range(m):
      newline = [1] * (i+1)
      for j in range(i - 1):
          newline[j+1] = oldline[j] + oldline[j+1]
      oldline = newline
  print(oldline)

#方阵互换3*3
def k16():
    # 123    147
    # 456    258
    # 789    369

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(3):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] ,matrix[i][j]
    print(matrix)

#方阵互换3*2
def k27():
    # 123    14
    # 456    25
    #        36

    matrix = [[1,2,3],[4,5,6]]
    tm = []
    for row in matrix:
        for i ,col in enumerate(row):
            if len(tm) < i + 1:
                tm.append([])
            tm[i].append(col)
    print(tm)
#优化方案
    matrix = [[1, 2, 3], [4, 5, 6]]
    tm = [[0 for j in range(len(matrix))]for i in range(len(matrix[0]))]
    for i in range(len(tm)):
        for j in range(len(tm[0])):
            tm[i][j] = matrix[j][i]
    print(tm)

#随机产生10个数字
def k50():
    import  random
    nums = []
    for _ in range(10):
        nums.append(random.randrange(21))

    nums = [random.randrange(21) for _ in range(10)]#解析式

    #nums = [11, 7, 5, 11, 7, 6, 11]
    length = len(nums)
    states = [0] * length

    samenums = []
    diffnums = []

    for i  in range(length):#12345
        if states[i] != 0:
            continue
        count = 0

        for j in range(i + 1, length):
            if states[j] != 0:
                continue
            if nums[i]  == nums[j]:
                count += 1
                states[j] = count

        if count:
            states[i] = count + 1
            samenums.append((nums[i], count + 1))
        else:
            diffnums.append(nums[i])

    print(samenums)
    print(diffnums)
    print(states)

#ipython使用,解构和丢弃变量，解构必须相等，%%timeit fac1
def k89():
    a = 1,2,3,4,5,6,7,8,9
    c,n = 3,5
    head, *_, tail = a
    #中间的丢弃变量，不需要
    lst = [1,(2,3,4),5]
    _,(*_,a),_ = lst#取4
    #取路径
    s = "JAVA HOME=/usr/bin=123"# env, path=s. split('=',1)
    env, _, path = s.partition('=')

    #冒泡排序
    nums = [5, 8, 66, 33, 88, 123, 11, 77]
    length = len(nums)
    count = 0
    count_swap = 0
    for i in range(length):
        flag = False
        for j in range(0, length - 1 - i):
            count += 1
            if nums[j + 0] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                flag = True
                count_swap += 1
        if not flag:
            break
    print(nums, count, count_swap)

# set  集合,只能是可以哈希的，不能哈希的就不能放进集合。可变，不重复，无序的
def k120():
    s = {77,2,3,4,5,1,2,2,3,4,6}#set 自己会去重 最后等于{1, 2, 3, 4, 5, 6}
    hash('asdasd') #哈希,打印出ID号，判断可不可以hash
    s.add(9)#增加字符串，或者元组，或者Int
    s.update([9,99,87,85],list(range(5)))#迭代增加元素，增加集合里面不重复的元素，相当于+增加，就地修改，不是新的，可以好几个迭代对象
    s.remove(99)#删除不存在则返回keyEeeor,set里面删除的代价小，比列表低
    s.discard(999)#删除一个元素，有就有，没有就没有不报异常
    s.pop()#移除一个元素，返回任意的元素
    # s.clear()#移除所有元素
    2 in s #迭代，很快ns纳秒级别的,list需要ms毫秒级别
    #可变数值型int、float、complex ，布尔型True、False，字符串string、bytes
    set1 = set(range(5))
    set2 = set(range(4,9))
    set1 = {0, 1, 2, 3, 4}
    set2 = {4, 5, 6, 7, 8}
    # print(set1|set2)
    # print(set1.union(set2))
    # set3 = set()
    # print(set3.update(set1,set2))
    #
    # print(set1)
    # print(set2)
    c = set1.intersection(set2) #共同好友是谁返回相同的intersection
    set3 = {4, 5}
    c = set3 - set2  #然后判断是不是空，就可以知道在不在里面
    c = set1|set2
    print(c)
    c.symmetric_difference(set1)
    print(c)

#字典dict,可变的，无序的,key不重复,key value
def k150():
    a = dict(a=1,b=2)
    a = {'a':1, 'b':2 }
    a = dict([('s',100),['h',66],('d',99)],a=1,b=2)
    a = dict.fromkeys(range(5))#{0: None, 1: None, 2: None, 3: None, 4: None}
    a[2] = 123 #如果2在则改变，如果没有则增加2
    a.get(2)  #拿这个key，有就返回，没有就返回None 或者a.get(2，3)如果2没有就找3
    a.setdefault('a',200) #如果有则返回对应的，没有就把200给到缺省值
    a.setdefault('a',1000) #这样有值了，所以1000不生效，则返回200
    a.update([(0,500)]) #因为0不能作业哈希，所以要用这样的方式，0=500不可用
    a.pop(1,'没有这个')#key在则移除value返回value，不在就返回备注的value
    c = a.popitem()#随机移除一个，并返回value
    del a[4] #删除字典中的一个key
    a = {'s': [100,200], 'h': 66, 'd': 99, 'a': 1, 'b': 2}
    # for i in a.keys():#或者value
    #     print(i,a[i])
    # for k,v in a.items():
    #     print(k,v)
    a.keys() or a.values() or a.items() #都是一个列表，返回所有的，或者用len统计有多少给key或者values

    a = {}
    for i in 'abcde':
        for j in range(3):
            if i not in a.keys():
                a[i] = []
            a[i].append(j)
    #{'a': [0, 1, 2], 'b': [0, 1, 2], 'c': [0, 1, 2], 'd': [0, 1, 2], 'e': [0, 1, 2]}

    from collections import  defaultdict,OrderedDict #defaultdict定期缺省值keyError，如果缺省就给定义一个
    a = defaultdict(list) #有定义缺省值的字典，如果缺少就补充定义的values
    for i in 'abcde':
        for j in range(3):
            a[i].append(j)

    #OrderedDict
    a = OrderedDict() #有记录顺序的字典,每次增加的key，都会记录顺序
    a = {2:'a', 3:'b', 4:'c'}
    a = sorted(a.items(), reverse=True)  #倒叙打印


#输入一个数字，打印每个数字重复及其次数
def k190():
    num = '54321543210'
    counter = {}
    for i  in num:
        # if i not in counter.keys():
        #     counter[i] = 0
        # counter[i] +=1
        # counter[i] = counter.get(i ,0) +1
        counter[i] = counter.setdefault(i ,0)+1
    print(counter)

#字符串重复统计
def k202():
    import random
    from collections import defaultdict
    mums = [random.randint(-1000, 1000)for _ in range(100) ]
    counter = defaultdict(int)
    for i in mums:
        counter[i] += 1

    #方法1
    newdict = sorted(counter.items(), reverse=True)
    print(newdict)

    #方法2
    keys = list(counter.keys())
    keys.sort()  # reverse=True 倒序
    for k in keys:
        print(k, counter[k])

    #方法3
    keys = list(counter.keys())
    keys.sort()  # reverse=True 倒序
    newlist = [0] * len(keys)
    for i,k in enumerate(keys):
        newlist[i] = k, counter[k]
    print(newlist)

#字符串重复统计
def k229():
    import string,random
    from collections import defaultdict
    #string.ascii_lowercase
    alpha = 'asdaseqasdqweqweaczxc'
    words = [random.choice(alpha) + random.choice(alpha) for _ in range(100)]
    counter = defaultdict(int)
    for w in words:
        counter[w] = counter[w,0] + 1
    print(counter)

#datetime 时间模块
import   datetime
def k241():
    d1 = datetime.datetime.now()#返回当前时间的datetime
    print(d1.date())
    print(datetime.datetime.today())#返回本地时区的当地时间
    print(datetime.datetime.utcnow()) #没有时区的当地时间
    print(datetime.datetime.timestamp(d1))#返回一个时间戳

    d2 = datetime.datetime.utcnow()
    print(d2.timestamp())
    d3 = datetime.datetime.fromtimestamp(int(d2.timestamp()))#把时间戳返回成时间
    print(d3)
    d1 = datetime.datetime.now()
    d1 = datetime.datetime.weekday(d1)#周一到周六0-6
    print(d1)
    d5 = datetime.datetime.strptime('2019,07,01,21,58,59','%Y,%m,%d,%H,%M,%S')
    print(d5)

    d5.strftime('%Y/%m-%d     %H:%M:%S')
    print(d5.strftime('%Y/%m-%d     %H:%M:%S'))
    "{0:%Y}{0:%S}".format(d5)
    print("{0:%Y} {0:%S}".format(d5))

    start = datetime.datetime.now()
    for i in range(100000):
        s = 1
        s += 1
    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)

#time标准时间库
import  time
def k273():
    time.sleep(10)#暂停10s

#列表解析式,基本写法，都是列表里面，减少代码
def k277():
    #生成一个列表，元素0-9.每个元素自增1秋平方返回新列表
    new = []
    for i in range(10):
        new.append((i+1)**2)
    print(new)

    new1 = [(i+1)**2 for i in range(10)]
    print(new1)
    #获取10以内的偶数
    new2 = []
    for i in range(10):
        if i % 2 == 0 :
            new2.append(i)
    print(new2)

    new3 = [i for i in range(10) if i % 2 == 0]
    print(new3)

    #双层if
    new4 = []
    for i in range(10):
        if i % 2 == 0 :
            if i % 3 == 0:
                new4.append(i)
    print(new2)


    new4 = [i for i in range(10) if i % 2 and i % 3 == 0]
    new4 = [i for i in range(10) if i % 2 if i % 3 == 0]
    new4 = [i for i in range(10) if i % 2 or i % 3 == 0]
    print(new4)

    #for双层循环
    ret = []
    for i in range(3):
        for j in range(3):
            ret.append('a')
    print(ret)

    ret1 = [(x,y) for x in 'abc' for y in range(3)]
    print(ret1)

    #多层循环，多层判断
    rat = [(i,j) for i in range(8) if i > 5 for j in range(20,25) if j > 20 if j >22]
    print(rat)

#列表解析式，1-10平方列表
list1 = [i*2 for i in range(10)]
#列表解析式，列表相邻的两数之和，的新列表
list2 = [2,6,2,4,7,3,5,1,9]
list3 = [list2[i] + list2[i+1] for i in range(len(list2)-1)]
#列表解析式9 9 乘法表
def k330():
    list4 = ([print("{}*{}={:<3}".format(j,i,j*i),end='\n' if i == j else '') for i in range(1,10) for j in range(1,i+1)])
#列表解析式，'0003.qzrgbnwqnk' 生成一些随机的验证
import random
#生成所有字母
list5 = bytes(range(97,123)).decode() #生成所有字母
list5 = random.choices(list5,k=10)  #choices 可以指定取出多少个随机字符
list6 = chr(random.randint(97,122))#生成所有小写字母
list6 = chr(random.randint(65,90))#生成所有大写字母

#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
list7 = "".join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)]) #循环10次，然后连接在一起
#生成头前面的然后补0
list8 = ['{:04}'.format(i) for i in range(0,101)]
#然后添加进去
list8 = ['{:04}.{}'.format(i,"".join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)])) for i in range(0,101)]



#迭代器，如果循环，不能二次循环，需要的时候才计算，不是放在内存中，立马运算,成一个列表，作为迭代的次数,延迟计算
def k350():
    list9 = ('{:04}.{}'.format(i,"".join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)])) for i in range(0,101))
    return list9
    print(next(list9))  #要注意调用可以多次调用，而在一个里面，只能一次
    print(next(list9))
    for i in list9:
        print(i)
        print(list9) #不能作为变量打印了，只是一个迭代器

#集合解析式
def k357(): #注意不可hash的值不能放进去
    j = {(x,x+1) for x in range(10)}
    print(j)

#字典解析式,
def k362():#要注意key 去重
    dict1 = {x:[x,x+1] for x in range(10)}
    print(dict1)

#简单排序,升序或者降序
def k370():
    nums = [1,9,8,5,6,7,4,3,2]
    length = len(nums)
    for i in range(length):
        maxindex = i
        for j in range(i+1,length):
            if nums[j] > nums[maxindex]:
                maxindex = j
        if maxindex != i:
            nums[i] , nums[maxindex] = nums[maxindex] ,nums[i]
    print(nums)

    #优化
    nums = [1,9,8,3,3,9,6,3,3,3,8,3,3,3,11]
    length = len(nums)
    counter_iter = 0
    counter_swap = 0
    for i in range(length // 2):
        maxindex = i
        minindex = -i-1
        counter_iter += 1
        minorigin = minindex
        for j in range(i+1,length - i):
            if nums[j] > nums[maxindex]:
                maxindex = j
            if nums[-j-1] < nums[minindex]:
                minindex = -j-1

        if nums[maxindex] == nums[minindex]:
            break

        if maxindex != i:
            counter_swap += 1
            nums[i] , nums[maxindex] = nums[maxindex] ,nums[i]
            #如果交换了就要更新索引，因为交换了记录的还是之前的
            if i == minindex or minindex == i - length:
                minindex = maxindex - length

        if minindex != -i-1 and nums[minorigin] != nums[minindex]:
            nums[-i-1] , nums[minindex] = nums[minindex] ,nums[-i-1]
    print(nums)
    print(counter_iter, counter_swap)


#内建函数
def k415():
    x = 1
    id(x) #返回内存地址
    hash(x) #返回是否可以hash
    type(x) #返回对象类型
    # float(x) ,int(x) ,bin(x), hex(x), oct(x), bool(x) ,list(x), tuple(x)
    # dict(x), set(x), complex(x), bytes(x), bytearray(x)
    input()#接受用户输入
    len() #统计长度
    isinstance('s',str)#判断是否相等
    issubclass()
    max(),max()#返回对象中最大或者最小值
    round()#四舍六入五去偶
    pow()#等价1**2  多少方
    range() #迭代器
    divmod() #等于x//y  ,x%y  整除然后取模
    sum()#求和
    chr(20013)#返回一个整数的对应字符
    ord('中')#返回字符串对应的整数
    hex(20013)
    str()
    repr()
    ascii()
    sorted()#返回一个新的列表，默认升序,或者添加severtse=True,降序
    reversed()#返回一个反转的迭代器
    list(reversed('123579')) #返回一个翻转的
    memoryview(range(10,15),10)#索引默认是0，现在设置为10
    iter('1,2,3,4')#将迭代对象封装成一个迭代器，然后通过Next来拨动
    next(_,10)#当跑完可以如果没有缺省值会抛stopiteration异常，现在设定为10
    s = zip(range(5),range(6,11),'abcdfqw') #把多个迭代对象合并在一起返回一个迭代器











