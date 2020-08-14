#-*- comding:utf-8   -*-
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

k3()