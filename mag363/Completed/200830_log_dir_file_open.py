# -*- comding:utf-8   -*-
from pathlib import Path


def load(*paths, encoding='utf-8', ext='*.log', r=False):
    for p in paths:
        path = Path(p)
        if path.is_dir():  # 如果路径是文件夹，就查找路径下的文件，然后读取
            if isinstance(ext, str):
                # 如果不是列表，就转成列表，考虑用户，是否需要不同的日志文件,ext=('*.log','*.txt')
                ext = [ext]
            for e in ext:
                # 遍历当前目录下，所有需要的文件,默认不遍历目录下面目录，如果需要遍历开启True
                logs = path.rglob(e) if r else path.glob(e)
                # print(list(logs)) #如果执行了，此列迭代器就失效了，下面就不执行了
                for log in logs:
                    print(log)
                    with log.open(encoding=encoding) as f:
                        for line in f:
                            print(line)

        elif path.is_file():  # 如果路径是文件，直接读取
            with open(path, encoding=encoding) as f:
                for line in f:
                    print(line)


# load(r'.\mag363\configurefile')
load(r'.\mag363\configurefile\test.log')
