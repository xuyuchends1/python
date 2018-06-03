#-*- coding: utf-8 -*-
#数据规范化
import pandas as pd
from sklearn.cluster import KMeans #引入KMeans

if __name__=='__main__':
  datafile = 'E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter4\discretization_data.xls' #参数初始化
  data = pd.read_excel(datafile) #读取数据
  data = data[u'肝气郁结证型系数'].copy()
  k = 4
  kmodel = KMeans(n_clusters = k, n_jobs = 4) #建立模型，n_jobs是并行数，一般等于CPU数较好
  kmodel.fit(data.values.reshape((len(data), 1))) #训练模型
  c = pd.DataFrame(kmodel.cluster_centers_).sort(0) #输出聚类中心，并且排序（默认是随机序的）
  w = pd.rolling_mean(c, 2).iloc[1:] #相邻两项求中点，作为边界点
  w = [0] + list(w[0]) + [data.max()] #把首末边界点加上
  d3 = pd.cut(data, w, labels = range(k))
