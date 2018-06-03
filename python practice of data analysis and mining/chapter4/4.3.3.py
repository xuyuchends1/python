
import pandas as pd
import math
file = 'E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter4\\discretization_data.xls'
data = pd.read_excel(file)
#等宽
k=4
data_describe=data[u'肝气郁结证型系数'].describe()
fenzu= (data_describe.loc['max']-data_describe.loc['min'])/k
searcharray=[]
for i in range(k+1):
    searcharray.append(i*fenzu)

d1=pd.cut(data[u'肝气郁结证型系数'],searcharray)


w = [1.0*i/k for i in range(k+1)]
w = data[u'肝气郁结证型系数'].describe(percentiles = w)[4:4+k+1] #使用describe函数自动计算分位数
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(data[u'肝气郁结证型系数'], w, labels = range(k))

#
# #肝气郁结证型系数
# import pandas as pd
#
# datafile = E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter4\\discretization_data.xls' #参数初始化
# data = pd.read_excel(datafile) #读取数据
# data = data[u'肝气郁结证型系数'].copy()
# k = 4
#
# d1 = pd.cut(data, k, labels = range(k)) #等宽离散化，各个类比依次命名为0,1,2,3