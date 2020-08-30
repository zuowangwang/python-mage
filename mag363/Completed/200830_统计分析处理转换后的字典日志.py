# -*- comding:utf-8   -*-



ss = [{'remote': '183.60.212.153', 
'datetime': 'datetime.datetime(2019, 2, 19, 10, 23, 29, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))', 
'method': 'GET', 
'url': '/o2o/media.html?menu=3', 
'protocol': 'HTTP/1.1', 
'status': 200, 
'length': 16691, 
'useragent': 'Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)'},
{'status': 200,'method': 'GET'},
{'status': 200,'method': 'GET'},
{'status': 300,'method': 'GET'},
{'status': 200,'method': 'GET'},
{'status': 300,'method': 'GET'},
{'status': 200,'method': 'GET'},
{'status': 500,'method': 'GET'}
]



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
    return {k:status[k]/total for k,v in status.items()} #替换status字典里面的v，判断占比

print(status_handler(ss))












