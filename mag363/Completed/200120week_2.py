#-*- comding:utf-8   -*-
import os
#第一个小练习，折半查找   22视频  50分钟
def k1 ():
    a = int(input('请输入数字a:'))
    b = int(input('请输入数字b:'))

    def pk(a):
        if a >= 1000:
            if a >= 10000:
                print('这是一个5位数')
            else:
                print('这是一个4位数')
        else:
            if a >= 100:
                print('这是一个3位数')
            elif a >= 10:
                print('这是一个2位数')
            else:
                print('这是一个1位数')

    if a > b:
        print(a)
        pk(a)
    elif b > a:
        print(b)
        pk(b)

#第二个小练习，  23视频  1分钟，给定一个正整数，判断该数的位数，依次打印每个位置的的数字
def k2 ():
    x = input('请输入一个数字：')
    n = x.count('', 1)
    print('这是一个%s位数' % n)
    w = 10 ** (n - 1)
    x = int(x)
    print('从高位依次打印到个位')
    for i in range(n):
        print(x // w)
        x = x % w  # 去除对应位置
        w = w // 10  # 再除以10

#第三个小练习，24  正方形打印
def k3 ():
    n = int(input(">>>"))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1 or i == n or j == n:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

    n = int(input(">>>"))
    print('*' * n)
    a = n - 2
    while a:
        print('*' + ' ' * (n - 2) + '*')
        a -= 1
    print('*' * n)

    n = 4
    for i in range(n):
        if i % n == 0:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

    n = int(input(">>>"))
    e = -(n // 2)
    for i in range(e, n + e):
        if i == e or i == n + e - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

#第四小练习  100内奇数和
def k4 ():
    s = 0
    for i in range(2 ,101 , 2):
            s += i
    print(s)

#阶乘 25
def k5 ():
    n = 5
    s = 0
    value = 1
    for i in range(1,n+1):
        value *= i
        s += value
        print(value,s)
    print(s)

#判断一个数是否素数,曾称质数。一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数。如2，3，5，7，11，13，17
def k6 ():

    x = 19777
    for i in range(2 ,x):
        if x % i == 0:
            print(x , 'is not a prime number')
            break
    else:
        print(x , 'is a prime mumber')

#打印九九乘法表
def k7 ():
    n = 9
    for i in range(1,n+1):
        for j in range(1,i+1):
            product = j*i
            if j>1 and product < 10:
                product = str(product) + ' '
            else:
                product = str(product)
            print(str(j) + '*'+ str(i) + '='+ product,end=' ')
            #print(str(j) + '*'+ str(i) + '='+ product,end=' ' + '\t')#利用\t自动补全
            #print('{}*{}={}\t'.format(j,i,j*i),end=' ')  #利用format传参
            line = ''
            line += ('{}*{}={:<{}}'.format(j,i,j*i,2 if j<2 else 3))
        print(line)
        print('{:<66}.format(line)')
        print('')

    #反着来 ,打印一个反的99表
    n = 9
    unit = ' ' * 7
    for i in range(1,n+1):
        print(unit * (i-1),end = '')
        for j in range(i,n+1):
            print('{}*{}={:<{}}'.format(i,j,j*i,2 if j<2 else 3),end='')
            print(' ',end='') if i==1 and j ==1 else  print('',end='')
            # if i == 1 and j == 1:
            #     print(' ', end='')
            # else :
            #     pass
            print()
            line = ''
            line += ('{}*{}={:<{}}'.format(j,i,j*i,2 if j<2 else 3))
        print('{:>66}.format(line)')

#打印菱形
def k8 ():
    # 第一种方法
    n = 13
    s = n//2
    for z in range(1,s+1):
        a = 1 + ((z - 1) * 2)
        print(' '*s + '*'*a + ''*s)
        s-=1
    print('*'*n)
    s = n//2
    c = 1
    for z in range(s,0,-1):
        a = 1 + ((z - 1)*2)
        print(' ' * c + '*' * a + '' * c)
        c+=1

    #第二种方法
    e = 7//2
    for i in range(-e,e+1):
        if i < 0:
            x = -i
        else:
            x = i
        print(x * ' ' + (7-2*x) * '*', i,x , 2*x)

#打印100以内的斐波那契数列  fib

def k9 ():
    a = 0
    b = 1
    #必须要给出两项
    while True:
        c = a + b
        if c > 100:
            break
        else:
            pass
        print(c)
        a = b
        b = c

#求斐波那契数列第101项
'''
a = 0
b = 1
index = 2
#必须要给出两项
while True:
    c = a + b
    a = b
    b = c
    print(index, c)
    if index == 101:
        break
    else:
        pass
        index +=1
'''

#求100内的所有素数
'''
n = 100
for i in range(3,n+1,2):
    if i > 10 and i % 5 ==0:
        continue
    for j in range(3 ,int(i**0.5)+1,2):
        if i % j == 0:
            # print(i , 'is not a prime number')
            break
    else:
        count *= 1
        print(i , 'is a prime mumber')
print(count)
'''

#正反renge打印一个数字
'''
for i in range(1,5):
    print(i,end=' ')   #= 1234
print('')
for i in range(4,0,-1):
    print(i,end=' ')  # = 4321
'''

#list 列表查询
'''
a = [87, 'asd', 2, 3, 5]
# print(a[0])  #='87' 0是第一位
# print(a[-1]) #=4   从最后开始

if a.count(5) > 0:
    c = a.index(5)  #找元素的索引号      
    print(a[c])
else:
    print('列表里面没有5这个元素')

print(len(a))
'''

#list  列表修改
'''
a = [87, 'asd', 2, 3, 5]
a[1] = 'gggg'  #修改制定的元素
print(a) #[87, 'gggg', 2, 3, 5]

a.append('99') #尾部插入一个元素
print(a)#[87, 'gggg', 2, 3, 5, '99']

a.insert(1,'65') #制定位置插入一个，元素的索引自动增加
print(a)#[87, '65', 'gggg', 2, 3, 5, '99']

print(len(a))#原本5，现在7

a.extend([1,2,3,4,5]) #把另外一个列表加入到本列表尾部,变量不变
print(a) #[87, '65', 'gggg', 2, 3, 5, '99', 1, 2, 3, 4, 5]

# a + a  , a * 2 列表  都要重新定义列表，是一个新的列表
p = list(range(5))+[99,98,97]
print(p)

'''

#三元表达式
'''
a =1
b =2
if  a>b:
    print(a)
else:
    print(b)
print(a) if a>b else print(b)
'''

#字符串格式化传参函数
'''
' '.format  字符串传参函数
'asdasda{}sdasd{}asd'.format('bbb','ccc')
{}代表需要传参的的地方，默认0开始。这个是0，1，位置分别传参
{} 里面可以｛:<4｝ 向左靠其，站4个位置
'''

#打印对顶三角形
'''
e = 7//2
for  i  in range(-e,e+1):
    x = -i if i<0 else i
    print(' '*(e-x) +'*' * (2*x+1))
'''

#打印闪电
'''
a = 11
e = a//2
char = '~'
for  i  in range(-e,e+1):
    if i<0:
        print(' '*(-i) + char * (e+1+i))
    elif i>0:
        print(' '*e + char*(e+1-i))
    else:
        print(char * a)
'''

#比较算法时间对比
'''
import  datetime

n = 100000
delta = [0,0]
count = [0,1]

start = datetime.datetime.now()
#代码
for i in range(2,n):
    for j in range(2 ,int(i**0.5)+1):
        if i % j == 0:
            # print(i , 'is not a prime number')
            break
    else:
        count[0] += 1
        # print(i , 'is a prime mumber')
delta[0] = (datetime.datetime.now() - start).total_seconds()


start = datetime.datetime.now()
#代码
for i in range(3,n,2):
    if i > 10 and i % 5 == 0:
        continue
    for j in range(3 ,int(i**0.5)+1,2):
        if i % j == 0:
            # print(i , 'is not a prime number')
            break
    else:
        count[1] += 1
        # print(i , 'is a prime mumber')
delta[1] = (datetime.datetime.now() - start).total_seconds()

print(count)
print(delta)
print(delta[0] - delta[1] )

'''









