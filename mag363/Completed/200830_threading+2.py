# -*- comding:utf-8   -*-
#完整的代码，合在一起，日志处理，然后消费者，然后分发处理，多线程
import datetime,re,threading,random,time
from queue import Queue
from pathlib import Path


#数据格式整理
ops = {
 'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
 'status': int,
 'length': int
}
#正则表达式，分组
pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] \
"(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/\d.]+)" \
(?P<status>\d+) (?P<length>\d+) .+ "(?P<useragent>.+)"'''

#从把日志修改为想要的数据列表
def extract(line:str) -> dict:   #正则分组取值，本身是一个元组，有分组和对应的值，然后重新构建一个字典，替换k，如果没有不替换
    regex = re.compile(pattern)
    matcher = regex.match(line)
    # print(matcher.groupdict().items())
    if matcher:
        return {k:ops.get(k, lambda x:x)(v) for k,v in matcher.groupdict().items()}
    else:
        return 'eeror'

#实际数据从日志中读取数据源
def loadfile(filename:str,encoding='utf-8'):  #寻找读取日志中的，正则取值
    with open(filename, encoding=encoding) as f:
        for line in f:
            time.sleep(0.5)
            fields = extract(line)
            if isinstance(fields, (dict,)): #转换成需要的格式
                yield fields
            else:
                print('No match.{}'.format(fields))

#遍历日志文件
def load(*paths,encoding='utf-8', ext='*.log',r=False):
    for p in paths:
        path = Path(p)
        if path.is_dir(): #如果路径是文件夹，就查找路径下的文件，然后读取
            if isinstance(ext, str): 
                ext = [ext] #如果不是列表，就转成列表，考虑用户，是否需要不同的日志文件,ext=('*.log','*.txt')
            for e in ext:
                logs = path.rglob(e) if r else path.glob(e) #遍历当前目录下，所有需要的文件,默认不遍历目录下面目录，如果需要遍历开启True
                # print(list(logs)) #如果执行了，此列迭代器就失效了，下面就不执行了
                for log in logs:
                    yield from loadfile(str(log.absolute()),encoding=encoding)#路径更新为绝对路径

                    # for x in loadfile(str(log.absolute())):
                    #     yield x
                        
        elif path.is_file(): #如果路径是文件，直接读取
            yield from  loadfile(str(path.absolute()),encoding=encoding)

#模拟测试的数据源
def source(seconds = 1):
    while True:
        yield {'datetime':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
        'value':random.randint(1,100)}
        time.sleep(seconds)


def status_handler(iterable):
 # 时间窗口内的一批数据
    status = {}
    for item in iterable:
        key = item['status']  #获取里面的值
        status[key] = status.get(key, 0) + 1  #增加对应的v，每次新增
        #同理
    for item in iterable:
        key = item['method']
        # print(key)
        status[key] = status.get(key, 0) + 1
    total = len(iterable) #统计当前传进来的数据有多少
    
    return {k:status[k]/total for k,v in status.items()}#替换status字典里面的v，判断占比

##创建一个日志消费者，进行消费
def window(q:Queue, handler, width:int, interval:int):
    start = datetime.datetime.strptime('20190101 000000 +0800', '%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20200101 010000 +0800', '%Y%m%d %H%M%S %z')
    buffer = [] 
    delta = datetime.timedelta(seconds=width-interval)
    while True:
        data = q.get(timeout=10) #创建了一个消费者，等待数据，有数据就消费，没有就等待，一旦执行会一直等待,10秒
        
        if data:
            # print(data)
            buffer.append(data) 
            current = data['datetime']
            
            # print(start)
            # print(123)
            # print(current)
            # print(len(buffer))
            # print((current - start).total_seconds())
            # print(interval)
        if (current - start).total_seconds() >= interval:  #要注意时间问题，时间5秒时间能有很多数据，如果时间一直改变，会一直生成数据
            ret = handler(buffer)
            # print('{:.2f}'.format(ret)) 
            print(ret)
            print(threading.current_thread())
            print('~~'*10)
            start = current
            buffer = [x for x in buffer if x['datetime'] > current - delta]
# window(source(), handler, 10, 5)



#数据分发到不同线程运行，创建多个数据源，然后多个消费者消费
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


if __name__ == "__main__":
    
    
    path = r'E:\python-mage\mag363\configurefile\test.log' #实际日志的数据源
    reg, run = dispatcher(load(path))
    reg(status_handler, 10, 5)
    print(threading.current_thread())
    run()

   
# import sys
# path = sys.argv[1]
# print(path)









