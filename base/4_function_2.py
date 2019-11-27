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


# 装饰器2：如果函数想带上参数怎么办
def tips(func):
    def wrapper(a, b):
        print("start")
        func(a, b)
        print("stop")

    return wrapper


@tips
def add(a, b):
    print(a + b)


@tips
def sub(a, b):
    print(a - b)


add(1, 2)
sub(1, 2)


# 输出：
# start
# 3
# stop

# start
# -1
# stop

# 如何让装饰器传递参数：
def new_tips(args):
    def tips(func):
        def wrapper(a, b):
            print("start %s" % args)
            func(a, b)
            print("stop")

        return wrapper

    return tips


@new_tips("haha 123")
def add(a, b):
    print(a + b)


@new_tips("haha 456")
def sub(a, b):
    print(a - b)


add(1, 3)
sub(1, 3)
# 输出：
# start haha 123
# 4
# stop
# start haha 456
# -2
# stop
