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


class Monster:
    # todo
    pass
