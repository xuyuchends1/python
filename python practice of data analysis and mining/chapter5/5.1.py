
#-*- coding: utf-8 -*-
#逻辑回归 自动建模
import pandas as pd

#参数初始化
filename = 'bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8]
y = data.iloc[:,8]

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
rlr = RLR(selection_threshold=0.25) #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y) #训练模型
# True 返回结果的index. false 返回所有的
result= rlr.get_support(True) #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
print(u'通过随机逻辑回归模型筛选特征结束。')
print("有效特征为:{0} 列".format(result))
#更方便的写法
x = data.iloc[:,result ]


lr = LR() #建立逻辑货柜模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
print(u'逻辑回归模型训练结束。')
print(u'模型的平均正确率为：%s' % lr.score(x, y)) #给出模型的平均正确率，本例为81.4%
#如果用全部的列来计算,得分会比现在的低