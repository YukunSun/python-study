# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def print_info(self):
        print('player info: %s %s' % (self.__name, self.age))

    def update_age(self, age):
        self.age = age

    def update_name(self, name):
        self.__name = name


p1 = Player('jerry', 12)
p2 = Player('tom', 13)
print(p1)  # <__main__.Player object at 0x10c87e5c0>
p1.print_info()  # player info: jerry 12
p2.print_info()  # player info: tom 13
# 修改成员变量的值
p2.update_age(8)
p2.print_info()
# 因为 age 并不是私有的，所以直接赋值也可以修改
p2.age = 7
p2.print_info()

# name 就不能直接赋值进行修改了，而必须通过方法修改
p2.name = 'tom2'
p2.print_info()  # 并没有被修改
p2.update_name('tom2')
p2.print_info()  # player info: tom2 7


class Animal:
    def __init__(self, weight=100):
        self.weight = weight

    def run(self):
        print('animal move')


# Cat 继承了 Animal，下同
class Cat(Animal):
    def __init__(self, weight=50):
        self.weight = weight


class Dog(Animal):
    def __init__(self, weight=30):
        super().__init__(weight)  # 可省略的一种写作方式

    def run(self):  # 会覆盖父类的方法
        print('Dog move')


a1 = Animal(99)
print(a1.weight)
a1.run()

a2 = Cat(50)
print(a2.weight)
a2.run()

a3 = Dog()
print(a3.weight)
a3.run()  # Dog move

print(type(a1))  # <class '__main__.Animal'>
print(isinstance(a1, Animal))  # True
