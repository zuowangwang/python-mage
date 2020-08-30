#-*- comding:utf-8   -*-

#消费清单，前后台时间对比
def k1():
    import datetime, requests
    delta = [0, 0]
    count = [0, 0]

    # 前台代码1
    start = datetime.datetime.now()
    for _ in range(1):
        url = "https://task-pre.renderbus.com/api/rendering/task/renderingTask/findConsumptionList"
        # payload = "{\"userId\":-1,\"submitDate\":\"2019-6-4\",\"completedDate\":\"2019-6-11 23:59:59\",\"projectId\":-1,\"platform\":-1,\"timeStatus\":0,\"pageNum\":1,\"pageSize\":10}"
        payload = '{"userId":-1,"submitDate":"2019-3-20","completedDate":"2019-6-18 23:59:59","projectId":-1,"platform":-1,"timeStatus":0,"pageNum":1,"pageSize":10}'
        headers = {
            'userkey': "2a94a230785e3cbf91942ae93d0f45d0",
            'content-type': "application/json",
            'signature': "rayvision2017",
            'platform': "2",
            'channel': "2",
            'version': "1.0.0",
            'cache-control': "no-cache",
            'postman-token': "b5667a5a-0289-9f9e-b62c-b4d3700c4df5"}
        response = requests.request("POST", url, data=payload, headers=headers, verify=False)
        # print(response.text)
        count[0] += 1
    delta[0] = (datetime.datetime.now() - start).total_seconds()

    # 后台代码2
    start = datetime.datetime.now()
    for _ in range(1):
        url = "https://admin-pre.renderbus.com/api/rendering/admin/front/pay/recharge/list/getConsumeList"

        # payload = "{\"pageNum\":1,\"pageSize\":50,\"userId\":\"10005363\",\"queryRelateUser\":0,\"timeStatus\":\"0\",\"consumeAmount\":\"0\",\"platform\":\"\",\"feeType\":[]}"
        payload = '{"pageNum":1,"pageSize":50,"userId":"10005363","queryRelateUser":0,"timeStatus":"0","consumeAmount":"0","platform":"","feeType":[]}'
        headers = {
            'languageflag': "0",
            'channel': "5",
            'content-type': "application/json",
            'x-auth-token': "25cf5807-0ede-42a9-a0cb-e1c1e59230ae",
            'signature': "rayvision2017",
            'platform': "2",
            'version': "1.0.0",
            'cache-control': "no-cache",
            'postman-token': "852606c2-977e-c94e-be88-965132338751"
        }
        response1 = requests.request("POST", url, data=payload, headers=headers, verify=False)
        # print(response1.text)
        count[1] += 1
    delta[1] = (datetime.datetime.now() - start).total_seconds()

    print(count)
    print(delta)
    print(delta[0] - delta[1])

#创建1000个子账户
def k333():
    count = 0
    zi = 213
    ph = 15210229545
    for i in range(1000):
        url = "https://task-pre.renderbus.com/api/rendering/user/addSubUser"
        payload = '{"subUserName":"test_baojis%s","subPassword":"Hj123456789","email":"test_baojis%s@qq.com","status":1,"phone":"%s"}' % (
        str(zi), str(zi), str(ph))
        headers = {
            'userkey': "3200696a805125941b7716ceb9091337",
            'content-type': "application/json",
            'signature': "rayvision2017",
            'platform': "2",
            'channel': "2",
            'version': "1.0.0",
            'cache-control': "no-cache"}
        response1 = requests.request("POST", url, data=payload, headers=headers, verify=False)
        kk = response1.json()['code']
        if int(kk) != 200:
            print(payload)
            print(response1.json())
            break
        count += 1
        zi += 1
        ph += 1
    print(count)

#random列表随机数整数,前后都包
'''
import random
# ss = random.randint(0,10)
# print(ss)
#
# for i in range(10):
#     ss = random.randint(0, 10)  #randint没有步长
#     print(ss,end=' ')
#
# for i in range(10):
#     dd = random.randrange(0,5,2) #randrange有步长
#     print(dd,end=' ')

list = list((range(10)))
random.choice(list)   #choice随机抽取列表中元素，可迭代对象  range（10）都可以

random.shuffle(list)    #->None  shuffle就地打乱列表元素

random.sample(list,2)   #从一个列表中，随机取2个元素生成一个新的列表   返回等于[5,8] 是一个新的列表
'''

