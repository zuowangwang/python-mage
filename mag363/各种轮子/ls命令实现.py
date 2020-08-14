#-*- comding:utf-8   -*-


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