# -*- comding:utf-8   -*-
##  定时查看日志，然后计算日志中的数据
import random,time,datetime

def source(seconds = 1):
    while True:
        yield {'datetime':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
         'value':random.randint(1,100)}
        time.sleep(seconds)

s = source()
# items = [next(s) for _ in range(3)]

# print(items)
def handler(iterable):
    return sum(map(lambda item:item['value'], iterable)) / len(iterable)

# print("{:.2f}".format(handler(items)))


def window(iterator, handler, width:int, interval:int):
    """
    窗口函数
    :param iterator: 数据源，生成器，用来拿数据
    :param handler: 数据处理函数
    :param width: 时间窗口宽度，秒
    :param interval: 处理时间间隔，秒
    """
    start = datetime.datetime.strptime('20190101 000000 +0800', '%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20190101 010000 +0800', '%Y%m%d %H%M%S %z')
    buffer = [] # 窗口中的待计算数据
    delta = datetime.timedelta(seconds=width-interval)
    while True:
    # 从数据源获取数据
        data = next(iterator)
        if data:
            buffer.append(data) # 存入临时缓冲等待计算
            current = data['datetime']
            # 每隔interval计算buffer中的数据一次
        # print(start ,current)
        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            for i in buffer:  #打印目前数据库内有什么数据
                print(i)
            print('~~~'*10)
            print('{:.2f}'.format(ret))  #打印handler函数执行的结果，判断的是value值的平均
            start = current
            # 清除超出width的数据
            buffer = [x for x in buffer if x['datetime'] > current - delta]
            for i in buffer:   #查看清除之后，的数据还有有没以前的数据
                print(i)
            print('***'*10)

window(source(), handler, 10, 5)













