# -*- coding: utf-8 -*-
# 装饰器
import time


def func1():
    start = time.time()
    time.sleep(5)  # 模拟程序运行
    stop = time.time()
    return stop - start


print("func1 spent time:%s" % func1())  # func1 spent time:5.005311012268066


# 使用装饰器改写上面的程序
def timer(func):
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        print("func1 spent time:%s" % (stop - start))

    return wrapper


@timer
def func2():
    print("my function")


func2()
