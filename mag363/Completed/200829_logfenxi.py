# -*- comding:utf-8   -*-
# 日志分析

def testlongchuant():

    import datetime
    line = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] \
    "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
    "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''
    CHARS = set(' \'"[]')
    # print(CHARS)
    def makekey(line: str):  #切片
        start = 0
        flag = False
        stopchar = ''
        for i, c in enumerate(line):  # [a]
            if c in CHARS:
                if c == '[':
                    flag = True
                    start = i + 1
                if c == ']':
                    flag = False
                if c == '"':
                    flag = not flag
                    if flag:
                        start = i + 1
                if flag:
                    continue
                if start == i:
                    start = i + 1
                    continue
                yield line[start:i]
                start = i + 1
        else:
            if start < len(line):
                yield line[start:]
    print(list(makekey(line)))

    names = ('remote', '', '', 'datetime', 'request','status', 'length', '', 'useragent')

    ops = (None, None, None, lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
        lambda request: dict(zip(['method', 'url', 'protocol'], request.split())),
        int, int, None, None)


    def extract(line: str):
        return dict(
            map(
                lambda item: (item[0], item[2](item[1]) if item[2] is not None else item[1]),
                zip(names, makekey(line), ops)
                )
            )


    print(extract(line))






import datetime
import re
line = '''183.60.212.153 - - [19/Feb/2019:10:23:29 +0800] \
"GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" \
"Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

ops = {
 'datetime': lambda timestr: datetime.datetime.strptime(timestr, '%d/%b/%Y:%H:%M:%S %z'),
 'status': int,
 'length': int
}

pattern = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] \
"(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/\d.]+)" \
(?P<status>\d+) (?P<length>\d+) .+ "(?P<useragent>.+)"'''



def extract(line:str) -> dict:   #正则分组取值，本身是一个元组，有分组和对应的值，然后重新构建一个字典，替换k，如果没有不替换
    regex = re.compile(pattern)
    matcher = regex.match(line)
    # print(matcher.groupdict().items())
    if matcher:
        return {k:ops.get(k, lambda x:x)(v) for k,v in matcher.groupdict().items()}
    else:
        return 'eeror'
        
# print(extract(line))


def load(filename:str):  #寻找读取日志中的，正则取值
    with open(filename, encoding='utf-8') as f:
        for line in f:
            # print(line)
            # print(type(line))
            # print(extract(line))
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                print('No match.{}'.format(fields))

for x in load(r'E:\python-mage\mag363\test.log'):
    print(x)

