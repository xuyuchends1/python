#归一化
import pandas as pd
file = 'E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter4\\normalization_data.xls' #餐饮菜品盈利数据
data = pd.read_excel(file, header=None)
print (data)
data=(data-data.mean())/data.std()
print ("归一化后")
print (data)