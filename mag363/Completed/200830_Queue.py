# -*- comding:utf-8   -*-

#大型系统可以使用第三方消息中间件：RabbitMQ、RocketMQ、Kafka

def testqueue():
    # queue模块提供了一个先进先出的队列Queue。
    # queue.Queue(maxsize=0) 
    # 创建FIFO队列，返回Queue对象。
    # maxsize 小于等于0，队列长度没有限制。
    # Queue.get(block=True, timeout=None) 
    # 从队列中移除元素并返回这个元素。
    # block 为 阻塞，timeout为超时。
    # 如果block为True，是阻塞，timeout为None就是一直阻塞。
    # 如果block为True但是timeout有值，就阻塞到一定秒数抛出Empty异常。
    # block为False，是非阻塞，timeout将被忽略，要么成功返回一个元素，要么抛出empty异常。
    # Queue.get_nowait() 
    # 等价于 get(False)，也就是说要么成功返回一个元素，要么抛出empty异常。
    # 但是queue的这种阻塞效果，需要多线程的时候演示。
    # Queue.put(item, block=True, timeout=None) 
    # 把一个元素加入到队列中去。
    # block=True，timeout=None，一直阻塞直至有空位放元素。
    # block=True，timeout=5，阻塞5秒就抛出Full异常。
    # block=False，timeout失效，立即返回，能塞进去就塞，不能则返回抛出Full异常。
    # Queue.put_nowait(item) 
    # 等价于 put(item, False)，也就是能塞进去就塞，不能则返回抛出Full异常。


    from queue import Queue
    q = Queue(5)   #可以给个队列上限，参数，预设

    print(q.empty()) #判断队列有没有数据，如果空为True
    print(q.full()) #判断队列有没有达到上限，如果没有为False

    q.put(1)  #提交数据
    q.put([1,2,3])
    c = [6,7]
    q.put(c)

    print(q.empty())  #如果有数据，为False
    print(q.full()) #如果达到了上限为True
    print(q.qsize())  #判读列表里面有几个数据

    # print(q.get())  #获取数据
    # print(q.get())
    # print(q.get())


    # print(q.get(timeout=5))  #如果没有数据会阻塞，卡主，所以需要加一个时间，超时抛出异常
    # print(q.get(False))  #如果没有数据，立即返回错误
    # print(q.get(True, 5))  #等5秒



    while True:
        a = input("<<<<<")
        # print(q.full())
        if not q.full():  #如果没有达到上线就继续添加
            q.put_nowait(a)
        else:     #如果达到上限就开始消费
            while not q.empty():   #如果不为空，则一直消费
                print(q.get())












