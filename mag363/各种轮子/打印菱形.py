#-*- comding:utf-8   -*-

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