# 计算杨辉三角前6行
def k79():
    n = 6
    triangle = []
    for i in range(6):
        cur = [1]
        triangle.append(cur)
        if i == 0: continue
        pre = triangle[i - 1]
        for j in range(i - 1):
            cur.append(pre[j] + pre[j + 1])
        cur.append(1)  # 在一个循环中，对一个变量进行修改，他的id不会变，所以数据可以追加
    print(triangle)

#元组
'''
t = tuple()        #空元组
s = (2,33,44)      #赋值元组
d = tuple(range(5))
r = tuple(list(range(5)))
# print(r)#(0, 1, 2, 3, 4)
r = list(tuple(range(5)))  #元组也可以迭代，也是一个迭代对象
# print(r)#[0, 1, 2, 3, 4]
p = (2,)  #一个元素必须要加,  否则就是一个数字或者一个字符

'''

#命名元素
'''
from collections import namedtuple
student = namedtuple('student','name age')
tom = student('tom',20)
jerry = student('jerry',18)
print(tom.name)
print(type(tom.name))
'''

#输入三个数，排序if排序
'''
import random
nums = []

out = None
for  i in range(100):
    a = random.randint(1,100)
    nums.append(a)
print('初始数值为',nums)

#if 排序
if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        if nums [1] > nums[2]:
            out = [0,1,2]
    else:
        out = [2,0,1]
else:
    if nums[0] > nums[2]:
            out = [1,0,2]
    else:
        if nums [1] > nums[2]:
            out = [1,2,0]
        else:
            out = [2,1,0]
for i in out:
    print(nums[i],end=' ')
print('')

'''

# 输入三个数，排序sort方法
'''
nums.sort(reverse=True)
print(nums)
'''

#输入三个数，排序max 循环方法
'''
nums = [5,8,11,77]
m = []
print(nums)
while nums:
    s = max(nums)
    m.append(s)
    nums.remove(s)
print(nums)
print(m)


[5, 8, 11, 77]
[]
[77, 11, 8, 5]

print('~~~~~~'*10)

nums1 = [5,8,11,77]
m = []
print(nums1)
length = len(nums1)
#for _ in nums1:  #为什么不能循环列表 意思就是说，如果迭代的对象是一个列表，如果对列表进行修改，此时就会有问题,
#如果要修改这个列表或者元组，那这个元组或者列表不能作为循环的对象
for _ in range(length):
    s = max(nums1)
    m.append(s)
    nums1.remove(s)
print(nums1)
print(m)


[5, 8, 11, 77]
[5, 8]
[77, 11]

'''

#输入三个数，排序冒泡排序
'''
nums = [5,8,66,33,88,123,11,77]
length = len(nums)
count = 0
count_swap = 0
for i in range(length):
   flag = False
   for j in range(0,length-1-i):
       count += 1
       if nums[j+0] >nums[j+1]:
           tmp = nums[j]
           nums[j] = nums[j+1]
           nums[j+1] = tmp
           flag = True
           count_swap += 1
   if not flag:
       break
print(nums,count,count_swap)

#可以查看一共循环多次作为比较，交换一次就会迭代一次
'''

# 求100以内25个质数n =1#奇偶数
'''
n = 100
count = 0
primenumbers = []
for x in range(2,n):
    for i in range(2,int(x**0.5)+1):#奇偶数
        if x % i == 0:
            break
    else:
        count+=1
        primenumbers.append(x)
print(count)
print(primenumbers)
'''

# 求100以内25个质数n =2#奇数
'''
n = 100000
count = 1
primenumbers = []
start = datetime.datetime.now()
for x in range(3, n, 2):
    for i in range(3, int(x**0.5)+1, 2):#奇数
        if x % i == 0:
            break
    else:
        count+=1
        # primenumbers.append(x)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
# print(primenumbers)
'''

