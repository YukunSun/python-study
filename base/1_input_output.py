# -*- coding: utf-8 -*-
# 书写规范
if 10 - 9 > 0:
    print('10-9>0')

# 变量
print(10 / 8)
length = 10
width = 8
print(length / width)

# 打印
print("1")
print(1)

# 序列：1.切片操作
arr = "array"
print(arr[0])
print(arr[0:3])
print(arr[-1])

# 序列应用举例：判断生肖
s = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 2019
print(s[year % 12])
print('今年的生肖是：' + s[year % 12])
# 2.成员关系操作
print('猴' not in s)
print('猴' in s)

# 元组：举例
# 星座
y = (u'摩羯座', u'水瓶座', u'白羊座'u'金牛座'u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
# 星座的日期
yDate = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# 随意一个日期
(month, day) = (2, 15)
yDay = filter(lambda x: x < (month, day), yDate)
add = len(list(yDay)) % 12
print('属于：' + y[add])

# 列表
list1 = ['a', 'b', 2]
list1.append('c')
list1.remove('a')
print(list1)

print(1 + 2)
print('1 + 1 = ', 1 + 1)

print(1, 2, 3, 4, 5, 6, 7)

# if 表达式
a = input('请输入数字：')
if a == 1:
    print("case 1")
elif a == 2:
    print("case 2")
else:
    print("case 3")

# 数据类型
print(1, -1, -8080)
print(1.0, -1.250)
print('hello "world" \n sun \\yukun')
print('''h 
e
l
l
o''')

print(True and False)
print(True and True)
print(False and False)
print(False or True)

print(20 / 2.0)
print(20 / 3.0, 20 % 3, 20 // 3)



