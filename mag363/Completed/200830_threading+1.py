# -*- comding:utf-8   -*-


#创建多个数据源，然后多个消费者分发处理消息
import random,time,datetime
from queue import Queue
import threading,time
##1 创建一个日志生产者
def source(seconds = 1):
    while True:
        yield {'datetime':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
        'value':random.randint(1,100)}
        time.sleep(seconds)

s = source()

def handler(iterable):
    return sum(map(lambda item:item['value'], iterable)) / len(iterable)

##2 创建一个日志消费者，进行消费
def window(q:Queue, handler, width:int, interval:int):
    """
    窗口函数
    :param iterator: 数据源，生成器，用来拿数据
    :param handler: 数据处理函数
    :param width: 时间窗口宽度，秒
    :param interval: 处理时间间隔，秒
    """
    start = datetime.datetime.strptime('20190101 000000 +0800', '%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20190101 010000 +0800', '%Y%m%d %H%M%S %z')
    buffer = [] 
    delta = datetime.timedelta(seconds=width-interval)
    while True:
        data = q.get(timeout=10) #创建了一个消费者，等待数据，有数据就消费，没有就等待，一旦执行会一直等待
        if data:
            buffer.append(data) 
            current = data['datetime']
        print(start,current)
        print((current - start).total_seconds())
        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print('{:.2f}'.format(ret)) 
            print(threading.current_thread())
            print('~~'*10)
            start = current
            buffer = [x for x in buffer if x['datetime'] > current - delta]
# window(source(), handler, 10, 5)



#3 数据分发到不同线程运行，创建多个数据源，然后多个消费者消费
def dispatcher(src):
    handlers = []
    queues = []

    def reg( handler, width:int, interval:int):
        q = Queue()
        t = threading.Thread(target=window, args=(q, handler, width, interval))
    
        #创建一个数据列表，q，然后把它存到数据集合里面
        #创建一个消费者t，然后把它存到数据集合里面

        queues.append(q)
        handlers.append(t)

    def run():
        for t in handlers:  #从消费者列表里面拿到一个消费者运行起来
            t.start()
        
        while True:
            data = next(src)
            for q in queues:  #从数据集合里面拿到不同的数据列表，分别给他们存数据，一人一个循环
                q.put(data)
    
    return reg, run

reg, run = dispatcher(s)

reg(handler, 10, 5)
reg(handler, 10, 5)

print(threading.current_thread())
run()














