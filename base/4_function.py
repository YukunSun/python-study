# -*- coding: utf-8 -*-
# 1.函数的定义
def my_func(x):
    if x < 0:
        return -x
    else:
        return x


print(my_func(-2))


# 2.
def func(a, b, c):
    print('a=%s' % a)
    print('b=%s' % b)
    print('c=%s' % c)


func(1, 2, 3)
# 可以颠倒参数的顺序
func(1, c=3, b=2)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, ))
print(calc(1, 2))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll(1, 2)


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(100))


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact2(100))

# 可变参数
print()
