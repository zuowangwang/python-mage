# -*- comding:utf-8   -*-


# 1、随机整数生成类
# 可以指定一批生成的个数，可以指定数值的范围
# 常规实现如下
#随机数，类定义
import random
class RandomGen:
     @classmethod
     def generate(cls, start=1, stop=200, patch=10):
        return [random.randint(start, stop) for x in range(patch)]

#start 起始  stop结尾  1-200范围   patch 10个值
print(RandomGen.generate())
print('\n')



#
# 2、打印坐标
# 使用上题中的类，随机生成20个数字，两两配对形成二维坐标系的坐标，把这些坐标组织起来，并打印输出
class Point:
     def __init__(self, x, y):
         self.x = x
         self.y = y

points = [Point(x,y) for x,y in
zip(RandomGen().generate(),RandomGen().generate())]
for p in points:
    print('{}:{}'.format(p.x, p.y))

print('\n')




#3、车辆信息
#记录车的品牌mark、颜色color、价格price、速度speed等特征，并实现增加车辆信息、显示全部车辆信息的功能
class Car: # 记录单一车辆
     def __init__(self, mark, speed, color, price):
         self.mark = mark
         self.speed = speed
         self.color = color
         self.price = price

     def __repr__(self):
         return '<{} {} {} {} {} >'.format(type(self).__name__ , self.mark,
                            self.color, self.speed, self.price)


class CarInfo:
     def __init__(self):
        self.info = []
     def addcar(self, car: Car):
        self.info.append(car)
     def getall(self):
         return self.info

ci = CarInfo()
car = Car('audi', 400, 'red', 100)
ci.addcar(car)
ci.addcar(car)
ci.getall() # 返回所有数据，此时在实现格式打印
print(ci.getall)
print(ci.getall())
print('\n')


#
# 4、实现温度的处理
# 实现华氏温度和摄氏温度的转换。
# ℃ = 5 × (℉ - 32) / 9
# ℉ = 9 × ℃ / 5 + 32
# 完成以上转换后，增加与开氏温度的转换，K = ℃ + 273.15





