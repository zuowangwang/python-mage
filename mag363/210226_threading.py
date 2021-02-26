# -*- comding:utf-8   -*-





# 线程
# 就绪(Ready)
# 运行(Running)
# 阻塞(Blocked)
# 终止(Terminated)



# import  threading
# import time
# #
# def worker(n,y):
#     time.sleep(5)
#     print('i m working')
#     print('finish')
#     print(n)
#     print(y)
#
# # def worker(): #循环执行
# #     while True:
# #         print('i m working')
# #         print('finish')
#
# # def worker(n): #结束
# #     count = 0
# #     while True:
# #         print('i m working')
# #         print('finish')
# #         count += 1
# #         if (count > n):
# #                 raise Exception('Thread error')  #异常结束
# #                 break #跳出循环
# #                 retunrn #返回值跳出循环
#
# t = threading.Thread(target=worker, name='worker1',args=(5,), kwargs= {'y':100 })
# #args  元组
# #kwargs  字典
# t.start()
#
# time.sleep(10)
# print('=====end=====') #此线程要等子线程结束后，才能运行


# import threading
# import time
#
# def showthreadinfo():
#      print("currentthread = {}".format(threading.current_thread()))  #返回当前线程对象
#      print("main thread = {}".format(threading.main_thread()))    #返回主线程对象
#      print("acive count = {}".format(threading.active_count()))  #当前处于alive状态的线程个数
#
#
# def worker():
#     count = 0
#     showthreadinfo()
#     while True:
#         if (count > 5):
#             break
#         time.sleep(1)
#         count += 1
#         print("I'm working")
#
# t = threading.Thread(target=worker, name='worker1') # 线程对象
# showthreadinfo()
# t.start() # 启动
# # t.is_alive() #判断线程是否是活动状态
#
# print('==End==')  #线程都是并行运行的
# print('==End==')
# print('==End==')
# print('==End==')
# print('==End==')


# t.start() # #当次线程停止运行后
# t.start() # 不能重新启动，需要创建新的线程，会报once错误




# import threading
# import time
# def worker():
#      count = 0
#      while True:
#          if (count > 5):
#              break
#          time.sleep(1)
#          count += 1
#          print('worker running')
#
# class MyThread(threading.Thread):
#      def start(self):
#         print('start~~~~~~~~~~~~~')
#         super().start()  #调用父类函数
#      def run(self):
#         print('run~~~~~~~~~~~~~')
#         super().run()
#
# t = MyThread(name='worker', target=worker)
# # t.start()
# t.run()
# print('123')

# t.start()  #会运行本身线程，和子线程，两个线程同步运行，多线程运行
# t.run()   #run 方法是运行线程，单线程运行






# import threading
# import time
#
#
# def worker():
#      count = 0
#      while True:
#          if (count > 5):
#             break
#          time.sleep(0.5)
#          count += 1
#          print('worker running')
#          print(threading.current_thread().name, threading.current_thread().ident)
#
# class MyThread(threading.Thread):
#      def start(self):
#          print('start~~~~~~~~~~~~~')
#          super().start()
#      def run(self):
#          print('run~~~~~~~~~~~~~')
#          super().run() # 看看父类再做什么
#
# t1 = MyThread(name='worker1', target=worker)
# t2 = MyThread(name='worker2', target=worker)
#
# t1.start()
# t2.start()#进程内有多个活动的线程并行的工作，就是多线程
#
# # t1.run()
# # t2.run()#这个线程就是主线程。一个进程至少有一个主线程。其他线程称为工作线程。
#
# print('=======end==========')




# import threading
# def worker():
#      for x in range(100):
#         print("{} is running.\n".format(threading.current_thread().name), end='')
# for x in range(1, 5):
#      name = "worker{}".format(x)
#      t = threading.Thread(name=name, target=worker)
#      t.start()
#

#不安全的print函数，所以不要换行，自己换行



# import threading
# import logging
#
# def worker():
#      for x in range(100):
#          #print("{} is running.\n".format(threading.current_thread().name), end='')
#          logging.warning("{} is running.".format(threading.current_thread().name))
# for x in range(1, 5):
#      name = "worker{}".format(x)
#      t = threading.Thread(name=name, target=worker)
#      t.start()


#不安全的print函数,使用loggin日志函数，线程安全



# import time
# import threading
# def bar():
#
#      time.sleep(10)
#      print('bar')
#
# def foo():
#      for i in range(20):
#          print(i)
#
# t = threading.Thread(target=bar, daemon=False)
# t.start()
# # 主线程是non-daemon线程
#
# t = threading.Thread(target=foo, daemon=True)
# t.start()
#
# print('Main Thread Exiting')

#daemon=True   则表示，主线程结束就结束，不会等子线程/工作线程
#如果全部都是false，也直接退出，如果都是True，等待
#如果一个false，一个true，则等待True结束后结束
#所有主线程结束的时候会检查一遍没有True 如果没有就结束


























