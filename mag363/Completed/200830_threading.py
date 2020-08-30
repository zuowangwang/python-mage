# -*- comding:utf-8   -*-
#创建一个线程，单独运行

import threading,time

def add(x,y):
    # print('enteringthis thread')
    # time.sleep(3)
    # print(x+y)

    while True:
        cmd = input('<<<<')
        if cmd == 'quit':
            break

t = threading.Thread(target=add, args=(4,5))  #线程对象，运行函数是什么，要传这个函数什么数据
t.start()


print('123')   #创建的线程会等主线程先运行，然后才会运行子线程











