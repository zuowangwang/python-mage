#-*- comding:utf-8   -*-

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