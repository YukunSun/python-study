# -*- coding: utf-8 -*-
print(ord('A'))
# print(ord('中'))
print(chr(66))
print(str('\u4e2d\u6587'))

# 循环1
sum1 = 0
for x in range(101):
    sum1 = x + sum1
print(sum1)

# 循环2
for i in range(1, 12):
    print(i)

# 循环3
sum2 = 0
n = 100
while n > 0:
    sum2 = n + sum2
    n = n - 1
print(sum2)

# 列表推导式
lst = [i * i for i in range(2, 6)]
print(lst)  # [4, 9, 16, 25]

# 字典推导式
dct = {i: i * i for i in range(2, 6)}
print(dct)  # {2: 4, 3: 9, 4: 16, 5: 25}
