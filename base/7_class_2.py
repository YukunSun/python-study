# -*- coding: utf-8 -*-

class Student:
    pass


sunyk = Student
sunyk.sex = 'Male'
sunyk.age = 13
print(sunyk.sex)
print(sunyk.age)


# 省却 try catch...

class TestWith:
    def __enter__(self):
        print('start')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit')
        else:
            print('exit exception %s' % exc_tb)


with TestWith():
    print('test is running 1')

with TestWith():
    print('test is running 2')
    raise NameError('TestException...')