#求100以内25个质数n =3#奇数都多，质数
'''
n = 100
count = 0
primenumbers = []

for x in range(2, n):
    for i in primenumbers:#奇数都多，质数列表
        if x % i == 0:
            break
    else:
        count+=1
        primenumbers.append(x)
print(count)
print(primenumbers)
'''

#求100以内25个质数n =4
'''
n = 100000
count = 0
primenumbers = []

start = datetime.datetime.now()
for x in range(2, n):
    flag = False #不是合数
    edge = x ** 0.5
    for i in primenumbers:#奇数都多，质数列表
        if x % i == 0: #找到了合数x
            flag = True #是合数
            break
        if i > edge: #找到了质数x
            break
    if not flag:#找到了质数x
        count+=1
        primenumbers.append(x)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
# print(primenumbers)
'''

#求100以内25个质数n =5 大于3的素数只有6N-1和6N+1两种形式
def k294():
    count = 2
    n = 100
    x = 5
    step = 2
    while x <= n:
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                break
        else:
            count += 1
        x += step
        step = 4 if step == 2 else 2
    print(count)

#字符串
def k310():
    #字符串可以相加
    a = '12312* qwe'
    #不能索引赋值  a[2] = 'ad'
    a = '12312* qwe'
    # for i in a : print(i)
    a = '12312* qwe'
    #迭代list可用
    l = list(a)
    #或者设为一个元素
    p = [a,'2131']
    #map,把0-10 分别转成字符串,join 必须要字符串，所有全部要map 转成字符串
    c = ','.join(map(str, range(10)))
    #字符可以用+ 相加
    a = '1'
    b = '2'
    c = a+b
    #split切开，分开，劈开,默认用空白字符切割，maxsplit指定切割几次,[]指切割后显示第几个
    l = 'a,b,c'
    s = l.split(',',maxsplit=1)[1] #等于b,c
    l = 'a,b,c'
    #partition返回  head，sep,tail
    l = l.partition('a')#('', 'a', ',b,c')
    #字符转转大写,小写，交互大小写
    l = 'a,b,c'
    l = (l.upper() + l.lower() + l.swapcase())
    #字符串排版，标题大写，首单词大写，居中打印，打印居右，左对齐，友对齐
    l = 'a,b,c'
    l.title() + l.capitalize() + l.center(50,'*') + l.zfill(20) + l.ljust(20) + l.rjust(20)
    #字符串修改replace,需要替换的值，和要替换几次
    l = 'www baidu com'
    l = l.replace('www','ccc',1)
    #strip字符串移除函数，移除字符串中制定字符,如果不指定去除两端的空白
    b = '    /t/r/nabasd das asdas asda /t'
    b.strip(' /t/r/na')
    b.lstrip()
    #字符串查找,找到返回索引，没找到返回-1，
    b = '    /t/r/nabasd das asdas asda /t'
    b.find('das')
    #字符串统计有几次
    b.count('da')
    #字符串判断什么开头什么结尾
    b.startswith('t')
    b.endswith('t')
    #字符串is判断
    'isalnum（）->bool'#是否是字母和数字组成
    #isalpha（）是否是字母
    #isdecimal（）是否只包含十进制数字
    #isdigit（）是否全部数字（0～9）
    #isidentifier（）是不是字母和下划线开头，其他都是字母、数字、下划线
    #islower（）是否都是小写
    #isupper（）是否全部大写
    'isspace（）'#是否只包含空白字符
    #字符串格式化
    A = 'aASDASD%03d' % (12) #%03D意思站位3个位置，然后不够就补0
    A = 'aASDASD%03s' % ('asd')
    #字符串精度%.Xf  x代表几位
    c = '%.4f'%1.23333
    #字符串判断
    '''
    字符串.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
    字符串.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。
    字符串.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。
    字符串.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。
    字符串.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。
    字符串.istitle()      所有单词都是首字母大写，为真返回 Ture，否则返回 False。
    字符串.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False
    '''
    #format字符串，｛｝传参,可以变量传参，详细查手册
    c = '{aname}{}:{}'.format('192.168.1.5',444,aname = 'IP地址为')

#切片
def k409():
    s = ('asdasdasdas'[0:5])
    #0-5的字符，然后可以加步长：1
    pass

#




































