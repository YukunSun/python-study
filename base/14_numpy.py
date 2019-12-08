# -*- coding: utf-8 -*-

# numpy 的使用 demo
import numpy as np

arr = np.array([1, 2, 3])
# 查看数据类型
print(arr.dtype)  # int64
print(arr)

arr2 = np.array([1.1, 2.1, 3.1])
print(arr2.dtype)  # float64
print(arr2)
# 直接两个列表累加
print(arr + arr2)
# 直接与标量计算：甚至不用写循环
print(arr2 * 10)  # [11. 21. 31.]

# 定义一个矩阵（二维数组）
data = [[1, 2, 3], [4, 5, 6]]
arr3 = np.array(data)
print(arr3)
'''
[[1 2 3]
 [4 5 6]]
'''
print(arr3.dtype)  # int64

# 定义一个全为0的一维数组
arr4 = np.zeros(7)
print(arr4)  # [0. 0. 0. 0. 0. 0. 0.]

# 定义一个全为0的矩阵
arr5 = np.zeros((3, 5))
print(arr5)
'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''
# 定义一个全为1的矩阵
arr6 = np.ones((3, 5))
print(arr6)
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''

# 对切片的运算示例
arr7 = np.arange(10)
print(arr7)  # [0 1 2 3 4 5 6 7 8 9]
print(arr7[2:4])  # [2 3]
arr7[5:7] = 12
print(arr7)  # [ 0  1  2  3  4 12 12  7  8  9]
# 但是有时候不想改变原值怎么办
arr7_copy = arr7.copy()
arr7_copy[:] = -1
print(arr7_copy)  # [-1 -1 -1 -1 -1 -1 -1 -1 -1 -1]
print(arr7)  # arr7_copy 变了，而原值 arr7 并没有改变
