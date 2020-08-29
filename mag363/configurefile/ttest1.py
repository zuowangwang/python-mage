#-*- comding:utf-8   -*-


# __all__ = ['z','_z']

class zuo():
    def zuo1(self):
        print(11111111)

c = 'sss'
z = 1
_z = 2
_r = 3
_t = 4

#这是一个运行模块
if __name__ == '__main__':
    print('in main ,主模块时候运行这里的代码','我的模块名字',__name__)

else:
    print('其他模块调用时候运行这里','我的模块名字',__name__)
    zuo().zuo1()