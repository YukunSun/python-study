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

# 函数的迭代器与生成器
lst = [1, 2, 3]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))

# start=1,stop=10,step=2，但是 step 必须为整数
for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9


# 自定义一个迭代器，实现 step 可以是 float
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frange(1, 10, 1.5):
    print(i)


# lambda
# 示例1：下面两个函数是等价的
def true():
    return True


# 省略函数名
func1 = lambda: True
print(func1())  # True


# 2
def add(a, b):
    return a + b


# 省略函数名、参数，冒号后面是返回值
func2 = lambda a, b: a + b

print(add(1, 3))  # 4
print(func2(1, 3))  # 4

# 内置函数
lst2 = [1, 2, 3]
print(list(filter(lambda x: x > 1, lst2)))  # [2, 3]
# map：对值依次处理
print(list(map(lambda x: x * 2, lst2)))  # [2, 4, 6]
lst3 = [1, 2, 3]
print(list(map(lambda x, y: x * y, lst2, lst3)))  # [1, 4, 9]

# 内建函数：reduce
from functools import reduce

# 等价于 (((2+1)+4)+6)
print(reduce(lambda x, y: x + y, [2, 4, 6], 1))  # 13

# 内建函数:zip
tpl1 = (1, 2, 3), (4, 5, 6)
for j in zip(tpl1):
    print(j)
# 返回：
# ((1, 2, 3),)
# ((4, 5, 6),)

for k in zip((1, 2, 3), (4, 5, 6)):
    print(k)
# 返回：
# (1, 4)
# (2, 5)
# (3, 6)

# 实现 key,value 对调
dct1 = {'k1': 'v1', 'k2': 'v2'}
dct2 = zip(dct1.values(), dct1.keys())
print(dict(dct2))


# 嵌套函数
def fun():
    a = 1

    def fun2():
        nonlocal a  # 使用外层函数的变量a
        a += 1
        print("func 2:", a)

    fun2()  # func 2: 2，这里调用 fun2()
    print("func 1:", a)


print(fun())  # func 1: 2


# 闭包:内部函数引用外部变量
def sum(a):
    def add(b):
        return a + b

    return add


num1 = sum(2)
num2 = num1(4)
print(type(num1))  # <class 'function'>
print(type(num2))  # <class 'int'>
print(num2)  # 6


# 闭包：举例1
def counter(first):
    cnt = [first]

    def addOne():
        cnt[0] += 1
        return cnt[0]

    return addOne


r1 = counter(7)
print(type(r1))
print(r1())
print(counter(10)())
print(counter(15)())


# 闭包 例2
def fun3(a, b, c):
    def para(x):
        return a * x ** 2 + b * x + c

    return para


f4 = fun3(1, 2, 3)
print(f4(1))
# 如果再想计算 x=2,3 的值，就太方便了
print(f4(2))
print(f4(3))
