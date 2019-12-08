# -*- coding: utf-8 -*-

from pandas import Series, DataFrame

# 可以灵活处理缺省值，默认值、数据的连接操作等，适用于数据清洗

# 1. Series 用于处理一维数组
arr = Series([4, 5, 6, -7])
'''
0    4
1    5
2    6
3   -7
dtype: int64
'''
print(arr)
print(arr.dtype)  # int64
print(arr.index)  # RangeIndex(start=0, stop=4, step=1)
print(arr.values)  # [ 4  5  6 -7]

# 手动指定索引
arr2 = Series([4, 5, 6, -7], index=['a', 'b', 'c', 'd'])
print(arr2)
'''
a    4
b    5
c    6
d   -7
dtype: int64
'''
# 像字典一样修改某一个 key 的值
arr2['a'] = 1
print(arr2)
# 查看某一个索引是否在某个 Series 中
print('c' in arr2)  # True
print('f' in arr2)  # False

# 字典 -> Series
dict = {'a': 1, 'b': 2}
s1 = Series(dict)
print(s1)
'''
a    1
b    2
dtype: int64
'''
# 修改 Series 的索引
s1.index = ['k1', 'k2']
print(s1)
'''
k1    1
k2    2
dtype: int64
'''

# 手动填充值
arr3 = Series([1, 3, -3], index=['c', 'a', 'b'])
# todo



############################################################################
# 2.DataFrame:操作更高维的数组

data = {
    'city': ['sh', 'bj', 'tj', 'sh'],
    'year': [2017, 2018, 2019, 2017],
    'area': [1, 2, 3, 8]
}
frame = DataFrame(data)
print(frame)
'''
  city  year  area
0   sh  2017     1
1   bj  2018     2
2   tj  2019     3
3   sh  2017     8
'''
# 改变列的前后顺序
frame2 = DataFrame(data, columns=['area', 'city', 'year'])
print(frame2)

# 按列取值
print(frame['city'])
print(frame.year)

# 新增一列
frame['col_1'] = 123
frame['col_2'] = frame.area < 3  # 添加的值也可以由其他的列计算出来的
print(frame)
'''
  city  year  area  col_1  col_2
0   sh  2017     1    123   True
1   bj  2018     2    123   True
2   tj  2019     3    123  False
3   sh  2017     8    123  False
'''

# 定义一个 DataFrame
data2 = {
    'foo': {2017: 512, 2018: 523, 2019: 550},
    'bar': {2017: 600, 2018: 601, 2019: 660}
}

frame3 = DataFrame(data2)
print(frame3)
'''
      foo  bar
2017  512  600
2018  523  601
2019  550  660
'''

# 矩阵的行列转换
print(frame3.T)
'''
     2017  2018  2019
foo   512   523   550
bar   600   601   660
'''
