# -*- comding:utf-8   -*-



import bisect
lst = [37, 99, 73, 48, 47, 40, 40, 25, 99, 51, 100]
newlst = sorted(lst) # 升序
print(newlst) # [25, 37, 40, 40, 47, 48, 51, 73, 99, 99, 100]
print(list(enumerate(newlst)))
print(20, bisect.bisect(newlst, 20)) #插入处的素引，重复值的时候推右插入
print(newlst)
print(30, bisect.bisect_left(newlst, 30))# 重复值的时候推左插入
print(newlst)
print(40, bisect.bisect_right(newlst, 40))#插入处的素引，重复值的时候靠右插入
print(newlst)
print(20, bisect.insort_left(newlst, 20))# inplace就地修改
print(newlst)
print('~~~~~')
for x in (20, 30, 40, 100):
     bisect.insort_left(newlst, x)   #
     print(newlst)

# 函数可以分2类：
# bisect系，用于查找index。
# Insort系，用于实际插入。
# 默认重复时从右边插入。

import bisect
def get_grade(socre):
     breakpoints = [60, 70, 80, 90]
     grades = 'EDCBA'
     return grades[bisect.bisect(breakpoints,socre)]

print(get_grade(89))

#可以查找某个数值，在一个数值的排序，前提这个数值是有序的
#可以查找某个值在第几位
#可以查找第几位是什么值

#121级




















