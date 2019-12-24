# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# 1.绘制简单曲线
plt.plot([1, 3, 5], [4, 8, 10])
plt.show()

# 2.绘制 numpy 的曲线
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
plt.plot(x, np.sin(x))
plt.show()

# 3.多条线的折线图
plt.figure(1, dpi=50)  # 创建图表
for i in range(1, 4):  # 画 3 条线
    plt.plot(x, np.sin(x / i))
plt.show()

# 4.直方图
plt.figure(1, dpi=50)
data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
plt.hist(data)
plt.show()

# 5.散点图
x = np.arange(1, 10)
y = x
fig = plt.figure()
plt.scatter(x, y, c='r', marker='o')  # 红色，圆形的点
plt.show()

# 绘制 pandas 的曲线
import pandas as pd

iris = pd.read_csv('./iris_training.csv')
print(iris.head())  # 展示前5行
iris.plot(kind='scatter', x="120", y="4")  # 展示“120”，“4”两列内容
plt.show()

# seaborn：一个生成更漂亮图的库
# todo