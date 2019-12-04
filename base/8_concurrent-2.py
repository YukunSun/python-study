# -*- coding: utf-8 -*-
# 生产者消费者模式
import threading
import queue
import random
import time

queue = queue.Queue(5)


class ProducerThread(threading.Thread):
    def run(self) -> None:
        name = threading.current_thread().getName()
        nums = range(10)
        while True:
            num = random.choice(nums)
            queue.put(num)
            print("producer %s generate: %d" % (name, num))
            time.sleep(1)


class ConsumerThread(threading.Thread):
    def run(self) -> None:
        name = threading.current_thread().getName()
        while True:
            num = queue.get()
            queue.task_done()
            print("consumer %s consumed: %s" % (name, num))
            time.sleep(1)


p1 = ProducerThread(name='p1')
p1.start()

p2 = ProducerThread(name='p2')
p2.start()

c1 = ConsumerThread(name='c1')
c1.start()
c2 = ConsumerThread(name='c2')
c2.start()
c3 = ConsumerThread(name='c3')
c3.start()
