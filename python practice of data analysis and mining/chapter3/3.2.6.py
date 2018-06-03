import pandas as pd
import matplotlib.pyplot as plt

dish_profit = 'E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter3\catering_sale_all.xls'
data = pd.read_excel(dish_profit, index_col = u'日期')
data.corr()[u'百合酱蒸凤爪']
print(data.corr()[u'百合酱蒸凤爪'])

data.corr()[u'百合酱蒸凤爪']
data1= data[u'百合酱蒸凤爪'].corr(data[u'金银蒜汁蒸排骨'])
print(data1)