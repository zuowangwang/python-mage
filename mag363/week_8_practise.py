#-*- comding:utf-8   -*-



#有一个配置文件test.ini内容如下，将其转换成json格式文件
'''
[DEFAULT]
a = test
[mysql]
default-character-set=utf8
a = 1000
[mysqld]
datadir =/dbserver/data
port = 33060
character-set-server=utf8
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
'''

def  ini_json_z():
     from configparser import ConfigParser
     import json
     filename = 'test1.ini'
     jsonname = 'test.json'

     cfg = ConfigParser()
     cfg.read(filename)
     dest = {}
     for sect in cfg.sections():
          print(sect, cfg.items(sect))
          dest[sect] = dict(cfg.items(sect))
     json.dump(dest, open(jsonname, 'w'))


def sys_z():#获取运行参数
     import sys
     for i in sys.argv: #sys.argv是一个列表，第一个是文件名，之后依次是参数列表
          print(i)

     #E:/python-mage/mag363/week_8_practise.py 123


def ls_z():
    import argparse
    import stat
    from pathlib import Path
    from datetime import datetime
    # 获得一个参数解析器
    parser = argparse.ArgumentParser(prog='ls', description='list directory contents', add_help=False)
    parser.add_argument('path', nargs='?', default='.', help="directory") # 位置参数，可有可无，缺省值，帮助
    parser.add_argument('-l', action='store_true', help='use a long listing format')
    parser.add_argument('-a', '--all', action='store_true', help='show all files, do not ignore entries starting with .')
    parser.add_argument('-h', '--human-readable', action='store_true', help='with -l, print sizes in human readable format')

    def listdir(path, all=False, detail=False, human=False):
         def _gethuman(size: int):
               units = ' KMGTP'
               depth = 0
               while size>=1000:
                    size = size // 1000
                    depth += 1
               return '{}{}'.format(size, units[depth])
         def _listdir(path, all=False, detail=False, human=False):
              """详细列出本目录"""
              p = Path(path)
              for i in p.iterdir():
                    if not all and i.name.startswith('.'): # 不显示隐藏文件
                        continue
                    if not detail:
                        yield (i.name,)
                    else: # -l
                    # -rw-rw-r-- 1 python python 5 Oct 25 00:07 test4
                    # mode 硬链接 属主 属组 字节 时间 name
                         st = i.stat()
                         mode = stat.filemode(st.st_mode)
                         atime = datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                         size = str(st.st_size) if not human else _gethuman(st.st_size)
                         yield (mode, st.st_nlink, st.st_uid, st.st_gid, size, atime, i.name)
          # 排序
         yield from sorted(_listdir(path, all, detail, human), key=lambda x: x[len(x) - 1])

    if __name__ == '__main__':
     args = parser.parse_args() # 分析参数，同时传入可迭代的参数
     print(args) # 打印名词空间中收集的参数
     # parser.print_help() # 打印帮助
     files = listdir(args.path, args.all, args.l, args.human_readable)
     # print(list(files))
    for i in list(files):
        print(i)




def p_r_tree(array, unit_width=2):
    import math
    length = len(array)
    index = 1
    depth = math.ceil(math.log2((length)))
    sep = ' ' * unit_width
    for i in range(depth-1,-1,-1):
        pre = 2 ** i -1
        print(sep * pre, end='')
        offset = 2 ** (depth -i -1)
        line = array[index: index+offset]
        intervalspace = sep * (2 * pre + 1)
        print(intervalspace.join(map(str,line)))

    # pr_tree([0,30,20,80,40,50,10,60,70,90,22])
    # pr_tree([0,30,20,80,40,50,10,60,70,90,22,33,44,55,66,77])
    # pr_tree([0,30,20,80,40,50,10,60,70,90,22,33,44,55,66,77,88,99,11])





def zz_z():
    ''' 正则学习 '''
    import re
    #findall  匹配一个列表
    #search,match   匹配一次之后就不匹配了match类型，search匹配有很多正则比较好
    s = '13978962341asdad1497896232212313asdad  0123-67823456  very very vary 192.168.213.123'

    n = re.findall(r'1\d{10}', s )
    print("正则取出来的值：",n , "他的格式:", type(n))
    print('取列表第一个：',n[0], type(n[0]))

    print('--'*10)

    b = re.search(r'1\d{10}', s)   #1开头，后面10位
    print("正则取出来的值：", b ,"他的格式:", type(b))
    print('只取一次：', b.group(),type(b.group()))

    print('--' * 10)
    m = re.findall(r'\d{3,4}-\d{7,8}', s)   #前面3-4位数字，后面7-8位数字
    print(m)

    print('--' * 10)
    w = re.findall(r'(14|13)\d{9}', s)  #['13', '14']
    w1 = re.search(r'(14|19)\d{9}', s)  #<_sre.SRE_Match object; span=(16, 27), match='14978962322'>
    w2 = re.match(r'(14|19)\d{9}', s)
    print(w,w1,w2)

    print('--' * 10)
    m  = re.findall(r'(very)\s+\1', s) #['very']
    m1 = re.search(r'(very)\s+\1', s) #<_sre.SRE_Match object; span=(54, 63), match='very very'>
    m2 = re.match(r'(very)\s+\1', s)
    print(m,m1,m2)

    print('--' * 10)
    m = re.findall(r'1\d{10}(?=123)', s)  #断言，判断后面一定有123
    print(m)

    print('--' * 10)
    m = re.findall(r'(?:(\d{1,3}).){3}(\d{1,3})', s)
    m1 = re.search(r'(?:(\d{1,3}).){3}(\d{1,3})', s)
    m2 = re.match(r'(very)\s+\1', s)
    print(m)
    print(m1)


zz_z()




















