# 拉格朗日插值法
import pandas as pd
from scipy.interpolate import lagrange # 拉格朗日插值法
import matplotlib.pyplot as plt  # 导入图像库

sales_path = 'E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter4\catering_sale.xls'
data = pd.read_excel(sales_path, index_col=u'日期')
# sales.loc[sales[u'销量'].isna()]
data[(data['销量'] < 500) | (data['销量'] > 5000)] = None


# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果


# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:  # 如果为空即插值。
            data[i][j] = ployinterp_column(data[i], j)
