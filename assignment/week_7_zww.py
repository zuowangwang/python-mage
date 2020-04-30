#-*- comding:utf-8   -*-
# 第七周作业
# P22第七周（7.8-7.9）学习安排及作业内容：
# 请同学们至少完成腾讯课堂如下学习章节：
# 【一：章节学习】
# 20、Python文件IO(一)文件操作：
#         1、文件编码；
#         2、文件的模式；
#         3、文件指针操作；
#         4、缓冲区；
#         5、文件对象的读写方法
#         6、上下文管理
# 21、 Python文件IO(二)路径操作：
#         1、习题base64解码；
#         2、习题命令分发器、copy和单词统计；
#         3、StringIO和BytesIO和os.path；
#         4、Path对象基本操作
#         5、通配和文件操作
# 22、Python文件IO(三)   高级文件操作和序列化：
#         1、shutil模块使用；
#         2、csv模块使用；
#         3、ini文件操作；
#         4、序列化和反序列化及pickle；
#         5、msgpack使用
# 【二：本周作业】请同学们于下周天晚上10点前，将作业上传至GitHub；
# 1. 优化ATM作业(改写成函数的方法)
# 2.使用正则序列化。
#     text = 'foo = 23 + 42 * 10'
#     将字符串像下面这样转换为序列对：
#      tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
#           ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]


import re

"""
使用正则序列化。
    text = 'foo = 23 + 42 * 10'
    将字符串像下面这样转换为序列对：
     tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
"""


def tokenize(code):
    tokens = []
    token_specification = [
        ('NAME', r'[a-z]+\w*'),
        ('EQ', r'='),
        ('NUM', r'\d+'),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('TIMES', r'\*'),
        ('NEWLINE', r'\n'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            if mo.end() == 1:
                continue
            yield tokens
            tokens = []
        else:
            tokens.append((kind, value))
            if mo.end() == len(code):
                yield tokens


text = '''
foo = 23 + 42 * 10 
foo1 = 23 - 214 + 800
f =  42 * 10 + 23 
'''
for token in tokenize(text):
    print(token)

text = 'foo = 23 + 42 * 10'
for token in tokenize(text):
    print(token)


"""
写的很棒~
"""





# '''
# 使用正则序列化。
#     text = 'foo = 23 + 42 * 10'
# 将字符串像下面这样转换为序列对：
#     tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
#           ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
# '''
#
# import re
#
# # 定义正则匹配元字符
# tokens_list = [('NAME', '[a-zA-Z]+'),
#                ('EQ', '\='),
#                ('NUM', '\d+'),
#                ('PLUS', '\+'),
#                ('TIMES', '\*')
#               ]
#
# # 定义测试字符串
# text = '''foo = 23 + 42 * 10,
#           bar = 50 * 2 + 3,
#           test = 0.62 + -3 + 10000    # 不支持
#        '''
#
# # 正则表达式，使用|连接，表示匹配每个|左边或者右边的正则表达式，re.M表示采用多行匹配模式
# reg_patterns = re.compile('|'.join(r'(?P<%s>%s)' % pattern for pattern in tokens_list), re.M)
#
# # 搜索字符串，返回一个顺序访问每一个Match对象的迭代器
# for reg_pattern in re.finditer(reg_patterns, text):
#     # 打印序列对
#     print([(reg_pattern.lastgroup, reg_pattern.group())], end=',')
#
# """
# 主要考点是 "|" 的用法
# """