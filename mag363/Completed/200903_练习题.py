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



# 4、实现温度的处理
# 实现华氏温度和摄氏温度的转换。
# ℃ = 5 × (℉ - 32) / 9
# ℉ = 9 × ℃ / 5 + 32
# 完成以上转换后，增加与开氏温度的转换，K = ℃ + 273.15



class Temperature:
    def __init__(self, t, unit='c'):
        self._c = None
        self._f = None
        self._k = None

        if unit == 'k':
            self._k = t
            self._c = self.k2c(t)
        elif unit == 'f':
            self._f = t
            self._c = self.f2c(t)
        else:
            self._c = t

    @property
    def c(self):  # 摄氏度
        return self._c

    @property
    def k(self):  # 开氏温度
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k

    @property
    def f(self):  # 华氏温度
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @classmethod
    def c2f(cls, c):
        return 9 * c / 5 + 32

    @classmethod
    def f2c(cls, f):
        return 5*(f-32)/9

    @classmethod
    def c2k(cls, c):
        return c + 273.15

    @classmethod
    def k2c(cls, k):
        return k - 273.15

    @classmethod
    def f2k(cls, f):
        return cls.c2k(cls.f2c(f))

    @classmethod
    def k2f(cls, k):
        return cls.c2f(cls.k2c(k))

print(Temperature.c2f(40))
print(Temperature.f2c(104.0))
print(Temperature.c2k(40))
print(Temperature.k2c(313.15))
print(Temperature.f2k(104))
print(Temperature.k2f(313.15))


t = Temperature(40)
print(t.c, t.k, t.f)

t = Temperature(313.15, 'k')
print(t.c, t.k, t.f)
print('\n')


# 5、模拟购物车购物
# 思路
# 购物车购物，分解得到两个对象 购物车 、 物品 ，一个操作 购买 。
# 购买不是购物车的行为，其实是人的行为，但是对于购物车来说就是 增加add 。
# 商品有很多种类，商品的属性多种多样，怎么解决？
# 购物车可以加入很多不同的商品，如何实现？


class Color:
     RED = 0
     BLUE = 1
     GREEN = 2
     GOLDEN = 3
     BLACK = 4
     OTHER = 1000
class Item:
     def __init__(self, **kwargs):
         self.__spec = kwargs
     def __repr__(self):
         return str(sorted(self.__spec.items()))
class Cart:
     def __init__(self):
         self.items = []
     def additem(self,item:Item):
         self.items.append(item)
     def getallitems(self):
         return self.items

mycart = Cart()
myphone = Item(mark='Huawei', color=Color.GOLDEN, memory='4G')
mycart.additem(myphone)
print(mycart.getallitems())
print('~~~~分隔符~~~~')
mycar = Item(mark='Red Flag', color=Color.BLACK, year=2017)
mycart.additem(mycar)
print(mycart.getallitems())
print('~~~~分隔符~~~~')
mycart.additem(mycar)
print(mycart.getallitems())
print('~~~~分隔符~~~~')



























