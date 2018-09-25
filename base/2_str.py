# -*- coding: utf-8 -*-
print(ord('A'))
# print(ord('中'))
print(chr(66))
print(str('\u4e2d\u6587'))

a = 1
if a == 2:
    print('a=2')
elif a == 3:
    print('a=3')
else:
    print(a)


a = input('pls input a number:')
if a == 2:
    print('a=2')
elif a == 3:
    print('a=3')
else:
    print(a)



sum = 0
for x in range(101):
    sum = x + sum
print(sum)


sum = 0
n = 100
while n > 0:
    sum = n + sum
    n = n-1
print(sum)