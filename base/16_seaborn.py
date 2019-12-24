# -*- coding: utf-8 -*-

# seaborn：一个生成更漂亮图的库

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = pd.read_csv('./iris_training.csv')
# 设置样式
sns.set(style="white", color_codes=True)
# 设置绘制格式为散点图
sns.jointplot(x="120", y="4", data=iris, height=5)
sns.distplot(iris['120'])
plt.show()
