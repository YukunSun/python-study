# -*- coding: utf-8 -*-
import threading
import time


def thread1(arg1, arg2):
    print(threading.current_thread().name)
    time.sleep(1)
    print("%s %s" % (arg1, arg2))


# 例1
# for i in range(1, 6, 1):
#    thread1(i, i + 1)

# 例1：改写
for i in range(1, 6, 1):
    t1 = threading.Thread(target=thread1, args=(i, i + 1))
    t1.start()


# 例3
class MyThread(threading.Thread):
    def run(self):
        print(threading.current_thread().getName(), 'start')
        print("MyThread run")


t2 = MyThread()
t2.start()
t2.join()
print(threading.current_thread().getName(), 'stop')
