# -*- comding:utf-8   -*-



class Person:
    def get_score(self):
        return {'English':80, 'chinese':88, 'history':90}


def get_score(a):
    return {'name':a.__class__.__name__, 'chinese':100, 'English':99}


def monkeypath4Person():
    Person.get_score = get_score


tom = Person()
print(tom.get_score()) #{'English': 80, 'chinese': 88, 'history': 90}


monkeypath4Person()  #动态打补丁，动态修改
tom = Person()
print(tom.get_score())