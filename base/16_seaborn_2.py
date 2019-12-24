# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = pd.read_csv('./iris_training.csv')
print(iris.head())
# 设置样式
sns.set(style="white", color_codes=True)
# sns.FacetGrid(iris, hue='virginica', height=5).map(plt.scatter, "120", "4").add_legend()
sns.FacetGrid(iris, hue='virginica', height=5).map(plt.scatter, "setosa", "versicolor").add_legend()
plt.show()
