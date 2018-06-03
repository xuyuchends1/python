import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

#sales[sales.isna().values==True]

def pin_lv(arr):
    return arr.count()/sales.describe().loc['count']


sale_path='E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter3\catering_sale.xls'
sales= pd.read_excel(sale_path,index_col='date')
sales=sales.dropna()
sales_describe= sales.describe()
#极差
sales_describe.loc['ji_cha']=sales_describe.loc['max']-sales_describe.loc['min']
fen_zu_shu = math.ceil(sales_describe.loc['ji_cha']/1000)
#分组间隔
list_fen_zu=[]
for index in range(fen_zu_shu+1):
    list_fen_zu.append(index*1000)

fen_zu_qu_jian=pd.cut(sales['sale'],list_fen_zu)
group=sales.groupby(by=fen_zu_qu_jian)

group=group.agg(['count','sum',pin_lv])
group.columns=group.columns.droplevel()

group['lei_ji']=group['pin_lv'].cumsum(skipna=True)
group['lei_ji']=group['lei_ji'].fillna(method='ffill')

group.plot.bar(logy=True,figsize=[12,6],rot=15)
plt.show()


